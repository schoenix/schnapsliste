#!/usr/bin/env python3

import toml
import argparse
import re
from os.path import exists

def auskommentieren(zutat, zutatenliste_auskommentiert):
    if zutat in zutatenliste_auskommentiert:
        return "#" + zutat
    else:
        return zutat

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mischliste', default='mischliste.toml', dest='mischlistendatei', help="Die Datei mit der Mischliste für die Schnäpse.")
    parser.add_argument('-z', '--zutatenliste', default='zutatenliste.txt', dest='zutatenliste_datei', help="Die Datei mit den Ergebnissen (die Zutatenliste für alle Shots).")
    
    args = parser.parse_args()

    mischliste_dict = toml.load(args.mischlistendatei)
    mischliste = list(mischliste_dict["shots"].items())

    zutatenliste_alt = []
    if exists(args.zutatenliste_datei):
        with open(args.zutatenliste_datei, 'r') as zutatenliste_alt_fd:
            zutatenliste_alt = [line.rstrip() for line in zutatenliste_alt_fd]
    zutatenliste_auskommentiert = [zutat for zutat in zutatenliste_alt if re.match("#.*", zutat)] 
    print(zutatenliste_auskommentiert)
    print("\n")
    zutatenliste_auskommentiert = [zutat[1:] for zutat in zutatenliste_auskommentiert]
    print(zutatenliste_auskommentiert)
    print("\n")

    zutatenliste = [zutat["name"] for shot in mischliste for zutat in shot[1]["zutaten"]]
    zutatenliste = list(dict.fromkeys(zutatenliste))
    zutatenliste.sort()
    print(zutatenliste)
    print("\n")

    zutatenliste = [auskommentieren(zutat, zutatenliste_auskommentiert) for zutat in zutatenliste]
    print(zutatenliste)

    with open(args.zutatenliste_datei, 'w') as all_zutatenliste_fd:
        for zutat in zutatenliste:
            all_zutatenliste_fd.writelines(zutat+'\n')
