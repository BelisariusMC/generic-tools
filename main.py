#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================================================================
# Created By  : BelisariusMC
# Created Date: 19 jun. 2022
# Version     : 1.0.3
# License     : BSD 3-Clause "New" or "Revised" License
# ------------------------------------------------------------------------------
# Generic tools to help development and maintenance of Minecraft mods, modpacks
# and servers. Included features:
# > Excel files to Markdown (.md) tables converter
# > Paper world format to Vanilla format (and vice-versa)
# ==============================================================================
__author__ = "BelisariusMC"
__copyright__ = "Copyright 2022, BelisariusMC"
__license__ = "BSD 3-Clause \"New\" or \"Revised\" License"
__version__ = "1.0.3"
# ==============================================================================
import os

from excel_conv import ExcelMarkdown
from paper_conv import PaperWorld
# ==============================================================================
print('# ' + '=' * 77)
print('Author: ' + __author__)
print('Copyright: ' + __copyright__)
print('License: ' + __license__)
print('Version: ' + __version__)
print('# ' + '=' * 77)
# ------------------------------------------------------------------------------
# TODO: Export system for modpack development from an usable instance
# TODO: modpack conversion (Packwiz, MultiMC, CurseForge, Modrinth)
# ------------------------------------------------------------------------------
"""
Example to convert the Technical Enhanced 1.18.2 mod list from .xlsx to .md

Note that the first five rows aren't necessary, as well as specific properties 
like the jar file name. So pandas arguments are parsed to not generate these 
infos on the final .md table.
"""

modlist_path = os.getcwd() + "/example_excel_to_md/MODLIST.xlsx"
ExcelMarkdown(modlist_path).to_markdown(skiprows=5, header=None, usecols=range(0, 6))
# excel_to_md('MODLIST.xlsx').to_markdown(skiprows=5, header=None, usecols=range(0, 6))
# ------------------------------------------------------------------------------
""" Example to convert a Paper world into a Vanilla world """

root_path = os.getcwd() + "/example_paper_to_vanilla"
world_paper_path = root_path + "/world_paper"
world_vanilla_path = root_path + "/world_vanilla"

PaperWorld(world_paper_path, world_vanilla_path).paper_to_vanilla()
# ==============================================================================
