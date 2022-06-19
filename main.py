#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================================================================
# Created By  : BelisariusMC
# Created Date: 19 jun. 2022
# Version     : 1.0.0
# License     : BSD 3-Clause "New" or "Revised" License
# ------------------------------------------------------------------------------
# Generic tools to help development and maintenance of Minecraft mods, modpacks
# and servers. Included features:
# > Excel files to Markdown (.md) tables converter
# > Paper world format to Vanilla format (and vice-versa)
# ==============================================================================
# from __future__ import *
# ------------------------------------------------------------------------------
__author__ = "BelisariusMC"
__copyright__ = "Copyright 2022, BelisariusMC"
__credits__ = ["BelisariusMC"]
__license__ = "BSD 3-Clause \"New\" or \"Revised\" License"
__version__ = "1.0.0"
__maintainer__ = "BelisariusMC"
__email__ = "belisariusmc@gmail.com"
__status__ = "Development"
# ==============================================================================
# Built-in/Generic Imports
# Libs
# Own modules
from excel_to_md import *
from paper_to_vanilla import *
# ==============================================================================
print('# ' + '=' * 78)
print('Author: ' + __author__)
print('Copyright: ' + __copyright__)
print('Credits: ' + ', '.join(__credits__))
print('License: ' + __license__)
print('Version: ' + __version__)
print('Maintainer: ' + __maintainer__)
print('Email: ' + __email__)
print('Status: ' + __status__)
print('# ' + '=' * 78)
# ------------------------------------------------------------------------------
"""
Example to convert the Technical Enhanced 1.18.2 mod list from .xlsx to .md

Note that the first five rows aren't necessary, as well as specific properties 
like the jar file name. So pandas arguments are parsed to not generate these 
infos on the final .md table.
"""

Excel_to_md('MODLIST.xlsx').to_markdown(skiprows=5, header=None, usecols=range(0, 6))
# ------------------------------------------------------------------------------
""" Example to convert a Paper world into a Vanilla world """

root_path = "D:/Projects/generic-tools (minecraft)/paper_to_vanilla_example/"
world_paper_path = "world_paper"
world_vanilla_path = "world_vanilla"

Paper_to_vanilla(root_path, world_paper_path, world_vanilla_path).paper_to_vanilla()
# ==============================================================================
