# -*- coding: utf-8 -*-
"""
@Time    : 2024/11/4 18:45
@Author  : sky
@Email   : your-email@example.com
@File    : text_utils.py
@Description: 
"""
import json


# 文本倒序输出
def text_reversed():
    file_path = './static/text_old/text.txt'
    file_new_path = './static/text_new/text2.txt'
    texts = []
    text = ''
    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            if "  " in line and "、" in line:
                print(text)
                texts.append(text)
                text = ''
            text += line
        print(text)
        texts.append(text)  # 添加最后一章
    # 生成新文件
    with open(file_new_path, "w") as f:
        for text in reversed(texts):  # 倒序
            f.write(text)
    print(len(texts))
    print(f'{texts}')


def calculate_word():
    file_path = './static/text_old/text.txt'
    file_new_path = './static/text_new/text2.txt'
    chapter_list = []
    chapter = []
    contain_01 = "第"
    contain_02 = '节'
    # contain_02 = '卷'
    # contain_03 = '章'

    # contain_01 = "、"
    # contain_02 = '  '
    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            # if line.__contains__(contain_01) and line.__contains__(contain_02):
            #     continue
            line = line.replace("　", "") \
                .replace("，", "") \
                .replace("。", "") \
                .replace("；", "") \
                .replace("！", "") \
                .replace("、", "") \
                .replace("？", "") \
                .replace("：", "") \
                .replace("“", "") \
                .replace("”", "") \
                .replace("‘", "") \
                .replace("’", "") \
                .replace("?", "") \
                .replace("【", "") \
                .replace("】", "") \
                .replace("「", "") \
                .replace("」", "") \
                .replace("[ ", "") \
                .replace("]", "") \
                .replace(" ", "") \
                .replace("~", "") \
                .replace("·", "") \
                .replace(".", "") \
                .replace("（", "") \
                .replace("）", "") \
                .replace("(", "") \
                .replace(")", "") \
                .replace("《", "") \
                .replace("》", "") \
                .replace("+", "") \
                .replace("\n", "") \
                .replace("0", "") \
                .replace("1", "") \
                .replace("2", "") \
                .replace("3", "") \
                .replace("4", "") \
                .replace("5", "") \
                .replace("6", "") \
                .replace("7", "") \
                .replace("8", "") \
                .replace("9", "")

            # if line.__contains__('第') and line.__contains__('章'):
            if line.__contains__(contain_01) and line.__contains__(contain_02):
                chapter_list.append(chapter)
                chapter = [line]
            else:
                if len(line) == 0:
                    continue
                chapter.append(line)
        chapter_list.append(chapter)
    print(chapter_list)
    print('列表长度', len(chapter_list))
    count_all = 0
    title_count = 0
    count_list = []
    for chapter in chapter_list:
        count = 0
        # 去掉标题，只统计内容字数
        for line in range(1, len(chapter)):
            count += len(chapter[line])
        print(chapter[0], count)
        count_list.append(count)
        count_all += count
        if len(chapter) > 1:
            title_count += len(chapter[1])
    print(count_list)
    count_list.pop(0)
    print(count_list)
    print(sorted(count_list))

    print("文本长度", count_all)
    print("标题长度", title_count)
    with open(file_new_path, "w") as f:
        for chapter in chapter_list:
            for text in chapter:
                f.write(text)


