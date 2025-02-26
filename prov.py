class Prov:
    def __init__(self, namePro, email, direction, phone):
        self.namePro = namePro
        self.email = email
        self.direction = direction
        self.phone = phone

    def toDBCollection(self):
        return{
            "namePro" : self.namePro,
            "email" : self.email,
            "direction" : self.direction,
            "phone" : self.phone
        }