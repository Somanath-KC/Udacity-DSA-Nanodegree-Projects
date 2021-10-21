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

add_handler() & lookup() need to traverse through every word of the path in worst-case, Therefore the worst-case time complexity is O(n)
	
### Space Complexity

The Spce complexity of this problem is O(m * n) where m is number of words in path and n is the path.
