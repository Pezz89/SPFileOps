import os

def file_must_exist(path):
    """
    Checks that the path specified exists
    If not or the path is a directory then raises and IOError
    """
    # Check that path is a string value
    if not isinstance(path, basestring):
        raise TypeError("File path argument is not a string")
    if not os.path.isfile(path):
        raise IOError("File doesn't exist: ", path)
    else:
        return True

def dir_must_exist(path):
    """
    Checks that the directory exists.
    If not then tries to create the directory.
    If this fails then an IOError is raised.
    """
    if not isinstance(path, basestring):
        raise TypeError("Directory path argument is not a string")
    try:
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise IOError("Directory can't be created: ", path)

    return True

def listdir_nohidden(path):
    """
    List all files and subdirectories of a directory that aren't hidden.
    """
    dir_must_exist(path)
    return [i for i in os.listdir(path) if not i.startswith('.')]
