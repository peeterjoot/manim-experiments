
# experimentation for python calling in different ways

def foo(a,b):
    print("a = {:#x}".format( a ))
    print("b = {}".format( b ))

def foo2(x,*args):
    print('x = ', x)        
    for a in args:
        print('* = ', a)        

def foo3(p,q,**args):
    print('p = ', p)        
    print('q = ', q)        
    for a in args:
        print('**: ', a, args[a])  

play_kw = {"run_time": 2, "blah": 7.3}

def main():
    print("Hello World!")
    print("foo!")
    foo(1,2)
    print("foo2!")
    foo2(2)
    print("foo2!")
    foo2(2,3,4)
    print("foo3!")
    foo3(2,3,**play_kw)

# don't need this
#if __name__ == "__main__":
#    main()

main()
