# Let’s say you are given with n electricity poles in a line. Each pole i has a flexible varying height from 1 to maximum MaxHeight(i) .
# MaxHeights are defined in a separate array MaxHeight[1...n].
# These poles can vary their size (expand to max height / shrink to lowest height 1) at any time.

# You need to write code to find out the length of wire you would need to connect all these poles from top,
# such that no matter how much is the current height of each pole, the wire should be able to connect all these poles from top.
# What is the minimum wire length required to sufficiently connect these poles from top in any configurations of poles ?

def findMinLengthOfWireToConnectAllPoles(MaxHeights):
    def findHypotenuse(x):
        return (x**2+1)**0.5

    maxLength = [1]*len(MaxHeights)
    maxLength[0], maxLength[1] = findHypotenuse(MaxHeights[0]-1), max(findHypotenuse(MaxHeights[1]-1), findHypotenuse(MaxHeights[0]-1))
    for i in range(2,len(MaxHeights)):
        maxLength[i] = max(findHypotenuse(MaxHeights[i-2]-1) + maxLength[i-2], maxLength[i-1] + findHypotenuse(MaxHeights[i-1]-1))
    return maxLength[-1]

print(findMinLengthOfWireToConnectAllPoles([11,11,11,11,11,11,11]))
print(findMinLengthOfWireToConnectAllPoles([1,2,3,4,5]))
