from artNumbers import logo
import random

numbers = list(range(1, 101))

target = random.choice(numbers)

print(logo)
print("Bienvenido al juego de los números")

game_level = input("Estoy pensando en un número entre el 1 y el 100. ¿Puedes adivinarlo?\nEscoge el nivel de dificultad: Escribe 'pro' 'intermedio' o 'noob': ")

if game_level == "pro":
    chances = 5
elif game_level == "intermedio":
    chances = 7
elif game_level == "noob":
    chances = 10
else:
    print("No entendí lo que escogiste. Te voy a asignar 'noob'")

while chances > 0:
    print(f"Te quedan {chances} oportunidades para adivinar el número.")
    guess_number = int(input("Adivina el número: "))
    if guess_number == target:
        print(f"Lo lograste! El número era {target}")
        break
    elif guess_number > target:
        print("Muy alto.")
        if chances == 1:
            print("Lo siento, perdiste :(")
    else:
        print("Muy bajo.")
        if chances == 1:
            print("Lo siento, perdiste :(")
    chances = chances - 1
