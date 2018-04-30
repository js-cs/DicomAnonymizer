import os
import zipfile
import pydicom
from pydicom.errors import InvalidDicomError
from pydicom.data import get_testdata_files

#path = '/Users/jscs/test/DICOM.zip'
#pathOut = '/Users/jscs/test'


def unzip(path, pathOut):
    if zipfile.is_zipfile(folder): #buscar formatos
        zip_ref = zipfile.ZipFile(folder, 'r')
        zip_ref.extractall(pathOut) 
        zip_ref.close() 

def dicomReader(file_):
    try:
        pydicom.dcmread(file_)
    except InvalidDicomError:
        return False
    else:
        return True

def walking(folder, function_on_the_walking):
    for(root,dirs,files) in os.walk(folder):
        for(file) in files:
            return function_on_the_walking(root+'/'+file)

def recursiveWalking(folder):
    if (os.path.isfile(folder)):
       dicomFileAnonymizer(folder) 
    else:
        for(root,dirs,files) in os.walk(folder):
            for dir in dirs:
                recursiveWalking(os.path.join(root,dir))
            for file in files:
                if dicomReader(os.path.join(root, file)):
                    print(os.path.join(root, file))
                    dicomFileAnonymizer(os.path.join(root, file))
    return
            
def dicomFileAnonymizer(path):
    """Args:
           path(str): The path of the DICOM file 
        Returns:
            DICOM file saved without personal information"""
        

    filename = get_testdata_files(path)
    dataset = pydicom.dcmread(path)
    
    data_elements = ['PatientName','PatientID','IssuerOfPatientID','TypeOfPatientID',
                    'PatientBirthDate','PatientBirthTime','PatientBirthDateInAlternative',
                    'PatientDeathDateInAlternative','PatientDeathDateInAlternative',
                    'PatientSex','PatientInsurancePlanCode','OtherPatientIDs','PatientAge',
                    'PatientSize','PatientWeight','PatientAddress','InsurancePlanIdentification',
                    'MilitaryRank','BranchOfService','PatientTelephoneNumbers',
                    'AdditionalPatientHistory']
                    
    """re
    You can add or remove elements to delete  based on 'keywords' of 
    http://dicom.nema.org/medical/dicom/current/output/pdf/part06.pdf
    (personal information (0010,xxxx) pag. 29-31) 
    """
    
    for element in data_elements:
        if element in dataset:
            delattr(dataset, element)
    return dataset.save_as(path)

def DicomAnonymizer(path):
    print('--> Searching zip files and unzipping')
    Walking(path, Unzip)
    print('--> Searching Dicom files and Anonymizing')
    Walking(path, DicomFileAnonymizer)



recursiveWalking('/Users/jscs/test/DICOM')
