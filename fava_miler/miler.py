#!/usr/bin/env python3
# Description: Beancount Tax Loss Harvester

import argparse,argcomplete,argh
import libmiler
import fava_miler.common.beancountinvestorapi as api
from fava_miler.common.clicommon import *

def miler(beancount_file,
        accounts_pattern='^Assets.*Reward',
        exclude_currencies='POINTS',
        ):
    """Miles expiration, value"""
    accapi = api.AccAPI(beancount_file, locals())
    result = libmiler.get_miles_expirations(accapi, accapi.options)
    pretty_print_table(*result)

#-----------------------------------------------------------------------------
def main():
    parser = argh.ArghParser(description="Beancount Miler: Rewards Miles")
    argh.set_default_command(parser, miler)
    argh.completion.autocomplete(parser)
    parser.dispatch()

if __name__ == '__main__':
    main()
