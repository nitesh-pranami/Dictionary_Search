# Dictionary Search
## Problem: 
You have to design a dictionary Data structure, where when any word is entered, it searches the entered word in the dictionary and returns the relevant searched word if any!
## Approach:
1. First I implemented a Trie to load and search given query keyword
2. Then I improved by adding the Levenshtein distance algorithm approach so in case if query keyword is matching up to a given threshold keyword distance. Here are keywords with partial recommendations when it is matched up to 80%. user can customise in code by setting variable name **threshold**
3. I have added elapsed time to measure search performance
* Run time complexity: O(M*N) 

* Memory Space complexity: O(M+N)
* where m is max word length and n is number of nodes in the trie.

```shell
$ python3 dict_search.py
Keyword search: hello
Results: 

        Recommended | bello
        Recommended | cello
        Recommended | hallo
        Recommended | helio
        Recommended | hell
        Exact       | hello
        Recommended | hellos
        Recommended | hells
        Recommended | hollo
        Recommended | hullo

Elapsed Time: 10.2882 ms
```
Here are keywords with partial recommendations when it is matched up to 80%. 
## Improvements:
I wanted to introduce phonetic match of the keyword but it needed some more time
i.e. if there is a keyword in the dictionary "cat" but the user wants to search "kat" so here both words are phonetically similar.



