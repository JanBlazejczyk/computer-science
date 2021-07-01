'''
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print: Number of vowels: 5
NOTE: This was done on purpose without grouping the vowels in a list
'''

s = input('Type in a string')

counter = 0

for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        counter += 1

print('Number of vowels: ', counter)
