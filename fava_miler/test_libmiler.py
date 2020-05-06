#!/usr/bin/env python3

import common.beancountinvestorapi as api
import functools
from beancount.utils import test_utils
import libmiler
from datetime import datetime
from decimal import Decimal
from beancount.core.amount import Amount
# python3 -m unittest discover . to run



class TestScriptCheck(test_utils.TestCase):
    def setUp(self):
        self.options = {}

    @test_utils.docfile
    def test_valid_case(self, f):
        """
        option "operating_currency" "USD"
        1990-01-01 commodity MILESAIRALD
            expiry-months: 24
            points-value: 0.015 USD

        2000-01-01 open Assets:Miles:AirAldorra MILESAIRALD
        2000-01-01 open Income:Misc
        
        2010-01-01 * "Credit card miles"
                Assets:Miles:AirAldorra 100 MILESAIRALD
                Income:Misc
        """
        accapi = api.AccAPI(f, {})

        rtypes, rrows = libmiler.get_miles_expirations(accapi, self.options)
        self.assertEqual(1, len(rrows))
        self.assertEqual(rrows[0].balance, Decimal('100'))
        self.assertEqual(rrows[0].value, Amount(Decimal(1.500), 'USD'))
        self.assertEqual(rrows[0].expiry, datetime.date(datetime(2012, 1, 1)))

    @test_utils.docfile
    def test_no_commodity_decl(self, f):
        """
        option "operating_currency" "USD"
        2000-01-01 open Assets:Miles:AirAldorra MILESAIRALD
        2000-01-01 open Income:Misc
        
        2010-01-01 * "Credit card miles"
                Assets:Miles:AirAldorra 100 MILESAIRALD
                Income:Misc
        """
        accapi = api.AccAPI(f, {})

        rtypes, rrows = libmiler.get_miles_expirations(accapi, self.options)
        self.assertEqual(1, len(rrows))
        self.assertEqual(rrows[0].balance, Decimal('100'))
        self.assertEqual(rrows[0].value, Amount(Decimal(0), 'NONE'))
        self.assertEqual(rrows[0].expiry, datetime.date(datetime(2010, 1, 1)))

