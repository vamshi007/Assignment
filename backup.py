import os
import shutil
import time
import datetime


def backup_file(source_file, backup_dir, interval):
    if not os.path.exists(source_file):
        print(f"Source file {source_file} does not exist.")
        return

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    while True:
        current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        backup_file_name = f"{os.path.basename(source_file)}_{current_time}"
        backup_file_path = os.path.join(backup_dir, backup_file_name)

        try:
            shutil.copy2(source_file, backup_file_path)
            print(f"Backup successful: {backup_file_path}")
        except Exception as e:
            print(f"Backup failed: {e}")

        time.sleep(interval)


def main():
    source_file = "backup.py"
    backup_dir = "sample/backups"
    interval = 3600
    backup_file(source_file, backup_dir, interval)


if __name__ == "__main__":
    main()
