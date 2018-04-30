import pydicom
from pydicom.errors import InvalidDicomError

def DicomReader(file_):
    try:
        pydicom.dcmread(file_)
    except InvalidDicomError:
        return('Not Dicom file')
    else:
        return('Dicom file')
