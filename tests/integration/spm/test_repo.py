# -*- coding: utf-8 -*-
"""
Tests for the spm repo
"""
from __future__ import absolute_import, print_function, unicode_literals

import os
import shutil

import pytest
from tests.support.case import SPMCase


@pytest.mark.destructive_test
@pytest.mark.windows_whitelisted
class SPMRepoTest(SPMCase):
    """
    Validate commands related to spm repo
    """

    def setUp(self):
        self.config = self._spm_config()
        self._spm_build_files(self.config)

    @pytest.mark.slow_test(seconds=1)
    def test_spm_create_update_repo(self):
        """
        test spm create_repo
        """
        self._spm_create_update_repo(self.config)

        self.assertTrue(os.path.exists(self.config["spm_db"]))

        l_repo_file = os.path.join(self.config["spm_cache_dir"], "local_repo.p")
        self.assertTrue(os.path.exists(l_repo_file))

    def tearDown(self):
        shutil.rmtree(self._tmp_spm)
