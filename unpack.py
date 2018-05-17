import os
import fleep
import zipfile
import patoolib
from patoolib.util import PatoolError


def unpack(input_file, output_folder):
    """
    :param input_file: file to unpack
    :param output_folder: folder to save file unpacked
    :return: Message of unpacked or no file detected

    """
    print(input_file)
    if os.path.isdir(input_file):
        return False

    with open(input_file, "rb") as file:
        info = fleep.get(file.read(128))

    extensions_supported = {'rar', '7z', 'dmg', 'gz', 'iso', 'tar.z', 'zip'}
    
    print(info.extension)
    
    if not info.extension:
        result = False
    elif set(info.extension) & extensions_supported:
        print(set(info.extension) & extensions_supported)
        print('---> File recognized, unpacking <---')
        try:
            patoolib.extract_archive(input_file, outdir=output_folder)
        # probably a false positive
        except PatoolError:
            return False
        result = True
    else:
        result = False
    return result


def unzip(path, path_out):
    if zipfile.is_zipfile(path):
        zip_ref = zipfile.ZipFile(path, 'r')
        zip_ref.extractall(path_out)
        zip_ref.close()

"""
input_file = '/Users/jscs/Downloads/test/faa.rar'
output_folder = '/Users/jscs/Downloads/test'

unpack(input_file, output_folder)
"""
