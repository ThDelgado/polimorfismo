class Persona:
    def __init__(self, nombre:str) -> None:
        self.nombre = nombre

        def caminar(self):
            return f"{self.nombre} esta caminando"

class Maratonista(Persona):

    def __init__(self, nombre:str) -> None:
        super().__init__(nombre)
        self.velocidad = 16
        

    def caminar(self):
        return f"{self.nombre} esta caminando a {self.velocidad}  km/hr"
    
    def trotando(self):
        return f"{self.nombre} esta trotando a {self.velocidad}  km/hr"

class Ciclista(Persona):

    def __init__(self, nombre:str) -> None:
        super().__init__(nombre)
        self.velocidad = 40

    def caminar(self) -> None:
        velocidad = self.velocidad/40
        return f"{self.nombre} esta caminando a {self.velocidad} km/hora"

    def trotando(self) -> str:
        return f"El ciclisgta {self.nombre()} esta rodando a {self.velocidad} km/h"

maratonista = Maratonista("Hugo")
ciclista = Ciclista("Pedro")

print(maratonista.caminar())
print(maratonista.trotando())

print()
print(ciclista.caminar())