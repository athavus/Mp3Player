from pygame import mixer
from PySimpleGUI import PySimpleGUI as sg

sg.theme('DarkPurple1') # Definição do tema da interface do programa

layout = [
    [sg.Text('MP3 PLAYER'.center(50), font='Consolas')], # Título do programa
    [sg.Text('NOME DA MÚSICA:', font='Consolas'), sg.Input(key='music', size=(42, 1))], # Input da música que será tocada
    [sg.Button('▶', size=(55, 1))] # Botão para fazer tocar a música
]   
janela = sg.Window('Mp3 player', layout) # Criação da janela

while True:
    try: # Tentativa de abrir o arquivo da música e da leitura dos inputs de cima
        eventos, valores = janela.read()
        musica = open(valores['music'])
    except: # Caso o usuário não coloque um valor válido no input, temos uma mensagem de Erro! Porém o programa não se encerra
        print('Erro! :/')
    else: # Se tudo ocorrer corretamente, chegamos nesta condição onde o player enfim toca a música
        if eventos == sg.WIN_CLOSED:
            break
        if eventos == '▶':
            mixer.init() # Iniciador do mixer do Pygame
            mixer.music.load(musica) # Comando que carrega a música recebida pelo input
            mixer.music.play() # Comando que toca a música que foi recebida pelo input
            print(f'Está tocando {valores["music"]}... Aproveite') # Comando que mostra a música que está tocando
