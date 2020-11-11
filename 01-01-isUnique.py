# Is Unique:
# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def isUnique(string):
  if (len(string)) > 128:   # There are 128 ASCII characters. If the string is longer, 
    return False            # It would have to repeat characters.
  i = 0
  length = len(string)

  while i < length:
    char = string[i]                  # store the character in question
    lastIndex = string.index(char)    # last index where that character exists
    if lastIndex != i:                # If that last index is not the index in question,
      return False                    # then it must be a repetition.
    i += 1                            # Otherwise, the whole string is unique.
  return True

print(isUnique("yeet"))     # False
print(isUnique("yet"))      # True