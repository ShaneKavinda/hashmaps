
namelist = ["Apple", "Bob", "Cat", "Jam", "Zoo"]

# Get the sum of ASCII characters in the word
def charSum(word):
    return sum(ord(i) for i in word)

# Use the length of the array to determine the modulus
arrLen = len(namelist)

#  Place the word in the hashmap using modulus as the index
hashedList = [None for i in range(arrLen)]
for w in range(arrLen):
    idx = charSum(namelist[w]) % arrLen
    print(namelist[w], idx)
   
    if hashedList[idx] is None:
        hashedList[idx] = namelist[w]
    else:   #Handle hash collisions by linear probing
        while (hashedList[idx] is not None):
            idx += 1
            if (idx > arrLen):
                idx = 0
            if (hashedList[idx] is None):
                hashedList[idx] = namelist[w]
                break


for i in hashedList:
    print(i, end="\t")
print("\n")
# Search for a given word
word = "Jam"

#Search for the given word
idx = charSum(word) % arrLen
found = False
while (found == False):
    if hashedList[idx] == word:
        print("found word, index: ", idx)
        found = True
    else:
        idx += 1
        if (idx > arrLen):
            idx = 0


