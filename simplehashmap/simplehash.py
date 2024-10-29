
namelist = ["Apple", "Bob", "Cat", "Jam", "Zoo"]

# Get the sum of ASCII characters in the word
def charSum(word):
    return sum(ord(i) for i in word)

# Use the length of the array to determine the modulus
arrLen = len(namelist)

#  Place the word in the hashmap using modulus as the index
hashedList = [None for i in range(arrLen)]
for w in namelist:
    hashedList[charSum(w) % arrLen] = w

for i in hashedList:
    print(i)

