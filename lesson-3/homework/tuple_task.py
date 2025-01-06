#1 Count Occurrences: Given a list and an element, find how many times the element appears in the list.
t=(6,1,7,4,5,6,1,1,2,1,1,3,8,8)
print("1 lar soni",t.count(1), ta)

#3 Max Element: From a given list, determine the largest element.
t=(1,2,3,4,5,6,8,7,2)
print("eng katta elementi:", max(t))

#4 Min Element: From a given list, determine the smallest element.
t=(9,21,31,46,56,11)
print("eng kichik element:", min(t))

#5 Check Element: Given a list and an element, check if the element is present in the list.
t=(1,2,3,1,2,3,12,2,2,4,3,2,1)
print(t.count(9)!=0)
print(t.count(2)!=0) 

#6First Element: Access the first element of a list, considering what to return if the list is empty.
t=(1,2)
my_list=list(t)
if bool(my_list)==False:
    print('list bosh')
elif bool(my_list)==True:
    print('listning birinchi elementi:',my_list[0])  
