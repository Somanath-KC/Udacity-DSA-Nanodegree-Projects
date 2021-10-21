 # Problem - 3

Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

> Example: [1, 2, 3, 4, 5]
> The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

## Design Choices

Used MergeSort to sort the input_list items in decending order, then traversed through each element in sorted input list to get max sum numbers.

## Efficiency

The overall time complexity for this problem is O(nlog(n)) and space complexity is O(n).


### Time Complexity

* mergesort() function takes input input_list of length n and sorts the items in decending order which will take O(n log(n)) order of time to sort elements.
* In rearrange_digits(), After completing mergesort() the rearrange_digits traveses through every element of sorted input list which takes linear order of time O(n). Therfore the overall complexity is O(n log(n)) + O(n) -> O(n log(n)).
	
### Space Complexity

* The Spce complexity of this problem is O(n) Because the merge sort take O(n) space complexity to sort elements
* > Ref: https://stackoverflow.com/questions/10342890/merge-sort-time-and-space-complexity
