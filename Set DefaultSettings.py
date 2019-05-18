import pickle

options = {
	"Pong : Joueur 1 - Gauche": "left",
	"Pong : Joueur 1 - Droite": "right",
	"Pong : Joueur 2 - Gauche": "q",
	"Pong : Joueur 2 - Droite": "d",
	"Pong : Musique": "Activée",
}

with open("DefaultSettings", "wb") as file:
	a = pickle.Pickler(file)
	a.dump(options)

with open("DefaultSettings", "rb") as file:
	a = pickle.Unpickler(file)
	readoptions = a.load()

for name in options:
	print(name, ":", options[name])