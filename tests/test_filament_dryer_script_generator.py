#!/usr/bin/env python

"""Tests for `filament_dryer_script_generator` package."""


import io
import unittest

import pytest

import filament_dryer_script_generator as script_generator


class TestFilament_dryer_script_generator(unittest.TestCase):
    """Tests for `filament_dryer_script_generator` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_no_heaters(self):
        with pytest.raises(Exception) as _:
            with io.BytesIO() as handle:
                script_generator.create_script(handle, 300, 70, False, False)

    def test_create_script_1(self):
        with io.BytesIO() as handle:
            script_generator.create_script(handle, 300, 70, True, True)

    def test_create_script_2(self):
        with io.BytesIO() as handle:
            script_generator.create_script(handle, 300, 70, True, False)

    def test_create_script_3(self):
        with io.BytesIO() as handle:
            script_generator.create_script(handle, 300, 70, False, True)

    def test_create_file_abs(self):
        script_generator.create_file(
            "samples/ABS_Filament-Dryer.gcode", 300, 70, True, True
        )

    def test_create_file_nylon(self):
        script_generator.create_file(
            "samples/NYLON_Filament-Dryer.gcode", 360, 74, True, True
        )

    def test_create_file_pla(self):
        script_generator.create_file(
            "samples/PLA_Filament-Dryer.gcode", 240, 50, True, True
        )

    def test_create_file_tpu(self):
        script_generator.create_file(
            "samples/TPU_Filament-Dryer.gcode", 240, 45, True, True
        )
