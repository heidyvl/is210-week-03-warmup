#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Task 12"""
from fractions import Fraction
from decimal import Decimal
INTVAL = 1
FLOATVAL = round(Decimal(0.1), 1)
DECVAL = Decimal(1)/Decimal(10)
FRACVAL = Fraction('1/10')

print INTVAL
print FLOATVAL
print DECVAL
print FRACVAL
