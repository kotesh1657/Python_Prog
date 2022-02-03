#https://www.geeksforgeeks.org/python-list/



#Creating a List basic prog



py_list = []
print(py_list)

py_list1 =[1,2,4]
print(py_list1)

py_list2 = [1,"Name","2.0"]
print(py_list2)
#LIST IS MUTABLE THAT MEANS WE CAN CHANGE THE VALUES.
py_list2[1] = "hemanth"
py_list2[2] = 0.4
print(py_list2)

#multidimensional list
py_list3 = [[1,"Name","2.0"], ["nik","pak","check"]]
print(py_list3)

# list can have duplicate values 
dup_list = [1,2,2,3,4,4,5,6,6,7,7]
print(dup_list)

#print the list values using index numbers
print(dup_list[0:6])# here it will print the output of n-1 that 0:5 
print(dup_list[2:])
print(dup_list[-1])
print(dup_list[:-3])
print(dup_list[::-1])# reverse order
print("Then size of the list using len method :", len(dup_list))# length of a list



#Adding Elements to a List

#append a list takes only single argument as input

app_list = [1,2,3]
app_list.append(4)
app_list.append((6,8))
app_list.append(["we can append", "tuple and new list", "to the existing list"])
print(app_list)

#Insert takes two arg one for index val and other is for input value
ins_list = [1,2,3]
ins_list.insert(0,"first")
ins_list.insert(2,"last")
print(ins_list)

#extend method is same as append just here we can add multiple values to the list.

ext_list = [1,64,52,9,10,5]
ext_list.extend([6,7])
ext_list.sort()
print(ext_list)
"""
des_list =[23,64,32,10,1,23]
des_list.sort(reverse=true)
print(des_list)
"""



