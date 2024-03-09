# -*- coding: utf-8 -*-
"""
Purpose: To copy a file from one directory, to another


src directory
    files

dst directory
    ....
"""



import os
import shutil


def copy_file(src_dir, dest_dir, filename):
    source_path = os.path.join(src_dir, filename)
    dest_path = os.path.join(dest_dir, filename)

    if not os.path.exists(src_dir):
        print("No such source directory. Aborting...")
        return

    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    if os.path.exists(dest_path):
        print("file already exists. So, deleting")
        os.remove(dest_path)

    shutil.copyfile(source_path, dest_path)


copy_file("test_dir_1", "test_dir_2", "test_file_1.txt")