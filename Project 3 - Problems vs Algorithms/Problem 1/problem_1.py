def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if type(number) != int or number < 0:
        return

    if number in [0, 1]:
        return number

    left = 1
    right = number//2  # Becase square root of n is always less than n/2
    middle = (left + right)//2

    while right >= left:
        if middle*middle == number:
            return middle
        elif middle*middle < number:
            left = middle+1
        else:
            right = middle-1
        middle = (left + right)//2

    return middle


#####     #####
#   Testing   #
#####     #####

# Test Case 1
print("\n", "#"*8, " - Test Case 1 [General Working] - ", "#"*8, "\n")
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (4 == sqrt(24)) else "Fail")


# Test Case 2
print("\n", "#"*8, " - Test Case 2 [Negative Values] - ", "#"*8, "\n")
print("Pass" if (None is sqrt(-9)) else "Fail")


# Test Case 3
print("\n", "#"*8, " - Test Case 3 [Zero value] - ", "#"*8, "\n")
print("Pass" if (0 == sqrt(0)) else "Fail")


# Test Case 4
print("\n", "#"*8, " - Test Case 4 [Null value] - ", "#"*8, "\n")
print("Pass" if (None is sqrt(None)) else "Fail")
