from Chars import Char


class ProgressBar:
    def __init__(self, fillChar='#', emptyChar='-', units=50):
        self.fillChar = fillChar.value if isinstance(fillChar, Char) else fillChar
        self.emptyChar = emptyChar.value if isinstance(emptyChar, Char) else emptyChar
        self.units = units

    def draw(self, percent, newLine=False):
        block = self.units / 100
        shownBlocks = round(block * percent)
        bar = ""
        for i in range(self.units):
            if i < shownBlocks:
                bar += str(self.fillChar)
            else:
                bar += str(self.emptyChar)

        print(f"{str(percent).zfill(2)}% [{bar}]", end="\r")
        if newLine: print()