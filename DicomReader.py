import pydicom
from pydicom.data import get_testdata_files
from pydicom.errors import InvalidDicomError

folder = '/Users/jscs/DICOM/Untitled.rtf' #Cualquier archivo no dicom

try:
    pydicom.dcmread(folder)
except InvalidDicomError: 
    print('sfs')
else:
    print('woj') 
