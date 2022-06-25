#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================================================================
# Created By  : BelisariusMC
# Created Date: 19 jun. 2022
# Version     : 1.0.2
# License     : BSD 3-Clause "New" or "Revised" License
# ==============================================================================
import os
import shutil
from distutils import dir_util
# ==============================================================================
# TODO: Optimize the rename_file function


class dir_handler:

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

    @staticmethod
    def rename_file(path, name):
        dir_handler.copy_file(path, os.path.dirname(path) + '/' + name,
                              path, os.path.dirname(path) + '/' + name)
        dir_handler.remove_file(path, path)

# ==============================================================================
