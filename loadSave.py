from json import dump

def guardar(agenda):
	with open("agenda.db", "w") as fout:
		dump(agenda, fout)
