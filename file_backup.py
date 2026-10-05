import argparse
import logging
import os
import shutil
from datetime import datetime

# Set up clean logging to terminal
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


def backup_files(source_dir: str, target_dir: str) -> bool:
    """
    Copies all files and subdirectories from source_dir to target_dir.
    
    :param source_dir: Path to the directory containing files to back up.
    :param target_dir: Path to the destination directory.
    :return: True if the backup succeeded, False otherwise.
    """
    # Check if the source folder exists
    if not os.path.exists(source_dir):
        logging.error(f"Source directory does not exist: {source_dir}")
        return False

    # Create target directory if it doesn't exist
    if not os.path.exists(target_dir):
        try:
            os.makedirs(target_dir)
            logging.info(f"Created target directory: {target_dir}")
        except PermissionError:
            logging.error(f"Permission denied: Cannot create {target_dir}")
            return False

    # Perform file copying with error handling
    try:
        logging.info(f"Starting backup from '{source_dir}' to '{target_dir}'...")
        for item in os.listdir(source_dir):
            s = os.path.join(source_dir, item)
            d = os.path.join(target_dir, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)
        
        logging.info("Backup completed successfully!")
        return True

    except Exception as e:
        logging.error(f"An unexpected error occurred during backup: {e}")
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Automated Python File Backup Tool"
    )
    parser.add_argument(
        "--source", 
        required=True, 
        help="Path to the source directory to back up"
    )
    parser.add_argument(
        "--target", 
        required=True, 
        help="Path to the destination backup directory"
    )

    args = parser.parse_args()
    backup_files(args.source, args.target)
