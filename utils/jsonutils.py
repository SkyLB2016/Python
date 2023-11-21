import json

from model.Animal import Animal
from model.Student import Student


def obj2dict(temp):
    return {
        'name': temp.name,
        'gender': temp.gender,
        'age': temp.age
    }


def learn_json():
    print("learn_method_31")
    print("json的loads与dumps方法应用")
    # print("json.dumps()	将 Python 对象编码成 JSON 字符串")
    # print("json.loads()	将已编码的 JSON 字符串解码为 Python 对象")
    # print("json.dump()	将Python内置类型序列化为json对象后写入文件")
    # print("json.load()	读取文件中json形式的字符串元素转化为Python类型")

    # json.dumps()	将 Python 对象编码成 JSON 字符串
    # json.loads()	将已编码的 JSON 字符串解码为 Python 对象
    # json.dump()	将Python内置类型序列化为json对象后写入文件
    # json.load()	读取文件中json形式的字符串元素转化为Python类型
    d = dict(name='李彬', age=59)
    text = {"name": '李彬', "age": '33'}
    print(f"字典dict: d=={d}")
    print(f"字典dict: text=={text}")
    print(f"type(d) == type(text)=={type(d) == type(text)}")
    json_str = json.dumps(d)
    print(f"1.字典转字符串 == {json_str}，类型是== {type(json_str)}")
    dict1 = json.loads(json_str)
    print(f"2.字符串转成字典 == {dict1}，类型是== {type(dict1)}")

    ani = Animal('狗熊', '雄性', 333)
    json_str = json.dumps(ani, default=obj2dict)
    print(f"3.将实例对象转成 json 字符串 == {json_str}")

    anis = [ani, ani]
    json_str = json.dumps(anis, default=obj2dict)
    print(f"4.将 list集合转成 json数组 字符串 == {json_str}")

    json_str = json.dumps(ani, default=lambda temp: {
        'name': temp.name,
        'gender': temp.gender,
        'age': temp.age
    })
    print(f"5.使用匿名函数  格式化json 字符串== {json_str}")

    json_str = json.dumps(ani, default=lambda temp: temp.__dict__)
    print(f"6.使用自带的 __dict__ 格式化后的 json 字符串== {json_str}")

    print(f"json.loads()方法把对应的字符串转成对象")
    ani1 = json.loads(json_str, object_hook=lambda temp: Animal(temp['name'], temp['gender'], temp['age']))
    print(f"7.把字符串 转成 对象 == {ani1}，类型是=={type(ani1)}")

    stu = Student('李彬', '男', 33, 88)
    json_str = json.dumps(stu, default=Student.stu_dict)
    print(f"8.把对象格式化成 json 字符串=={json_str}")

    # 从文件中读取JSON数据
    with open('./file/json.txt', 'r') as f:
        data = json.load(f)
    print(f"9.使用 json.load(f)从文件中获取的json字符串，是dict格式的，== {data}")
    stu = json.loads(json.dumps(data),
                     object_hook=lambda temp: Student(temp['name'], temp['gender'], temp['age'], temp['score']))
    print(f"10.输出生成的学生实例== {str(stu)}")
    with open('./file/json.json', 'r') as f:
        data = json.load(f)
    print(f"11.使用json.load(f)从文件中获取的json字符串数组，是dict格式的，== {data}")
    stu = json.loads(json.dumps(data),
                     object_hook=lambda temp: Student(temp['name'], temp['gender'], temp['age'], temp['score']))
    print(f"12.输出生成的学生实例数组== {str(stu)}")

    json_str = json.dumps(stu, default=Student.stu_dict)
    json_dict = json.loads(json_str)
    print("13.使用 json.dump 方法生成 json 文件")
    print("13.json.dump的文本最好是dict格式的，ensure_ascii为Fasle时输出的是utf_8格式，indent是缩进格式化")
    f = open('./file/dump.json', "w")
    json.dump(json_dict, f, ensure_ascii=False, indent=2)
    f.close()
    f = open('./file/dump.txt', "w")
    json.dump(json_dict, f, ensure_ascii=False, indent=1)
    f.close()
