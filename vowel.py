#text = "Python Programming"
text=input("enter the string:")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(count) 