#!/usr/bin/env python3
"""Beancount Airline Miles/Rewards/Points Manager"""

import click
import fava_miler.libmiler as libmiler
import fava_miler.common.beancountinvestorapi as api
from fava_miler.common.clicommon import pretty_print_table


@click.command()
@click.argument('beancount_file', type=click.Path(exists=True))
@click.option('--accounts-pattern', help='Regex for rewards account to include', default='^Assets.*Reward')
@click.option('--exclude-currencies', help='Comma separated list of points currencies to exclude', default='POINTS')
def miler(beancount_file, accounts_pattern, exclude_currencies):
    """Beancount Miles and Rewards Manager"""
    accapi = api.AccAPI(beancount_file, locals())
    result = libmiler.get_miles_expirations(accapi, accapi.options)
    pretty_print_table(*result)


if __name__ == '__main__':
    miler()