def learn_method_40():
    file_path = './static/text_old/text.txt'
    file_new_path = './static/text_new/text_100.txt'

    chapter_list = []
    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            if line.__contains__('第') and line.__contains__('章'):
                continue

            line = line.replace("　", "") \
                .replace("，", "") \
                .replace("。", "") \
                .replace("；", "") \
                .replace("！", "") \
                .replace("、", "") \
                .replace("？", "") \
                .replace("：", "") \
                .replace("“", "") \
                .replace("”", "") \
                .replace("‘", "") \
                .replace("’", "") \
                .replace("?", "") \
                .replace("【", "") \
                .replace("】", "") \
                .replace("「", "") \
                .replace("」", "") \
                .replace("[ ", "") \
                .replace("]", "") \
                .replace(" ", "") \
                .replace("~", "") \
                .replace("·", "") \
                .replace(".", "") \
                .replace("（", "") \
                .replace("）", "") \
                .replace("(", "") \
                .replace(")", "") \
                .replace("《", "") \
                .replace("》", "") \
                .replace("+", "") \
                .replace("\n", "") \
                .replace("0", "") \
                .replace("1", "") \
                .replace("2", "") \
                .replace("3", "") \
                .replace("4", "") \
                .replace("5", "") \
                .replace("6", "") \
                .replace("7", "") \
                .replace("8", "") \
                .replace("9", "")
            if len(line) > 0:
                chapter_list.append(line)
    print("列表长度", len(chapter_list))
    print([chapter_list])
    count_all = -3
    for line in chapter_list:
        count_all += len(line)
    print(count_all)

    # 按一百一行划分
    count = 0
    with open(file_new_path, "w") as f:
        for text in chapter_list:
            length = len(text)
            if count + length >= 100:
                # print('原句', text)
                start = text[0:100 - count]
                # print('前段', start)
                end = text[100 - count:length]
                # print('后段', end)
                f.write(start)
                f.write('\n')
                f.write(end)
                count = length - 100 + count
            else:
                count += length
                f.write(text)


"""
Description: 文章方法处理
"""


