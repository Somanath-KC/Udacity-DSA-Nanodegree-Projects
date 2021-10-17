import random


def get_min_max(ints=[]):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not (ints is None) and (len(ints) > 0):
        min, max = ints[0], ints[0]
    else:
        return ()

    for i in ints:
        if i < min:
            min = i
        if i > max:
            max = i
    return min, max


#####     #####
#   Testing   #
#####     #####

# Test Case 1
print("\n", "#"*8, " - Test Case 1 [General Working] - ", "#"*8, "\n")
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Test Case 2
print("\n", "#"*8, " - Test Case 2 [Single Element] - ", "#"*8, "\n")
l = [1]
print("Pass" if ((1, 1) == get_min_max(l)) else "Fail")

# Test Case 3
print("\n", "#"*8, " - Test Case 3 [Empty Input] - ", "#"*8, "\n")
l = None
print("Pass" if (() == get_min_max(l)) else "Fail")

# Test Case 4
print("\n", "#"*8, " - Test Case 4 [Large Numbers] - ", "#"*8, "\n")
l = [i for i in range(10000, 999999)]  # a list containing -Large Numbers
random.shuffle(l)
print("Pass" if ((10000, 999998) == get_min_max(l)) else "Fail")

# Test Case 5
print("\n", "#"*8, " - Test Case 5 [Negative Numbers] - ", "#"*8, "\n")
l = [i for i in range(-25, 0)]  # a list containing -25 to -1
random.shuffle(l)
print("Pass" if ((-25, -1) == get_min_max(l)) else "Fail")
