# 📦 Python File Backup Tool

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

A lightweight command-line utility to quickly back up files and directories with progress tracking and logging.

---

## 📸 Demo

![CLI Tool Screenshot](assets/demo.png)

---

## ✨ Features

* 🚀 **Fast Copying**: Efficiently transfers large files and directories.
* 📝 **Automated Logging**: Keeps track of backup operations with detailed timestamps.
* 🛡️ **Safe Overwrites**: Prevents accidental file loss with user confirmation prompts.

---

## ⚙️ Command-Line Arguments

| Flag | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| `--source` | `path` | **Yes** | Path to the source file or directory |
| `--target` | `path` | **Yes** | Path to the target backup location |
| `--log` | `path` | **No** | Custom path for output logs (Default: `backup.log`) |

---

## 💻 Example Usage

Run the tool from your terminal:

```bash
python file_backup.py --source ./my_folder --target ./backup_folder
