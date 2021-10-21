 # Problem - 4

Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.

> O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.

## Design Choices

Used linear search approach to filter 0s, 1s, and 2s and stored in separate arrys. Finally All the three arrys were merged and returned.

## Efficiency

The overall time complexity for this problem is O(n) and space complexity is O(1).


### Time Complexity

* sort_012() function takes input input_list of length n containing 0, 1, 2. The algorithm will traverse through each element once hence it takes linear time order. Therefor the worst-case time complexity is O(n).
	
### Space Complexity

* The Spce complexity of this problem is O(1) The variable assignments is done only once through out the algorithm.
