import string
import random
def gerar_senha(tamanho):
    alfabeto = string.ascii_letters
    numeros = string.digits
    simbolo = string.punctuation

    todos_caracteres = ""
    while True:
        letras = input("Quer letras? [S/N] ").upper()
        if letras == "S":
            todos_caracteres += alfabeto
            
        quer_numero = input("Quer numeros? [S/N] ").upper()
        if quer_numero == "S":
            todos_caracteres += numeros
            
        quer_simbolos = input("Quer simbolos? [S/N] ").upper()
        if quer_simbolos == "S":
            todos_caracteres += simbolo
            
        if todos_caracteres != "":
            break
        else:
            print("Escolha pelo menos uma opção")
        
    senha_lista = random.choices(todos_caracteres, k=tamanho)
    senha_final = "".join(senha_lista)

    print(f"{senha_final}")
    print("")
 
   
i = 1
quantidade = int(input("Quantas senhas você quer: "))
tamanho = int(input("Diga o tamanho da sua senha: "))
    
while i <= quantidade:
    gerar_senha(tamanho)
    i += 1
    