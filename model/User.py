# Implementacion de la clase USUARIO - Creamos el objeto al momento de registrarnos en el Login

class User:
    def __init__(self, username, password, email, address):
        self.username = username
        self.password = password
        self.email = email
        self.address = address

# Algunos metodos para manipular la clase usuario, faltan algunas pero cuando las utilice las implementaré
    def getUsername(self):
        return self.username

    def updatePassword(self, newPassword):
        self.password = newPassword

    def updateEmail(self, newEmail):
        self.email = newEmail

    def updateAddress(self, newAddress):
        self.address = newAddress
