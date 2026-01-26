import os
from testExam.LMS.service.MemberService import *
from testExam.LMS.common.Session import *

def main():
    MemberService.load()
    run = True
    while run:
        print("""\033[32m
===============================
    MBC 아카데미 LMS 프로그램
===============================\033[0m
1. 회원가입 2. 로그인 3.내정보수정
4. 로그아웃 5.관리자메뉴 6.회원탈퇴
7. 내정보 조회하기
9. LMS 프로그램 종료""")
        member = Session.login_member
        if member is None:
            print("\n\033[31m현재 로그인 상태가 아닙니다.\033[0m")
        else:
            print(f"\n\033[34m{member.name}님 {member.role}권한으로 로그인 중\033[0m")
        sel = input("\n이용하시려는 메뉴를 선택하세요.")
        if sel == "1": MemberService.signup()
        elif sel == "2": MemberService.login()
        elif sel == "3": MemberService.modify()
        elif sel == "4": MemberService.logout()
        elif sel == "5": MemberService.admin_menu()
        elif sel == "6": MemberService.delete()
        elif sel == "7": MemberService.self_info()
        elif sel == "9":
            print("\033[31m프로그램을 종료합니다.\033[0m")
            MemberService.save()
            run = False
        else:
            print("\n\033[31m잘못된 메뉴 선택입니다.\033[0m")


if __name__ == "__main__":
    main()