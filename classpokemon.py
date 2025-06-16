class Pokemon:
    def __init__(self, nroPokedex, especie, tipo, hp, atk, defesa, xp=0, level=1, shiny=False):
        self.nroPokedex = nroPokedex
        self.especie = especie
        self.tipo = tipo
        self.hp = hp
        self.atk = atk
        self.defesa = defesa
        self.level = level
        self.xp = xp
        self.shiny = shiny

    def mostrarInformacoes(self):
        print(f'''
------- Poke Entry -------
Número: {self.nroPokedex}
Espécie: {self.especie}
Level: {self.level}
Tipo: {self.tipo}
HP: {self.hp}
ATK: {self.atk}
DEF: {self.defesa}
{'SEU POKÉMON É SHINY!' if self.shiny else 'Pokémon normal'}
''')

    def atacar(self, inimigo):
        if inimigo.hp <= 0:
            print(f"{inimigo.especie} já está desmaiado!")
            return

        dano = int(10 * (self.atk / inimigo.defesa))
        inimigo.hp -= dano
        inimigo.hp = max(inimigo.hp, 0) 

        print(f"{self.especie} atacou {inimigo.especie} e causou {dano} de dano!")
        print(f"{inimigo.especie} possui {inimigo.hp} de vida restante!")