import string
import random
import pyperclip
senhas = []
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
    
    if tamanho >= 12 and letras == "S" and quer_numero=="S" and quer_simbolos=="S":
        senhas.append(f"{senha_final} -> Senha Forte")
        
    elif tamanho >= 8 and op >= 2:
        senhas.append(f"{senha_final} -> Senha Médiana")
    else:
        senhas.append(f"{senha_final} -> Senha Fraca")
        
    with open(r"C:\Users\ruanp\Documents\Projetos\Gerenciador De senhas seguras\senhas.txt", "a") as arquivo:
        if tamanho >= 12 and letras == "S" and quer_numero=="S" and quer_simbolos=="S":
            arquivo.write(f"Senha: {senha_final} -> Segurança Forte\n")
        elif tamanho >= 8 and op >= 2:
            arquivo.write(f"Senha: {senha_final} -> Segurança Médiana\n")
        else:
            arquivo.write(f"Senha: {senha_final} -> Segurança Fraca\n")
    
    quer_salva = input("Quer copiar a senha para a área de transferência? [S/N] ").upper()
    if quer_salva == "S":
        pyperclip.copy(senha_final)
        print("Senha copiada para a área de transferência!")
    
def loop_menu():
    while True:
        print("============================================")
        print("             GERADOR DE SENHAS              ")
        print("============================================")
        print(" 1. Gerar Senhas")
        print(" 2. Ver Dicas de Segurança")
        print(" 3. Ver senhas já criadas")
        print(" 4. Sair")
        print("============================================")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print("\n --- Configuração Das Senhas ---")
            quantidade = int(input("Quantas senhas você quer: "))
            
            i = 1
            senhas.clear()
            while i <= quantidade:
                print(f"\n--- [Senha {i} de {quantidade}] ---")
                tamanho = int(input("Diga o tamanho da sua senha: "))
                gerar_senha(tamanho)
                i += 1
                   
            print("=" * 30)
            print("    |      SENHA(S)      |")
            print("=" * 30)
            
            for todas_senhas in senhas:
                print(todas_senhas)
                
        elif opcao == "2":
            print("\n--- DICAS DE SEGURANÇA ---")
            print("* Uma senha forte deve ter pelo menos 12 caracteres.")
            print("* Misture sempre letras, números e símbolos.")
            print("* Evite usar dados pessoais como nomes ou aniversários.\n")
        
        elif opcao == "3":
            with open(r"C:\Users\ruanp\Documents\Projetos\Gerenciador De senhas seguras\senhas.txt", "r") as arquivo:
                conteudo = arquivo.read()
                print(conteudo)
           
        elif opcao == "4":
            print("\nSaindo...")
            break
        
        else:
            print("\nOpção inválida!!!")

loop_menu()