import random
def bank_card(self, bank):
    """
    Bank_card.

    Args:
        bank (str) :

    Returns:
        str

    """
    bank_len = BANK_BIN_INFO[bank]["LEN"]
    if bank_len == 16:
        bank_no = str(random.sample(BANK_BIN_INFO[bank]["BIN"], 1)[0]) + \
                  str(self.cust_random(9))
    elif bank_len == 17:
        bank_no = str(random.sample(BANK_BIN_INFO[bank]["BIN"], 1)[0]) + \
                  str(self.cust_random(10))
    elif bank_len == 18:
        bank_no = str(random.sample(BANK_BIN_INFO[bank]["BIN"], 1)[0]) + \
                  str(self.cust_random(11))
    else:
        bank_no = str(random.sample(BANK_BIN_INFO[bank]["BIN"], 1)[0]) + \
                  str(self.cust_random(12))
    reve = [int(x) for x in reversed(bank_no)]
    j = sum(reve[1::2]) + sum((x // 10 + x % 10) for x in [2 * i for i in reve[::2]])
    if j % 10 == 0:
        return bank_no + "0"
    else:
        return bank_no + str(10 - j % 10)
BANK_BIN_INFO = {
    # 工行 620302,620200 18
    "ICBC": {"BIN": [620302, 620200], "LEN": 18},
    # 光大 622660,622663 16
    "CEB": {"BIN": [622660, 622663], "LEN": 16},
    # 广发 622555,622555 16
    "GDB": {"BIN": [622555, 622555], "LEN": 16},
    # 华夏 621222,623020 16
    "HXB": {"BIN": [621222, 623020], "LEN": 16},
    # 建行 620060,621081 19
    "CCB": {"BIN": [620060, 621081], "LEN": 19},
    # 农行 622844,622845 19
    "ABC": {"BIN": [622844, 622845], "LEN": 19},
    # 平安 623058,621626 19
    "PAB": {"BIN": [623058, 621626], "LEN": 19},
    # 浦发 622177,622266 16
    "SPDB": {"BIN": [622177, 622266], "LEN": 16},
    # 兴业 622909,622908 18
    "CIB": {"BIN": [622909, 622908], "LEN": 18},
    # 招商 621483,621485 16
    "CMB": {"BIN": [622588, 622580], "LEN": 16},
    # 中行 621661,621663 19
    "BOC": {"BIN": [621661, 621663], "LEN": 19},
    # 中信 622690,622691 16
    "CITIC": {"BIN": [622690, 622691], "LEN": 16},
    # 民生 622615,622616 16
    "CMBC": {"BIN": [622615, 622616], "LEN": 16},
    # 邮政 622150,622151 19
    "PSBC": {"BIN": [622150, 622151], "LEN": 19},
    # 交通 622258,622259 17
    "BOCOM": {"BIN": [622258, 622259], "LEN": 17}}