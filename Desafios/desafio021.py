# deafio 021
# Faca um programa em Python que abra e reproduza o audio de um arquivo MP3
import playsound

# Caminho absoluto para o arquivo Naja.mp3
caminho_absoluto = r'G:\cursos\curso-python\Desafios\naja.mp3'

try:
    playsound.playsound(caminho_absoluto)
except FileNotFoundError:
    print("Arquivo não encontrado:", caminho_absoluto)