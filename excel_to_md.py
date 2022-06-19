#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================================================================
# Created By  : BelisariusMC
# Created Date: 11 jun. 2022
# Version     : 1.0.1
# License     : BSD 3-Clause "New" or "Revised" License
# ==============================================================================
# Libs
from openpyxl import load_workbook
import pandas as pd
# ==============================================================================


class Excel_to_md:

    def __init__(self, file):
        # Input
        self.file = file

        # Processed
        self.file_name = file.split('.', 1)[0]
        self.file_type = '.' + file.split('.', 1)[1]
        self.file_converted = self.file

    def hyperlink(self):
        """
        :return: Excel table with hyperlink cells converted into Markdown format
        """

        wb = load_workbook(self.file)
        # Makes ws an IterableWorksheet
        ws = wb.active

        # Iterate thru all cells and if hyperlink found attempt modification of cell
        for row in ws.rows:
            for cell in row:
                try:
                    if len(cell.hyperlink.target) > 0:
                        # Join cell.value and hyperlink target into string
                        cell.value = "".join(['[', cell.value, '](', cell.hyperlink.target, ')'])
                except:
                    pass

        # Save workbook to original Excel file type
        self.file_converted = self.file_name + '_CONVERTED' + self.file_type
        wb.save(self.file_converted)

        print("Converted " + self.file_name + " hyperlink cells to Markdown format")

    def to_markdown(self, convert_hyperlink=True, md_header="keys", **kwargs):

        if convert_hyperlink:
            Excel_to_md(self.file).hyperlink()
            self.file_converted = self.file_name + '_CONVERTED' + self.file_type  # ########

        df = pd.read_excel(self.file_converted, sheet_name=0, **kwargs)
        df = df.fillna('')
        df.to_markdown(buf=self.file_name + '.md', index=False, headers=md_header)

        print("Converted " + self.file_name + " from " + self.file_type + " to Markdown")


# ==============================================================================
