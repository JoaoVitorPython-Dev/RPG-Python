from time import sleep

itens_inventario = []
drops = ['Ferro', 'Madeira']
itens_loja = ['Armadura','Espada']

# Status do personagem
level = 0
exp = 0
vida_maxima = 100
vida = vida_maxima
dmg = 25
moedas = 0

# Status do inimigo
inimigo_vida = 50
inimigo_dmg = 10


def carregamento():
    print('Carregando', end='')
    for _ in range(3):
        sleep(0.5)
        print('.', end='', flush=True)
    print('\n')


def carregamento2():
    print('Processando', end='')
    for _ in range(3):
        sleep(0.7)
        print('.', end='', flush=True)
    print()


def status():
    carregamento2()
    print('-' * 20, 'STATUS', '-' * 20)
    print('-' * 50)
    print(f'Level: {level}')
    print(f'Experiência: {exp}')
    print(f'Vida: {vida}')
    print(f'Dano: {dmg}')
    print(f'Moedas: {moedas}')
    print('-' * 50)
    carregamento2()
    print()


def resumo_batalha(exp_ganha, moedas_ganha, niveis_subidos):
    print('\n' + '=' * 40)
    print('RESUMO DA BATALHA')
    print('=' * 40)
    print(f'EXP ganha: +{exp_ganha}')
    print(f'Levels subidos: {niveis_subidos}')
    print(f'Moedas ganhas: +{moedas_ganha}')
    print('-' * 40)
    print('STATUS ATUAL')
    print(f'Level: {level}')
    print(f'Experiência: {exp}')
    print(f'Vida: {vida}')
    print(f'Dano: {dmg}')
    print(f'Moedas: {moedas}')
    print('=' * 40 + '\n')


def batalha():
    global exp, moedas, level, vida, dmg, inimigo_vida, inimigo_dmg, vida_maxima

    vida_inimigo = inimigo_vida
    carregamento()
    print('Você estava andando pela floresta e de repente se deparou com um inimigo!')
    sleep(1)
    print('-' * 20, 'BATALHA', '-' * 20)
    print(f'O inimigo possui {vida_inimigo} de vida e causa {inimigo_dmg} de dano.')
    print('-' * 50)

    while vida > 0 and vida_inimigo > 0:
        print('O que você deseja fazer?')
        print('1 - Atacar')
        print('2 - Ver seus status')
        print('3 - Fugir')
        print('-' * 50)
        escolha_batalha = input('Escolha uma opção: ').strip()

        while escolha_batalha not in ['1', '2', '3']:
            print('Opção inválida! Tente novamente.')
            escolha_batalha = input('Escolha uma opção: ').strip()

        if escolha_batalha == '1':
            vida_inimigo -= dmg
            print(f'Você atacou o inimigo e causou {dmg} de dano!')
            print(f'Vida do inimigo: {max(vida_inimigo, 0)}')
            print('-' * 50)
            carregamento2()

            if vida_inimigo <= 0:
                exp_ganha = 50
                moedas_ganha = 20
                exp += exp_ganha
                moedas += moedas_ganha

                niveis_subidos = 0
                while exp >= 100:
                    exp -= 100
                    level += 1
                    vida_maxima += 20
                    dmg += 5
                    niveis_subidos += 1
                vida = vida_maxima

                print('Você derrotou o inimigo!')
                print(f'EXP ganha: +{exp_ganha}')
                print(f'Moedas ganha: +{moedas_ganha}')
                if niveis_subidos > 0:
                    print(f'Você subiu {niveis_subidos} nível(ns)!')
                print('-' * 50)
                resumo_batalha(exp_ganha, moedas_ganha, niveis_subidos)

                inimigo_vida += 10
                inimigo_dmg += 2
                print('Você continua andando pela floresta...')
                print()
                return

            vida -= inimigo_dmg
            print(f'O inimigo te atacou e causou {inimigo_dmg} de dano!')
            print(f'Sua vida agora é {max(vida, 0)}')
            print('-' * 50)

            if vida <= 0:
                vida = 0
                print('Você foi derrotado!')
                print('Fim de jogo! Tente novamente outra vez.')
                print('-' * 50)
                return

        elif escolha_batalha == '2':
            status()

        elif escolha_batalha == '3':
            print('Você fugiu da batalha e voltou para a floresta.')
            print('-' * 50)
            return


def menu():
    print('-' * 12, 'SEJA BEM-VINDO AO RPG!', '-' * 12)
    print('=' * 20, 'MENU', '=' * 20)
    print('1 - JOGAR')
    print('2 - INVENTÁRIO')
    print('3 - STATUS')
    print('4 - LOJA')
    print('5 - SAIR')
    print('-' * 50)


def jogar():
    print('Iniciando o jogo')
    carregamento()
    print('-' * 20, 'JOGO', '-' * 20)
    print('Seja bem-vindo ao mundo do RPG! Prepare-se para enfrentar desafios e conquistar vitórias!')
    print()

    while vida > 0:
        batalha()
        if vida <= 0:
            break
        print('Você decidiu seguir adiante pela floresta...')
        sleep(1)


def inventario():
    carregamento2()
    print('-' * 20, 'INVENTÁRIO', '-' * 20)
    print('-' * 50)
    if not itens_inventario:
        print('Seu inventário está vazio.')
    else:
        print('Itens no inventário:')
        for item in itens_inventario:
            print(f'- {item}')
    print('-' * 50)
    carregamento2()
    print()


def loja():
    carregamento2()
    print('-' * 20, 'LOJA', '-' * 20)
    print('Bem-vindo à loja! Aqui você pode comprar itens para melhorar seu personagem.')
    print('Itens disponíveis:')
    print('-' * 50)
    print('1 - Armadura (50 moedas)')
    print('2 - Espada (100 moedas)')
    print('-' * 50)
    carregamento2()
    print()

while True:
    menu()
    escolha = input('Escolha uma opção: ').strip()

    while escolha not in ['1', '2', '3', '4', '5']:
        print('Opção inválida! Tente novamente.')
        escolha = input('Escolha uma opção: ').strip()

    if escolha == '1':
        jogar()

    elif escolha == '2':
        inventario()

    elif escolha == '3':
        status()

    elif escolha == '4':
        loja()

    elif escolha == '5':
        carregamento()
        print('Saindo do jogo... Até a próxima!')
        break