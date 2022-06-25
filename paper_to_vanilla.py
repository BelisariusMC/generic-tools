#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================================================================
# Created By  : BelisariusMC
# Created Date: 19 jun. 2022
# Version     : 1.0.2
# License     : BSD 3-Clause "New" or "Revised" License
# ==============================================================================
from dir_handler import *
# ==============================================================================


class paper_to_vanilla:

    def __init__(self, world_paper_path, world_vanilla_path):
        self.world_paper_path = world_paper_path
        self.world_vanilla_path = world_vanilla_path

    def paper_to_vanilla(self):
        dir_handler.copy_dir(self.world_paper_path, self.world_vanilla_path,
                             "Paper world", "Vanilla world")
        dir_handler.copy_dir(self.world_paper_path + "_nether/DIM-1",
                             self.world_vanilla_path + "/DIM-1",
                             "Paper world_nether", "Vanilla world")
        dir_handler.copy_dir(self.world_paper_path + "_the_end/DIM1",
                             self.world_vanilla_path + "/DIM1",
                             "Paper world_the_end", "Vanilla world")
        dir_handler.remove_file(self.world_vanilla_path + "/paper-world.yml", "Paper stuff")
        dir_handler.remove_dir(self.world_vanilla_path + '/datapacks/bukkit', "Paper stuff")

        print("Converted Paper worlds " + self.world_paper_path + ", " + self.world_paper_path + "_nether, " +
              self.world_paper_path + "_the_end" + " to Vanilla world " + self.world_vanilla_path)

    def vanilla_to_paper(self):
        """ Note: Paper handles this automatically when migrating from Vanilla """
        print("Note: Paper handles this automatically when migrating from Vanilla")

        dir_handler.copy_dir(self.world_vanilla_path, self.world_paper_path,
                             "Vanilla world", "Paper world")
        dir_handler.copy_dir(self.world_vanilla_path + "/DIM-1",
                             self.world_paper_path + "_nether/DIM-1",
                             "Vanilla world nether", "Paper world_nether")
        dir_handler.copy_dir(self.world_vanilla_path + "/DIM1",
                             self.world_paper_path + "_the_end/DIM1",
                             "Vanilla world the end", "Paper world_the_end")

        print("Converted Vanilla world " + self.world_vanilla_path + " to Paper worlds " +
              self.world_paper_path + ", " + self.world_paper_path + "_nether, " + self.world_paper_path + "_the_end")

# ==============================================================================
