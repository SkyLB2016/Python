import datetime

YMD = '%Y-%m-%d'
YMDHM = '%Y-%m-%d %H:%M'
YMDHMS = '%Y-%m-%d %H:%M:%S'
CYMD = '%Y年%m月%d日'
CYMDHM = '%Y年%m月%d日 %H:%M'
CYMDHMS = '%Y年%m月%d日 %H:%M:%S'


def time_format():
    date_time = datetime.datetime.now()
    print(f"1.默认获取的时间：time1=={str(date_time)}")
    print(f"2.默认获取的时间：time1默认的类型=={type(date_time)}")
    print(f'3.时间格式：{YMD}，对应的时间：{date_time.strftime(YMD)}')
    print(f'4.时间格式：{YMDHM}，对应的时间：{date_time.strftime(YMDHM)}')
    print(f'5.时间格式：{YMDHMS}，对应的时间：{date_time.strftime(YMDHMS)}')
    print(f'6.时间格式：{CYMD}，对应的时间：{date_time.strftime(CYMD)}')
    print(f'7.时间格式：{CYMDHM}，对应的时间：{date_time.strftime(CYMDHM)}')
    print(f'8.时间格式：{CYMDHMS}，对应的时间：{date_time.strftime(CYMDHMS)}')

    date_time = datetime.datetime.strftime(datetime.datetime.now(), '%Y年%m月%d日 %H:%M:%S')
    print(f"9.datetime.strftime()方法把 datetime 类型转换成字符串格式")
    print(f"10.datetime.strftime()方法，格式化后的时间time2=={date_time}")
    print(f"11.datetime.strftime格式化后，time2的类型=={type(date_time)}")

    date_time = datetime.datetime.strptime('2023年11月14日17:16:54', '%Y年%m月%d日%H:%M:%S')
    print(f"12.datetime.strptime()方法把 时间字符串格式 转换成 datetime 类型")
    print(f"13.datetime.strptime()方法，格式化后的时间time3=={date_time}")
    print(f"14.datetime.strptime() 格式化后，time3的类型=={type(date_time)}")
    print("15.", datetime.datetime.fromtimestamp(datetime.datetime.now().timestamp()))  # 本地时间
    print("16.", datetime.datetime.utcfromtimestamp(datetime.datetime.now().timestamp()))  # UTC时间

    # 创建一个当前日期和时间的对象
    now = datetime.datetime.now()
    print(now)
    print(now.month)

    # 创建一个特定的日期和时间对象
    specific_date = datetime.datetime(2023, 10, 23, 14, 30, 15)
    print(specific_date)
    # 加一天
    one_day_later = now + datetime.timedelta(days=1)
    print(one_day_later)

    # 减一小时
    one_hour_ago = now - datetime.timedelta(hours=1)
    print(one_hour_ago)
