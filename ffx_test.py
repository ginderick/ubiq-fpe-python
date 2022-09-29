#!/usr/bin/env python3

import unittest

import importlib
ffx = importlib.import_module('ubiq-fpe-python.ffx')

class TestFFX(unittest.TestCase):
    def test_context(self):
        self.assertIsNotNone(
            ffx.Context(bytes([0]*32), bytes([0]*7),
                        2**32,
                        0, 7,
                        10, ffx.DEFAULT_ALPHABET))
