import string
import random
import os
import sys

try:
    import pyperclip
    pyperclip_disponivel = True
except ImportError:
    pyperclip_disponivel = False

def caminho_base():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


arquivo_senhas = os.path.join(caminho_base(), "senhas.txt")
    
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
        classificacao = "Senha Forte"
        classificacao_arquivo = "Segurança Forte"
    elif tamanho >= 8 and op >= 2:
        classificacao = "Senha Médiana"
        classificacao_arquivo = "Segurança Médiana"
    else:
        classificacao = "Senha Fraca"
        classificacao_arquivo = "Segurança Fraca"
    
    senhas.append(f"{senha_final} -> {classificacao}")
    
    with open(arquivo_senhas, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Senha: {senha_final} -> {classificacao_arquivo}")
    
    if pyperclip_disponivel:
        quer_salva = input("Quer copiar a senha para a área de transferência? [S/N] ").upper()
        if quer_salva == "S":
            pyperclip.copy(senha_final)
            print("Senha copiada para a área de transferência!")
    else:
        print(f"\nSua senha: {senha_final}")
    
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
            print("\n--- SENHAS SALVAS ---")
            if not os.path.exists(arquivo_senhas):
                print("Nenhuma senha gerada ainda")
            else:
                with open(arquivo_senhas, "r", encoding="utf-8") as arquivo:
                    conteudo = arquivo.read()
                    print(conteudo if conteudo else "Arquivo vazio")
           
        elif opcao == "4":
            print("\nSaindo...")
            break
        
        else:
            print("\nOpção inválida!!!")

if __name__ == "__main__":
    loop_menu()