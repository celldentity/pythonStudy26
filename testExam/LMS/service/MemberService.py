import os
from testExam.LMS.common.Session import * #이닛 파일 만들고 common 까지만 작성해도 파일 연결이 안되어 부득히 Session까지 프롬에 넣었습니다.
from testExam.LMS.domain.Member import *

File_DIR = os.path.dirname(os.path.abspath(__file__))
File_Path = os.path.join(File_DIR, '..', 'data', 'member.txt')

members = []

class MemberService:

    @classmethod
    def load(cls):
        cls.members = []
        if not os.path.exists(File_Path):
            cls.save()
            return

        with open(File_Path, "r", encoding="utf-8") as f:
            for line in f:
                cls.members.append(Member.from_line(line))

    @classmethod
    def save(cls):
        with open(File_Path, "w", encoding="utf-8") as f:
            for m in cls.members:
                f.write(m.to_line() + "\n")

    @classmethod
    def self_info(cls):
        if not Session.is_login():
            print("\n로그인 후 이용 가능합니다.")
            return
        member = Session.login_member
        print(f"""
[내 정보 확인 메뉴]
아이디:{member.uid}
비밀번호:{member.pw}
이름:{member.name}
권한:{member.role}
활성화 여부:{member.active}""")


    @classmethod
    def signup(cls):
        print("\n회원가입 서비스 입니다.")
        uid = input("\n 사용하시려는 아이디를 입력하세요")
        if any (m.uid == uid for m in cls.members):
            print("\n이미 존재하는 아이디입니다.\n로그인을 진행하시거나 관리자에게 문의하세요.")
            return
        pw = input("\n사용하려는 비밀번호를 입력하세요")
        name = input("이름: ")
        if cls.members == []:
            role = "admin"
            member = Member(uid, pw, name, role)
            cls.members.append(member)
            cls.save()
            print("회원가입 완료")
            Session.login_member = member
            return
        else:
            member = Member(uid, pw, name)
            cls.members.append(member)
            cls.save()
            Session.login_member = member
            print("회원가입 완료")

    @classmethod
    def login(cls):
        print("\n로그인 서비스 입니다.")
        uid = input("아이디를 입력하세요: ")
        pw = input("비밀번호를 입력하세요: ")
        for m in cls.members:
            if m.uid == uid:
                if not m.active:
                    print("\n\033[31m비활성화 된 계정입니다. 관리자에게 문의하세요.\033[0m")
                    return
                if m.pw == pw:
                    Session.login(m)
                    print(f"{m.name}님 로그인 성공 {m.role}권한")
                    print(m) # str 기능 활용
                    return
                else:
                    print("\n\033[31m비밀번호가 틀렸습니다. 확인하세요.\033[0m")
                    return
        else:
            print("존재하지 않는 아이디입니다.")
            return

    @classmethod
    def logout(cls):
        if not Session.is_login():
            print("\n033[31m로그인 후 이용 가능합니다.\033[0m")
            return
        ot = input("\n정말 로그아웃 하시겠습니까?\n진행하시려면 \033[31m'Enter'\033[0m키를 아니면 아무키나 눌러주세요")
        if ot == "":
            Session.login_member = None
            return
        else:
            print("\n이전 메뉴로 돌아갑니다.")

    @classmethod
    def modify(cls):
        if not Session.is_login():
            print("\n033[31m로그인 후 이용 가능합니다.\033[0m")
            return
        print("\n회원수정 메뉴에 진입했습니다.")
        member = Session.login_member
        print("""
[내 정보 수정 서비스]
1. 이름변경
2. 비밀번호 변경
3. 취소""")
        sel = input("선택: ")
        if sel == "1":
            member.name = input("새로운 아이디 입력: ")
        elif sel == "2":
            member.pw = input("새로운 비밀번호 입력: ")
        else:
            return
        cls.save()
        print("\n내 정보 수정완료")

    @classmethod
    def delete(cls):
        if not Session.is_login():
            print("\n033[31m로그인 후 이용 가능합니다.\033[0m")
            return
        member = Session.login_member
        print("""
[회원탈퇴 서비스]
1. 계정 비활성화
2. 영구탈퇴""")
        dn = input("이용하시려는 메뉴를 선택하세요")
        if dn == "1":
            member.active = False
            Session.logout()
            cls.save()
            print("\n\033[31m사용자 비활성화되어 로그아웃 처리되었습니다.\033[0m")
        elif dn == "2":
            cls.members.remove(member)
            Session.logout()
            cls.save()
            print("\n\033[31m회원탈퇴가 완료되어 로그아웃 되었습니다.\033[0m")
        else:
            print("잘못된 선택입니다.")
#------------------------------------관리자메뉴------------------------------
    @classmethod
    def admin_menu(cls):
        if not Session.is_login() or not Session.login_member.is_admin():
            print("\033[34m관리자 계정만 이용할 수 있습니다.\033[0m")
            return
        while True:
            print("""
[관리자 서비스 입니다.]
1. 전체 회원 조회
2. 권한 변경
3. 블랙리스트 처리
4. 뒤로가기""")
            sel = input("선택: ")
            if sel == "1":
                cls.list_members()
            elif sel == "2":
                cls.change_role()
            elif sel == "3":
                cls.block_member()
            elif sel == "4":
                break

    @classmethod
    def list_members(cls):
        print("\n[회원목록]")
        for list in cls.members:
            print(list)
        print(f"전체회원 출력이 완료되었습니다.")

    @classmethod
    def change_modify(cls):
        print("\n[회원정보 수정 서비스]")
        cls.list_members()
        sel = input("\n정보를 수정하려는 회원의 아이디를 입력하세요")
        for list in cls.members:
            if list == sel:
                list.uid = input("변경할 아이디: ")
                list.pw = input("변경할 비밀번호: ")
                list.name = input("변경할 이름: ")
                list.Session.logout()
                cls.save()
            else:
                print("\n\033[31m선택한 회원의 정보가 존재하지 않습니다.\033[0m")

    @classmethod
    def change_role(cls):
        print("회원권한 변경 서비스")
        cls.list_members()
        sel = input("\n권한을 변경하려는 회원의 아이디를 입력하세요")
        for l in cls.members:
            if sel == l.uid:
                print(f"\n선택한 회원의 권한은{l.role}입니다.")
                cn = input("""
변경하려는 권한을 선택하세요
1. user
2. manager
3. admin""")
                if cn == "1":
                    l.role = "user"
                    cls.save()
                    print(f"{l.name}회원의 권한이 {l.role}로 수정되었습니다.")
                elif cn == "2":
                    l.role = "manager"
                    cls.save()
                    print(f"{l.name}회원의 권한이 {l.role}로 수정되었습니다.")
                elif cn == "3":
                    l.role = "admin"
                    cls.save()
                    print(f"{l.name}회원의 권한이 {l.role}로 수정되었습니다.")
                else:
                    print("잘못된 입력입니다.")

    @classmethod
    def block_member(cls):
        print("\n[블랙리스트 처리]")
        cls.list_members()
        sel = input("\n블랙하려는 회원의 아이디를 입력하세요")
        for m in cls.members:
            if sel == m.uid:
                m.active = False
                Session.logout()  #비활성화 처리된 회원의 로그아웃처리
                cls.save()
                print(f"\n\033\31m{m.name}회원의 블랙 처리가 완료되었습니다.\033[0m")

