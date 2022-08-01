#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================================================================
# Created By  : BelisariusMC
# Created Date: 11 jun. 2022
# Version     : 1.0.3
# License     : BSD 3-Clause "New" or "Revised" License
# ==============================================================================
import os
from openpyxl import load_workbook
import pandas as pd

from dirhandler import DirHandler
# ==============================================================================


class ExcelMarkdown:

    def __init__(self, file, out_path=None):
        # Input
        self.file = os.path.basename(file)
        self.file_path = os.path.dirname(file) + "/"
        self.out_path = out_path

        # Processed
        self.file_name = os.path.splitext(os.path.basename(file))[0]
        self.file_type = os.path.splitext(file)[1]
        self.local_path = os.path.dirname(file) + "/"
        self.file_converted = self.file

    def hyperlink(self, saveLocal=False):

        wb = load_workbook(self.local_path + self.file)
        ws = wb.active

        for row in ws.rows:
            for cell in row:
                try:
                    if len(cell.hyperlink.target) > 0:
                        cell.value = "".join(["[", cell.value, "](", cell.hyperlink.target, ")"])
                except:
                    pass

        self.file_converted = self.file_name + "_CONVERTED" + self.file_type

        if self.out_path is None:
            wb.save(self.local_path + self.file_converted)
        else:
            wb.save(self.out_path + "/" + self.file_converted)
            if saveLocal:
                DirHandler.copy(self.out_path + "/" + self.file_converted, self.local_path)

        print("Converted " + self.file_name + " hyperlink cells to Markdown format")

    def to_markdown(self, convert_hyperlink=True, md_header="keys", **kwargs):

        if convert_hyperlink:
            self.hyperlink(saveLocal=True)
            df = pd.read_excel(self.local_path + self.file_converted, sheet_name=0, **kwargs)
            DirHandler.remove(self.local_path + self.file_converted)
        else:
            df = pd.read_excel(self.local_path + self.file, sheet_name=0, **kwargs)

        df = df.fillna("")

        if self.out_path is None:
            df.to_markdown(buf=self.local_path + self.file_name + ".md", index=False, headers=md_header)
        else:
            df.to_markdown(buf=self.out_path + self.file_name + ".md", index=False, headers=md_header)

        print("Converted " + self.file_name + " from " + self.file_type + " to Markdown")

# ==============================================================================
