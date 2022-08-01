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
# TODO: Optimize the rename_file function


class DirHandler:

    @staticmethod
    def remove_dir(path, description=None, debug=False):
        if debug is True and description is None:
            description = path

        if os.path.isdir(path):
            dir_util.remove_tree(path)
            if debug is True:
                print("Deleted " + description)
        else:
            if debug is True:
                print("Skipped " + description + " deletion, didn't exist")

    @staticmethod
    def remove_file(path, description=None, debug=False):
        if debug is True and description is None:
            description = path

        if os.path.isfile(path):
            os.remove(path)
            if debug is True:
                print("Deleted " + description)
        else:
            if debug is True:
                print("Skipped " + description + " deletion, didn't exist")

    @staticmethod
    def copy_dir(from_path, to_path, from_desc=None, to_desc=None, debug=False):
        if debug is True:
            if from_desc is None:
                from_desc = from_path
            if to_desc is None:
                to_desc = to_path

        if os.path.isdir(from_path):
            dir_util.copy_tree(from_path, to_path)
            if debug is True:
                print("Copied " + from_desc + " to " + to_desc)
        else:
            if debug is True:
                print("Skipped " + from_desc + " copying to " + to_desc + ", didn't exist")

    @staticmethod
    def copy_file(from_path, to_path, from_desc=None, to_desc=None, debug=False):
        if debug is True:
            if from_desc is None:
                from_desc = from_path
            if to_desc is None:
                to_desc = to_path

        if os.path.isfile(from_path):
            shutil.copy2(from_path, to_path)
            if debug is True:
                print("Copied " + from_desc + " to " + to_desc)
        else:
            if debug is True:
                print("Skipped " + from_desc + " copying to " + to_desc + ", didn't exist")

    @staticmethod
    def rename_file(path, name, description=None, debug=False):
        if description is None:
            description = path + " to " + name

        DirHandler.copy_file(path, os.path.dirname(path) + '/' + name, debug=debug)
        DirHandler.remove_file(path, debug=debug)
        if debug is True:
            print("Renamed " + description)

    # ==============================================================================
