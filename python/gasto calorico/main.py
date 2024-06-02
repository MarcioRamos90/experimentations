import json


class Pessoa:
    def __init__(self, peso_em_kg, altura_em_cm, idade_em_anos, gasto_escedente) -> None:
        self.peso_em_kg = peso_em_kg
        self.altura_em_cm = altura_em_cm
        self.idade_em_anos = idade_em_anos
        self.gasto_escedente = gasto_escedente
        self.eaten = 0
        self.basal = 0
        self.total = 0

    def calcula():
        pass
    
    def total_dia(self, eaten):
        total_dia = self.basal - eaten
        self.total += total_dia
        return total_dia


class Homem(Pessoa):
    def __init__(self, peso_em_kg, altura_em_cm, idade_em_anos, gasto_escedente) -> None:
        super().__init__(peso_em_kg, altura_em_cm, idade_em_anos, gasto_escedente)
    
    def calcula(self):
        self.basal = int(88.362 + (13.397 * self.peso_em_kg) + (4.799 * self.altura_em_cm) - (5.677 * self.idade_em_anos) + self.gasto_escedente)
        

class Mulher(Pessoa):
    def __init__(self, peso_em_kg, altura_em_cm, idade_em_anos, gasto_escedente) -> None:
        super().__init__(peso_em_kg, altura_em_cm, idade_em_anos, gasto_escedente)
    
    def calcula(self):
        self.basal =  int(88.362 + (13.397 * self.peso_em_kg) + (4.799 * self.altura_em_cm) - (5.677 * self.idade_em_anos) + self.gasto_escedente)

homi = Homem(
    peso_em_kg = 103,
    altura_em_cm = 170,
    idade_em_anos = 34,
    gasto_escedente = 500,
)

muie = Mulher(
    peso_em_kg = 85,
    altura_em_cm = 165,
    idade_em_anos = 30,
    gasto_escedente = 500,
)

homi.calcula()
muie.calcula()

with open("./gasto_diario.json", "r") as f:
    arquivo = json.load(f)


print()
print("homi")
for day, data in arquivo.items():
    if data["man"]:
        for value in data["man"]["items"]:
            print(f"total dia {day}:", homi.total_dia(value["value"]))


print("homi emagreceu até agora", homi.total)


print()
print("muie")
for day, data in arquivo.items():
    if data["woman"]:
        for value in data["woman"]["items"]:
            print(f"total dia {day}:", muie.total_dia(value["value"]))


print("a muie emagreceu até agora", muie.total)
