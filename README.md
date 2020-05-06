# fava_miler
Airline miles and rewards points: expiration and value reporting for Fava/Beancount
(Personal finance software).

## Introduction
Airline miles and rewards points typically expire after a period of inactivity. They
also can be viewed as having a value in a currency of your choice. If you track airline
mile transactions in Beancount, this simple plugin reports on the value of miles and
their expiry date. This is particularly useful if you have miles/points on many airlines
or businesses.

## Installation
```bash
pip install fava-miler
```

### Configuring your beancount source
- Define your `operating_currency`
- Declare the currency for each of your airline miles
- Add `expiry-months` and `points-value` metadata to your commodity declaration

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
