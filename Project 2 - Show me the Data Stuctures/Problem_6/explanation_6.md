# Problem - 6

Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.

## Design Choices

As given the inputs will be linked lists, input linked lists will be converted to sets before performing union or intersection, such that the union & intersection will take O(n) time.


## Efficiency

The overall time complexity for this problem is O(n) and space complexity is O(n).


### Time Complexity

* To perform union() operation, we'll traverse throught every element of the linkedlists to convert them to set which will be of O(m) + O(n) time complexity for two input linked list respectily. The set union operation will take O(len(m)+len(n)), By Ignoring the lower order terms the overall time complexity for union operation is O(n). 

* To perform intersection() operation, we'll traverse throught every element of the linkedlists to convert them to set which will be of O(m) + O(n) time complexity for two input linked list respectily. The set intersection operation will take O(len(m)+len(n)) in worst case, By Ignoring the lower order terms the overall time complexity for union operation is O(n). 
  
> Ref: https://wiki.python.org/moin/TimeComplexity

### Space Complexity

* The Space complexity of this problem is O(len(m) + len(n) + 32)
-> O(n). Space complexity for both union & intersetion will depend on the size two input linkedlist, Therefore the worst case is O(m+n+2(32)) -> O(n)