# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, update_quality


class GildedRoseTest(unittest.TestCase):
    def test_foo(self) -> None:
        items = [Item("foo", 0, 0)]
        update_quality(items)
        self.assertEqual("foo", items[0].name)


if __name__ == "__main__":
    unittest.main()
