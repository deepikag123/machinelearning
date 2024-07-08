mylist=[1,2,3,4,5]
mylistt=["hi","hello","everyone"]
print("mylist: ",mylist)
mylist.append(6)
print("append: ",mylist)
print("slice: ",mylist[0:3])
mylist.reverse()
print("reverse: ",mylist)
print("length: ",len(mylist))
print("maximum: ",max(mylist))
print("minimum: ",min(mylist))
mylist.pop()
print("pop: ",mylist)
mylist.remove(2)
print("remove: ",mylist)
mylist.extend(mylistt)
print("extend: ",mylist)
mylist.clear()
print("clear: ",mylist)


