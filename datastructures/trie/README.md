# Data Structure: Trie [![Build Status](https://travis-ci.org/lukebiggerstaff/simple-python-ds.svg?branch=master)](https://travis-ci.org/lukebiggerstaff/simple-python-ds)

## Operations include
- insert - takes a string and creates a node for each character in the string with one additional empty node with a boolean value indicating end of the string time complexity is O(k) with k being the length of the string
- search - takes a string and traverses the character nodes until a character in the string is not present in the trie or the end character boolean is found. returns a boolean. takes O(k) time where k is the length of the string
- delete - much like search but will keep track of the last branch starting with root of trie. time complexity if O(k) where k is length of the string
