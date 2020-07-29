#!/usr/bin/env python3

"""
HomeInventory.py

Author: Dr. Andreas Janzen, janzen@gmx.net
Date: 2020-07-29
"""

import sqlite3
import sys

from contextlib import contextmanager


DBNAME = "HomeInventory"

