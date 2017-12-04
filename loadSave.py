from json import dump

def save(dairy):
    with open("dairy.db", "w") as fout:
        dump(dairy, fout)
		
