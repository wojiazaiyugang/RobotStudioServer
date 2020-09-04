from communication import get_msg, send_msg
from file import set_all_config, get_all_config

if __name__ == '__main__':
    while True:
        command = get_msg()
        # print(command)
        func, *args = command.split("|")
        try:
            result = eval(f"{func}(args)") or "ok"
            send_msg(result)
        except ValueError:
            raise ValueError
