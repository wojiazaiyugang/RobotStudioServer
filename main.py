from communication import get_msg, send_msg
from file import get_ini_config

if __name__ == '__main__':
    while True:
        command = get_msg()
        # print(command)
        # func, *args = command.split("|")
        # result = eval(f"{func}(args)")
        # send_msg(result)
        send_msg(command)
