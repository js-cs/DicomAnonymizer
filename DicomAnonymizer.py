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

#

for element in data_elements:
    if element in dataset:
        delattr(dataset, element)

   
