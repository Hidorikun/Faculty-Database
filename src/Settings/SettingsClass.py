class SettingsError(Exception):
    pass


class ParsingError(SettingsError):
    pass


class Settings(object):
    def __init__(self, file_name):
        self.__filename = file_name
        self.__settings = {}
        self.load()

    def __parse_line(self, line):
        args = line.split('=')
        for i in range(len(args)):
            args[i] = args[i].strip('\n')
            args[i] = args[i].strip(' ')

        if len(args) != 2:
            raise ParsingError('The format of any line in this file must be "property = value"')
        return args

    def __set(self, line):
        args = self.__parse_line(line)
        property = args[0]
        value = args[1]
        self.__settings[property] = value


    def load(self):
        try:
            with open(self.__filename) as f:
                for line in f:
                    if line[0] not in ['#', '\n']:
                        self.__set(line)
        except IOError:
            raise SettingsError("File : {0} is missing".format(self.__filename))

    def __getitem__(self, property):
        return self.__settings[property]
