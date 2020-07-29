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


def scrub(text):
    return "".join([chr for chr in text if chr.isalnum()])


def create_room():
    pass


def create_inventory():
    pass


def show_inventory():
    pass


def show_value():
    pass


def main_menu():
    menu = dict()

    menu["1"] = "Create new room"
    menu["2"] = "Create new inventory"
    menu["3"] = "Show inventory list"
    menu["4"] = "Show total value"
    menu["5"] = "Quit"

    while True:
        print("\n")
        for item, description in sorted(menu.items()):
            print(f"{item}) {description}")
        print()

        choice = scrub(input("Please chose an action > "))
        if choice == "1":
            create_room()
        elif choice == "2":
            create_inventory()
        elif choice == "3":
            show_inventory()
        elif choice == "4":
            show_value()
        elif choice == "5":
            sys.exit()
        else:
            print("\n=== Invalid input. Please try again! ===\n")


main_menu()
