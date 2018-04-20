import os
import pydicom
from pydicom.data import get_testdata_files

folder = #folder path '/Users/jscs/DICOM/'
os.chdir(folder) 
for file_ in os.listdir(os.curdir):
    if file_.endswith('.dcm'):
        filename = get_testdata_files(file_)
        dataset = pydicom.dcmread(file_)
        
        data_elements = ['PatientName','PatientID','IssuerOfPatientID','TypeOfPatientID',
                        'PatientBirthDate','PatientBirthTime','PatientBirthDateInAlternative',
                        'PatientDeathDateInAlternative','PatientDeathDateInAlternative',
                        'PatientSex','PatientInsurancePlanCode','OtherPatientIDs','PatientAge',
                        'PatientSize','PatientWeight','PatientAddress','InsurancePlanIdentification',
                        'MilitaryRank','BranchOfService','PatientTelephoneNumbers',
                        'AdditionalPatientHistory']
          
        """
        You can add or remove DICOM data to delete  based on 'Keywords' of 
        http://dicom.nema.org/medical/dicom/current/output/pdf/part06.pdf
        (personal information (0010,xxxx) pag. 29-31) 
        """
        
        for element in data_elements:
            if element in dataset:
                delattr(dataset, element)
        dataset.save_as(file_)
