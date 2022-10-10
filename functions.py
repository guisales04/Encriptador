import json


def encript(msg: str = "Olá Mundo!") -> str:
    first_encript = ""
    final_message = ""
    file = open("combinations.json", "r")
    # Obtendo a lista de caracteres
    combs = file.read()
    file.close()
    combinations = json.loads(combs)

    # Substituindo os caracteres pela primeira combinação
    for letra in range(len(msg)):
        first_encript += combinations["encript"]["first"][msg[letra].upper()]

    # Substituindo os caracteres pela segunda combinação
    for letra in range(len(first_encript)):
        final_message += (combinations["encript"]
                          ["second"][first_encript[letra].upper()])

    return final_message


def decript(msg: str) -> str:
    first_decript = ""
    final_message = ""
    file = open("combinations.json", "r")
    combs = file.read()
    file.close
    combinations = json.loads(combs)

    for letra in range(len(msg)):
        first_decript += combinations["decript"]["second"][msg[letra].upper()]

    for letra in range(len(first_decript)):
        final_message += (combinations["decript"]
                          ["first"][first_decript[letra].upper()])

    return final_message
