import math

class Custom:



    def person(name, age, **kw):
        print('name:', name, 'age:', age, 'kw:', kw)

    def person1(name, age, *, city, job):
        print(name, age, city, job)

    def person2(name, age, *args, city, job):
        print(name, age, args, city, job)

    def person3(name, age, *, city='Beijing', job):
        print(name, age, city, job)

    def f1(a, b, c=0, *args, **kw):
        print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

    def f2(a, b, c=0, *, d, **kw):
        print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

    # def ride(n):
    #     return ride_iter(n, 1)
    #
    # def ride_iter(num, result):
    #     return ride_iter(num - 1, num * result)
    #


def tuple1():
    x = math.sin(math.pi / 6)
    y = math.cos(math.pi / 6)
    return x, y
