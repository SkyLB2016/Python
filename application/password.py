# -*- coding: utf-8 -*-
"""
@Time    : 2025/4/28 10:46
@Author  : 李彬
@Email   : your-email@example.com
@File    : password.py
@Description: 
"""
import hashlib
import random
import secrets
import string

import bcrypt


def generate_password():
    # 定义字符集合
    # uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    uppercase = string.ascii_uppercase
    # lowercase = 'abcdefghijklmnopqrstuvwxyz'
    lowercase = string.ascii_lowercase
    # digits = '0123456789'
    digits = string.digits
    special = '~!@#$%^*()-+_=,.'

    # 组合所有字符类别
    categories = {
        'upper': uppercase,
        'lower': lowercase,
        'digit': digits,
        'special': special
    }

    # 随机选择3个不同类别
    selected = secrets.SystemRandom().sample(list(categories.keys()), 3)

    # 确保每个选中类别至少有1个字符
    password = [secrets.choice(categories[cat]) for cat in selected]

    # 补充剩余字符（从所有类别中随机选择）
    all_chars = uppercase + lowercase + digits + special
    password += [secrets.choice(all_chars) for _ in range(8 - len(password))]

    # 打乱字符顺序
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


# 验证函数（测试用）
def check_password(pw):
    types = {
        'upper': False,
        'lower': False,
        'digit': False,
        'special': False
    }

    for c in pw:
        if c.isupper():
            types['upper'] = True
        elif c.islower():
            types['lower'] = True
        elif c.isdigit():
            types['digit'] = True
        elif c in '~!@#$%^*()-+_=,.':
            types['special'] = True

    return sum(types.values()) >= 3


def get_random_str(length=8):
    """ 随机生成16位字符串
    @return: 16位字符串
    """
    rule = string.ascii_letters + string.digits
    random_str = random.sample(rule, length)
    return "".join(random_str)


def md5_text(password):
    md = hashlib.md5(password.encode())  # 创建md5对象
    password = md.hexdigest()  # md5加密
    return password


def hash_pw(password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=6))
    return hashed.decode()

def check_pwd(pw,stored_hash):
    # 验证密码是否匹配
    is_valid = bcrypt.checkpw(pw.encode(), stored_hash.encode())
    print("验证结果:", is_valid)  # 输出 True


# 生成并验证示例
password = generate_password()
# print(f"生成的密码: {get_random_str()}")
print(f"生成的密码: {password}")
print(f"符合要求: {check_password(password)}")

print("md5和hash_pw加密：", hash_pw(md5_text('123456')))

hash_pwd=hash_pw('qwerty')
print("hash_pw加密：", hash_pwd)

# print("$2a$10$WHuHT5vHtWctWkBtF6Ysou58/ug2xjdBXvovvrXJs4Uy7Xt0njaaq")
print('$2a$10$iccEo.X9wHeBX5Mp257dA..bo9OAZKJj3iIwEK0GTSj1EAIEhM4gC')

check_pwd('123456',hash_pwd)