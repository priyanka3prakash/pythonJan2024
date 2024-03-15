#!/usr/bin/python
"""
Purpose:
Take a backup zip file for all files on desktop
"""
import os
from zipfile import ZipFile

file_path = os.environ("USERPROFILE", "") + os.sep + "Downloads"
print(f"file_path:{file_path}")

os.makedirs(file_path, exist_ok=True)

with ZipFile("content.zip", "w") as zp_fh:
    for ech_dir, dirs, files in os.walk(file_path):
        for ech_file in files:
            # print(ech_file)
            zp_fh.write(os.path.join(ech_dir, ech_file))
    zp_fh.close()


# Assignment - Use this program to automate downloads folder backup
# and schedule that python script to run daily at sometime, using windows scheduler
    