def text_modify():
    file_path = './static/text_old/text.txt'
    file_new_path = './static/text_new/诗词.txt'

    poetry_list = []
    poetry = []
    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            if line.__contains__('  '):
                poetry_list.append(poetry)
                poetry = []
                # print(line)
                if line.__contains__('、'):
                    poetry.append(line.split("、")[1])
                else:
                    poetry.append(line)
            else:
                poetry.append(line)
        poetry_list.append(poetry)
    print(poetry_list)
    poetry_one = poetry_list.pop(0)
    # print(poetry_one[0],poetry_one[1])
    print(poetry_one)
    print("诗有", len(poetry_list), '首')
    # 王朝列表结构
    # dynasty_map = {
    #     '唐': {
    #         "李白": [
    #             ['静夜思', "床前明月光"],
    #             ['独坐敬亭山', '众鸟高飞尽']
    #         ],
    #         "杜甫": [
    #             ['绝句', '迟日江山丽']
    #         ]
    #     },
    #     '宋': {
    #         "王安石": [
    #             ['元日'],
    #             ['书湖阴先生壁']
    #         ],
    #         "苏轼": [
    #             ['水调歌头']
    #         ]
    #     }
    # }
    # 王朝列表
    dynasty_map = {}
    # poetry_map = {}
    for poetry in poetry_list:
        if len(poetry) == 0:
            continue
        first = poetry[0]
        # print(poetry[0])
        if first.__contains__('  '):
            sp = first.split('  ')[1].split('·')
            # 朝代
            dynasty = sp[0].replace("\n", "")
            # 作者
            auth = sp[len(sp) - 1].replace("\n", "")
            # 根据朝代，获取作者集合
            if dynasty in dynasty_map:
                dy_map = dynasty_map[dynasty]
                # 判断作者是否已存在
                if auth in dy_map:
                    # 存在
                    dy_map[auth].append(poetry)
                else:
                    # 不存在
                    dy_map[auth] = [poetry]
            else:
                # 朝代未加入
                dynasty_map[dynasty] = {auth: [poetry]}
        else:
            if '佚名' in dynasty_map:
                dynasty_map['佚名']['佚名'].append(poetry)
            else:
                dynasty_map['佚名'] = {'佚名': [poetry]}
    print("数据源", json.dumps(dynasty_map, ensure_ascii=False))
    # dynasty_keys = dynasty_map.keys()
    # print("朝代列表", dynasty_keys)
    dynasty_keys = [key for key in dynasty_map]
    print("朝代列表", dynasty_keys)

    # 规定好的朝代顺序
    keys = [
        '佚名', '诗经', '秦汉', '汉', '汉乐府', '三国~魏', '东晋', '南朝~梁', '南朝~宋', '北朝民歌',
        '古诗十九首', '唐', '北宋', '南宋', '元', '明', '清', '毛泽东'
    ]
    # 规定好的唐朝诗人顺序
    tang_keys = [
        '白居易', '岑参', '储光羲', '崔护', '常建', '陈子昂', '杜甫', '杜牧', '杜荀鹤', '高适', '胡令能',
        '韩翃', '韩愈', '贺知章', '贾岛', '李白', '李贺', '李峤', '李商隐', '李绅', '李世民', '林杰', '令狐楚',
        '刘长卿', '刘禹锡', '柳宗元', '卢纶', '罗隐', '骆宾王', '吕岩', '孟浩然', '孟郊', '皮日休', '司空曙',
        '宋之问', '王湾', '王勃', '王昌龄', '王翰', '王建', '王维', '王之涣', '韦应物', '温庭筠', '颜真卿',
        '虞世南', '元稹', '张籍', '张继', '张九龄', '张志和'
    ]

    beisong_keys = [
        '程颢', '范仲淹', '黄庭坚', '寇准', '柳永', '欧阳修', '秦观',
        '邵雍', '苏轼', '王观', '王安石', '翁卷', '晏殊', '张俞',
    ]

    nansong_keys = [
        '范成大', '雷震', '李清照', '卢钺', '陆游', '林升', '唐士耻',
        '辛弃疾', '文天祥', '杨万里', '叶绍翁', '曾几', '赵师秀', '朱熹',
    ]

    # 每首的顺序
    count = 1
    # 目录
    title_all_list = []
    # 内容
    poetry_all_list = []
    for k in keys:
        poetry_map = dynasty_map[k]
        # for k2, poetries in poetry_map.items():
        #     for poetry in poetries:
        #         poetry[0] = str(count) + '、' + poetry[0]
        #         for text in poetry:
        #             f.write(text)
        #         count += 1
        # 获取作者列表
        auth_keys = [key for key in poetry_map]
        # print(sorted(auth_keys))
        # 根据定好的作者顺序输出
        if k == '唐':
            print("朝代", k, "作者列表", tang_keys)
            count = 1
            count, title_list, poetry_list = write_text(tang_keys, count, f, poetry_map)
        elif k == '北宋':
            print("朝代", k, "作者列表", beisong_keys)
            count = 1
            count, title_list, poetry_list = write_text(beisong_keys, count, f, poetry_map)
        elif k == '南宋':
            print("朝代", k, "作者列表", nansong_keys)
            count, title_list, poetry_list = write_text(nansong_keys, count, f, poetry_map)
            count = 1
        else:
            if k == '毛泽东':
                count = 1
            print("朝代", k, "作者列表", auth_keys)
            count, title_list, poetry_list = write_text(auth_keys, count, f, poetry_map)
        title_all_list += title_list
        poetry_all_list += poetry_list

    with open(file_new_path, "w") as f:
        # 文章头
        for text in poetry_one:
            f.write(text)
        # 文章目录
        for text in title_all_list:
            f.write(text)

        f.write('\n')
        f.write('\n')

        # 文章内容
        for text in poetry_all_list:
            f.write(text)


def write_text(tang_keys, count, f, poetry_map):
    title_list = []
    poetry_list = []
    for auth in tang_keys:
        # 获取诗人名下的诗列表
        for poetry in poetry_map[auth]:
            title = str(count) + '、' + poetry[0]
            poetry[0] = title
            title_list.append(title)
            poetry_list += poetry
            # print(poetry)
            # print(poetry[0])
            # for text in poetry:
            #     f.write(text)
            count += 1
    title_list.append('\n')
    # print(title_list)
    # print(poetry_list)
    return count, title_list, poetry_list

def read_dd():
    file_path = './static/text_old/dd.txt'

    chapter_list = []
    with open(file_path,encoding="gbk") as f:
        f.readline()
        lines = f.readline()
        print(len(lines))
        # lines = f.readline()
        # print(lines)
    print("列表长度", len(chapter_list))
def main():
    # text_modify()
    # learn_method_40()
    calculate_word()
