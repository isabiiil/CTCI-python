# URLify: 
# Write a method to replace all spaces in a astring with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.

def URLify(string):
  return string.strip().replace(" ", "%20")
# strip() removes leading and trailing whitespace
# replace(" ", "%20") does what the question wants

print(URLify("Hello World"))