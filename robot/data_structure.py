from ctypes import Structure, c_int, c_char_p


class CommandArg(Structure):
    _fields_ = [
        ("path", c_char_p),
        ("mode", c_int),
        ("dete_background", c_int),
        ("EtherCATonly", c_int),
        ("server_modbus", c_int),
        ("port", c_int),
        ("iscopy", c_int)]


if __name__ == '__main__':
    command_arg = CommandArg(c_char_p(bytes("/hanbing", encoding="utf8")), 1, 0, 0, 0, 6666, 1)
