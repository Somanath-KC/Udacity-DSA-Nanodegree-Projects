def sort_012(input_list=[]):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if input_list is None or len(input_list) == 0:
        return []

    list0 = []
    list1 = []
    list2 = []

    for i in input_list:
        if i == 0:
            list0.append(i)
        elif i == 1:
            list1.append(i)
        elif i == 2:
            list2.append(i)
        else:
            return []

    return list0 + list1 + list2


def test_function(test_case=[]):
    sorted_array = sort_012(test_case)
    # print(sorted_array)
    sorted_list = sorted(test_case)
    if sorted_array == sorted_list or sorted_array == []:
        print("Pass")
    else:
        print("Fail")


#####     #####
#   Testing   #
#####     #####

# Test Case 1
print("\n", "#"*8, " - Test Case 1 [General Working] - ", "#"*8, "\n")
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])


# Test Case 2
print("\n", "#"*8, " - Test Case 2 [Same Value] - ", "#"*8, "\n")
test_function([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])


# Test Case 3
print("\n", "#"*8, " - Test Case 3 [Empty List/Null Value] - ", "#"*8, "\n")
test_function([])
test_function()


# Test Case 4
print("\n", "#"*8, " - Test Case 4 [Other Than 0,1,2] - ", "#"*8, "\n")
test_function([0, 0, 1, 2, 2, 1, 5])  # Returns Empty List becase 5 is not in range 0 to 2
