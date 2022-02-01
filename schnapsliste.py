#!/usr/bin/env python3

import toml
import argparse
import re

#true if all of alist are in blist
def all_in(alist, blist):
    matches = [x for x in alist if x in blist]
    if len(matches) == len(alist):
        return True
    else:
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mischliste', default='mischliste.toml', dest='mischlistendatei', help="Die Datei mit der Mischliste für die Schnäpse.")
    parser.add_argument('-z', '--zutaten', default='zutatenliste.txt', dest='zutatenliste_datei', help="Die Datei mit den vorhanden Zutaten.")
    parser.add_argument('-s', '--schnapsliste', default='schnapsliste.txt', dest='schnapsliste_datei', help="Die Datei mit den Ergebnissen.")
    
    args = parser.parse_args()

    zutatenliste = []
    with open(args.zutatenliste_datei, 'r') as zutatenliste_fd:
        zutatenliste = [line.rstrip() for line in zutatenliste_fd]
    zutatenliste = [zutat for zutat in zutatenliste if not re.match("#.*", zutat)] 
    #print(zutatenliste)
    #print("\n\n")

    mischliste_dict = toml.load(args.mischlistendatei)
    mischliste = list(mischliste_dict["shots"].items())
    #print(mischliste)
    #print("\n\n")

    schnapsliste = [shot[1]["name"] for shot in mischliste if all_in([zutat["name"] for zutat in shot[1]["zutaten"]], zutatenliste)]
    print(schnapsliste)

    with open(args.schnapsliste_datei, 'w') as schnapsliste_fd:
        for schnaps in schnapsliste:
            schnapsliste_fd.writelines(schnaps+'\n')
