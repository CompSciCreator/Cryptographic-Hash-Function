SHA-1 Cryptographic Hash Function 

Overview 

The SHA-1 cryptographic hash function is among the most popular hash functions in the 
world. It was developed by the National Security Agency (NSA) and published by the National 
Institute of Standard and Technology (NIST) in 1993. There are many different versions of the 
SHA (secure hash algorithm) such as SHA-256, SHA-224, SHA-384, and SHA-512. We chose 
SHA-1 because it is one of the first standardized hashing algorithms and it led to the 
development of more robust hash functions. SHA-1 fulfils all the requirements of hash functions 
although it is considered insecure by today’s standards due to some minor vulnerabilities that 
allow for hash collisions. In fact, it’s been considered insecure since 2005 and it was completely 
retired by NIST in 2022, saying its use is “inadvisable”. We believe SHA-1 is still a viable 
algorithm to use for learning and demonstration purposes. 
The algorithm takes an input and produces a 160-bit hash value which is known as a 
message digest. The message digest is rendered as a 40 digit long hexadecimal number. The 
algorithm hashes messages in blocks where each block passes through some number of rounds 
similar to a block cipher.  

Steps 

SHA-1 has 8 steps in total. They are as follows. 

1. Get the plaintext input (up to 264 bits long) 

2. Input padding: The input gets padded to ensure its length is congruent to 448 modulo 
512. That is to say, it is a multiple of 512 bits. This prepares the input for processing in 
512-bit blocks. 

3. Round word computation: The message is divided into blocks of 512 bits and each block 
is divided into 16 words of 32 bits. SHA-1 then expands these 16 words into an 80-word 
schedule. The extra words are created by XORing and rotating bits from previous words. 

4. Round initialize: Initialization of five working variables with specific constant values. 
These are used to compute the hash value iteratively. 

5. Round Constants: SHA-1 uses four constant values, each applied to a specific range of 
rounds. There are typically 80 rounds, so 20 rounds per constant value. Note these are 
different from the 5 constants in step four. 

6. 80 rounds (Compression function): The main loop of the program. Divided into four 
stages of 20 rounds each. In each round, we rotate the bits of the intermediate hash 
values, then a sequence of logical operations are performed on the five working variables 
using the four constant words generated in the previous step. 

7. Final round addition: After all 80 rounds, the resulting values for the working variables 
are added to the original constant values 

8. Produce the final hash: Combines the results from the final round addition to form the 
final message digest. 

Sources 

Geek for Geeks: SHA-1 Hash in Java:  
https://www.geeksforgeeks.org/sha-1-hash-in-java/ 

NIST Retires SHA-1 Cryptographic Algorithm:
https://www.nist.gov/news-events/news/2022/12/nist-retires-sha-1-cryptographic-algorithm 

Information Security: Principles and Practices, 2nd edition, Mark Stamp. P 133 
