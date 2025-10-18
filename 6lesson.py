word = input()
reversed_word = ""
for i in range(len(word),0,-1):
    reversed_word += word[i-1]
print(reversed_word.upper())