import pydicom
from pydicom.data import get_testdata_files
from pydicom import dcmread, filereader

folder = '/Users/jscs/DICOM/Untitled.rtf' #Cualquier archivo no dicom

try:
    pydicom.dcmread(folder)
except InvalidDicomError: 
    print('sfs')    #se espera que se ejecute cuando no es archivo dicom
else:
    print('woj') #lo que se ejecuta si es archivo dicom

    
#un ejemplo que sí funciona con una error por defecto
""" 
try:
    1/0
except ZeroDivisionError:
    print('juak')
else:
    print('woj')
    """
