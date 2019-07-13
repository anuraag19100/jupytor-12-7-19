#!/usr/bin/env python
# coding: utf-8

# 
# # Regular Expression
# - Pattern Matching
# - Pattern(re) Package
# - Cap symbol is used to represent the start of re
# - doll symbol is used to represent the end of re
# - [0-9] --> Any digit matching
# > Two digit number (^[0-9]{2}$)
# > five Digt number (^[0-9]{5}$)
# 

# ### Regular Expression for characters
# - [a--z]-->Any Lower case characters
# - [A--Z]-->Any Upper case characters
# - ^[a-z]{5}$ --> It accepts 5 lower case characters
# - ^[a-zA-Z]{8}$ -->Accept 8 characters can be anything lower and upper
# - 
# 

# In[ ]:


# Function to test two digit number matching
import re
def twoDigitMatching(n):
    pattern = '^[0-9]{2}$'
    n = str(n)
    if re.match(pattern,n):
        return True
    return False
print(twoDigitMatching(12)) #True
print(twoDigitMatching(123)) #False


# In[ ]:


# Function to define to test username having 8 characters
# Upper case and lower
def testUsername(s):
    pattern = '^[a-zA-Z]{8}$'
    if re.match(pattern,s):
        return True
    return False
print(testUsername('GitamHYD'))
print(testUsername('Gitam188'))


# ### Regular Expression to match the Indian Mobile Number
# - 10 Digits
# - (first digit will be [6-9] and remaining 9 digits will be [0-9]
# - Example:-9787688734
# - Re - ^[6-9][0-9]{9}$
# - Example :-09988774455 (Re - ^[0][6-9][0-9]{9}Dollar)
# - Example:-+919988774455
# - Re-^[+][9][1][6-9]{9}

# In[ ]:


# Function to validate the Indian Mobile number
def phoneNumberValidation(phone):
    pattern = '^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$'
    phone = str(phone)
    if re.match(pattern,phone):
        return True
    return False
phoneNumberValidation('+919988774455')


# - Regular Expression to Validate the RollNumber
#      - Example : 1521A05001
#      - Example : 1521A0109
#      - Example : 1521A0499
#  - Regular Expression to validate the password
#         - Parameters : Len min of 6 characters and max of 15 characters
#         - Accept Lower case,Upper case,Digits spl char(@,#,!)
#   
#   

# # Email Id validation using Regular Expression
# - Example :- Username@DomainName.extension
# - Username :- 
#    - Length will be [6-15]
#    - No specials characters apart from Underscore(_)
#    - Should no begin and end with Underscore(_)
#    - Characters set : All digits and lower case
# - DominName :-
#    - Length will be [3-18]
#    - No special characters
#    - Character set  : All digits are lower case 
#  - Extensions :-
#    - Length will be [2-4]
#    - No special characters
#    - Characters set : lower case characters
# 
# 
#      

# In[ ]:


import re
def mail(n):
    pattern = '^[A-za-z0-9@.]{8,30}$'
    if re.match(pattern,n):
        return True
    return False
print(mail('Anuraaglalaji14@gmail.com'))
    


# In[2]:


import re
def sites(n):
    pattern = '^[h][t][t][p][s][:][/][/][a-z]{1,30}[.][a-z]{1,30}[.][c][o][m][/][a-z]{1,30}[/][0-9]{1,30}$'
    if re.match(pattern,n):
        return True
    return False
print(sites('https://mail.google.com/mail/u/0/#inbox/FMfcgxwChcrgrrznlrHQcWDQPTKFLlrR'))


# ### Python Turtle
# - Turtle Graphics

# In[ ]:


# Step 1 : Make all the turtle package to be imported
import turtle
# Turtle method creates and returns a new object
a1= turtle.Turtle()
# forward() method moves 100 pixels
turtle.forward(250)
#we are done
turtle.done()


# In[ ]:


#Line draw in reverse direction
import turtle as tt
a1 = tt.Turtle()
tt.backward(100)
tt.done()


# In[ ]:


# Draw square
import turtle as tt
a1 = tt.Turtle()
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
tt.done


# In[ ]:


# Star
import turtle as t
a1 = t.Turtle()
for i in range(40):
    a1.forward(50)
    a1.right(144)
t.done()


# In[ ]:


# Spiraling Star
import turtle as t
a1 = t.Turtle()
a1.pencolor('blue')
for i in range(40):
    a1.forward(i*10)
    a1.right(144)
t.done()


# In[1]:


# Square Spiral help of Turtle
import turtle as t
a1= t.Turtle()
for i in range(250):
    a1.forward(i)
    a1.left(91)   
t.done()


# In[5]:


# Hexagon with Multi color
from turtle import *
colors = ['blue','green','yellow','orange','purple','red']
for x in range(360):
    pencolor(colors[x%6])
    width(x/100+1)
    forward(x)
    left(59)


# In[ ]:





# In[ ]:




