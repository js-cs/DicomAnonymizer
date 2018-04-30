import os
import pydicom
from DicomReader import *
from pydicom.data import get_testdata_files
from pydicom.errors import InvalidDicomError

path = '/Users/jscs/Downloads/test'
for(root,dirs,files) in os.walk(path):
    print(root,'+++++++++++++++++++++++++++++++**+++++++++++++++++++++++++++++')
    for(file) in files:
        print(file)
        DicomReader(root+'/'+file)
        
