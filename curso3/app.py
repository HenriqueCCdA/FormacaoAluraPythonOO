from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_japa = Restaurante('Japa', 'Gourmet')

restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('lais', 8)
restaurante_praca.receber_avaliacao('Emy', 5)



def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()
