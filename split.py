data = input("data")
list1 = data.split(",")
list2  = []
list2 = list1
print("list1 is list2:", list1 is list2)
print("list2 is list1:", list2 is list1)
index = int(input("index:"))

if index<len(list1) and index>=-len(list1):
    element = input("element:")
    list1[index] = element
    print("list1 is list2: ", list1 is list2)
    print("list2 is list1:", list2 is list1)
else:
    print("enter valid index")