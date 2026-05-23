import string
import random
def gerar_senha(tamanho):
    alfabeto = string.ascii_letters
    numeros = string.digits
    simbolo = string.punctuation

    while True:
        todos_caracteres = ""
        op = 0
        letras = input("Quer letras? [S/N] ").upper()
        if letras == "S":
            todos_caracteres += alfabeto
            op += 1
            
        quer_numero = input("Quer numeros? [S/N] ").upper()
        if quer_numero == "S":
            todos_caracteres += numeros
            op += 1
            
        quer_simbolos = input("Quer simbolos? [S/N] ").upper()
        if quer_simbolos == "S":
            todos_caracteres += simbolo
            op += 1
            
        if todos_caracteres != "":
            break
        else:
            print("Escolha pelo menos uma opção")
        
    senha_lista = random.choices(todos_caracteres, k=tamanho)
    senha_final = "".join(senha_lista)

    print(f"{senha_final}")
    print("")
    
    if tamanho >= 12 and letras == "S" and quer_numero=="S" and quer_simbolos=="S":
        print("Senha forte")
        
    elif tamanho >= 8 and op >= 2:
        print("Senha mediana")
        
    else:
        print("Senha fraca")
    
def loop_menu():
    while True:
        print("============================================")
        print("             GERADOR DE SENHAS              ")
        print("============================================")
        print(" 1. Gerar Senhas")
        print(" 2. Ver Dicas de Segurança")
        print(" 3. Sair")
        print("============================================")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print("\n --- Configuração Das Senhas ---")
            quantidade = int(input("Quantas senhas você quer: "))
            tamanho = int(input("Diga o tamanho da sua senha: "))
            
            i = 1
        
            while i <= quantidade:
                print(f"\n--- [Senha {i} de {quantidade}] ---")
                gerar_senha(tamanho)
                i += 1
                
        elif opcao == "2":
            print("\n--- DICAS DE SEGURANÇA ---")
            print("* Uma senha forte deve ter pelo menos 12 caracteres.")
            print("* Misture sempre letras, números e símbolos.")
            print("* Evite usar dados pessoais como nomes ou aniversários.\n")
            
        elif opcao == "3":
            print("\nSaindo...")
            break
        
        else:
            print("\nOpção inválida!!!")

loop_menu()