import sys
import time

class TrieNode:
    def __init__(self):
        self.word = None
        self.child = {}

        global NodeCount
        NodeCount += 1

    def insert( self, word ):
        node = self
        for letter in word:
            if letter not in node.child: 
                node.child[letter] = TrieNode()

            node = node.child[letter]

        node.word = word

#Enter the directory address of the dictionary list
Dictionary = "/Users/charlie/Desktop/GTROPY/list.txt"; 
keyword = input('Keyword search: ')
threshold = .2
MAXCOST=int((len(keyword )*threshold)+.5)

NodeCount = 0
WordCount = 0



trie = TrieNode()
for word in open(Dictionary,"rt").read().split():
    WordCount += 1
    trie.insert(word)

def search( word, maxCost ):
    currentRow = range( len(word) + 1 )
    results = []
    for letter in trie.child:
        searchRecursive( trie.child[letter], letter, word, currentRow, 
            results, maxCost )
    return results

def searchRecursive( node, letter, word, previousRow, results, maxCost ):

    columns = len( word ) + 1
    currentRow = [ previousRow[0] + 1 ]

    for column in range( 1, columns ):

        insertCost = currentRow[column - 1] + 1
        deleteCost = previousRow[column] + 1

        if word[column - 1] != letter:
            replaceCost = previousRow[ column - 1 ] + 1
        else:                
            replaceCost = previousRow[ column - 1 ]

        currentRow.append( min( insertCost, deleteCost, replaceCost ) )

    if currentRow[-1] <= maxCost and node.word != None:
        if currentRow[-1]==0:
            category='Exact      '
        else:
            category='Recommended'
        results.append((node.word,category))

    if min( currentRow ) <= maxCost:
        for letter in node.child:
            searchRecursive( node.child[letter], letter, word, currentRow, 
                results, maxCost )

start = time.time()
results = search( keyword, MAXCOST )
end = time.time()
print("Results: \n")

for result in results: 
   print("\t%s | %s" % (result[1], result[0]))
print("\nElapsed Time: %g ms\n" % (1000*(end - start)))


