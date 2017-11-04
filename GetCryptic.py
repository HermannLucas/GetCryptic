import string

class case1:

    def __init__(self):
        self.HEX_TABLE = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        self.BASE_TABLE = list(string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/")

    def hexConverter(self, hexValue):

        decimalValues = ["{0:04b}".format(self.HEX_TABLE.index(value)) for value in list(hexValue)]

        decimalValues = "".join(decimalValues)

        result = [decimalValues[bits:bits + 6] for bits in range(0, len(decimalValues), 6)]
        return result

    def convert(self, hexValue):

        binaryArray = self.hexConverter(hexValue)

        result = ""
        for sixBits in binaryArray:
            baseEncoded = self.baseConverter(sixBits)
            result += baseEncoded

        return result

    def baseConverter(self, sixBits):

        sixBits = "{:0<6}".format(sixBits)

        index = int(sixBits, 2)

        result = self.BASE_TABLE[index]
        return result
