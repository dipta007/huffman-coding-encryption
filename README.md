# huffman-coding-encryption

### Papers
- [x] [Text Encryption with Huffman Compression](https://research.ijcaonline.org/volume54/number6/pxc3882307.pdf)
- [x] [EFFICIENT HUFFMAN DECODING WITH TABLE LOOKUP ](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.93.9447&rep=rep1&type=pdf)

## Encoding

To run encoding, you need to provide a text file.

```
$ python encode.py filename
```

## Decoding
To run decoding, you need to provide a encoded file generated from previous step.

```
$ python decode.py filename
```

## Comparing
To compare the encoding and decoding results, you need to provide two files - one the input file and the other the decoded file.


```
$ python compare.py filename1 filename2
```

### References
- [x] [Huffman Coding](https://en.wikipedia.org/wiki/Huffman_coding)
- [x] https://www.geeksforgeeks.org/huffman-decoding/
- [x] https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/