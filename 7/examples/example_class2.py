# eigene Klasse mit init funktion
#bestimmte Eigenschaften zuweisen
#nach Main diese Class instanzieren

games = []
class Games():
    def __init__(self, g_title, g_genre, g_year, g_price):
        self.g_title = g_title
        self.g_genre = g_genre
        self.g_year = g_year
        self.g_price = g_price



if __name__ == '__main__':
    Battlefield = Games("Battlefield", "Shooter", "2008", "25")
    print Battlefield.g_title

    E = raw_input("Insert a game name")
    F = raw_input("Insert the Genre")
    G = raw_input("Insert the Year")
    H = raw_input("Insert the Price")

    newgame = Games(E,F,G,H)

    games.append(newgame)

    for game in games:
        print game.g_title