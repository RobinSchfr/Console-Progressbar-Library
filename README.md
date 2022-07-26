## Description
A small library to use customizable progressbars. You can use predefined enums or custom Character.

**Please Note:**
- Only works in a native console properly, and not in built-in consoles in IDE's
- The *units* should fit with the width of the console
## Example
```python
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

pb5 = pB.ProgressBar()
for percent in range(101):
    pb5.draw(percent)
    time.sleep(0.2)
```
### Output
```
82% [██████████████████████████████████████████████████████████████████--------------]
43% [XXXXXXXXXXXXXXXXXXXXXX----------------------------]
22% [****~~~~~~~~~~~~~~~~]
60% [######----]
100% [##################################################]
```
