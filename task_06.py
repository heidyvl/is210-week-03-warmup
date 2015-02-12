#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A very long book."""

FHANDLER = open('war_and_peace.txt', 'r')

WORDS = FHANDLER.read()
WORDCT = WORDS.split(); WORDCT = len(WORDCT)

print WORDCT
FHANDLER.close()
