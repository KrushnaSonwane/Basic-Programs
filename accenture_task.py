pass1 = 'krushna'
pass2 = 'rahul'
def test_psw_equal():
    if pass1 == pass2:
        return True
def test_psw_equal2():
    if pass1.lower() == pass2.lower():
        return True
def test_psw_equal3():
    if pass1 != pass2:
        return False
print(test_psw_equal3())
        