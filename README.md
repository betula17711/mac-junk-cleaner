# Mac Junk Cleaner

Mac Junk Cleaner is a simple **PyQt6-based GUI application** for cleaning temporary and system junk files on macOS.

This project was created for learning and practical purposes.

## 🧹 What the application cleans

- **.DS_Store files** — Finder metadata files  
- **AppleDouble files (._*)** — macOS resource fork files  
- **Spotlight Search Index** — Spotlight search index files  
- **System Trash Folder** — system-level trash  
- **File System Event Logs** — file system event log files

Only well-known temporary and system-related files are removed.

## 🚀 Run from source

```bash
pip install -r requirements.txt
python main.py
```