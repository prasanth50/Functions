a=10
def some():
    a = 9
    x=globals()['a']

    print(a)
    globals()['a']=15
some()
print(a)