def count_uppercase_and_non_uppercase(sentence):
    uppercase = 0
    other = 0

    for character in sentence:
        if character.isupper():
            uppercase += 1
        elif character is not ' ':
            other += 1

    return uppercase, other


sentence = "The quick Brown Fox"
print(sentence)
result_tuple = count_uppercase_and_non_uppercase(sentence)
print("The sentence has {} uppercase and {} other characters".format(result_tuple[0], result_tuple[1]))
