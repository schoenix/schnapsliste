#!/usr/bin/env python3

import toml
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='mischlistendatei', help="Die Datei mit der Mischliste für die Schnäpse")
    parser.add_argument(dest='zutaten_datei', help="Die Datei mit den vorhanden Zutaten")
    
    args = parser.parse_args()
    print(args.mischlistendatei)
    print(args.zutaten_datei)

    mischliste_dict = toml.load(args.mischlistendatei)
    zutaten_dict = toml.load(args.zutaten_datei)
    zutatenliste = zutaten_dict["zutaten"]
    print(zutatenliste)

    mischliste = list(mischliste_dict["shots"].items())
    print(mischliste[0][1])
