import os
from PIL import Image
import zpl


l = zpl.Label(60,60)
height = 0
l.origin(0,20)
l.write_text(98, char_height=10, char_width=8, line_width=60, justification='C')
l.endorigin()
print(l.dumpZPL())
l.preview()