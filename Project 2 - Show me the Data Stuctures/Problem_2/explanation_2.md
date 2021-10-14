# Problem - 2

For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

## Design Choices

For this problem I've choosed recursive approach to accomplish the task.

## Efficiency

The overall time complexity for this problem is O(n) and space complexity is O(n).

### Time Complexity

* The Find_files() function will be called recursively until traversing through every folder. Therefore the time complexity is O(n).
	
### Space Complexity

* Since the function is called for every directory, considering input path with n directories the space complexity will be O(5n) -> O(n).