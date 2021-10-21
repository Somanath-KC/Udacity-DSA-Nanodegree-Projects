 # Problem - 5

Autocomplete with Tries

> Before we move into the autocomplete function we need to create a working trie for storing strings. We will create two classes:
* A Trie class that contains the root node (empty string)
* A TrieNode class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.


## Design Choices

Used Trie Data Structure to store the words, Such that we can save some memory and can easily retrive the suffixes for auto complete purpose.

## Efficiency
The overall time complexity for this problem is O(n) and space complexity is O(n).


### Time Complexity
* insert() method will travrse through every element in input word and inserts to trie node, which takes linear time complexity O(n).
	
### Space Complexity

* The Spce complexity of this problem is O(n), In worst case each and every character is inserted in dictionary if not already exists.

### Refrences
* https://www.youtube.com/watch?v=TRg9DQFu0kU