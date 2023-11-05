import random
from os import system, name

def limpar_tela():
    _ = system('cls')

def game():

    limpar_tela()
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo\n")

    palavras = ["banana", "uva", "morango", "abacate"]

    palavra = random.choice(palavras)

    letras_descobertas = ['-' for letra in palavra]

    chances = 6

    letras_erradas = []

    while chances > 0:
        print(" ".join(letras_descobertas))
        print("\nChances restantes: ", chances)
        print("Letras erradas: ", letras_erradas)

        tentativa = input("\nDigite uma letra: ").lower()

        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
        
        if "_" not in letras_descobertas:
            print("\nVocê venceu! A palavra era ", palavra)
            break

    if "_" not in letras_descobertas:
        print("\nVocê perdeu! A palavra era ", palavra)
      

    
if __name__ == "__main__":
    game()
    #print("")