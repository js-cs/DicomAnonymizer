import pydicom
from pydicom.data import get_testdata_files

path = #file_path

filename = get_testdata_files(path)
dataset = pydicom.dcmread(path)

data_elements = ['PatientName','PatientID','IssuerOfPatientID','TypeOfPatientID',
                 'PatientBirthDate','PatientBirthTime','PatientBirthDateInAlternative',
                 'PatientDeathDateInAlternative','PatientDeathDateInAlternative',
                 'PatientSex','PatientInsurancePlanCode','OtherPatientIDs','PatientAge',
                 'PatientSize','PatientWeight','PatientAddress','InsurancePlanIdentification',
                 'MilitaryRank','BranchOfService','PatientTelephoneNumbers',
                 'AdditionalPatientHistory']
                
                 """
                 You can add or remove elements to delete  based on 'keywords' of 
                 http://dicom.nema.org/medical/dicom/current/output/pdf/part06.pdf
                 (personal information (0010,xxxx) pag. 29-31) 
                 """

for element in data_elements:
    if element in dataset:
        delattr(dataset, element)
