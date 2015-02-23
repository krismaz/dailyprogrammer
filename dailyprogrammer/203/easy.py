#Simple Solution using Pillow
from PIL.Image import * 
from PIL.ImageDraw import * 

img = new('RGB', (200, 200) , (0, 0, 0))

drawing = Draw(img)
drawing.rectangle(((50,50), (150,150)), 'pink', 'pink')

img.show()