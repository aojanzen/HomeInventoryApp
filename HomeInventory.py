#!/usr/bin/env python3

"""
HomeInventory.py

Author: Dr. Andreas Janzen, janzen@gmx.net
Date: 2020-08-03
"""

import sqlite3
import sys

from contextlib import contextmanager


DB = "HomeInventory.db"


def first_launch():
    """ Creates a new database on first launch """
    try:
        conn = sqlite3.connect(DB)
    except:
        sys.exit(f"Error: could not create database {DB}")


@contextmanager
def access_db():
    """ Generator to yield a DB cursor and close the connection afterwards """
    try:
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        yield cursor
    finally:
        conn.commit()
        conn.close()


def scrub(text):
    """ Removes all non-alphanumeric characters from the input string """ 
    return "".join([chr for chr in text if chr.isalnum()])


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


def create_room():
    name = input("\nWhat name would you like to give the room? > ")
    name = scrub(name)
    with access_db() as cursor:
        cursor.execute("CREATE TABLE '" + name.lower() + "' (Item TEXT, Value REAL)")
    print(f"\nA room with name {name} has been added to the database.\n")


def create_inventory():
    pass


def show_inventory():
    pass


def show_value():
    pass


first_launch()
main_menu()
