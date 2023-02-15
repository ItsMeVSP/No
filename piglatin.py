print("PIG LATIN WORD")
s1={'a','e','i','o','u'}
word=input("Enter word:")
for i in word:
    if i not in s1:
        cons=i
        break
plwrd=word[1:]+cons+"ay"
print("Pig Latin word for ",word,"is ",plwrd)
