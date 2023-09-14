import datetime


def registrar_estudo():
    # Data e hora atual.
    agora = datetime.datetime.now()

    # Solicita ao usuário o assunto e o que foi estudado.
    assunto = input("Digite o assunto do estudo: ")
    conteudo = input("Descreva o que você estudou: ")

    # Formatação de Data/Hora
    data_hora_formatada = agora.strftime("%Y-%m-%d %H:%M:%S")

    
    # Criação do arquivo onde os registros ficaram salvos.
    with open("registro_de_estudo.txt", "a") as arquivo:
        # Escreve as informações no arquivo
        arquivo.write(f"Data/Hora: {data_hora_formatada}\n")
        arquivo.write(f"Assunto: {assunto}\n")
        arquivo.write(f"Conteudo estudado:{conteudo}\n")
        arquivo.write("-" * 40 + "\n")

        print("Estudo registrado com sucesso!")


def visualizar_registros():
    try:
        # Aqui abrimos um arquivo de registro, onde as opções registradas será salvas em modo de leitura.
        with open("registro_de_estudo.txt", "r") as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print("Nenhum registro de estudos encontrado.")

# Função na qual o usuário escolhe o que melhor atende.
def main():
    while True:
        print("\nMenu:")
        print("1. Registrar estudo")
        print("2. Visualizar registros")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_estudo()
        elif opcao == "2":
            visualizar_registros()
        elif opcao == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
