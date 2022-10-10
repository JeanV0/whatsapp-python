from csv import reader
from json import load, dumps

from utils.Numbers import Numbers


class Config():
    def __init__(self):
        self.config = open('config.json', 'r')
        self.backup = {
            "message": "message.txt",
            "contatos": "boticario.csv",
            "midia": "example.midia",
            "limit": 200
        }

    def setConfig(config, self):
        atualizacao = dumps(config)
        file = open('config.json', 'w')
        file.write(atualizacao)
        self.config = config

    def getConfig(self):
        try:
            config = load(self.config)
            return (config)
        except:
            file = open('config.json', 'w')
            file.write(dumps(self.backup))
            return self.backup

    def validateConfig(self, configuration,limit,ddd):
        for config in configuration:
            if (config == 'message'):
                path = configuration[config]
                try:
                    with open('users/messages/{}'.format(path), 'r', encoding="utf-8") as file:
                        return ({"message": file.readlines()})
                except:
                    return ({'message': ['ola\nSou uma mensagem teste']})

            if (config == 'contatos'):
                path = configuration[config]
                try:
                    with open('users/contatos/{}'.format(configuration['contatos']), 'r', encoding="utf-8") as csv_file:


                        csv_reader = reader(csv_file, delimiter=';')

                        csv_reader.__next__()
                        csv = []

                        # Adicionando as informações em um arquivo para usar no robô
                        for row in csv_reader:
                            csv.append(row)
                            
                        return ({"contatos": csv})
                except:
                    
                    generateNumbers = Numbers(int(limit))
                    generateNumbers.setDdd(ddd)
                    generateNumbers.generateNumbers()

                    return ({"contatos": generateNumbers.getNumbers()})
            if (config == 'midia'):
                key = 0
                midias = {'midia': {}}
                files = configuration[config].split(",")
                for file in files:
                    try:
                        with open('users/midia/{}'.format(file), 'r') as file:
                            file.open()
                            midias['midia'] = {
                                "{}".format(key), 
                                file
                               }
                    except:
                        return(midias)
