# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 17:08:05 2024

@author: jalli
"""

# Prime Numbers

# Taking input from the user
n=int(input("Enter the number = "))

# first checking given input is a less then then 1 because ever prime numbers
# starts from 2
if n>1:
    # the usr enterd a value greater then 2
    # we are checking the number is dividible with any number below half of it's range recursively
    # so we go with for loop with stating 2  
    
    for i in range(2,n//2+1,1):
        # checking the enterd number is divisible by any of the number below it's value
        if n%i==0:
            
            # if the number is divisible by any number printing it is not a prime number
            print('Entered number is not a prime number')
            
            # if the number is divisible by a number atleast one time it mean's it is sufficent to justify 
            # the number is a non-prime number
            break
        
    # if the above if block not executed then it means it is prime number
    print('Enterd number is a prime number')
        
else:
    # if the entered number is not greater then 1 or it may be a negative number
    print('Enterd number is not a prime number')
            
        
        





# 2)  Product of Random Numbers

# for generating a random number we use random library for it
import random

# generating a random number between 1,20
n1=random.randint(1, 20)

# generating a random number between 1,100
n2=random.randint(1, 100)

# taking the product input from the user 
pro_ent=int(input('Can you say Product of '+str(n1)+'x'+str(n2)+' = '))


# this code releated to if the user entered wrong value but when he enterd correct value then only this function get stop
# def rep_fun():
#     # taking the product input from the user 
#     pro_ent=int(input('Can you say Product of '+str(n1)+'x'+str(n2)+' = '))
#     if pro_ent!=(n1*n2):
#         print('You enterd Incorrect vlaue Reenter the value')
#         rep_fun()
#     else:
#         print('Enterd correct value')
# rep_fun()
    


# checking the user enter correct product value
# if he entered correct product input run the delow  block other wise else block
if pro_ent==n1*n2:
    print('Entered correct product value')
else:
    print('Entered incorrect value')







# 3) Square of even or Odd numbers bv/w 100-200

# Taking the input fromn the user
inp=str(input('for even numbers enter -> even ,for odd -> odd  = '))

# if the user enter enter 'even' the we are going to print only even numbers from 100,200
if inp=='eve':
    # if want only bulk even number recursively 
    for i in range(100,201,2):
        print(i)
    # if want only bulk odd number recursively 
else:
    for i in range(101,200,2):
        print(i)





# 4) Word count


# taking input from the user and placing in array with removing spaces and split then words there a space between 
# two words before  this convert the word into lowcase letters in the word
inp1=[str(x) for x in input('Enter u desired data = ').lower().strip().split()]

# Creating a empty dictionary for placing words as key and value as number of 
# repeating of the same number arround the sentence
s={}

# taking 'for' loop for checking every item in the list any duplicate word or not
for i in inp1:
    # Here i means word in the list 'inp1', checking any other same word present if present increase the value 
    # of the coresponding key in the dictionary
    if i in s:
        s[i]+=1
    else:
        # First assign the value as '1' for every key in the list 
        s[i]=1
# printing every word and it's corresponding repeating number
for i in inp1:
    print(i+' : '+str(s[i]))





# 5)  checking Palindrome
# Palindrome mean's reading the same letter from forword and backword

# Taking the input from the user
inp=input('Enter the input : ').lower()

# knowing how long the input entered
le=len(inp)
count=0

# taking its half length of the entered input and seeing it is a plindrome or not
for i in range(le//2):
    # inp[i] gives the staring half input and inp[le-1-i] gives remaining half 
    # example: inp[i] = give's 1'st index value and inp[le-1-i] giv's last index 
    if inp[i]==inp[le-1-i]:
        
        # every time when this if block run's raising the count by 1 
        count+=1
   
# checking the count is equal to the half of the count of the word
if count==le//2:
    
    # if it's satisife the condition mean's it is a palindrome
    print(True)
else:
    # if not it is not a palindrome
    print(False)








    
    