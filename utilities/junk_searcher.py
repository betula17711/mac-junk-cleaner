from pathlib import Path
from config import JUNK_RULES

def get_junks(path: Path):
    files = []
    dirs = []
    for path in path.rglob('*'):
        try:
            if path.is_file():
                for name, enabled in JUNK_RULES["files_exact"].items():
                    if enabled and path.name == name:
                        files.append(path)
                for prefix, enabled in JUNK_RULES["files_prefix"].items():
                    if enabled and path.name.startswith(prefix):
                        files.append(path)
            elif path.is_dir():
                for name, enabled in JUNK_RULES["dirs_exact"].items():
                    if enabled and path.name == name:
                        dirs.append(path)
        except (PermissionError, FileNotFoundError):
            continue
    return files, dirs