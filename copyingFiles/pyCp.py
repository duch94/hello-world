import shutil
import os
import xml.etree.ElementTree as ET

tree = ET.parse('files.xml')
root = tree.getroot()
for child in root:
    file = child[0].text
    destFrom = child[1].text
    destTo = child[2].text
    fileFrom = os.path.join(destFrom, file)
    fileTo = os.path.join(destTo, file)
    try:
        shutil.copy2(fileFrom, fileTo)
    except IOError:
        print 'ERROR: probably file does not exist'
        raise
