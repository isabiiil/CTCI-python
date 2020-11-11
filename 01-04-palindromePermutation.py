# Palindrome Permutation:
# Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

def palindromePermutation(string):
    string = string.lower()
    sort = sorted(string)
    sortedString = "".join(sort)        # sort the string

    isPerm = True
    oddCounter = 0
    charCount = len(sortedString)

    if charCount % 2 == 0:                                         # If there is an even number of characters,
        for char in range(0, charCount, 2):                        # loop through the string, pairing up each letter to the one after it.
            if sortedString[char] == sortedString[char+1]:         # If all the pairs match up,
                isPerm = True                                      # then the whole thing is a permutation of a palindrome.
            else:                                                  # Otherwise, 
                isPerm = False                                     # it is not. 
    else:                                                          # If there is an odd number of characters, 
        for char in range(0, charCount-1, 2):                      # loop through the string minus that odd one out, pairing up the letters.
            if sortedString[char] == sortedString[char+1]:         # If the pair matches up,
                isPerm = True                                      # then continue to the next pair.
            else:                   
                oddCounter += 1
                sortedString.replace(sortedString[char], "", 1)
        if oddCounter > 1:
            isPerm = False
            

    return isPerm


print(palindromePermutation("tact coa"))   # True
print(palindromePermutation("abdccdcdba")) # True
print(palindromePermutation("yeet"))       # False