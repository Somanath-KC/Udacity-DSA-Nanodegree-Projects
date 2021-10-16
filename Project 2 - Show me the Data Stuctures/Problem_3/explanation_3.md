# Problem - 3

A. Huffman Encoding
Assume that we have a string message comprising of characters to be encoded. The string message can be an unsorted one as well. We will have two phases in encoding - building the Huffman tree (a binary tree), and generating the encoded data.

B. Huffman Decoding
Once we have the encoded data, and the (pointer to the root of) Huffman tree, we can easily decode the encoded data 

## Design Choices

* As suggested in the problem page, I've used binary tree to construct Huffman tree. 
* For calculating the frequency of each character I've used dictionaries with character and frequencry as key value pairs.
* To get the characters with minimum frequency I've used min heap.
* For Generating the Huffman code I've used recursive approach in which the base case will the leaf and huffman code is concatenated through out the traversal.


## Efficiency

The overall time complexity for this problem is O(n log n) and space complexity is O(n).

### Time Complexity

> Encoding
While Encoding, . Runtimes for creation of generating binary tree with worst case time complexity of  O(n), Where as Min Heap will take constant time for pushing & popping of nodes i.e O(1), But for heapifing the list the algorithm suggessts worst case time complexity of O(n log n). 
Therefore, O(n) + O(n log n) -> O(n log n)

> Decoding
While Decoding, We'll have to traverse through every node of the tree when there all unique characters in the input string which tends to take linear time.
Therefore the worst case time complexity for decoding is O(n)
	
### Space Complexity

* The Average Space complexity is the number of unique characters in the input string i.e k -> O(k).
* In the worst case the the size of dictionary will the length of input stirng if all of the were unique characters, 
Hence the worst case space complexity is O(n).
