# Schnapsliste

Dies ist ein kleines Script für die [Schnapspause](http://schnapspause.info/) beim Metalmittwoch im [Z10](https://z10.info/) um Schnapslisten aus der Auswahl an vorhandenen Schnäpsen zu erzeugen.

## Installation
Es wird benötigt: python3, am besten erstellt man dann eine virtuelle python-Umgebung und installiert die Abhängigkeiten:
```bash
  mkdir schnapsliste
  cd schnapsliste
  python3 -m venv .
  source bin/activate
  pip install toml
  pip install argparse
  git clone ...
  cd schnapsliste
  chmod +x get_list.py
  
  ## optional
  deactivate # Falls man es nicht direkt ausführen will um die virtuelle python-Umgebung wieder zu verlassen
  ##
```

## Benutzung
Es gibt zwei Dateien im [toml](https://toml.io/en/)-Format eine mit den Mischlisten und eine mit den Vorhandenen Zutaten (siehe Beispieldateien)

```bash
  ## optional
  # in das entsprechende Verzeichnis wechseln (siehe Installation)
  source ../bin/activate # falls noch nicht zuvor ausgeführt, also direkt nach der Installation ist es nicht nötig
  ##
  
  ./get_list.py <mischliste> <vorhandene_zutaten>
  
  ## optional
  deactivate # Falls man es nicht nochmal ausführen will um die virtuelle python-Umgebung wieder zu verlassen
  ##
```
Man erhält eine Liste mit den möglichen Schnäpsen aus diesen Zutaten.
