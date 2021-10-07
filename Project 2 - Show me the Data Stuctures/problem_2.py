import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    c_files = list()

    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path, i)):
            c_files += find_files(suffix, os.path.join(path, i))
        else:
            if i[-2:] == suffix:
                c_files.append(os.path.join(path, i))

    return c_files


print(find_files(".c", "testdir"))
