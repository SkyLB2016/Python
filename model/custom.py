import math


def custom_field(*args):
    print(f'可变参数*args {args}参数的类型是 =={type(args)}')
    return sum(args)


def person(name, age, **kw):
    print('关键字参数：', 'name =', name, '；age =', age, '；kw =', kw)


def person1(name, age, *, city, job="开发"):
    print('命名关键字参数:一个 * 后边的参数是：固定的关键字参数：', "name =", name, "；age =", age, "；city =", city, "；job =",
          job)


def person2(name, age, *args, city, job):
    print('可变参数+命名关键字参数：', "name =", name, "；age =", age, "；args =", args, "；city =", city, "；job =", job)


def person3(name, age, *, city='Beijing', job):
    print('命名关键字参数的默认参数：', "name=", name, "；age=", age, "；city=", city, "；job=", job)


def f1(name, phone, age="默认1", address="默认2", *args, **kw):
    print("固定参数 + 默认参数 + 可变参数 + 关键字参数：",
          '固定参数name =', name, '；固定参数phone =', phone,
          '；默认参数age =', age,
          '；默认参数address =', address,
          '；可变参数args 只能在 关键字参数kw 之前',
          '；可变参数args =', args,
          '；关键字参数kw =', kw)


def f2(name, phone, age="默认", address="默认2", *, email, qq=0, **kw):
    print("固定参数 + 默认参数 + 可变参数 + 关键字参数：",
          '固定参数 name =', name,
          '；固定参数 phone =', phone,
          '；默认参数 age =', age,
          '；默认参数 address =', address,
          '；命名关键字参数 email =', email,
          '；命名关键字参数 qq =', qq,
          '；关键字参数kw =', kw)
