import configparser

config = configparser.RawConfigParser()

config_path = r'C:\Users\hp\PycharmProjects\Gimalconfig\configuration\config.in'

config.read(config_path)



class Readconfig():

    @staticmethod
    def geturl():
        url = config.get('common info', 'Url')
        return url



