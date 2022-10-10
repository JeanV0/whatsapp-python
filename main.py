#encoding: utf-8
from bot import Bot
from painelpy import Painel
from utils.Config import Config

if __name__ == "__main__":

    configBot = Config()
    configGet = configBot.getConfig()

    painel = Painel(configGet)
    config = painel.run()
    
    bot = Bot(config)
    bot.initializer()
    bot.auth()
    bot.sendMsg()

    
    
    