# Problem - 1

> For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.

## Design Choices

Doubly Linkedlist & Dictionaries(Hash Map) for LRU Cache Implementation.

* With Doubly Linkedlist, The insertion, removal & moving of values will take constant time.

* Dictionaries were used to make look-ups in constant time. Therefore references to linkedlist nodes were stored in dictionary.

## Efficiency

The overall time complexity for this problem is O(1) and space complexity is O(n).


### Time Complexity

* Since we are using dictonories for storing the refrences of cache values, LRU_Cache().get() method will O(1) time for the lookup.
* LRU_Cache().set() method will also take O(1) time becasue appending the value to linkedlist takes constant time.
	
### Space Complexity

* The Spce complexity of this problem is O(n) becasue the size may vary with respect to the storage size of LRU Cache.

