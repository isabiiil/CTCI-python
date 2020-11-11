# One Away:
# There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

def oneAway(string1, string2):
  if string1 == string2:  # if they are the same string
    return True

  else:
    if abs(len(string1) - len(string2)) > 1:  # if the difference in length is more than one
      return False

    split1 = [char for char in string1]       # split string into array of characters
    split2 = [char for char in string2]

    count = 0
    for i in range(min(len(split1)-1, len(split2)-1)):  # loop through based on the length of the shorter string
      if split1[i] != split2[i]:                        # if they are not the same character
        count += 1                                      # add to the counter
    
    if count > 1:   # if there are more than one edits 
      return False
    else:           # if there is only one edit
      return True

print(oneAway("pale", "ple"))       # True
print(oneAway("pales", "pale"))     # True
print(oneAway("pale", "bale"))      # True
print(oneAway("pale", "bake"))      # False

print(oneAway("yes", "yes"))        # True
print(oneAway("Alex", "Alexa"))     # True
print(oneAway("today", "tomorrow")) # False
print(oneAway("yeet", "heyo"))      # False