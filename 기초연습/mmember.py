from prompt_toolkit.key_binding.bindings.named_commands import clear_screen
import os
import datetime
import time

run = True
login_user = None

menu = """
===========================
mbc 아카데미 회원 관리 프로그램
===========================
1. 회원가입
2. 로그인
3. 회원보기
4. 내정보수정
5. 프로그램 종료
"""

# 회원 DB
sns = [1, 2, 3]
ids = ["kkw", "lhj", "ksb"]
names = ["김기원", "임현정", "김수빈"]
passwords = ["1234", "4321", "7410"]
emails = ["admin@mbc.com", "lhj@mbc.com", "ksb@mbc.com"]
admins = [True, False, False]
login_user = None

while run:
    print(menu)
    if login_user is not None:
        if admins[idx]:
            print(f" >>> 현재접속중: {names[login_user]}님\n관리자 계정입니다.")
        else:
            print(f" >>> 현재접속중: {names[login_user]}님\n일반사용자 계정입니다.")

    select = input("메뉴를 선택하세요: ")

    #1. 회원가입
    if select == "1":
        print("\n[회원가입]")
        sn = input("사번: ")
        while True:
            new_id = input("생성할 아이디: ")
            if new_id in ids:
                print(f"'{new_id}'는 이미 사용중인 아이디입니다. \n 다른 아이디를 입력해주세요.")
            else:
                if new_id not in ids:
                    new_pw = input("생성할 비밀번호: ")
                    name = input("성명: ")
                    email = input("이메일 계정: ")
                    if input("회원가입을 희망하시면 y키를 \n희망하지 않으실 경우 n키를 눌러주세요.:" ).lower() == "y":
                        sns.append(sn)
                        ids.append(new_id)
                        passwords.append(new_pw)
                        names.append(name)
                        emails.append(email)
                        admins.append(False)
                        print("회원가입이 완료되었습니다. \n3초뒤 메인화면으로 돌아갑니다.")
                        time.sleep(3)
                    else:
                        print("회원가입 진행이 취소되었습니다. \n다시 처음부터 진행하세요. \n3초뒤 메인화면으로 돌아갑니다.")
                        time.sleep(3)
                break

    #2. 로그인
    elif select == "2":
        print("\n[로그인 화면]")
        logid = input("[로그인 id 입력]: ")
        logpw = input("[로그인 pw 입력]: ")
        #로그인 성공 조건 부여
        if logid in ids:
            idx = ids.index(logid)
            if passwords[idx] == logpw:
                login_user = idx
                os.system('cls')
                print(f"{names[idx]}님, 환영합니다! \n3초뒤 메뉴로 돌아갑니다.")
                time.sleep(3)
            else:
                print("비밀번호가 틀렸습니다. 로그인을 다시 진행해주세요. \n 3초뒤 메뉴로 돌아갑니다.")
                time.sleep(3)
        else:
            print("등록된 아이디가 아닙니다. 아이디를 확인해주시거나 회원가입을 먼저 진행해주세요. \n 3초뒤 메뉴로 돌아갑니다.")
            time.sleep(3)



