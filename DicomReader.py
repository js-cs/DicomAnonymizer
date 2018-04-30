import pydicom
from pydicom.errors import InvalidDicomError

file_ = "/Users/jscs/DICOM/Untitled.rtf"
def DicomReader(file_):
    try:
        pydicom.dcmread(file_)
    except InvalidDicomError:
        print('Not Dicom file')
    else:
        print('Dicom file')

