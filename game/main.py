#cachipun.py
import random

options = ["piedra", "papel", "tijera"]

def computer_choice():
    return random.choice(options)

def user_choice():
    user_option = int(input("Elige una opción: \n1- piedra \n2- papel \n3- tijera \n"))
    if user_option == 1:
        return "piedra"
    elif user_option == 2:
        return "papel"
    elif user_option == 3:
        return "tijera"
    else:
        print("Opción no válida. Intenta de nuevo.")
        return user_choice()

def determine_winner(user, computer):
    if user == computer:
        return "Empate"
    elif (user == "piedra" and computer == "tijera") or \
         (user == "papel" and computer == "piedra") or \
         (user == "tijera" and computer == "papel"):
        return "Ganaste"
    else:
        return "Perdiste"
    
#Funcion para iniciar jeugo con contador, al llegar a 3 victorias el contador se acaba el jeugo y se elige un ganador
def play_game():
    user_wins = 0
    computer_wins = 0

    while user_wins < 3 and computer_wins < 3:
        user = user_choice()
        computer = computer_choice()
        print(f"Tu elección: {user}")
        print(f"Computadora eligió: {computer}")
        result = determine_winner(user, computer)   

        print(result)
        if result == "Ganaste":
            user_wins += 1
        elif result == "Perdiste":
            computer_wins += 1
        print(f"Marcador: Tú {user_wins} - Computadora {computer_wins}\n")

    if user_wins == 3:
        print("¡Felicidades! Ganaste el juego.")
    else:
        print("Lo siento, la computadora ganó el juego.")

def main():
    print("Bienvenido al juego de Piedra, Papel o Tijera")
    play_game()
    while True:
        play_again = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if play_again == 's':
            play_game()
        elif play_again == 'n':
            print("Gracias por jugar. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor elige 's' o 'n'.")

if __name__ == "__main__":
    main()