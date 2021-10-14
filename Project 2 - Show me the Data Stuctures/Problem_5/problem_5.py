import json
import hashlib
import datetime


class DoublyNode:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        """
            Add's value at list tail.
        """
        if self.length == 0:
            self.head = DoublyNode(value)
            self.tail = self.head
        else:
            t_node = DoublyNode(value)
            t_node.prev = self.tail
            self.tail.next = t_node
            self.tail = t_node
        self.length += 1

        return self.tail

    def size(self):
        """
            Return size of linked list
        """
        return self.length

    def get_head(self):
        """
            Return's node present at head.
        """
        return self.head

    def get_tail(self):
        """
            Return's node present at tail.
        """
        return self.tail


class Block(DoublyNode):
    def __init__(self, index, data, prev_hash):
        super().__init__(value=None)
        self.index = index
        # TimeStamp at creation on new block
        self.__time_stamp = datetime.datetime.now(
            datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f%Z")
        self.__data = data
        self.__prev_hash = prev_hash
        self.__hash = self.calc_hash()
        self.value = self.to_json()

    def to_json(self):
        """
            Returns data of current block info in json format.
        """
        data = {"index": self.index,
                "time_stamp": self.__time_stamp,
                "data": self.__data,
                "hash": self.__hash,
                "prev_hash": self.__prev_hash
                }
        return json.dumps(data)

    def get_hash(self):
        """
            Return's current block hash digest
        """
        return self.__hash

    def calc_hash(self):
        """
            Calculate Hashdigest  for current block
        """
        data = {"index": self.index,
                "time_stamp": self.__time_stamp,
                "data": self.__data,
                "prev_hash": self.__prev_hash
                }

        json_encoded_data = json.dumps(data).encode()
        self.__hash = hashlib.sha256(json_encoded_data).hexdigest()
        return self.__hash


class BlockChain(DoublyLinkedList):
    def __init__(self):
        super().__init__()

    def append(self, data=None):
        """
            Append's new block to chain.
        """
        # Check If Data is not empty
        if not data:
            return
        # Calc Prev Hash
        if not self.head:
            prev_hash = 0
            index = 0
        else:
            prev_hash = self.tail.get_hash()
            index = self.tail.index + 1
        # Creating New Block
        new_block = Block(index=index, data=data, prev_hash=prev_hash)

        if self.size() == 0:
            self.head = new_block
            self.tail = self.head
        else:
            new_block.prev = self.tail
            self.tail.next = new_block
            self.tail = new_block
        self.length += 1


#####     #####
#   Testing   #
#####     #####


# Test case 1 / Add Diffrent Data Blocks
print("\n",  "#"*10, " - Test Case 1 - ", "#"*10, "\n")
block_chain = BlockChain()

print(block_chain.size())  # Prints 0

# Add new record to block chain
block_chain.append("Record 1")
print(block_chain.size())  # Prints 1
print(block_chain.head)  # Prints Record 1 Block data
print(block_chain.tail)  # Prints Record 1 Block data because there is only one block in chain


# Add new record to block chain
block_chain.append("Record 2")
print(block_chain.size())  # Prints 2
print(block_chain.head)  # Prints Record 1 Block data
print(block_chain.tail)  # Prints Record 2 Block data


# Add new record to block chain
block_chain.append("Record 3")
print(block_chain.size())  # Prints 3
print(block_chain.head)  # Prints Record 1 Block data
print(block_chain.tail)  # Prints Record 3 Block data


# Test case 2 / Blocks with same data but diffrent hash digest
print("\n",  "#"*10, " - Test Case 2 - ", "#"*10, "\n")
block_chain_2 = BlockChain()
block_chain_2.append("Same Record")
block_chain_2.append("Same Record")
print(block_chain_2.head.value)
print(block_chain_2.tail.value)
assert(block_chain_2.head.get_hash() != block_chain_2.tail.get_hash())


# Test case 3 / Inserting Empty Data
print("\n",  "#"*10, " - Test Case 3 - ", "#"*10, "\n")
block_chain_2 = BlockChain()
block_chain_2.append()
block_chain_2.append()
print(block_chain_2.tail)  # Prints None sine empty data not accepted!
assert(block_chain_2.size() == 0)
