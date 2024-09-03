import time

def execute_task():
    # 在这里编写需要执行的任务的代码
    print("任务执行完毕")

while True:
    current_time = time.localtime()
    if current_time.tm_hour == 11:
        execute_task()
        break
    time.sleep(1)
