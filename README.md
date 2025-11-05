## Pattern searching algorithms
### 1. alphabet, text, pattern 
Let A be a set of elements (eg. letters), called the alphabet.

Let T be a sequence of elements that belong to the alphabet, called the text. Elements from the text are indexed from 0 to |T|.

Let P be a sequence of elements that belong to the alphabet, called the pattern. Elements from the pattern are indexed from 0 to |P|.
#### Example
*A = {A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z}* and *|A| = 26*

*T = AABACABAC* and *|T| = 9* 

*P = BAC* and *|P| = 3* 

### 2. matchesAt function
Pattern *P* matches *T* at position *p* if T[*p* + *i*] = P[*i*], *p* = 0, 1, 2, ..., |*P*| - 2, |*P*| - 1   

matchesAt condition: *p* < |*T*| - 1

optimistic scenario: 1 comparison when T[p + 0] != P[0]

pesimistic scenario: (|T| - |P| + 1) * |P| comparisons
#### Example no. 1
matchesAt(T, P, p), *T = AABACABAC*, *P = BAC*, *p* = 1 returns **false**


ABA != BAC
#### Example no. 2
matchesAt(T, P, p), *T = AABACABAC*, *P = BAC*, *p* = 2 returns **true**


ABA == ABA
### 3. Naive algorithm 
Naive algorithm runs |T| - |P| + 1 (i = 0, 1, 2, ..., |T| - |P| + 1) iterations. In each iterations function matchesAt is calling with p = i.

