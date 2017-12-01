from json import dump

def save(diary:
	with open("diary.db", "w") as fout:
		dump(diary, fout)
