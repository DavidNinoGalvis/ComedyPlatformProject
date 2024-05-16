class Artist:
    def __init__(self, name, genre, bio, city):
        self.name = name
        self.genre = genre
        self.bio = bio
        self.city = city

    def updateBio(self, newBio):
        self.bio = newBio

    def updateGenre(self, newGenre):
        self.genre = newGenre

    def updateCity(self, newCity):
        self.city = newCity