# 1

x = input("Name: ")
y = input("age: ")
xy =x+y


print(x,y)

# 2

x=input()
y=input()

def swap_integers(a,b):
    a,b=b,a
    return (a+b)

z = swap_integers(x,y)
print(z)

# 3
a = input()
b = input()

if int(a)%6==0 or int(b)%6==0:
    print("Yes")
else:
    print("No")
if int(b)%10==0 and int(a)%10==0:
    print("Yes")
else:
    print("No")


#4

x = int(input())
y = int(input())
z = x
sum = 0

def sum_up(x,y):
    if (y>x) and (x<0 and y<0):
        print("zero")

while z<=y:
    sum=sum+z
    print(z)
    print(sum)
    z = z + 1

sum_up(x,y)

#5

π = 3.14
r1 = float (input ("Enter the radius: "))
r2 = float (input ("Enter the radius: "))
r3 = float (input ("Enter the radius: "))

def findArea(r1,r2,r3):
    circle_1 = π * r1 * r1
    circle_2 = π * r2 * r2
    circle_3 = π * r3 * r3
    return circle_1 + circle_2 + circle_3

print("Sum of all the areas:", findArea(r1,r2,r3))

#6

string = input(("Check your string: "))

def check_string(string):
    if string.endswith('a') or string.startswith('a'):
        print("True")
    if string.startswith('A') or string.endswith('a'):
        print("True")

check_string(string)



