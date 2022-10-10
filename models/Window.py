from PySimpleGUI import Input
from PySimpleGUI import Frame
from PySimpleGUI import Button
import PySimpleGUI as sg
from PySimpleGUI import theme

class Window():
    def __init__(self, configBot):
        self.config = configBot

    def createPainel(self):
        theme('Dark Blue 3')

        message = [
            [Input(
                self.config['message'], key="message")]
        ]

        lista_contatos = [
            [Input(
                self.config['contatos'], key="contatos"), ]
        ]

        arquivo = [
            [Input(
                self.config['midia'], key='midia')]
        ]

        limite = [
            [Input(
                self.config['limit'], key='limit')]
        ]
        
        dddSelect = [
            [Input(
                "95", key="ddd"
            )]
        ]

        layout = [
            [Frame('message', layout=message, key="message"),Button("Mostrar", key='mensagem')],
            
            [Frame("contatos", layout=lista_contatos,key="contatos"), Button("Mostrar", key='contato')],
            
            [Frame('midia', layout=arquivo, key="midia"),Button("Mostrar", key='midia')],
            
            [Frame('Gerar numeros ( Se nao existir lista )', layout=limite, key="limite")],
            
            [Frame('ddd para gerar numeros' , layout=dddSelect, key="ddd")],
            
            [Button('Iniciar'), Button('Apagar')]
        ]

        return sg.Window('Todo List', layout)
