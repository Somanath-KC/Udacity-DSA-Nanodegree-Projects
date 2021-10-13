# Problem - 5

A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

Finally you need to link all of this together in a block chain, which you will be doing by implementing it in a linked list. All of this will help you build up to a simple but full blockchain implementation!

## Design Choices

As Block chain is made up of links connecting individual blocks, Linked List would be the great fit to implement block chain. With this we will 
store the hash digest of the previous block in the current block to maintain data integrity of the block. 

Since we keep track of head and tail of linked list, it would avoid traversing through entire linked list when adding new block of data.


## Efficiency

The overall time complexity for this problem is O(1) and space complexity is O(n).


### Time Complexity

* BlockChain.append() method will take O(1) time to insert new record to block chain. Because we are keeping track of linked list's tail which will be used to insert new record in constant time.

### Space Complexity

* The Space complexity of this problem is O(n*(m+34)+2) -> O(n). The space depends on number of inputs, Because each block is added for new record i.e n input blockchain contains n blocks.
