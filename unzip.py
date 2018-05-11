import os
import fleep
import patoolib


def unpack(input_file, output_folder):
    """
    :param input_file: file to unpack
    :param output_folder: folder to save file unpacked
    :return: Message of unpacked or no file detected

    Beside the packages above, you must have installed patool
    """
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
        patoolib.extract_archive(input_file, outdir=output_folder)
        result = True
    else:
        result = False
    return result
            
