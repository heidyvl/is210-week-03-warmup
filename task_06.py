#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A very long book."""

FHANDLER = open('war_and_peace.txt', 'r')

WORDS = FHANDLER.read()
WORDS.split(); WORDCT =len(WORDS)
print WORDCT
FHANDLER.close()
