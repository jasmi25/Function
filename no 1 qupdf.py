#Q1.Write a Python program to count the number of strings where the string length is 2 or more and
#the first and last characters are the same from a given list of strings.
#ist=['abc', 'xyz', 'aba', '1221']
#result= 2.
def list(characters):
    count=0
    for characters in characters:
        if len(characters)>1 and characters[0]==characters[-1]:
            count=count+1
    print(count)
list(['abc', 'xyz', 'aba', '1221'])
def match_words(words):
  ctr = 0
  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
      print(ctr)
match_words(['abc', 'xyz', 'aba', '1221']),
