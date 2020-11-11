# Check Permutation: 
# Given two strings, write a method to decide if one is a permutation of the other.

def checkPermutation(string1, string2):
	sorted1 = sorted(string1)        # sort both strings
	str1 = "".join(sorted1)          # Since sorted() returns a list,
	sorted2 = sorted(string2)        # we need to turn it back into a string.
	str2 = "".join(sorted2)

	if len(str1) != len(str2):       # If the lengths are different,
		return False                 # they couldn't possibly be permutations.
	else:
		for i in range(0, len(str1)):
			if str1[i] == str2[i]:         # If the characters are the same at each point,
				return True                # then they must be permutations.
			else:                          # Because the strings are already sorted,
				return False               # the order of the letters are irrelevant.

print(checkPermutation("yeet", "teye"))    # True
print(checkPermutation("yeet", "hello"))   # False