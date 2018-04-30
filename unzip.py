import zipfile

path = '/Users/jscs/Downloads/df6b126ff72ec87952ad820a4babcead64e2.pdf' #'/Users/jscs/Downloads/do not hesitate.zip'
if zipfile.is_zipfile(path):
    zip_ref = zipfile.ZipFile(path, 'r')
    zip_ref.extractall('/Users/jscs/Downloads')
    zip_ref.close()

#Work on directories and folders of execution 

