#NUMBERS:

#Answer these 3 questions without typing code. Then type code to check your answer.
#What is the value of the expression 4 * (6 + 5)
print(4 * (6 + 5)) #44
#What is the value of the expression 4 * 6 + 5 
print( 4 * 6 + 5) #29
#What is the value of the expression 4 + 6 * 5 
print(4 + 6 * 5 ) #33

#What is the type of the result of the expression 3 + 1.5 + 4?
float

#What would you use to find a number’s square root, as well as its square?
print(3**0.5)
print(3*3)

#STRINGS:

#Given the string 'hello' give an index command that returns 'e'. 
s = 'hello'
print(s[1])

#Reverse the string 'hello' using slicing:
s ='hello'
print(s[::-1])

#Given the string hello, give two methods of producing the letter 'o' using indexing.
s ='hello'
print(s[-1])
print(s[4])

#LISTS:

#Build this list [0,0,0] two separate ways.
example1=[0,0,0]
print(example1)

#Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)

#Sort the list below:
list4 = [5,3,4,6,1]
list4.sort()
print(list4)

#DICTIONARIES

# Grab 'hello'
d = {'simple_key':'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['nest_key'][1])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['tough'][2])

#TUPLES

#What is the major difference between tuples and lists?
#Tuples are unchangeable

#How do you create a tuple?
#Use () instead of []

#SETS

#What is unique about a set?
#Sets can't have repeated objects

#Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))

#BOOLEANS

# Answer before running cell
2 > 3 #False

# Answer before running cell
3 <= 2 #False

# Answer before running cell
3 == 2.0 # False

# Answer before running cell
3.0 == 3 #True

# Answer before running cell
4**0.5 != 2 #False

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1'] #False

