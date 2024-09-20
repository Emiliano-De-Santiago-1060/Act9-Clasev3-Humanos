print("Act 9 clase humano")
print("Emiliano De Santiago Soto, 22308051281060")

print("")
# Zona De Clases
class Humano1060:
    # Zona de atributos
    edad=0
    genero=""
    colordeojos=""
    colordepelo=""
    estatura=0
    musicafav=""
# Zona de funciones dentro de la clase
    def cantar1060(self, n):
        print(f"{n} esta cantando")
    
    def escuchar1060(self, n):
        print(f"{n} esta escuchando a Caifanes")
        
    def manejar1060(self, n):
        print(f"{n} esta manejando")
        
    def querer1060(self, n):
        print(f"{n} quiere una novia")


# Zona de creación de objetos
Emi=Humano1060()
Edgar=Humano1060()
# Zona usando objetos

Emi.edad=17
Emi.genero="masculino"
Emi.colordeojos="cafe"
Emi.colordepelo="negro"
Emi.estatura=1.82
Emi.musicafav="Gustavo Cerati"

print("Resultado para Emi")
print(f"Edad: {Emi.edad}")
print(f"Emi es del genero: {Emi.genero}")
print(f"Los ojos de emi con color: {Emi.colordeojos}")
print(f"El color de cabello de emi es: {Emi.colordepelo}")
print(f"Emi mide: {Emi.estatura}")
print(f"LA musica fav de emi es de: {Emi.musicafav}")

print("")

Edgar.edad=17
Edgar.genero="masculino"
Edgar.colordeojos="cafe"
Edgar.colordepelo="castaño claro"
Edgar.estatura=1.80
Edgar.musicafav="Junior H"

print("")

print("")
print("Resultado para Edgar")
print(f"Edad: {Edgar.edad}")
print(f"Edgar es del genero: {Edgar.genero}")
print(f"Los ojos de Edgar con color: {Edgar.colordeojos}")
print(f"El color de cabello de Edgar es: {Edgar.colordepelo}")
print(f"Edgar mide: {Edgar.estatura}")
print(f"La musica fav de Edgar es de: {Edgar.musicafav}")

print("")

# Zona usando funciones
print("Resultado para Emi")
Emi.cantar1060("Emi")
Emi.escuchar1060("Emi")
Emi.manejar1060("Emi")
Emi.querer1060("Emi")

print("")
print("Resultado para Edgar")
Edgar.cantar1060("Edgar")
Edgar.escuchar1060("Edgar")
Edgar.manejar1060("Edgar")
Edgar.querer1060("Edgar")