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
    parser.add_argument('-s', '--schnapsliste', default='schnapsliste.txt', dest='schnapsliste_datei', help="Die Datei mit den Ergebnissen.")
    parser.add_argument('-d', '--datum', dest='datum', help="Das Datum des Metalmittwoch.")
    
    args = parser.parse_args()
    print(args.datum)

    mischliste_dict = toml.load(args.mischlistendatei)
    mischliste = list(mischliste_dict["shots"].items())
    #print(mischliste)
    #print("\n\n")

    schnapsliste = []
    with open(args.schnapsliste_datei, 'r') as schnapsliste_fd:
        schnapsliste = [line.rstrip() for line in schnapsliste_fd]
    schnapsliste = [schnaps for schnaps in schnapsliste if not re.match("#.*", schnaps)] 

    mischliste_abend = [shot for shot in mischliste if shot[1]["name"] in schnapsliste]

    print(mischliste_abend)

    shots_str = ""
    shots_str += "\documentclass{article}\n"
    shots_str += "\\usepackage{graphicx}\n"
    shots_str += "\\usepackage{array}\n"
    shots_str += "\n"
    shots_str += "\\begin{document}\n"
    shots_str += "    \\pagenumbering{gobble}\n"
    shots_str += "    \\begin{center}\n"
    shots_str += "        {\\Huge Heavy Metal Mittwoch Shots}\n"
    shots_str += "        \\\\[2\\baselineskip]\n"
    shots_str += "        {\\large Shots - 4 cl}\n"
    shots_str += "        \\\\[2\\baselineskip]\n"
    shots_str += "        \\begin{tabular}{ >{\\raggedright}m{5cm}>{\\raggedleft}m{5cm} }\n"
    shots_str += "            %\\hline\n"
    for shot in mischliste_abend:
        shots_str += "            \\includegraphics[height=1cm]{" + shot[1]["logo"] + "} & "+ shot[1]["preis"] +" €\n"
        shots_str += "            \\tabularnewline\n"
    shots_str += "            %\\hline\n"
    shots_str += "        \\end{tabular}\n"
    shots_str += "    \\end{center}\n"
    shots_str += "\\end{document}\n"

    print(shots_str)

    with open(args.datum + '.tex', 'w') as shots_fd:
        shots_fd.write(shots_str)

    mische_str = ""
    mische_str += "\documentclass{article}\n"
    mische_str += "\\usepackage{graphicx}\n"
    mische_str += "\\usepackage{array}\n"
    mische_str += "\n"
    mische_str += "\\begin{document}\n"
    mische_str += "    \\pagenumbering{gobble}\n"
    mische_str += "    \\begin{center}\n"
    mische_str += "        {\\large Heavy Metal Mittwoch Shots}\n"
    mische_str += "        \\\\[2\\baselineskip]\n"
    mische_str += "        {\\large Mischliste}\n"
    mische_str += "        \\\\[2\\baselineskip]\n"
    mische_str += "        {\\large Shots - 4 cl}\n"
    mische_str += "        \\\\[2\\baselineskip]\n"
    mische_str += "        \\begin{tabular}{ |c|c|c| }\n"
    mische_str += "            \\hline\n"
    for shot in mischliste_abend:
        mische_str += "            "+ shot[1]["name"] +" & & \\\\\n"
        for zutat in shot[1]["zutaten"]:
            mische_str += "            & "+ zutat["name"] +" & "+ zutat["menge"] +"\\\\\n"
        mische_str += "            \\hline\n"
    mische_str += "        \\end{tabular}\n"
    mische_str += "    \\end{center}\n"
    mische_str += "\\end{document}\n"

    print(mische_str)

    with open(args.datum + '-mische.tex', 'w') as mische_fd:
        mische_fd.write(mische_str)
