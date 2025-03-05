GIVENLIST = [2,1,1,2,3,4,5]

def firstrecurfinder(arr):
    mydict = {}
    for i in arr:
        if i in mydict:
            return i
        else:
            mydict[i]=i
    return 0

print(f"ARR-->{GIVENLIST}")
frecur = firstrecurfinder(GIVENLIST)
print(f"FIRST RECURRING ELEMENT --> {frecur}")