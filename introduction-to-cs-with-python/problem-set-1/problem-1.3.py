'''
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print: Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print: Longest substring in alphabetical order is: abc
'''

s = input('Type in a string')

longest_substring = ''
substring = ''

for i in range(len(s)):
    if i != len(s)-1 and s[i] <= s[i+1]:
        substring += s[i]

    else:
        substring += s[i]

        if len(substring) > len(longest_substring):
            longest_substring = substring
            substring = ''
        else:
            substring = ''

print("Longest substring in alphabetical order is:", longest_substring)
