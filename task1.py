#"1.Create a list of the 10 elements of four different types of Data Types like int, string, complex and float."
from typing import List

list4=[1,"two",3.1,4j+1]
print(list4)

#"2.Create a list of size 5 and execute the slicing structure ")
list5=[1,2,3,4,5]
print(list5[1:4])

#"3.Create a list of given structure and run ")
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
print(x[5][:5])
#[1, 2, 3, 4, 5]

print(x[6:8])
#[600, 700]

print(x[:9:2])

print(x[::-1])

print(x[5][5][0])

#4. 	Create a list of thousand number using range and xrange and see the difference between each other.

print(list(range(1000)))
#xrange is used in py2

#5. 	How Tuple is beneficial as compare to the list?
#list is mutable, whereas a tuple is immutable.

#6. Write a program in Python to iterate through the list of numbers in the range of 1,100 and print the number
# which is divisible by 3 and a multiple of 2.

list3and2=[]
for i in range(1,100):
    if(i%3==0) and (i%2==0):
        list3and2.append(i)
print(list3and2)

#7. Write a program in Python to reverse a string and print only the vowel alphabet if exist in the string with their index .

string = "apple"

newstr = string;

vowels = ('a', 'e', 'i', 'o', 'u');
for x in string.lower():
    if x in vowels:
        newstr = newstr.replace(x,"");
print(newstr);

#8. 	Write a program in Python to iterate through the string “hello my name is abcde” and print the string which has
# even length of word.

sentence="hello my name is abcde"
sentence=sentence.split(' ')
for i in sentence:
    if len(i)%2==0:
        print(i)


#9. 	Write a program in python to print the pair of numbers whose sum is equal to result number that is let's say 8.
#x=[1,2,3,4,5,6,7,8,9,-1]
x=[1,2,3,4,5,6,7,8,9,-1]
result=8
count=0
for i in x:
    s = result - i
    x.remove(i)
    if s in x:
        x.remove(s)
        count+=1
print(count)



#10. 	Write a program in Python to complete the following task:
#Create two different list as in even_list and odd_list

even_list=[]
odd_list=[]

#Ask user to enter the number in the range of 1,50 and make sure if the entered number is even append it to the even_list
# and if the entered number is odd append it to the odd list.
#Keep that in mind you can only add 5 items in each list

counter_even=1
counter_odd=1
while counter_even<=5 and counter_odd<=5:
        x = int(input("enter a number between 1 and 50: "))

        if x%2==0 :
            counter_even = counter_even + 1
            even_list.append(x)
            if counter_even > 6:
                print("Even Game over!")

        else:
            counter_odd = counter_odd + 1
            odd_list.append(x)
            if counter_odd > 6:
                print(" odd Game over!")
        print(even_list)
        print(odd_list)

#Make sure once you entered the total 5 element calculate the sum of the list and return the maximum out of the list.

print("sum of integers in even list is:",  sum(even_list))
print("sum of integers in odd list is:", sum(odd_list))


#11. 	Write a program to find out the occurrence of a specific word from an alphanumeric statement.
# Example: 12abcbacbaba344ab
                      #Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic

example =  "12abcbacbaba344ab"
letterCount=0
dict = {}
for i in example:
    if i.isalpha():
        if i in dict.keys():
            dict[i] = dict[i]+1
        else:
            dict[i] = 1

print(dict)




#12.Generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

tp = (1,2,3,4,5,6,7,8,9,10)
li = list()
for i in tp:
	if i%2 == 0:
		li.append(i)

tp2 = tuple(li)
print(tp2)