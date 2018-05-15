import os
import os.path
import zipfile
import pydicom
import patoolib
from pydicom.errors import InvalidDicomError
from pydicom.data import get_testdata_files

# problema: formatos

def unzip(path, path_out):
    if zipfile.is_zipfile(path):
        zip_ref = zipfile.ZipFile(path, 'r')
        zip_ref.extractall(path_out)
        zip_ref.close()


def read_unpack(file_path):
    """
    :param file_path: file to unpack
    :param output_folder: folder to save file unpacked (Whish: =os.path.abspath(os.path.join(file_path, os.pardir)))
    :return: Message of unpacked or no file detected

    """
    ends = ['.rar', '.7z', '.dmg', '.gz', '.iso', '.tar', '.zip','.bz2']
    output_folder = os.path.abspath(os.path.join(file_path, os.pardir))
    if any(file_path.lower().endswith(end) for end in ends):
        #if read pydicom or nifti
        if patoolib.extract_archive(file_path, outdir=output_folder):
            return 'Done'
    # else:
        #  raise ValueError('File extension is not supported')
    else:
        pass


def dicom_reader(file_):
    try:
        pydicom.dcmread(file_)
    except InvalidDicomError:
        return False
    else:
        return True


def walking(folder, applied_function):
    """
    Walks through folder doing an specified function in the second parameter
    :type applied_function: function
    :param folder: the folder to execute the walking
    :param applied_function: specified function to do on the walking
    :return: walking applying the function
    Example walking('/Users/jscs/Downloads/test', print)
    """
    for (root, dirs, files) in os.walk(folder):
        for (file) in files:
            applied_function(os.path.join(root, file))


def recursive_walking(folder):
    if os.path.isfile(folder):
        if dicom_reader(folder):
            dicom_file_anonymizer(folder)
    else:
        for (root, dirs, files) in os.walk(folder):
            for dir in dirs:
                recursive_walking(os.path.join(root, dir))
            for file in files:
                if dicom_reader(os.path.join(root, file)):
                    print(os.path.join(root, file))
                    dicom_file_anonymizer(os.path.join(root, file))
    return


def dicom_file_anonymizer(path):
    """Args:
           path(str): The path of the DICOM file 
        Returns:
            DICOM file saved without personal information"""

    filename = get_testdata_files(path)
    data_set = pydicom.dcmread(path)

    data_elements = ['PatientName', 'PatientID', 'IssuerOfPatientID', 'TypeOfPatientID',
                     'PatientBirthDate', 'PatientBirthTime', 'PatientBirthDateInAlternative',
                     'PatientDeathDateInAlternative', 'PatientDeathDateInAlternative',
                     'PatientSex', 'PatientInsurancePlanCode', 'OtherPatientIDs', 'PatientAge',
                     'PatientSize', 'PatientWeight', 'PatientAddress', 'InsurancePlanIdentification',
                     'MilitaryRank', 'BranchOfService', 'PatientTelephoneNumbers',
                     'AdditionalPatientHistory']

    """
    You can add or remove elements to delete  based on 'keywords' of 
    http://dicom.nema.org/medical/dicom/current/output/pdf/part06.pdf
    (personal information (0010,xxxx) pag. 29-31) 
    """

    for element in data_elements:
        if element in data_set:
            delattr(data_set, element)
    return data_set.save_as(path)


def dicom_anonymizer(path):
    print('--> Searching zip files and unzipping')
    walking(path, unzip)
    print('--> Searching Dicom files and Anonymizing')
    walking(path, dicom_file_anonymizer)


path = '/Users/jscs/Downloads/test'

walking(path, read_unpack)
