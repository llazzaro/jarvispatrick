#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_jarvispatrick
----------------------------------

Tests for `jarvispatrick` module.
"""

import unittest

from jarvispatrick import JarvisPatrick


class TestJarvisPatrick(unittest.TestCase):

    def test_small_case(self):

        def hardcoded_length(element, element2):
            if element in [1, 2] and element2 in [1, 2]:
                return 0.6
            if element in [1, 3] and element2 in [1, 3]:
                return 0.55
            if element in [2, 3] and element2 in [2, 3]:
                return 0.67
            if element in [2, 4] and element2 in [2, 4]:
                return 0.9
            if element in [4, 5] and element2 in [4, 5]:
                return 0.6
            if element in [4, 6] and element2 in [4, 6]:
                return 0.57
            if element in [5, 6] and element2 in [5, 6]:
                return 0.7
            if element in [5, 8] and element2 in [5, 8]:
                return 0.88
            if element in [3, 8] and element2 in [3, 8]:
                return 0.9

            return 1.0

        elements = [1, 2, 3, 4, 5, 6, 7, 8]
        clustering = JarvisPatrick(elements, hardcoded_length)
        cluster = clustering(3, 2)
        self.assertEquals(cluster, {1: 0, 2: 0, 3: 0, 4: 3, 5: 3, 6: 3, 7: 6, 8: 7})


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
