#!/usr/bin/env python3

def main():
    totalFail = 0

    loginFail = 0

    with open("/home/student/mycode/attemptlogin/keystone.common.wsgi", "r") as keystone_file:
        for line in keystone_file:
            if "-] Authorization failed" in line:
                totalFails += 1
            if "- - - - -] Authorization failed" in line:
                loginFail += 1

    print('Failed Login Attempts:', loginFail)
    print()
    print('Successful Login Attempts:', totalFail-loginFail)


if __name__ == '__main__':
    main()
