import pydicom
from pydicom.errors import InvalidDicomError

def DicomReader(file_):
    try:
        pydicom.dcmread(file_)
    except InvalidDicomError:
        print('Not Dicom file')
    else:
        print('Dicom file')
