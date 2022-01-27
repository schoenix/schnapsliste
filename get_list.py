#!/usr/bin/env python3

import toml
import argparse

#true if all of alist are in blist
def all_in(alist, blist):
    matches = [x for x in alist if x in blist]
    if len(matches) == len(alist):
        True
    else:
        False

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mischliste', default='mischliste.toml', dest='mischlistendatei', help="Die Datei mit der Mischliste für die Schnäpse.")
    parser.add_argument('-z', '--zutaten', default='vorhandene_zutaten.toml', dest='vzutaten_datei', help="Die Datei mit den vorhanden Zutaten.")
    parser.add_argument('-s', '--schnapsliste', default='schnapsliste.toml', dest='schnapsliste_datei', help="Die Datei mit den Ergebnissen.")
    
    args = parser.parse_args()

    mischliste_dict = toml.load(args.mischlistendatei)
    vzutaten_dict = toml.load(args.vzutaten_datei)
    vzutatenliste = vzutaten_dict["zutaten"]

    mischliste = list(mischliste_dict["shots"].items())

    schnapsliste = [shot[1]["name"] for shot in mischliste if [zutat["name"] for zutat in shot[1]["zutaten"]] == vzutatenliste]
    schnapsliste_dict = { "shots": schnapsliste }

    with open(args.schnapsliste_datei, 'w') as schnapsliste_fd:
        toml.dump(schnapsliste_dict, schnapsliste_fd)
