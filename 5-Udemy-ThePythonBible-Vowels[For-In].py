# for number in range (1,11):
#     print (number) => 1,2,3
# for letter in "abc":
#     print(letter) => a,b,c,
vowels = 0
consonants =0
word = "supercalifragilistic"
for letter in word:
    if letter.lower() in "aeiou":
        vowels=vowels+1
    elif letter == " ":
        pass
    else:
        consonants=consonants+1
print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))
