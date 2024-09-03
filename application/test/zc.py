import time

def move(dx, dy):
    """移动桌宠"""
    print("桌宠移动了", dx, "单位横向距离，", dy, "单位纵向距离")

def rotate(degrees):
    """旋转桌宠"""
    print("桌宠旋转了", degrees, "度")

def show_message(message):
    """显示消息"""
    print("桌宠显示消息：", message)

def hide_message():
    """隐藏消息"""
    print("桌宠隐藏了消息")

def main():
    while True:
        print("请输入指令：")
        print("1. 移动桌宠")
        print("2. 旋转桌宠")
        print("3. 显示消息")
        print("4. 隐藏消息")
        print("5. 退出程序")
        command = input()
        if command == "1":
            dx = int(input("请输入横向移动距离："))
            dy = int(input("请输入纵向移动距离："))
            move(dx, dy)
        elif command == "2":
            degrees = int(input("请输入旋转角度："))
            rotate(degrees)
        elif command == "3":
            message = input("请输入要显示的消息：")
            show_message(message)
        elif command == "4":
            hide_message()
        elif command == "5":
            print("程序已退出。")
            break
        else:
            print("无效的指令，请重新输入。")

if __name__ == "__main__":
    main()

# 这个桌宠代码可以根据用户输入的指令进行不同的动作，包括移动、旋转、显示消息和退出程序等。用户可以通过输入指令来控制桌宠的行为。例如，用户输入“1”然后分别输入横向和纵向移动距离来移动桌宠；输入“2”然后输入旋转角度来旋转桌宠；输入“3”然后输入要显示的消息来让桌宠显示消息；输入“4”来隐藏消息；输入“5”来退出程序。