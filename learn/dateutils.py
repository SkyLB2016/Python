from datetime import datetime

YMD = '%Y-%m-%d'
YMDHM = '%Y-%m-%d %H:%M'
YMDHMS = '%Y-%m-%d %H:%M:%S'
CYMD = '%Y年%m月%d日'
CYMDHM = '%Y年%m月%d日 %H:%M'
CYMDHMS = '%Y年%m月%d日 %H:%M:%S'


def time_format():
    time = datetime.now()
    print(f"默认获取的时间：time1=={str(time)}")
    print(f"默认获取的时间：time1默认的类型=={type(time)}")
    print(f'时间格式：{YMD}，对应的时间：{time.strftime(YMD)}')
    print(f'时间格式：{YMDHM}，对应的时间：{time.strftime(YMDHM)}')
    print(f'时间格式：{YMDHMS}，对应的时间：{time.strftime(YMDHMS)}')
    print(f'时间格式：{CYMD}，对应的时间：{time.strftime(CYMD)}')
    print(f'时间格式：{CYMDHM}，对应的时间：{time.strftime(CYMDHM)}')
    print(f'时间格式：{CYMDHMS}，对应的时间：{time.strftime(CYMDHMS)}')

    time = datetime.strftime(datetime.now(), '%Y年%m月%d日 %H:%M:%S')
    print(f"datetime.strftime()方法把 datetime 类型转换成字符串格式")
    print(f"datetime.strftime()方法，格式化后的时间time2=={time}")
    print(f"datetime.strftime格式化后，time2的类型=={type(time)}")

    time = datetime.strptime('2023年11月14日17:16:54', '%Y年%m月%d日%H:%M:%S')
    print(f"datetime.strptime()方法把 时间字符串格式 转换成 datetime 类型")
    print(f"datetime.strptime()方法，格式化后的时间time3=={time}")
    print(f"datetime.strptime() 格式化后，time3的类型=={type(time)}")
    print(datetime.fromtimestamp(datetime.now().timestamp()))  # 本地时间
    print(datetime.utcfromtimestamp(datetime.now().timestamp()))  # UTC时间

