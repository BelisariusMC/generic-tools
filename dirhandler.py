#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================================================================
# Created By  : BelisariusMC
# Created Date: 19 jun. 2022
# Version     : 1.0.3
# License     : BSD 3-Clause "New" or "Revised" License
# ==============================================================================
import os
import shutil
from distutils import dir_util
# ==============================================================================


class DirHandler:

    @staticmethod
    def remove(path, description=None, debug=False):
        if debug is True and description is None:
            description = path

        if os.path.isdir(path):
            dir_util.remove_tree(path)
            if debug is True:
                print("Deleted directory " + description)
        elif os.path.isfile(path):
            os.remove(path)
            if debug is True:
                print("Deleted file " + description)
        else:
            if debug is True:
                print("Skipped " + description + " deletion, didn't exist")

    @staticmethod
    def copy(from_path, to_path, from_desc=None, to_desc=None, debug=False):
        if debug is True:
            if from_desc is None:
                from_desc = from_path
            if to_desc is None:
                to_desc = to_path

        if os.path.isdir(from_path):
            dir_util.copy_tree(from_path, to_path)
            if debug is True:
                print("Copied directory " + from_desc + " to " + to_desc)
        elif os.path.isfile(from_path):
            shutil.copy2(from_path, to_path)
            if debug is True:
                print("Copied file " + from_desc + " to " + to_desc)
        elif debug is True:
            print("Skipped " + from_desc + " copying to " + to_desc + ", didn't exist")

    @staticmethod
    def rename(path, name, description=None, debug=False):
        if description is None:
            description = "Renamed " + path + " to " + name

        os.rename(path, name)
        if debug is True:
            print(description)

    @staticmethod
    def create_temp(path, name=".temp", description=None, debug=False):
        if debug is True and description is None:
            description = path

        local_path = os.path.dirname(path)

        if os.path.isdir(path):
            DirHandler.copy(path, local_path + "/" + name, debug=debug)
        elif os.path.isfile(path):
            temp_file = name + os.path.splitext(path)[1]
            DirHandler.copy(path, local_path + "/" + temp_file, debug=debug)
        elif debug is True:
            print("Skipped " + description + ", didn't exist")

    # ==============================================================================
