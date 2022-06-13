# === HEADER ===
# Project: Excel to Markdown
# Script: main.py
# Author: BelisariusMC
# Creation: 11 jun. 2022
# Last update: 11:37 13 jun. 2022


# === PACKAGES ===
# Tabulate is also required for pandas functions
import pandas as pd
from openpyxl import load_workbook


# === CLASS ===
class Converter:
    """

    """

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
        ws = wb.active  # ws is now an IterableWorksheet

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

    def to_markdown(self, convert_hyperlink=True, md_header="keys", **kwargs):

        if convert_hyperlink:
            Converter(self.file).hyperlink()
            self.file_converted = self.file_name + '_CONVERTED' + self.file_type  # ########

        df = pd.read_excel(self.file_converted, sheet_name=0, **kwargs)
        df = df.fillna('')
        df.to_markdown(buf=self.file_name + '.md', index=False, headers=md_header)


# === MAIN ===
"""
Here is example to convert the VamoDale 1.18.2 mod list from .xlsx to .md

Note that the first five rows aren't necessary, as well as specific properties like the jar file name
So pandas arguments are parsed to not generate these infos on the final .md table
"""

Converter('MODLIST.xlsx').to_markdown(skiprows=5, header=None, usecols=range(0, 5+1))
