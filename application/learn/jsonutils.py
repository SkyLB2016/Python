import json

from application.model.Animal import Animal
from application.model.models import Student


def obj2dict(temp):
    return {
        'name': temp.name,
        'gender': temp.gender,
        'age': temp.age
    }


person = [
    {
        "name": "张三",
        "age": 11,
        "gender": "男",
        "score": 99
    },
    {
        "name": "张三",
        "age": 11,
        "gender": "男",
        "score": 99
    }
]


def learn_json():
    print("learn_method_31")
    print("json的loads与dumps方法应用")
    # json.dumps()	将 Python 对象编码成 JSON 字符串
    # json.loads()	将已编码的 JSON 字符串解码为 Python 对象
    # json.dump()	将Python内置类型序列化为json 字符串
    # json.load()	读取文件中json形式的字符串元素转化为Python类型
    # person = dict(name='李彬', age=59)
    json_str = json.dumps(person)
    print(f"1.字典转字符串 == {json_str}")
    json_str = json.dumps(person, ensure_ascii=False)
    print(f"2.字典转字符串，ensure_ascii为False == {json_str}")
    dict1 = json.loads(json_str)
    print(f"3.字符串转成字典 == {dict1}")

    ani = Animal('狗熊', '雄性', 333)
    json_str = json.dumps(ani, default=obj2dict, ensure_ascii=False)
    print(f"4.将实例对象转成 json 字符串 == {json_str}")

    anis = [ani, ani]
    json_str = json.dumps(anis, default=obj2dict, ensure_ascii=False)
    print(f"5.将 list 实例集合转成 json数组 字符串 == {json_str}")
    # dict1 = json.loads(json_str)
    # print(f"3.字符串转成字典 == {dict1}")
    #
    json_str = json.dumps(ani, default=lambda temp: {
        'name': temp.name,
        'gender': temp.gender,
        'age': temp.age
    }, ensure_ascii=False)
    print(f"6.使用匿名函数  格式化json 字符串== {json_str}")

    json_str = json.dumps(person, default=lambda temp: temp.__dict__, ensure_ascii=False)
    print(f"7.使用自带的 __dict__ 格式化后的 json 字符串== {json_str}")

    print(f"json.loads()方法把对应的字符串转成对象")
    ani1 = json.loads(json_str, object_hook=lambda temp: Animal(temp['name'], temp['gender'], temp['age']))
    print(f"8.把字符串 转成 对象 == {ani1}，类型是=={type(ani1)}")
    #
    # 从文件中读取JSON数据，目录要从当前根目录还是找起
    with open('../../static/json.txt', 'r') as f:
        data = json.load(f)
    print(f"9.使用 json.load(f)从文件中获取的json字符串，是dict格式的，== {data}")
    json_dict = json.loads(json_str)
    print("13.使用 json.dump 方法生成 json 文件")
    print("13.json.dump的文本最好是dict格式的，ensure_ascii为Fasle时输出的是utf_8格式，indent是缩进格式化")
    print("13.json.dumps的文本最好是dict格式的，ensure_ascii为Fasle时输出的是utf_8格式，indent是缩进格式化")
    # 输出信息到 dump.json 文件中
    f = open('../../static/dump.json', "w")
    json.dump(json_dict, f, ensure_ascii=False, indent=2)
    f.close()
    # 输出信息到 dump.txt 文件中
    f = open('../../static/dump.txt', "w")
    json.dump(json_dict, f, ensure_ascii=False, indent=2)
    f.close()


learn_json()
