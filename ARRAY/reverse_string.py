string = "GANESH IS THE BEST"
str_arr = list(string)

#1
print(string[::-1])

#2
reversed(string)
print(string)

#3
def reverse(stri):
  mylist=[]
  for i in range(len(stri)-1,-1,-1):
    mylist.append(stri[i])
  return ''.join(mylist)

x=reverse('I am theja')
print(x)

