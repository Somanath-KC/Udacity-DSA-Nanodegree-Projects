# Problem - 2

You are given a sorted array which is rotated at some random pivot point.

> Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

## Design Choices

Used Binary Search Variant approach using recursion to find the index of given target.

## Efficiency

The overall time complexity for this problem is O(log(n)) and space complexity is O(1).


### Time Complexity

* rotated_array_binary_search() takes input_list, start_index, end_index and target integer number, which will then perform binary search variant approach to find the index of the target. The worst-case time complexity of this function is O(log(n)) since it performing binary search.
	
### Space Complexity

* The Spce complexity of this problem is O(1) becasue the initalization of data happens only once. Therefore it has constant space complexity.
