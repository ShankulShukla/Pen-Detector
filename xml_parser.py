import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

# Specify the your path over here your you saved your data
path = r'C:\Users\shankul\Desktop\object-detection\images\train'
for xml_file in glob.glob(path + '/*.xml'):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for member in root.iter('filename'):
        ex = member.text[member.text.rfind("."):]
        member.text = str(xml_file[xml_file.rfind("\\")+1:-4]+ex)
    for member in root.iter('path'):
        member.text = str(xml_file[:-4]+".jpg")
    tree.write(xml_file)
