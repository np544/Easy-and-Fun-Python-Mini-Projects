
wordlist=input('Enter any number of words separated by 1 space\n').split(" ")
pallist=[]
for i in wordlist:
    j=i[::-1]
    if(i==j):
        pallist.append(i)
print("So the words in your list that is palindrome are: ",*pallist,sep=" ")