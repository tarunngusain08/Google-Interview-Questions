# Given an array of n strings with length m return true if there is one pair such that 
# there is only one difference between the words, e.g, abcd and abce would yield true, 
# but abcc and abdd would be false.

from collections import defaultdict
class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isWord = False
    
class Trie:
    def __init__(self):
        self.root = Node("*")
    
    def addWordAndCheckDifference(self, root, word, count):
        if word == "": return False
            
        if word[0] not in root.children: 
            root.children[word[0]] = Node(word[0])
            count += 1

        if len(word)==1: 
            root.children[word[0]].isWord = True
            if count <= 1: return True
            return False

        return self.addWordAndCheckDifference(root.children[word[0]], word[1:], count)

def OneDifferencePairExistsWithTrie(listOfWords):
    trie = Trie()
    for word in listOfWords:
        ans = trie.addWordAndCheckDifference(trie.root, word, 0)
        if ans: return ans
    return False
