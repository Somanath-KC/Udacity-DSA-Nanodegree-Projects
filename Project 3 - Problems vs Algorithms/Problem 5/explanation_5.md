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
* TrieNode().insert() Traverses throught each char in the given word, which take linear order of time O(n).
* TrieNode().suffixes() This medthod will visit all the child nodes. Such that branches of each node is N. We also need to visit the every child of node which is similar to length of each suffix of length L. Which takes O(m*n) order of time.
* Trie().insert() The time-complexity for this method is O(n), Because it traverses through every word of input.
* Trie().find() In worst case the this method will visit every node in the dictionary if it dose not exists, which makes the time complexity O(n)
* By Ignoring the lower order terms and summing parts the overall time complexity is O(n).
	
### Space Complexity

* The Spce complexity of this problem is O(n), In worst case each and every character is inserted in dictionary if not already exists.

### Refrences
* https://www.youtube.com/watch?v=TRg9DQFu0kU