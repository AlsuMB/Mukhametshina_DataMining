import math

from hashlib import *


class CBFs:

    def __init__(self, expected_inputS, hashing_ns, length_of_CBF, false_positiveP=0.0001):

        self.expected_inputS = expected_inputS  # The expected input size (n)
        self.false_positiveP = false_positiveP  # The desired false positive proability (p)

        # Finding the array size (m) from the function
        self.size = -1 * round((self.expected_inputS * math.log(self.false_positiveP)) / (math.log(2)) ** 2)
        if (self.size < length_of_CBF):
            self.size = length_of_CBF

        self.array = [0] * self.size  # Creating a list of zeros with size m

        self.hashing_n = hashing_ns  # Finding the optimal number of hashing functions

        # Check if the number of hashing funcitons is greater than 6 or less than one
        # So, the number of hashing functions stays in the bounderies between 1 and 6
        if (self.hashing_n > 14):
            self.hashing_n = 6
        elif (self.hashing_n < 1):
            self.hashing_n = 1

    def hashing(self, element):  # Define the hash functions
        keys = []  # That list will the keys for the element
        library = [md5, sha1, sha224, sha256, sha384, sha512, blake2b, blake2s, sha3_224, sha3_256, sha3_384, sha3_512,
                   shake_128, shake_256]
        count = 0
        for i in library:
            hash_object = i(element.encode())
            keys.append(int(hash_object.hexdigest(), 16))
            if count >= self.hashing_n:
                break
            count += 1

        return keys  # Return the list of keys

    def add(self, element):  # use the Add method to add elements into the array

        keys = self.hashing(element)  # Find the hashing keys for the element
        key = 0  # Reset the current key

        for indx in range(self.hashing_n):  # Loop through the every key in the list up to the limit
            key = int(keys[indx] % self.size)  # Find the key moduls from the list size
            self.array[key] += 1  # Increase the counter value by one

    def is_exist(self, element):
        keys = self.hashing(element)
        keyl = 0
        for indx in range(self.hashing_n):  # Loop through the every key in the list up to the limit
            key = int(keys[indx] % self.size)  # Find the key moduls from the list size
            if self.array[key] == 0:
                return False
        return True
