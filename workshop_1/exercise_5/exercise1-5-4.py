import string

string1 = "This is a sentence that has a word that occurs multiple times, for example: word."

wordlist = string1.split()

# Creates a translator that replaces members of the 3rd paramter list with none
translator = str.maketrans('', '', string.punctuation)

# Strip all punctuation
for i, word in enumerate(wordlist):
    wordlist[i] = word.translate(translator)

# Cast to set, to get a unique set of words
wordset = set(wordlist)

for word in wordset:
    print("{} occurs {} time(s) in the sentence".format(word, string1.count(word)))
