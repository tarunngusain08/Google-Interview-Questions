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

def OneDifferencePairExists(listOfWords):
    word_set = set()
    for word in listOfWords:
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + char + word[i+1:]
                if new_word in word_set:
                    return True
            word_set.add(word)
    return False


listOfWords = ["tarun", "tarub"]
print(OneDifferencePairExists(listOfWords))

listOfWords = ["tarun", "tarun"]
print(OneDifferencePairExists(listOfWords))

listOfWords = ["aarun", "tarun"]
print(OneDifferencePairExists(listOfWords))
