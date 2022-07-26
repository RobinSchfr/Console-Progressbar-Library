import time
import ProgressBar as pB
from Chars import Char

pb1 = pB.ProgressBar(Char.BLOCK, Char.DASH, 80)
pb2 = pB.ProgressBar("X", Char.DASH)
pb3 = pB.ProgressBar(Char.ASTERISK, "~", 20)
pb4 = pB.ProgressBar(units=10)

pb1.draw(82, True)
pb2.draw(43, True)
pb3.draw(22, True)
pb4.draw(60, True)

pB5 = pB.ProgressBar()
for percent in range(101):
    pB5.draw(percent)
    time.sleep(0.2)