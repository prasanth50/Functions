def count(list):
    even=0
    odd=0
    print('length of list is:',len(list))
    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return odd,even
list=[20,30,40,31,79,52,63,41,97]
odd,even=count(list)
print('count of even numbers is:',even)
print('count of odd numbers is:',odd)
print('Even : {} and odd : {} '.format(even,odd))