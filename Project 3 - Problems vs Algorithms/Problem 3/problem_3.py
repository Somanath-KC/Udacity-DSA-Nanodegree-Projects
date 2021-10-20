def rearrange_digits(input_list=[]):
    """
    Rearrange Array Elements so as to form two
    number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    output_list = [0, 0]

    if input_list is None:
        return output_list

    sorted_input_list = mergesort(input_list)
    for i in range(0, len(input_list)):
        if i % 2 == 0:
            output_list[0] = (output_list[0] * 10) + sorted_input_list[i]
        else:
            output_list[1] = (output_list[1] * 10) + sorted_input_list[i]

    print("Input List ->", input_list, ", Sorted List ->",
          sorted_input_list, ", Output List ->", output_list)
    return output_list


# Using merge sort in descending order
# Ref: https://classroom.udacity.com/nanodegrees/nd256/parts/da17de0f-f834-46f8-bb48-ee2705d95dc4/modules/b849517a-9ee0-4fa8-8e22-b49fd084a350/lessons/902b8515-a2ef-485b-9543-f9a9aad9843f/concepts/50d8c2cc-7ac3-41c3-a9dd-4e407bb6e8e0
# Ref: https://knowledge.udacity.com/questions/370722

def mergesort(items):

    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = mergesort(items[:mid])
    right = mergesort(items[mid:])

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


#####     #####
#   Testing   #
#####     #####

# Test Case 1
print("\n", "#"*8, " - Test Case 1 [General Working] - ", "#"*8, "\n")
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

# Test Case 2
print("\n", "#"*8, " - Test Case 2 [Single Value] - ", "#"*8, "\n")
test_function([[1, 1, 1, 1, 1], [111, 11]])
test_function([[1], [1, 0]])

# Test Case 3
print("\n", "#"*8, " - Test Case 3 [Empty Value] - ", "#"*8, "\n")
test_function([[], [0, 0]])
test_function([None, [0, 0]])
