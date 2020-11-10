#File: AlgorithmsPS5.py
"""
Jason Snare
CS-343
Problem Set #5
Huffman algorithm implementation for compression/decompression.
"""

class HeapNode:
    """
    Node object for HuffmanEncoder
        * __init__(): constructor taking in character and frequency.
        * __str__(): toString for debugging purposes.
    """
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        
    def __str__(self):
        return "Node " + "'" + self.char + "'" + " with frequency " + str(self.freq)
    

class HuffmanEncoder:
    """
    Huffman encoding object
        * __init__(): Constructor takes in character frequency dictionary.
        * buildPQ(): Creates node objects from dictionary items and builds priority queue.
        * buildHT(): Creates Huffman tree from priority queue.
        * build_codes(): Creates compressed binary letter codes.
        * build_codes_aux(): Recursive auxillary function for build codes.
        * encode(): Takes in string and returns compressed code.
        * decode(): Takes in encoded text and returns original string.
    """
    def __init__(self, char_dict):
        self.char_dict = char_dict
        self.pq = []
        self.codes = {}
        self.reverse_mapping = {}    
        
    def buildPQ(self):
        self.char_dict = {k: v for k, v in sorted(self.char_dict.items(), key=lambda item: item[1])}
        for item in self.char_dict:
            self.pq.append(HeapNode(item, self.char_dict[item]))
            
    def buildHT(self):
        while(len(self.pq) > 1):
            node1 = self.pq.pop(0)
            node2 = self.pq.pop(0)
            merge_node = HeapNode(None, node1.freq + node2.freq)
            merge_node.left = node1
            merge_node.right = node2
            self.pq.append(merge_node)
            self.pq.sort(key=lambda x: x.freq)
            
    def build_codes_aux(self, root, current_code):
        if(root == None):
            return
        if(root.char != None):
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return
        self.build_codes_aux(root.left, current_code + "0")
        self.build_codes_aux(root.right, current_code + "1")

    def build_codes(self):
        root = self.pq[0]
        current_code = ""
        self.build_codes_aux(root, current_code)
        
    def encode(self, text):
        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]
        return encoded_text
        
    def decode(self, encoded_text):
        current_code = ""
        decoded_text = ""
        for char in encoded_text:
            current_code += char
            if(current_code in self.reverse_mapping):
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = ""
        return decoded_text


if __name__ == "__main__": #start-up code
    
    freq_dict = ({"A":9, "B":2, "C":2, "D":3, "E":12, "F":2, "G":3, "H":2, "I":9, "J":1, "K":1, "L":4, "M":2, 
             "N":6, "O":8, "P":2, "Q":1, "R":6, "S":4, "T":6, "U":4, "V":2, "W":2, "X":1, "Y":2, "Z":1})
   
    encoder = HuffmanEncoder(freq_dict)
    encoder.buildPQ()
    encoder.buildHT()
    encoder.build_codes()
    encoded_text = encoder.encode("ACE")
    decoded_text = encoder.decode(encoded_text)
    print("Encoded text: " + encoded_text)
    print("Decoded text: " + decoded_text)