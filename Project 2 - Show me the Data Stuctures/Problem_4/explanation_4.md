# Problem - 4

In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.

## Design Choices

For this problem I've choosed recursive approach to accomplish the task. The function will be called until depth of groups is reached or if the given id is found.

## Efficiency

The overall time complexity for this problem is O(n) and space complexity is O(n).

### Time Complexity

* The is_user_in_group() function will be called recursively until traversing through every group or the given id is found. Therefore the time complexity is O(n).
	
### Space Complexity

* Since the function is called for every group in the worst case, the space complexity will be O(5n) -> O(n).