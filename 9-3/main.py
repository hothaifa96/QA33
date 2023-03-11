def check_password(password):
    if len(password) > 8 and password[0] == password[0].upper() and not password.isalpha():
        return True
    else:
        return False


# print(check_password('Hothaifagfhjnhbg')) #F
# print(check_password('Hothaifa12344')) # T
# print(check_password('othaifagf123123')) #F
# print(check_password('fagfasfasg')) #F
# print(check_password('H2134567854')) #T


def withdraw(amount):
    if amount % 100 == 0 and amount < 4000:
        return True
    else:
        return False

# N  4000 4100 - P 3900
# N- 330   N - 5050

def deposit(amount):
    if 0 < amount <= 10000:
        return True
    else:
        return False

# ------(-100)---0-------5000-------10000--11000---