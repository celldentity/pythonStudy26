import time
import sys
import os
from datetime import datetime

# 회원관리 CRUD를 사용자 지정 함수로 만들어 보자.
# C : 회원가입
# R : 관리자인경우 회원암호 변경, 블랙리스트로 생성, 권한 부여
# R : 로그인  id 와 pw를 활용하여 로그인 상태 유지 session
# U : 회원정보 수정
# D : 회원탈퇴, 회원비활성화

#프로그램에서 사용될 변수들
#전역변수(global) -> py파일 안에서 전체적으로 사용되는 변수
#지역변수(local) -> while, if, for, def안에서 사용되는 변수
run = True #while 에서 전체적으로 사용되는 변수(프로그램 구동)
session = None # 로그인상태 저장용   -> 로그인한 사용자의 리스트 인덱스 기억용(어떤숫자든 활성화 되어 있으면 로그인 상태)

# 프로그램에서 사용될 리스트 들 (더미 데이터)
# sns = [1] # 회원번호들 회원삭제 및 추가시 번호가 흔들릴 수 있음
ids = ["kkw", "ksb", "wow", "sad"] # 로그인 아이디 들
pws = ["1234", "5678", "8888", "0000"] # 암호 둘
names = ["김기원", "김수빈", "개깜놀", "김탈퇴"] # 사용자 명
roles = ["admin", "manager", "user", "user"] # 사용자 권한 (admin, manager, user)
active = [True, True, True, False] # 회원사용중, 탈퇴, 중지, 블랙리스트 등...
addTime = [0, 0, 0, 0]
roletype = {
    "1": "관리자",
    "2": "매니저",
    "3": "일반유저"}
# 차후에는 파일처리로 변환 할 예정    탈퇴할 경우 탈퇴한 회원을 관리자가 조회할 수 있어야 한다.

#프로그램에서 사용될 함수들
def typewriter(text, speed=0.01):
    for char in text:
        sys.stdout.write(char) # 한 글자씩 출력
        sys.stdout.flush()     # 버퍼를 비워 즉시 화면에 표시
        time.sleep(speed)      # 다음 글자까지 대기 시간 (초 단위)
    print() # 마지막에 줄바꿈
#--------------------------------------------------------------------------------------------------------

def member_add():
    typewriter("\n회원가입 메뉴로 진입합니다.")
    id = input("가입하시려는 아이디를 입력하세요.")
    if id in ids:
        print("\033[31m이미 회원가입된 아이디 입니다.\033[0m")
        return
    else:
        pw = input("가입하시려는 비밀번호를 입력하세요.")
        print(roletype)
        while True:
            role = input("가입하시려는 권한을 선택하세요.")
            if role.isdigit():
                roleNum = int(role)
                break
            else:
                print("\033[31m오류: 1~3숫자만 입력 가능합니다.\033[0m")
        while True:
            if roleNum == 1:
                adPass = input("\n관리자 계정을 선택하셨습니다. 관리자 비밀번호를 입력하세요")
                while True:
                    if adPass == "1004":
                        print("\033[32m관리자로 계정을 생성합니다.\033[0m")
                        roles.append("admin")
                        break
                    else:
                        print("\n비밀번호가 틀렸습니다. 관리자에게 문의하세요.")
                break
            elif roleNum == 2:
                print("\033[32m매니저로 계정을 생성합니다.\033[0m")
                roles.append("manager")
                break
            elif roleNum == 3:
                print("\033[32일반사용자로 계정을 생성합니다.\033[0m")
                roles.append("user")
                break
            else:
                print("\n잘못된 입력입니다. 입력을 확인하세요.")
        name = input("\n이름을 입력하세요")
        if input(f"\n입력된 정보를 확인하세요.{id}, {pw}, {name}, {roletype[str(roleNum)]}\n저장하시려면 'Enter'키를, 취소하려면 다른키를 누르세요") == "":
            names.append(name)
            pws.append(pw)
            ids.append(id)
            active.append(True)
            typewriter("\033[32m회원가입이 완료되었습니다.\033[0m")
            return




        print(f"입력된 숫자: {number}")

def member_login(): #가입된 회원을 확인하여 로그인 처리 후 session 변수에 인덱스를 넣음
    typewriter("로그인 메뉴로 진입합니다.")
    global session
    if session is not None:
        # is not None 싱글톤이라는 객체가 있는지 비교하는 용
        # if session != None -> 자료형 비교를 위한 표현
        print("\n\033[31m이미 로그인 한 상태입니다.\033[0m")
        print(f"로그인한 사용자는 {names[session]}님 입니다.")
        return # 되돌아간다.
    else:
        user_id = input("로그인 ID")
        user_pw = input("비밀번호")
    if user_id in ids :
        idx = ids.index(user_id)
        if not active[idx]:
            print("비활성화/차단된 계정입니다.")
            return
        else:
            if user_pw == pws[idx]:
                session = idx
            else:
                print("\n\033[31m비밀번호가 다릅니다.\033[0m")

def member_admin(): #관리자 권한으로 할 수 있는 것들, 관리자가 로그인 할 수 있는 기술들 제공
    typewriter("member_login 함수로 진입합니다.")
    #전체회원 보기, 블랙 리스트 등록, 본인 포함 다른 사용자 정보 수정

    typewriter("member_login 함수를 종료합니다.")

def member_logout(): #회원 로그 아웃
    if input("\n로그아웃 하시려면 'Enter'키를\n취소하시려면 다른 키를 누르세요.") == "":
        global session
        session = None
    else:
        print("\n이전 메뉴로 돌아갑니다.")
    return

def member_modify(): #로그인 상태인지 확인하고 자신의 정보를 확인하고 수정한다.
    print("\n이전 메뉴로 돌아갑니다.")


def member_delete(): #회원탈퇴 또는 휴면계정 처리(비활성화 처리)
    print("\n이전 메뉴로 돌아갑니다.")


def main_menu():
    typewriter(f"""
====== MBC아카데미 회원관리 프로그램입니다. ======
1. 회원가입     2. 로그인      3. 회원정보수정
4. 로그아웃       5.회원탈퇴
9. 프로그램 종료
=============================================""")

run = True
while run:
    main_menu()
    select = input("\n이용하시려는 메뉴를 선택해주세요.")
    if select == "1": member_add()
    elif select == "2": member_login()
    elif select == "3": member_admin()
    elif select == "4": member_logout()
    elif select == "5": member_delete()
    elif select == "9": run  = False
    else:
        typewriter("\n올바른 입력이 아닙니다. 다시 입력해주세요.")
