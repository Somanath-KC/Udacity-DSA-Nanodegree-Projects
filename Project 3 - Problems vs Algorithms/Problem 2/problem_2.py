def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return rotated_array_binary_search(input_list, 0,
                                       len(input_list)-1, number)


def rotated_array_binary_search(input_list, start, end, target):
    """
        Using binary search to find the index
        Ref: https://knowledge.udacity.com/questions/430575
    """

    if start > end or type(target) != int or len(input_list) == 0:
        return -1

    middle = (start+end)//2

    if input_list[middle] == target:
        return middle
    elif input_list[start] <= input_list[middle]:
        if target >= input_list[start] and target <= input_list[middle]:
            return rotated_array_binary_search(input_list,
                                               start, middle-1, target)
        else:
            return rotated_array_binary_search(input_list,
                                               middle+1, end, target)
    elif target >= input_list[middle] and target <= input_list[end]:
        return rotated_array_binary_search(input_list,
                                           middle+1, end, target)
    else:
        return rotated_array_binary_search(input_list,
                                           start, middle-1, target)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    l_output = linear_search(input_list, number)
    b_output = rotated_array_search(input_list, number)
    print("Input List ->", input_list, ", Target Value:",
          number, ", Linear Search Output:", l_output,
          ", Binary Search Output", b_output)
    if l_output == b_output:
        print("Pass")
    else:
        print("Fail")


#####     #####
#   Testing   #
#####     #####

# Test Case 1
print("\n", "#"*8, " - Test Case 1 [General Working] - ", "#"*8, "\n")
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Test Case 2
print("\n", "#"*8, " - Test Case 2 [Empty List] - ", "#"*8, "\n")
test_function([[], 1])

# Test Case 3
print("\n", "#"*8, " - Test Case 3 [Negative Values List] - ", "#"*8, "\n")
test_function([[_ for _ in range(-25, -1)], 6])
test_function([[_ for _ in range(-25, -1)], -6])

# Test Case 4
print("\n", "#"*8, " - Test Case 4 [NaN value for target] - ", "#"*8, "\n")
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], '6'])
