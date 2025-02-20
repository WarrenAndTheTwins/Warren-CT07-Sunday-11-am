# print("Hello from lesson 4")

# solar_system = [
#     "Mercury",
#     "Venus",
#     "Earth",
#     "POOP LAND",
#     "free chimichangas here",
#     "I can't defeat you-",
#     "But he can",
# ]
# solar_system.append ("Potato")

# print(solar_system.pop(3))
# del(solar_system[5])
# for ppphhhkkkkk in solar_system:
#     print(str(ppphhhkkkkk))

# listLOL = [1,2,3,4,5,6]

# import random

# pokemons = [
#     "Pikachu", "Charizard", "Bulbasaur", "Squirtle",
#     "Jigglypuff", "Meowth", "Psyduck", "Eevee", "Snorlax",
#     "Mewtwo", "Lapras", "Gengar", "Dragonite", "Machamp",
#     "Arcanine", "Alakazam", "Gyarados", "Vaporeon", "Scyther",
#     "Electabuzz"
# ]

# powers = [
#     55, 84, 49, 48, 45,
#     45, 52, 55, 110, 110,
#     85, 65, 134, 130, 110,
#     50, 125, 65, 110, 83
# ]

# choose1 = random.choice (pokemons)

# num1 = pokemons.index(choose1)

# power1 = powers[num1]

# choose2 = random.choice (pokemons)

# num2 = pokemons.index(choose2)

# power2 = powers[num2]

# if power1 > power2:
#     print(choose1 + " wins!")
# elif power1 < power2:
#     print(choose2 + " wins!")
# else:
#     print("There's a tie!")

# students = [
#     ["Olivia", "F"], ["Noah", "M"], ["Emma", "F"],
#     ["Liam", "M"], ["Ava", "F"], ["Ethan", "M"],
#     ["Sophia", "F"], ["Lucas", "M"], ["Mia", "F"],
#     ["Aiden", "M"], ["Isabella", "F"], ["Jackson", "M"],
#     ["Amelia", "F"], ["Logan", "M"], ["Lily", "F"]
# ]
# for student in students:
#     name, gender = student
#     print(name + " is a " + gender + "." )
chipi = 0
chipi_man = ""
chapa_man = ""
chapa = 0
while True:
    chosen = input("Choose a word:")
    if len(chosen) <3:
        print("too short")
    elif len(chosen) != len(set(chosen)):
        print("repeated letters.")
    elif len(chosen) >15:
        print("too long")
    else:
        print("filler")
        print("filler")
        print("filler")
        print("filler")
        print("filler")
        print("filler")
        print("filler")
        print("filler")
        print("filler")
        print("filler")
        print("filler")
        print("filler")
        print("filler")
        print("filler")
        print("filler")
        print("filler")
        print("filler")
        print("filler")
    while True:
        
        print("The number of letters is " + str(len(chosen)))
        guess = input("Guess!") 
        if len(guess)> 1:
            print("nah bro, thats not a letter")
        if guess in chosen:
            if guess not in chipi_man:
                print("Yup!")
                chipi += 1
                chipi_man = chipi_man + "guess"
        else:
            print("nope!")
            chapa_man = chapa_man + "guess"
            if guess not in chapa_man:
                chapa += 1
        if chipi == len(chosen):
            print("you win!")
        
        if chapa > 7: 
            print("you lose")
        break
    break

        