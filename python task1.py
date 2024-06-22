def arithmetic_oper(a,b):
    if a>b:
        x=a+b
    else:
        x=a-b
    return x
a=34
b=26
x=arithmetic_oper(a,b)
print(x)

#multiplication of two lists
def mul_lists(list1,list2):
    result=[]
    for i in range(len(list1)):
        result.append(list1[i]*list2[i])
    return result
list1=[1,2,3,4]
list2=[2,4,6,8]
result=mul_lists(list1,list2)
print(result)

#arithmetic operations
a =76
b =33
if a>b:
    c =a+b
else:
    c =a-b
print(c)

#multiplication and division
x=29
y=47
if x>y:
    z=x*y
else:
    z=x/y
print(z)

