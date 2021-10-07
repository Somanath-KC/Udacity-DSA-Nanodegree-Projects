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

    matched_files = list()

    # Checks if given path is file & checks if it matches suffix
    if os.path.isfile(path) and path[-len(suffix):].lower() == suffix.lower():
        return [path]

    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            matched_files += find_files(suffix, os.path.join(path, item))
        else:
            if item[-len(suffix):].lower() == suffix.lower():
                matched_files.append(os.path.join(path, item))

    return matched_files


print(find_files(".c", "testdir"))
