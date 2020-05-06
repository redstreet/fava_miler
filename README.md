# fava_miler
Airline miles and rewards points: expiration and value reporting for Fava/Beancount
(Personal finance software).

## Introduction
Airline miles and rewards points typically expire after a period of inactivity. They
also can be viewed as having a value in a currency of your choice. If you track airline
mile transactions in Beancount, this simple plugin reports on the value of miles and
their expiry date. This is particularly useful if you have miles/points on many airlines
or businesses.

![Screenshot: Miler](https://images2.imgbox.com/7f/84/rnlNN133_o.png)

## Installation
```bash
pip install fava-miler
```

### Configuring your beancount source
- Define your `operating_currency`
- Declare the currency for each of your airline miles
- Add `expiry-months` and `points-value` metadata to your commodity declaration
  - Any negative value for `expiry-months` signifies that this commodity never expires

This should get the reporter working. Example:

```
option "operating_currency" "USD"
1990-01-01 commodity MILESAIRALD
    expiry-months: 24
    points-value: 0.015 USD

2000-01-01 open Assets:Miles:AirAldorra MILESAIRALD
2000-01-01 open Income:Misc

2010-01-01 * "Credit card miles"
        Assets:Miles:AirAldorra 100 MILESAIRALD
        Income:Misc
```

## Running

### beancount
```
./miler.py --help
```

### fava
Add the following to your source and run fava as you normally would.

```
2010-01-01 custom "fava-extension" "fava_miler" "{
  'accounts_pattern' : '^Assets.*Reward',
  'exclude_currencies' : '(POINTS_ABC)|(POINTS_DEF)',
}"
```
