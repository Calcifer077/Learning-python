# Below is a simple declaration of a function:
# You don't mention datatype here.
# You don't use '{}' here just use indentation (tab) everything after that tab will be under that function.
def addNumber(a, b):
        return a+b;

# Calling that function
print(addNumber(10, 20));

def getName(name, age):
    print("Hello " + name);
    print("Age:" + age);# Here, the function will think 'age' as string and concatenate them.
    
getName('Mahesh', '19');

def getName1(name, age):
    print("Hello " + name);
    print("Age:", age); # Here, the function will treat it as 
    
getName1('Mahesh', 19);

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
