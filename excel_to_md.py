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
# TODO: Optimize to not use a temp file


class excel_to_md:

    def __init__(self, file):
        # Input
        self.file = os.path.basename(file)
        self.file_path = os.path.dirname(file) + '/'

        # Processed
        self.file_name = self.file.split('.', 1)[0]
        self.file_type = '.' + self.file.split('.', 1)[1]
        self.local_path = os.path.dirname(os.path.abspath(__file__)) + '/'
        self.file_converted = self.file
        self.file_temp = self.file

    def create_temp_file(self):
        self.file_temp = 'temp' + self.file_type

        if self.file_path != '':
            dir_handler.copy_file(self.file_path + self.file, self.local_path + self.file_temp,
                                  self.file_path + self.file, self.local_path + self.file_temp)
        else:
            dir_handler.copy_file(self.local_path + self.file, self.local_path + self.file_temp,
                                  self.local_path + self.file, self.local_path + self.file_temp)

    def save_original_path(self, _file):
        dir_handler.copy_file(self.local_path + _file, self.file_path,
                              self.local_path + _file, self.file_path)
        dir_handler.remove_file(self.local_path + _file,
                                self.local_path + _file)

    def hyperlink(self, saveLocal=False):

        self.create_temp_file()
        wb = load_workbook(self.file_temp)
        ws = wb.active

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
            dir_handler.remove_file(self.local_path + self.file_temp,
                                    self.local_path + self.file_temp)
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

        dir_handler.remove_file(self.local_path + self.file_temp,
                                self.local_path + self.file_temp)
        dir_handler.remove_file(self.local_path + self.file_converted,
                                self.local_path + self.file_converted)
        if not saveLocal:
            self.save_original_path(self.file_name + '.md')

        print("Converted " + self.file_name + " from " + self.file_type + " to Markdown")

# ==============================================================================
