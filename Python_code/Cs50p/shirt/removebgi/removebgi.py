from rembg import remove
import easygui
from PIL import Image

inputPath = easygui.fileopenbox(title='.jpg')
outputPath = easygui.filesavebox(title='.jpg')

input = Image.open(inputPath)
output = remove(input)
output.save(outputPath)
