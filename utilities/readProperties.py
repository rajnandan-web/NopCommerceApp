import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\USER\\PycharmProjects\\NopCommerceApp\\Configurations\\config.ini")


class readConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'URL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
