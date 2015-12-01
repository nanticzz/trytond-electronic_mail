# This file is part of the electronic_mail module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class ElectronicMailTestCase(ModuleTestCase):
    'Test Electronic Mail module'
    module = 'electronic_mail'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        ElectronicMailTestCase))
    return suite