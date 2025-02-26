class Client:
    def __init__(self, fullName, email, direction, note):
        self.fullName = fullName
        self.email = email
        self.direction = direction
        self.note = note


    def toDBCollection(self):
        return{
            'fullName': self.fullName,
            'email' : self.email,
            'direction' : self.direction,
            'note' : self.note
        }