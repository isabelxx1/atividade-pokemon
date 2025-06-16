from classpokemon import *
from classtreinador import *
import random

def batalhaPokemon(meuPokemon, inimigo):
    print("----- BATALHA INICIADA -----")

    print(f"{meuPokemon.especie} X {inimigo.especie}")
    print()
    turnos = 1
    
    hpMax = meuPokemon.hp
    
    while (meuPokemon.hp > 0 and inimigo.hp > 0):
        print(f"----- TURNO {turnos} -----")
        meuPokemon.atacar(inimigo)

        if inimigo.hp <= 0:
            print(f"{inimigo.especie} desmaiou!")
            print(f"{meuPokemon.especie} venceu a batalha contra {inimigo.especie}")
            meuPokemon.xp += 15
            break 
        
        inimigo.atacar(meuPokemon)

        if (meuPokemon.hp <= 0):
            print(f"{meuPokemon.especie} desmaiou!")
            print(f"{inimigo.especie} venceu a batalha contra {meuPokemon.especie}")
            meuPokemon.hp = hpMax
        
            break
        turnos += 1

def gerarPokemonAleatorio():
    numeroPokedex = random.randint(1, 13)

    dados = pokedex[numeroPokedex]

    pokemonAleatorio = Pokemon(numeroPokedex, dados["especie"], dados["tipo"], dados["hp"], dados["atk"], dados["defesa"], dados["xp"], dados["level"])
    print("VOCÊ ENCONTROU UM POKEMON!")
    pokemonAleatorio.mostrarInformacoes()
    return pokemonAleatorio

pokedex = {
    1:  {"especie": "Bulbasaur",    "tipo": "Grama/Veneno", "hp": 45,  "atk": 49,  "defesa": 49, "level": 5, "xp": 5},
    2:  {"especie": "Ivysaur",      "tipo": "Grama/Veneno", "hp": 60,  "atk": 62,  "defesa": 63, "level": 5, "xp": 5},
    3:  {"especie": "Venusaur",     "tipo": "Grama/Veneno", "hp": 80,  "atk": 82,  "defesa": 83, "level": 5, "xp": 5},
    4:  {"especie": "Charmander",   "tipo": "Fogo",         "hp": 39,  "atk": 52,  "defesa": 43, "level": 5, "xp": 5},
    5:  {"especie": "Charizard",    "tipo": "Fogo/Voador",  "hp": 78,  "atk": 84,  "defesa": 78, "level": 5, "xp": 5},
    6:  {"especie": "Squirtle",     "tipo": "Água",         "hp": 44,  "atk": 48,  "defesa": 65, "level": 5, "xp": 5},
    7:  {"especie": "Wartortle",    "tipo": "Água",         "hp": 59,  "atk": 63,  "defesa": 80, "level": 5, "xp": 5},
    8:  {"especie": "Blastoise",    "tipo": "Água",         "hp": 79,  "atk": 83,  "defesa": 100,"level": 5, "xp": 5},
    9: {"especie": "Caterpie",     "tipo": "Inseto",       "hp": 45,  "atk": 30,  "defesa": 35, "level": 5, "xp": 5},
    10: {"especie": "Metapod",      "tipo": "Inseto",       "hp": 50,  "atk": 20,  "defesa": 55, "level": 5, "xp": 5},
    11: {"especie": "Butterfree",   "tipo": "Inseto/Voador","hp": 60,  "atk": 45,  "defesa": 50, "level": 5, "xp": 5},
    12: {"especie": "Weedle",       "tipo": "Inseto/Veneno","hp": 40,  "atk": 35,  "defesa": 30, "level": 5, "xp": 5},
    13: {"especie": "Kakuna",       "tipo": "Inseto/Veneno","hp": 45,  "atk": 25,  "defesa": 50, "level": 5, "xp": 5},
}

jogador = Jogador("Tarik", [])

print("Bem vindo ao mundo Pokemon!")

print("Para começar sua jornada você precisa de um parceiro!")

print()

print('''Escolha um Pokemon abaixo:
      
      
1. Charmander
2. Bulbasaur
3. Squirtle
      
''')

op = input("Digite o número do pokemon desejado: ")

if op == "1":
    pokemonInicial = Pokemon(4,"Charmander", "Fogo", 120, 20, 20, 0, 5)
elif op == "2":
    pokemonInicial = Pokemon(1, "Bulbasaur", "Grama", 100, 20, 20, 0, 5)
elif op == "3":
    pokemonInicial = Pokemon(7, "Squirtle", "Água", 100, 20, 20, 0, 5)
else:
    pokemonInicial = Pokemon(25, "Pikachu", "Elétrico", 100, 20, 20, 0, 5)
    print("Infelizmente esse pokemon não está mais disponível. Você receberá um Pikachu!")

jogador.capturarPokemon(pokemonInicial)

while True:
    print('''
Escolha uma opção do menu abaixo:
          
          1. Capturar Pokemon Aleatório
          2. Batalhar contra Pokemon Aleatório
          3. Ver Pokemons Capturados
          0. Sair

''') 
    op = input("Digite a opção desejada: ")

    if op == "1":
        jogador.capturarPokemon(gerarPokemonAleatorio())
    elif op == "2":
        batalhaPokemon(jogador.escolherPokemon(), gerarPokemonAleatorio())
    elif op == "3":
        jogador.verPokemons()
    elif op == "0":
        print("Você acorda do coma... Foi tudo um sonho... FIM DE JOGO")
        break
    else:
        print("Escolha uma opção válida!")

    input("DIGITE ENTER PARA CONTINUAR")


