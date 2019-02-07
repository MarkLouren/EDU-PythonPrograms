#find Even Numbers
even_numbers= [x for x in range (1,101) if x % 2 == 0]
print(even_numbers)

#find odd numbers
ood_numbers= [x for x in range (1,101) if x % 2 != 0]
print (ood_numbers)

#Create new list with new conditions without if statement
words= ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
answer = [[w.upper(), w.lower(),len(w)] for w in words]
print (answer)
