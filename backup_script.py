# backup_script.py

import os
import subprocess
from datetime import datetime

# Configuration
DB_USER = "root"
DB_PASSWORD = "Secret5555"
DB_NAME = "mysql"
DB_HOST = "127.0.0.1"

# Generate filename with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_filename = f"{DB_NAME}_backup_{timestamp}.sql"

# Command to dump the database
dump_command = [
    "mysqldump",
    f"-h{DB_HOST}",
    f"-u{DB_USER}",
    f"-p{DB_PASSWORD}",
    DB_NAME,
]

# Run the command and write output to file
with open(backup_filename, "w") as output_file:
    try:
        subprocess.run(dump_command, stdout=output_file, check=True)
        print(f" Backup successful: {backup_filename}")
    except subprocess.CalledProcessError as e:
        print(f" Backup failed: {e}")
