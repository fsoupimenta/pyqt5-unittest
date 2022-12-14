import sys
import unittest

from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import *
from app import Calculadora

application = QApplication(sys.argv)

class AppTest(unittest.TestCase):
    def setUp(self):
        self.form = Calculadora()

    def test_default(self):
        self.assertEqual(self.form.display.text(), "")

    def test_button(self):
        okWidget = self.form.button
        QTest.mouseClick(okWidget, Qt.LeftButton)
        self.assertEqual(self.form.display.text(), "2")