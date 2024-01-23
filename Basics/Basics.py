'''a = 10;
#THis is a comment


b = 30;
print("The value of a is", a);
print(a + b);
print(a - b);
print(a * b);
print(a // b); #It is floor value. It will make the float value into decimal value.
print(a % b);


print(a+b/b-a);
'''
'''
This
is 
a 
multi-
line 
comment.
'''

'''
a = 'Hello';
print(a);
print(a[0]);#It will return the first character of this string.
print(len(a));#It will return length of the charcter.

#integer, string, tuple are immutable
#list, dictionay are mutable in nature.

#Below is a list. It can contain different types of data together.
#We can also make nested lis meaning list inside list.
#List is ordered and mutable.
#Ordered means that item will be displayed in the same order as they are in the list.
li = [18, 20, 'Joe'];
print(li[0], li[1], li[2]);
print(li);

li1 = [1, 2, 3, 'A'];
li2 = [4, 5, 6, 'B'];
li3 = [7, 8, 9, 'C'];
li4 = [li1, li2, li3];#This is a list which contain more than one list.
print(li4[2][2]);#By this way, we can access list's item's items.


a = 10;
b = 10.5;
c = 'H';
print(type(a));
print(type(b));
print(type(c));

li5 = [li1, 10, 20];
print(li5);
li5.append('Mahesh');#This will add the new element at the end of your list.
print(li5);

li6 = li1 + li2;
print(li6);
'''

'''
a = 'Hello';
b = 'World';
print(a*4);
print(a + ' ' + b);
print(a + '!' * 4);

#tuple
t1 = (1, 2, 'Mahesh');
print(t1);
'''

'''
def addNumber(a, b):
        return a+b;
        

print(addNumber(10, 20));

def getName(name, age):
    print("Hello " + name);
    print("Age:" + age);
    
getName('Mahesh', '19');

def getName1(name, age):
    print("Hello " + name);
    print("Age:", age);
    
getName1('Mahesh', 19);
'''

'''
def swap(a, b):
    
    temp = a;
    a = b;
    b = temp;
    
    a,b = b,a;
    print(a, b);

a = 10;
b = 20;    

print('Before swapping');
print(a, b);

print('After swapping');
swap(a, b);


a = int(input('Enter first value: '));
b = int(input('Enter second value: '));
print(a + b);


# Experiment 1
# Review of python basics, data types, control structures, and functions in pytho

# dictionary, list inside dictonary, dictonary inside dictonary

di = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5:'E', 6:[20, 30, 'Mahesh']};
print(di);

di_two = {1: 2, 2: 'B', 3:'C', 4:{10:'Mahesh', 11:'Again Mahesh'}};
print(di_two);

li = [1,2,3,4,5,6,'Mahesh'];

for i in li:
    print(i);

di_two = {1: 2, 2: 'B', 3:'C', 4:{10:'Mahesh', 11:'Again Mahesh'}};
print(di_two[4][11]);



li1 = [1,2,3,4];
li2 = [5,6,7,8];
dic = {1: li1, 2: li2};
print(dic[1]);
print(dic[2]);
print(dic.keys());


a = int(input('Enter the value for a: '));
b = int(input('Enter the value for b: '));
c = int(input('Enter the value for c: '));

if(a > b and a > c):
    print('a is max');
    
elif(b > c  and b > a):
    print('b is max');
    
else:
    print('c is max');
    
'''

for x in range(20):
    print(x, ' ');
