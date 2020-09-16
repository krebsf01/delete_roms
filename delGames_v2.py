import send2trash, re
from pathlib import Path


pattern = re.compile('''
^(.*?)      #Before name
(\(Japan\)|\(Europe\)|\(Spain\)|\(Italy\)|\(France\)|\(Germany\)|Copia|Beta|Wii U Virtual Console) # names
(.*?)$
''', re.VERBOSE)

p = Path('C:/Users/thikr/OneDrive/Documentos/Roms')
for foldername, subfolders, filenames in os.walk(p):
    for filename in filenames:
        gameFound = re.search(pattern, str(Path(Path(foldername)/filename).name))
        if gameFound == None:
            continue
        gameName = gameFound.group(0)
        print((str(Path(foldername)/gameName)))
        #send2trash.send2trash(str(Path(foldername)/gameName))

print('Done')
