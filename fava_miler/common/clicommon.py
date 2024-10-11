#!/usr/bin/env python3
# Description: CLI tools

import tabulate
tabulate.PRESERVE_WHITESPACE = True


def pretty_print_table(rtypes, rrows, **tabulate_options):
    headers = [i[0] for i in rtypes]
    tabulate_options.setdefault('tablefmt', 'simple')
    print(tabulate.tabulate(rrows,
                            headers=headers[1:],  # Skip the first header as per your logic
                            **tabulate_options))



def pretty_print_table_bare(rrows):
    print(tabulate.tabulate(rrows, tablefmt='simple'))
