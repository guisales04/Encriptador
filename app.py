from os import system
from functions import encript, decript


while True:
    system("cls")
    print(f"""{"=-" * 30}
    Encriptador & Decriptador de Mensagem:
    1 - Encriptar Mensagem
    2 - Decriptar Mensagem
    3 - Sair
{"=-" * 30}""")

    choice = input("Selecione a opção desejada: ")

    while choice not in ("1", "2", "3"):
        choice = input("Insira uma opção válida: ")

    match choice:
        case "1":
            message = str(input("\nDigite sua mensagem: "))
            print(f"Sua mensagem encriptada: {encript(message)}")
        case "2":
            message = str(input("\nDigite sua mensagem encriptada: "))
            print(f"Sua mensagem decriptada: {decript(message)}")
        case "3":
            print("\n", "Obrigado por usar o nosso encriptador!", sep="")
            break

    choice = input("\n Deseja continuar? [S/N]: ").upper()

    while choice not in ("S", "N"):
        choice = input("Digite apenas S ou N: ").upper()

    if choice == "N":
        print("\n", "Obrigado por usar o nosso encriptador!", sep="")
        break
