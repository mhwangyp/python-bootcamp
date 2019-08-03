x = 15
y = 3

z = "this is a string"

a = "hello"
b = "world"
c = "again"


myList = [1,12,3,45,5]

def myPrint(words):
    print(words, ", ok.")

myPrint("are you")

def myFunction(start, vList, step):
    for i in range(start,len(vList),step):
        print(vList[i])

def myRecursiveFunction(start, vList, step):
    if len(vList) > start + step:
        print(vList.pop())
        myRecursiveFunction(start, vList, step)

myRecursiveFunction(1,["hello",1,True,3.14159],2)


