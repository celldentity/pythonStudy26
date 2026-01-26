import os
from Member import *

class MemberService:
    def __init__(self, file_name="members.txt"):
        self.file_name = file_name
        self.members = []
        self.session = None
        self.load_members()

    def run(self):
        run = True
        while run:
            self.basic_menu()
            sel=input("\n이용하시려는 메뉴를 선택하세요")
            if sel == "1": self.member_add()
            elif sel == "2": self.member_login()
            elif sel == "9": run = False

    def load_members(self):
        if not os.path.exists(self.file_name):
            self.save_members()
            return
        self.members = []
        with(open(self.file_name, "r", encoding="utf-8")) as 로우파일:
            for line in 로우파일:
                self.members.append(Member.from_line(line))

    def save_members(self):
        with open(self.file_name, "w", encoding="utf-8") as 로우파일:
            for member in self.members:
                로우파일.write(member.to_line())  #여기서는 라인값을 전해주는 게 아니기 때문에 괄호가 비워진다.

    def find_member(self, uid):
        for member in self.members:
            if member.id == uid:
                return member
        return None

    def basic_menu(self):
        print("="*40)
        print("""[멤버메뉴]
1. 회원가입
2. 로그인
9. 프로그램종료""")
        print("="*40)

    def member_add(self):
        print("\n[계정생성]")
        uid = input("아이디를 입력하세요 : ")
        pw = input("비밀번호를 입력하세요 : ")
        if self.find_member(uid):
            print("이미 가입된 계정입니다.")
            return
        name = input("이름을 입력하세요 : ")
        role = "user"
        active = True      #아래는 사실 멤버스에 어팬드할건데, 멤버라는 클래스를 어팬드할거고 그 멤버 클래스에 필요한 인수는(1, 2, 3, 4, 5 이렇다)라고 지정해준 것일뿐 데이터를 넣는 순서는 시스템에서 정해진게없다.
        self.members.append(Member(uid, pw, name, role, active)) #여기서 클래스로 던져줘야 하나로 인식해서 뭉텡이가 들어간다.
        # 그러면서도 각 클래스의 어느 부분에 해당하는지 찾기도 편해진다.
        self.save_members()
        self.load_members()

    def member_login(self):
        print("\n[로그인]")
        uid = input("아이디를 입력하세요 : ")
        pw = input("패스워드를 입력하세요") #비밀번호까지 받고나서 대답해주면 보다 간단해진다.
        member = self.find_member(uid)  #이 비교를 통해서 멤버스에 있는 객체들을 하나씩 잡아 꺼내서 맞는 걸 멤버에 붙들어 놓을 수 있다. 여기서 리턴 멤버로 리턴값을 통째로 준다.
        if not member:
            print("\n가입된 아이디가 없습니다.")
            return
        if not member.active:
            print("\n차단된 아이디입니다. 관리자에게 문의하세요")
            return
        if member.pw == pw:
            self.session = member
            print(f"{member.name}님\n로그인이 완료되었습니다.{member.role}")
            self.loged_menu()
            self.loged_run()

    def loged_menu(self):
        print("""\n[회원메뉴]
1. 회원정보 수정
2. 회원탈퇴
3. 관리자메뉴
4. 로그아웃
9. 프로그램종료
        """)

    def loged_run(self):
        subrun = True
        while subrun:
            subsel = input("이용하시려는 메뉴를 선택하세요")
            if subsel == "1": self.member_modify()
            elif subsel == "2": self.member_delete()
            elif subsel == "3": self.admin_menu()
            elif subsel == "4":
                self.session = None
                subrun = False
                print("\n로그아웃 되었습니다. 기본메뉴로 돌아갑니다.")
            elif subsel == "9":
                print("\n프로그램이 종료되었습니다.")
                run = False
                exit()

    def member_modify(self):
       print("\n회원정보 수정 메뉴에 진입했습니다.")
       print(f"""
이름 : {self.session.name}
아이디 : {self.session.id}
비밀번호 : {self.session.pw}
권한 : {self.session.role}""")
       sn = input("""
\n변경하시려는 정보를 선택하세요.
1. 이름
2. 아이디
3. 비밀번호
4. 권한
5. 정보변경 취소
""")
       if sn == "1":
           name = input("\n변경할 이름을 입력하세요")
           self.session.name = name
           self.save_members()
           self.load_members()
           print(name)
           print("\n이름 변경이 완료되었습니다.")
        elif sn == "2":
            uid = input("\n변경할 아이디를 입력하세요")
            self.session.uid = uid
            self.save_members()
            self.load_members()
            print(uid)
            print("\n아이디 변경이 완료되었습니다.")
        elif sn == "3":
            pw = input("\n변경할 비밀번호를 입력하세요")
            self.session.pw = pw
            self.save_members()
            self.load_members()
            print(pw)
            print("\n비밀번호 변경이 완료되었습니다.")
        elif sn == "4":
            rolen = input("""
\n변경할 권한을 선택하세요"
1. 일반유저
2. 교수
3. 관리자""")
            if rolen == "1":
                self.session.role = "user"


        elif sn == "9": return
       else:
           print("\n 올바른 번호를 입력하세요")
