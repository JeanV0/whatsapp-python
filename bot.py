from email import message
from time import sleep

from os import getcwd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# Painel de aviso ou contagem de quantos foram enviados

# Classe do robô
class Bot(object):
    def __init__(self, configBot):
        self.options = Options()
        self.driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=self.options)
        self.configBot = configBot
        self.ddd = int
        self.roadMap = []
        self.message = ""

    def elementPresence(self, boxes=[], time=10):
        for x in range(time):
            for box in boxes:
                try:
                    boxSelect = self.driver.find_element(By.XPATH, box["box"])
                    if (boxSelect.text == box['text']):
                        return box['bool']
                except:
                    pass
            sleep(1)

    def execRoadMap(self, number):
        sleep(2)
        verifyBox = {"box": '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]',
                     "text": "Mensagem",
                     "bool": True}
        errorBox = {"box": '/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[1]',
                    "text": "O número de telefone compartilhado através de url é inválido.",
                    "bool": False}

        boxes = [verifyBox, errorBox]
        validation = self.elementPresence(boxes=boxes, time=20)
        if (validation):
            self.saveNumber(number)
            sleep(2)
            buttonSender = self.driver.find_element(
                By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
            for dict in self.roadMap:
                for road in dict:
                    print(dict[road])
                    textArea = self.driver.find_element(By.XPATH,
'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')

                    if (road == "message"):
                        message = dict[road]
                        textArea.send_keys(message)
                        sleep(2)

                    elif (road == "midia"):
                        try:
                            buttonSender.click()
                        except:
                            pass
                        attach = self.driver.find_element_by_css_selector(
                            "input[type='file']")
                        sleep(1)
                        path = getcwd()+'/users/midia/' + \
                            self.configBot[road["midia"]]
                        attach.send_keys(path)
                        sleep(3)
                        # Seleciona botão enviar
                        send = self.driver.find_element_by_xpath(
                            "//div[contains(@class, 'yavlE')]")
                        # Clica no botão enviar
                        send.click()

    def auth(self):
        self.driver.get('https://web.whatsapp.com/')
        boxes = [{
            "box": '/html/body/div[1]/div/div/div[4]/div/div/div[2]/div[1]/h1',
            "text": "WhatsApp Web",
            "bool": True
        }]

        self.elementPresence(boxes=boxes, time=40)

    def initializer(self):

        configs = self.configBot
        for config in configs:
            try:
                for line in config:
                    if (line == 'message'):
                        for key in config[line]:
                            line = key
                            analise = line.find('{')+1
                            analise0 = line.find('}')
                            resultado = line[analise:analise0]

                            if type(resultado) == int:
                                self.roadMap.append(
                                    {"midia": self.configBot['midia']['{}'.format(resultado)]})
                            else:
                                self.roadMap.append({"message": key})

            except:
                pass

    def sendMsg(self):
        sender = 0
        configs = self.configBot
        
        for config in configs:
            for value in config:
                if value == "contatos":
                    contatos = config[value]
                    for contato in contatos:
                        try:
                            if (self.loadNumber(number=contato[sender])):
                                number = "https://web.whatsapp.com/send?phone={}&source=&data=#".format(
                                    contato[sender])
                                self.driver.get(number)
                                self.execRoadMap(contato[sender])
                                sender =+ 1
                        except:
                            if (self.loadNumber(number=contato)):
                                number = "https://web.whatsapp.com/send?phone={}&source=&data=#".format(
                                contato)
                                self.driver.get(number)
                                self.execRoadMap(contato)
        

    def saveNumber(self, number):
        with open('save.txt', 'a') as file:
            try:
                file.write(number + "\n")
            except:
                file.write(number[0] + "\n")

    def loadNumber(self, number=int):
        if(number == ''):
            return False
        
        with open('save.txt', 'r') as file:
            if (file.read().find(str(number)) < 0):
                return True
            else:
                return False
