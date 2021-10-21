# Problem - 1

> Find the square root of the integer without using any Python library. You have to find the floor value of the square root.
> For example if the given number is 16, then the answer would be 4.
> If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.
> The expected time complexity is O(log(n))

## Design Choices

Used Binary Search approach using loop to calculate the square root. This will find the nearest possible in-case of fractional value or perfect square if the square root value is whole number. 

## Efficiency

The overall time complexity for this problem is O(log(n)) and space complexity is O(1).


### Time Complexity

* sqrt() takes integer number, which will then perform binary search variant approach to find squareroot. The worst-case time complexity of this function is O(log(n)) since it performing binary search.
	
### Space Complexity

* The Spce complexity of this problem is O(1) becasue the initalization of data happens only once. Therefore it has constant space complexity.

