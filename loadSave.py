from json import dump
from json import loads
from pathlib import Path

def save(dairy):
    with open("diary.db", "w") as fout:
        dump(dairy, fout)

def load():
	contactos = []
	
	archivoContactos = Path("diary.db")
	
	if archivoContactos.is_file():
		contactos = loads(open("diary.db").read())
		
	return contactos
