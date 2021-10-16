import sys
import heapq as hq


class Node:
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_right_child(self, node):
        self.right = node

    def set_left_child(self, node):
        self.left = node

    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.left

    def has_right_child(self):
        return self.right is not None

    def has_left_child(self):
        return self.left is not None

    def __lt__(self, node):
        return self.value < node.value

    def __repr__(self):
        return str(self.value)


class CharNode(Node):
    def __init__(self, char=None, value=None):
        super().__init__(value=value)
        self.char = char

    def set_char(self, char):
        self.char = char

    def get_char(self):
        return self.char

    def __repr__(self):
        return "{}:{}".format(self.char, self.value)


class BinaryTree:
    def __init__(self, value=None):
        self.root = Node(value=value)

    def get_root(self):
        return self.root

    def set_root(self, node):
        self.root = node


class Huffman(BinaryTree):
    def __init__(self, value=None):
        super().__init__(value=value)
        self.text_freq = {}
        self.heap = []
        self.char_codes = {}
        self.encoded_text = ""
        self.decoded_text = ""

    def calc_frequency(self, text):
        """
            Calculates the character frequency in input string
        """

        for i in text:
            if self.text_freq.get(i):
                self.text_freq[i] += 1
            else:
                self.text_freq[i] = 1

        return self.text_freq

    def heapify(self):
        """
            Store the character frequency in heapq.
        """

        if len(self.text_freq.keys()) == 0:
            return

        self.heap = []
        for key, freq in self.text_freq.items():
            self.heap.append(CharNode(key, freq))

        hq.heapify(self.heap)
        return self.heap

    def generate_binary_tree(self):
        """
           Generates binary tree from min heap
        """
        while len(self.heap) > 1:
            min1 = hq.heappop(self.heap)
            min2 = hq.heappop(self.heap)

            new_node = Node(min1.value+min2.value)
            new_node.left = min1
            new_node.right = min2
            hq.heappush(self.heap, new_node)
        else:
            self.root = hq.heappop(self.heap)

    def generate_huffman_code(self, node=None, b_code=""):
        """
            Generates Huffman code by travesing through every node in tree
        """
        if node is None and b_code == "":
            node = self.get_root()

        if node.right is None and node.left is None:
            if b_code == "":
                b_code = "1"
            self.char_codes[node.char] = b_code
        else:
            if node.right is not None:
                self.generate_huffman_code(node.right, b_code+'1')
            if node.left is not None:
                self.generate_huffman_code(node.left, b_code+'0')

    def generate_encoded_string(self, text):
        """
            Generates binary encoded string using huffman code of character.
        """
        out_encode = ""
        for i in text:
            out_encode += self.char_codes[i]

        self.encoded_text = out_encode
        return self.encoded_text

    def decode_binary_string(self, b_string, root, node, pos):
        """
            Decodes the Binary String and Get Original Data
        """
        if node.left is None and node.right is None:
            self.decoded_text += node.char
            if pos == 0:
                pos += 1
            if len(b_string[pos:]) > 0:
                self.decode_binary_string(b_string[pos:], root, root, 0)
            else:
                return self.decoded_text
        elif b_string[pos] == '1':
            self.decode_binary_string(b_string, root, node.right, pos+1)
        elif b_string[pos] == '0':
            self.decode_binary_string(b_string, root, node.left, pos+1)

    def encode(self, text):
        """
            Perform Huffman Encoding on given text
        """
        if text == "":
            return "0"
        self.calc_frequency(text)
        self.heapify()
        self.generate_binary_tree()
        self.generate_huffman_code()

        return self.generate_encoded_string(text)

    def decode(self, data, tree=None):
        """
            Perform's Huffman Decoding
        """
        if data == "0":
            return ""
        if tree is None:
            tree = self.root
        self.decode_binary_string(data, tree, tree, 0)
        return self.decoded_text


def huffman_encoding(data):
    huffman = Huffman()
    encoded_string = huffman.encode(data)
    huffman_tree = huffman.get_root()
    return encoded_string, huffman_tree


def huffman_decoding(data, tree):
    huffman = Huffman()
    huffman.set_root(tree)
    decoded_string = huffman.decode(data)
    return decoded_string


def test_case(num, text):
    """
        Used for Debugging
    """
    print("\n", "#"*8, " - Test Case " + str(num) + " - ", "#"*8, "\n")
    text = text
    huffman = Huffman()
    encoded_string = huffman.encode(text)
    print("Input String -> ", text)
    print("Encoded String -> ", encoded_string)
    decoded_string = huffman.decode(encoded_string, huffman.get_root())
    print("Decoded String -> ", decoded_string)
    assert(text == decoded_string)
    print("\nAssertion Passed!\n")


if __name__ == "__main__":
    codes = {}

    # Test Case 1
    print("\n", "#"*8, " - Test Case 1 [General Working] - ", "#"*8, "\n")
    sentence = "The bird is the word"
    print("The size of the data is: {}\n".format(sys.getsizeof(sentence)))
    print("The content of the data is: {}\n".format(sentence))

    encoded_data, tree = huffman_encoding(sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # Test Case 2
    print("\n", "#"*8, " - Test Case 2 [Same Character] - ", "#"*8, "\n")
    sentence = "GGGGG"
    print("The size of the data is: {}\n".format(sys.getsizeof(sentence)))
    print("The content of the data is: {}\n".format(sentence))

    encoded_data, tree = huffman_encoding(sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # Test Case 3
    print("\n", "#"*8, " - Test Case 3 [Empty Spaces] - ", "#"*8, "\n")
    sentence = "    "
    print("The size of the data is: {}\n".format(sys.getsizeof(sentence)))
    print("The content of the data is: {}\n".format(sentence))

    encoded_data, tree = huffman_encoding(sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # Test Case 4
    print("\n", "#"*8, " - Test Case 4 [Empty String] - ", "#"*8, "\n")
    sentence = ""
    print("The size of the data is: {}\n".format(sys.getsizeof(sentence)))
    print("The content of the data is: {}\n".format(sentence))

    encoded_data, tree = huffman_encoding(sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
