import os
import zipfile
import patoolib

inputFolder = '/Users/jscs/Downloads/test/faa.rar' 
outputFolder = '/Users/jscs/Downloads/test'

def unpack(inputFolder, outputFolder):
    if not (os.path.isdir(inputFolder)):
        if zipfile.is_zipfile(inputFolder):
            zip_ref = zipfile.ZipFile(inputFolder, 'r')
            return zip_ref.extractall(outputFolder)
            return zip_ref.close()
        else:
            patoolib.extract_archive(inputFolder, outdir= outputFolder)
            
