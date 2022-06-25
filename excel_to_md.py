#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================================================================
# Created By  : BelisariusMC
# Created Date: 11 jun. 2022
# Version     : 1.0.2
# License     : BSD 3-Clause "New" or "Revised" License
# ==============================================================================
from openpyxl import load_workbook
import pandas as pd
from dir_handler import *
# ==============================================================================
# TODO: Add comments
# TODO: Change the temp file name to 'temp'
# TODO: Optimize to not use a temp file


class Excel_to_md:

    def __init__(self, file, path=None, saveOriginalPath=True):
        # Input
        self.file = file
        self.file_path = path
        self.saveOriginalPath = saveOriginalPath

        # Processed
        self.file_name = file.split('.', 1)[0]
        self.file_type = '.' + file.split('.', 1)[1]
        self.file_converted = self.file
        self.file_temp = self.file

    def create_temp_file(self):
        # TODO: if file contains a path

        self.file_temp = 'temp' + self.file_type

        if self.file_path is not None:
            Dir_handler.copy_file(self.file_path + self.file, os.path.dirname(os.path.abspath(__file__)) + '/' + self.file_temp,
                                  self.file_path + self.file, os.path.dirname(os.path.abspath(__file__)) + '/' + self.file_temp)
        else:
            Dir_handler.copy_file(os.path.dirname(os.path.abspath(__file__)) + self.file, os.path.dirname(os.path.abspath(__file__)) + '/' + self.file_temp,
                                  os.path.dirname(os.path.abspath(__file__)) + self.file, os.path.dirname(os.path.abspath(__file__)) + '/' + self.file_temp)

    def save_original_path(self, _file):
        if self.saveOriginalPath:
            Dir_handler.copy_file(os.path.dirname(os.path.abspath(__file__)) + '/' + _file, self.file_path,
                                  os.path.dirname(os.path.abspath(__file__)) + '/' + _file, self.file_path)
            Dir_handler.remove_file(os.path.dirname(os.path.abspath(__file__)) + '/' + _file,
                                    os.path.dirname(os.path.abspath(__file__)) + '/' + _file)

    def hyperlink(self, saveLocal=False):
        """
        :return: Excel table with hyperlink cells converted into Markdown format
        """

        self.create_temp_file()
        wb = load_workbook(self.file_temp)
        ws = wb.active

        # Iterate thru all cells and if hyperlink found attempt modification of cell
        for row in ws.rows:
            for cell in row:
                try:
                    if len(cell.hyperlink.target) > 0:
                        cell.value = "".join(['[', cell.value, '](', cell.hyperlink.target, ')'])
                except:
                    pass

        self.file_converted = self.file_name + '_CONVERTED' + self.file_type
        wb.save(self.file_converted)

        if not saveLocal:
            Dir_handler.remove_file(os.path.dirname(os.path.abspath(__file__)) + '/' + self.file_temp,
                                    os.path.dirname(os.path.abspath(__file__)) + '/' + self.file_temp)
            self.save_original_path(self.file_converted)

        print("Converted " + self.file_name + " hyperlink cells to Markdown format")

    def to_markdown(self, convert_hyperlink=True, saveLocal=False, md_header="keys", **kwargs):

        if convert_hyperlink:
            self.hyperlink(saveLocal=True)
        else:
            self.create_temp_file()

        df = pd.read_excel(self.file_converted, sheet_name=0, **kwargs)
        df = df.fillna('')
        df.to_markdown(buf=self.file_name + '.md', index=False, headers=md_header)

        Dir_handler.remove_file(os.path.dirname(os.path.abspath(__file__)) + '/' + self.file_temp,
                                os.path.dirname(os.path.abspath(__file__)) + '/' + self.file_temp)
        Dir_handler.remove_file(os.path.dirname(os.path.abspath(__file__)) + '/' + self.file_converted,
                                os.path.dirname(os.path.abspath(__file__)) + '/' + self.file_converted)
        if not saveLocal:
            self.save_original_path(self.file_name + '.md')

        print("Converted " + self.file_name + " from " + self.file_type + " to Markdown")


# ==============================================================================
