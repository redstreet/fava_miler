"""Airline miles and rewards points expiry tracker"""

from fava.ext import FavaExtensionBase
from . import libmiler
from .common.favainvestorapi import *

class Miler(FavaExtensionBase):  # pragma: no cover
    """Airline miles and rewards points expiry tracker"""
    report_title = "Miler"

    def build_miles_tables(self):
        """Build main table"""
        accapi = FavaInvestorAPI(self.ledger)
        return libmiler.get_miles_expirations(accapi, self.config)
