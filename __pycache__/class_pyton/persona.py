from interface_persona import InterfacePersona

class Persona(InterfacePersona):

    def get_full_name(self)->str:
        return self.name + ' ' + self.lastName

    def set_name(self, name:str)->str:
        self.name = name

    def set_lastName(self, lastName:str)->str:
        self.lastName = lastName 




persona = Persona()
persona.set_name('wilmer') 
persona.set_lastName('López')
print(persona.get_full_name())
