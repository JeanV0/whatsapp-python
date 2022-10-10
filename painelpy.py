from os import close
from PySimpleGUI import WIN_CLOSED
from models.Window import Window
import traceback
import os
import platform

from utils.Config import Config

# Painel feito em PySimgleGui


class Painel():
    def __init__(self, configBot):
        self.configBot = configBot
        self.systemop = platform.system()
        self.configBotEnable = {}
        self.window = Window(self.configBot).createPainel()

        self.event, self.values = self.window.read()
        self.configBotEnable = []

    def run(self):

        while True:

            if self.event == WIN_CLOSED:
                exit()

            if self.event == 'Apagar':
                self.window.close()
                self.createWindow(self)

            if self.event == 'message':
                if self.systemop == 'Windows':
                    os.system('notepad.exe users\\messages\\{}'.format(
                        self.values['message']))

            if self.event == 'contato':
                if self.systemop == 'Windows':
                    os.system('explorer.exe users\\contatos\\{}'.format(
                        self.values['contatos']))

            if self.event == 'midia':
                if self.systemop == 'Windows':
                    os.system('explorer.exe users\\midia\\{}'.format(
                        self.values['midia']))

            # Iniciar o robô via selenium
            if self.event == 'Iniciar':
                self.window.close()

                configEnable = []
                validar = Config().validateConfig
                for value in self.values:
                    add = validar({value:self.values[value]},self.values['limit'],self.values['ddd'])
                    if (add == None):
                        print
                    else:
                        configEnable.append(add)
                    
                    
                
                return (configEnable)
