string = "This is a string with multiple characters and vowels, it should contain all five possible vowels"

vowels = ["a", "e", "i", "o", "u"]

for vowel in vowels:
    string = string.replace(vowel, "")

print(string)
