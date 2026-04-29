from colorama import Style, Fore
from time import sleep
import os
import random

periodos = ["seca", "chuva", "estavel"]

cores = { # Lista com todas as cores usadas no código
    "AZUL": Fore.BLUE,
    "VERMELHO": Fore.RED,
    "AMARELO": Fore.YELLOW,
    "VERDE": Fore.GREEN,
    "CIANO": Fore.CYAN,
    "MAGENTA": Fore.MAGENTA,
    "PRETO": Fore.BLACK,
}

def clearScreen(): # Funcao para limpar a tela, evita escrever muitas vezes o mesmo código
    os.system("cls")
    

        
def loadindscreen(): # Tela de carrgamento
    for i in range(11):
        sleep(0.5)
        clearScreen()
        print(cores["PRETO"], "SISTEMA INICIANDO, POR FAVOR AGUARDE... \n",f"█"* (i * 5), f"{10*i}%" ,"\n", Style.RESET_ALL)
        if i * 10 == 100:
            print(cores["VERDE"], "SISTEMA PRONTO!!! \n RESERVATÓRIO DA REPRESA BRASILEIRA", Style.RESET_ALL)

        
        
def reservatoryLevel(): # funçao que calcula o nível atual do reservatório
    nivel = 50
    while True:
        sleep(1)
        estacao = random.choice(periodos)
        if estacao == "seca":
            nivel -= 10
        elif estacao == "chuva":
            nivel += 15
        elif estacao == "estavel":
            nivel -= 2
            
        if nivel < 5:
            nivel = 5
        elif nivel > 100:
            nivel = 100
            
        clearScreen()
        print(cores["MAGENTA"], f"PERÍODO ATUAL: {estacao}", Style.RESET_ALL)
        if nivel > 85:
            print(cores["AZUL"], f"Nível do Reservatório, MUITO ALTO: {nivel}%")
        elif nivel > 70 and nivel <= 85:
            print(cores["CIANO"], f"Nível do Reservatório, ALTO: {nivel}%")
        elif nivel > 50 and nivel <= 70:
            print(cores["VERDE"], f"Nível do Reservatório, MÉDIO: {nivel}%")
        elif nivel > 30 and nivel <= 50:
            print(cores["AMARELO"], f"Nível do Reservatório, BAIXO: {nivel}%")
        elif nivel  <= 30:
            print(cores["VERMELHO"], f"Nível do Reservatório, MUITO BAIXO: {nivel}%")
        
        print(Style.RESET_ALL, "Para parar o código use CTRL+C")
        
def main():
    print(Style.RESET_ALL)
    loadindscreen()
    reservatoryLevel()

main()

