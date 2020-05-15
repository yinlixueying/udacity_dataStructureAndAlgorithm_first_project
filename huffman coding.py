import sys

class huffman_Node(object):
    def __init__(self, value, freq, left=None, right=None):
        self.left = left;
        self.right = right;
        self.value = value;
        self.freq = freq;
    def comparsion(self, node)
        return self.value < node.value;
def get_frequency(str):
    freq = {};
    for i in str:
        if i in freq:
            freq[i] += 1;
        else:
            freq[i] = 1;
    sorted_freq = sorted(freq.items(), key=lambda item:item[1]);

def huffman_encoding(data):
    pass

def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))