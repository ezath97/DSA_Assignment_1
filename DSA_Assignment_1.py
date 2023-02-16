#!/usr/bin/env python
# coding: utf-8

# # DSA Assignment 1

# In[7]:


# Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

#Solution

class array:
    def __init__(self):
        self.array=[]

    def insert(self):
        data = int(input('Enter:'))
        self.array.append(data)
        return self.array

    def print_array(self):
        for i in self.array:
            print(i,end=' ')
        print(' ')
    
    def find_sum_pair(self):
        given_number = int(input('Enter the Number: '))
        Match=0
        for i in self.array:
            for j in self.array:
                if i+j == int(given_number):
                    Match +=1
                    print ('Sum of pair (',i,'+',j,') is equal to',given_number)
        if Match == 0:
            print('No match found')


List=array()
List.insert()
List.insert()
List.insert()
List.insert()
List.insert()
List.print_array()
List.find_sum_pair()


# In[8]:


# Q2. Write a program to reverse an array in place? In place means you cannot create a new array. 
# You have to update the original array.

class array:
    def __init__(self):
        self.array=[]

    def insert(self):
        data = int(input('Enter:'))
        self.array.append(data)
        return self.array

    def print_array(self):
        for i in self.array:
            print(i,end=' ')
        print(' ')
    
    def reverse_own(self):
        self.array.reverse()
        print('Original array Reversed')
        return self.array


List=array()
List.insert()
List.insert()
List.insert()
List.insert()
List.insert()
List.print_array()
List.reverse_own()
List.print_array()


# In[12]:


# Q3. Write a program to check if two strings are a rotation of each other?

def String_rotation():
    String_1 = input('Enter String 1: ')
    String_2 = input('Enter String 2: ')

    String_1_Rotaion = String_1[::-1]

    if String_1_Rotaion == String_2:
        print('Yes!!!.... The two strings are rotation of each other')
    else:
        print('No..... The two strings are not rotation of each other')

r = String_rotation()


# In[31]:


# Q4. Write a program to print the first non-repeated character from a string?


def First_non_repetive_char():
    String = input('Enter String 1: ')
    for i in String:
        if (String.find(i,String.find(i)+1,len(String))) == -1:
            print('The first non-repetive character of the string -->',i)
            break
    else:
        print('There is no non-repeated character in the string')

x = First_non_repetive_char()


# In[32]:


# Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

def TowerOfHanoi(n, From, Extra, To):
    if n == 0:
        return
    TowerOfHanoi(n-1, From, Extra, To)
    print("Move disk", n, "from rod", From, "to rod", To)
    TowerOfHanoi(n-1, Extra, To, From)

X=int(input('Enter number of disks: '))
TowerOfHanoi(X, 'A', 'B', 'C')


# In[34]:


# Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

def Operator_check(x):
    Operator=['+','-','/','*']
    if x in Operator:
        return True 
    return False

def Post_to_Pre(expression):
    stack = []
    N = len(expression)
    for i in range(N):
        if (Operator_check(expression[i])):
            A = stack[-1]
            stack.pop()
            B = stack[-1]
            stack.pop()
            temp = expression[i] + B + A
            stack.append(temp)
        else:
            stack.append(expression[i])
 
    Pre_Expression = ''
    for i in stack:
        Pre_Expression += i
    print('Postfix Expression: ',expression)
    print('Prefix Expression: ',Pre_Expression)
    return Pre_Expression


X=Post_to_Pre('AB+CD-/')


# In[36]:


# Q7. Write a program to convert prefix expression to infix expression.


def Operator_check(x):
    Operator=['+','-','/','*']
    if x in Operator:
        return True 
    return False

def Pre_to_Infix(expression):
    stack = []
    i = len(expression)-1
    while i >= 0:
        if not Operator_check(expression[i]):
            stack.append(expression[i])
            i -= 1
        else:
            str = "(" + stack.pop() + expression[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
    stack = stack.pop()
    print('Prefix Expression: ',expression)
    print('Infix Expression: ',stack)
    return
 
X=Pre_to_Infix('*-A/BC-/AKL')


# In[44]:


# Q8. Write a program to check if all the brackets are closed in a given code snippet.


def Check_brackets(String):
    open_brackets = ["[","{","("]
    close_brackets = ["]","}",")"]
    stack = []
    for i in String:
        if i in open_brackets:
            stack.append(i)
        elif i in close_brackets:
            pos = close_brackets.index(i)
            if len(stack) > 0 and open_brackets[pos] == stack[len(stack)-1]:
                stack.pop()
            else:
                print (f"Unclosed brackets are in this String: {String}")
                stack.insert(0,'Unclosed')
    if len(stack) == 0:
        print (f"All brackets are closed in this String: {String}")
    else:
        print (f"Unclosed brackets are in this String: {String}")
 

String=Check_brackets("{1:[2+3]},{DDF:{(D34):7}}") 
 


# In[47]:


class Stack:
    def __init__(self):
        self.stack=[]

    def insert(self):
        data = int(input('Enter:'))
        self.stack.append(data)
        return self.stack

    def print_stack(self):
        for i in self.stack:
            print(i,end=' ')
        print(' ')
    
    def reverse_Stack(self):
        self.stack.reverse()
        print('Stack is Reversed')
        return self.stack


List=Stack()
List.insert()
List.insert()
List.insert()
List.insert()
List.insert()
List.print_stack()
List.reverse_Stack()
List.print_stack()


# In[52]:


# Q10. Write a program to find the smallest number using a stack.

class Stack:
    def __init__(self):
        self.stack=[]

    def insert(self):
        data = int(input('Enter:'))
        self.stack.append(data)
        return self.stack

    def print_stack(self):
        for i in self.stack:
            print(i,end=' ')
        print(' ')
    
    def Smallest_number(self):
        x=sorted(self.stack)
        print(f'Smallest number in the stack is: {x[0]}')
        return


List=Stack()
List.insert()
List.insert()
List.insert()
List.insert()
List.insert()
List.print_stack()
List.Smallest_number()


# In[ ]:




