'''
#exercise 1 
listOne = [3, 6, 9, 12, 15, 18, 21] #taking out odd-index positions
listTwo = [4, 8, 12, 16, 20, 24, 28]# taking out even-index positions
listThree = []                      # add the two lists to make list 3

odd_numbers = listOne[1::2]
print(odd_numbers)
even_numbers = listTwo[0::2]
print(even_numbers)

listThree.extend(odd_numbers)
listThree.extend(even_numbers)
print(listThree)


#exercise 2 #removes the element at index 4 and add it to the 2nd position and also, at the end of the list
list = [34, 54, 67, 89, 11, 43, 94]
list.remove(list[4])
print(list)
list.insert(2,11)
print(list)
list.append(11)
print(list)
'''

#exercise 3
list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print(list[0:3])
print (list[2::-1])
print(list[3:6])
print(list[5::-4])
print(list[6:9])
print(list[8::-5])





