#! /usr/local/bin/python3

# square brace lists are mutable, but round ones (tuples) are not:
#
# https://stackoverflow.com/a/8900189/189270
def rlist():
    return ('1',2,'3')

def func(*args):
    for it in args:
        print(it)

a = rlist()
func(*a)
b = rlist() + rlist() + a + (13, 's')
func(*b, *a)
