import os


def walking(folder, applied_function):
    """
    Walks through folder doing an specified function in the second parameter
    :type applied_function: function
    :param folder: the folder to execute the walking
    :param applied_function: specified function to do on the walking
    Example walking('/Users/jscs/Downloads/test', print)
    """
    for (root, dirs, files) in os.walk(folder):
        print('+++++++++++++**++++++++++++', 'Walking through', root, '+++++++++++++**+++++++++++++')
        for (file) in files:
            applied_function(os.path.join(root, file))

