#!/bin/env python3

from beancount.core.number import ZERO, Decimal, D
from beancount.core.amount import Amount
import collections
import datetime

# We want:
# - to set list and expiration policy by {commodity, account} metadata
# - optionally exclude currencies and accounts
# - display both under different tables


def get_miles_expirations(accapi, options):
    """Show expiry of airline miles, rewards points"""

    exclude = ''
    exclude_option = options.get('exclude_currencies', '')
    if exclude_option:
        exclude = "AND not currency ~ '{currencies}'".format(currencies=exclude_option)

    sql = """
       SELECT
         account,
         sum(number) AS Balance,
         currency as Points,
         LAST(date) AS Latest_Transaction
       WHERE
         not currency ~ '{currencies}'
         AND account ~ '{accounts_pattern}'
         {exclude}
       GROUP BY account,Points ORDER BY LAST(date)
    """.format(currencies = accapi.get_operating_currencies_regex(),
            accounts_pattern = options.get('accounts_pattern', 'Assets'),
            exclude=exclude,
    )
    rtypes, rrows = accapi.query_func(sql)
    if not rtypes:
        return [], {}, [[]]

    # our output table is slightly different from our query table:
    retrow_types = rtypes[:-1] +  [('value', int), ('expiry', datetime.date)]
    RetRow = collections.namedtuple('RetRow', [i[0] for i in retrow_types])

    commodities = accapi.get_commodity_directives()
    def get_miles_metadata(miles):
        try:
            return commodities[miles].meta
        except:
            return {}

    ret_rows = []
    for row in rrows:
        meta = get_miles_metadata(row.points)

        value = meta.get('points-value', Amount(Decimal(0), 'NONE'))
        converted_value = Amount(value.number * row.balance, value.currency)

        expiry_months = meta.get('expiry-months', 0)
        if expiry_months >=0:
            expiry = row.latest_transaction + datetime.timedelta(int(expiry_months)*365/12)
        else:
            expiry = datetime.date.max

        ret_rows.append(RetRow(*row[:-1], converted_value, expiry))

    ret_rows.sort(key=lambda r: r[-1])
    return retrow_types, ret_rows
