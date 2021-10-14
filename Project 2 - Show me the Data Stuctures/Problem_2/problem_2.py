import os


def find_files(suffix=".c", path="."):
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

    if (not os.path.isdir(path) and
            not os.path.isfile(path)) or suffix != ".c":
        return matched_files

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


#####     #####
#   Testing   #
#####     #####

# Test case 1 / General Working
print("\n",  "#"*10, " - Test Case 1 - ", "#"*10, "\n")
print(find_files(".c", "testdir"))  # Given Sample Directory

# Test case 2 / Invalid Directory Path
print("\n",  "#"*10, " - Test Case 2 - ", "#"*10, "\n")
print(find_files(".c", "testdirs_"))  # Invalid Directory returns []

# Test case 3 / Providing null directory path
print("\n",  "#"*10, " - Test Case 3 - ", "#"*10, "\n")
print(find_files(".c"))  # Current directory will considered by default

# Test case 4 / Trying with other files extensions
print("\n",  "#"*10, " - Test Case 4 - ", "#"*10, "\n")
print(find_files(".py"))  # Other extensions returns []
