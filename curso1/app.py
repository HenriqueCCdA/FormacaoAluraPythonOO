import os

restaurantes = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Pizza Sumprea', 'categoria': 'Pizza', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False},
]


def exibir_nome_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def voltar_ao_menu_principal():
    input('\nDigite um tecla para voltar para o menu ')
    main()

def exibir_subtitulo(texto):
    os.system('clear')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def exibir_opcoes():
    print('1. Cadastrar restaurente')
    print('2. Listar restaurante')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')

def opcao_invalida():
    print('Opção inálida!\n')
    voltar_ao_menu_principal()



def cadastro_novo_restaurante():
    '''Essa função é responsável por cadadstrar u novo restaurante'''

    exibir_subtitulo('Cadastro de novos restaurantes:')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')

    categoria = input(f'Digite o nome do categoria do restaurante {nome_do_restaurante}: ')

    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}

    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurante:')

    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurente = restaurante['nome']
        categoria = restaurante['categoria']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurente.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja alterarr o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = (
                f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo']
                else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            )
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha um opção: '))
        if opcao_escolhida == 1:
            cadastro_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except KeyboardInterrupt:
        finalizar_app()
    except:
        opcao_invalida()


def finalizar_app():
    exibir_subtitulo('Finalizando o programa')


def main():
    os.system('clear')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
