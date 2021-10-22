# Problem - 7

> HTTPRouter using a Trie

For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.

There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.


## Design Choices

* As instructed used Trie Data Structure to store and lookup routes for HTTPRouter

## Efficiency

The overall time complexity for this problem is O(n) and space complexity is O(m * n). 

### Time Complexity

* RouterTrieNode().insert() Traverses throught each path in the given path_list, which take linear order of time O(n).
* RouterTrie().suffixes() This medthod will visit all the child nodes. Such that branches of each node is N. We also need to visit the every child of node which is similar to length of each suffix of length L. Which takes O(m*n) order of time.
* RouterTrie().insert() The time-complexity for this method is O(n), Because it traverses through every path word of input.
* RouterTrie().find() In worst case the this method will visit every node in the dictionary if it dose not exists, which makes the time complexity O(n)
* Router.lookup() in this method ignoring the self.routes.find() & self.split_path(), overall time compliexty of this method is O(n).
* Router.split() traverses through every char of string, hence it takes O(n) order of time.
* By Ignoring the lower order terms and summing parts the overall time complexity is O(n).
	
### Space Complexity

The Spce complexity of this problem is O(m * n) where m is number of words in path and n is the path.
