from array import *
arr1 = array('i',[1,2,3,4,5,6,7])

# traverse
for i in arr1:
    print (i) #picks up element
    
# for i in range(len(arr1)):
#     print (i) picks up range

#access individual elements through index
print('step 2')
print(arr1[4])
#append array
print('step 3')
arr1.append(12)
print(arr1)

#insert array using insert method
print('step 4')
arr1.insert(4, 12) #index followed by element o(n) coz time consuming
print(arr1)

#extend array
print('step 5')
arr2 = array('i', [15,19,23])
arr1.extend(arr2)
print(arr1)

#use fromList
print('step 6')
lists = [1,2,3,4,5]
arr1.fromlist(lists)
print(arr1)

#remove element
print('step 7')
arr1.remove(15)
print(arr1)

#remove using pop

print('step 8')
arr1.pop()
print(arr1)

#fetch using index method
print('step 9')
print(arr1.index(3)) #index doesn't return 0

#reverse a python array using reverse method
print('step 10')
arr1.reverse()
print(arr1)

print('step 11')

print(arr1.buffer_info())
#print(arr1)
print('step 12')
print(arr1.count(4))  #counts occurence of the element
print('step 13')

print('step 14')
print('step 15')
print(arr1[1:4])

