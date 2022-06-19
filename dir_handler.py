#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================================================================
# Created By  : BelisariusMC
# Created Date: 19 jun. 2022
# Version     : 1.0.1
# License     : BSD 3-Clause "New" or "Revised" License
# ==============================================================================
# Built-in/Generic Imports
import os
import shutil
from distutils import dir_util
# ==============================================================================
# TODO: Add comments


class Dir_handler:

    @staticmethod
    def remove_dir(path, description):
        if os.path.isdir(path):
            dir_util.remove_tree(path)
            print("Deleted " + description)
        else:
            print("Skipped " + description + " deletion, didn't exist")

    @staticmethod
    def remove_file(path, description):
        if os.path.isfile(path):
            os.remove(path)
            print("Deleted " + description)
        else:
            print("Skipped " + description + " deletion, didn't exist")

    @staticmethod
    def copy_dir(from_path, to_path, from_desc, to_desc):
        if os.path.isdir(from_path):
            dir_util.copy_tree(from_path, to_path)
            print("Copied " + from_desc + " to " + to_desc)
        else:
            print("Skipped " + from_desc + " copying to " + to_desc + ", didn't exist")

    @staticmethod
    def copy_file(from_path, to_path, from_desc, to_desc):
        if os.path.isfile(from_path):
            shutil.copy2(from_path, to_path)
            print("Copied " + from_desc + " to " + to_desc)
        else:
            print("Skipped " + from_desc + " copying to " + to_desc + ", didn't exist")


# ==============================================================================
