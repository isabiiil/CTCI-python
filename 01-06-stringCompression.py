# String Compression:
# Implement a method to perform basic string compression using the counts of repreated characters. For example, the string aabccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a-z).

def stringCompression(string):
  string = [char for char in string]
  result = []
  count = 0
  for i in range(len(string)-1):
    if string[i] == string[i+1]:
      count += 1
    else:
      result.append(string[i])
      result.append(str(count))
  result = "".join(result)
  return result

print(stringCompression("aabcccccaaa"))