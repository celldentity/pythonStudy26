# 파이썬에 oop를 적용해보자.
# oop는 객체 지향 프로그래밍, object-oriented Progeamming
# 현실 세계의 '객체' 개념을 기반으로 데이터를 속성(데이터)과 행위(메서드)로 묶어 관리하고,
# 객체 간 상호작용을 통해 프로그램을 설계하는 프로그래밍 패러다임으로
# 코드 재사용, 유지보수 용이성, 가독성 향상 등의 장점이 있으며,
# 캡슐화, 상속, 다형성 드의 핵심 원칙을 가집니다.
from enum import member

# 지금까지는 2차원 배열을 이용해서 인덱스로 데이터에 접근을 하는데,
# [0]이곳에 무엇이 들어있는지 암기를 하고 [4]는 무엇이 들어갈지!???
# 메모장의 1줄로 되어있는 자료를 클래스로 만들면
# Member.name / Menber.id / Member.pw 등으로 접근할 수 있다.

# Member.py는 개인의 객체 - 변수와 게터(나오는값처리)/세터(입력값처리)등을 담당한다.
# Member.py는 CRUD용 메서드들이 들어 있는 모듈
# main.py는 주 실행 코드

from Member import Member
import os

#사용법 member=member() = 객체가 생성됨
        #member.필드/메서드

#외부파일 (모듈 가져와)
# app = MemberManager

# Member 객체를 CRUD 기능을 넣는다.
# 메뉴 구현
# 텍스트파일 처리(파일 읽기, 파일 저장)
# 회원가입, 로그인, 로그아웃, 회원수정, 회원탈퇴

class MemberService:

    def __init__(self, file_name="members.txt"): # 클래스 생성자 근데 생성자는 왜 필요할까?
        self.file_name = file_name
        self.members = [] # 회원들을 리스트로만들어 Member()객체를 담는다.
        self.session = None  #로그인상태를 담당하는 (members의 인덱스 보관용)
        self.load_members()

    def run(self):
        run = True
        while True:
            self.main_menu()
            sel = input(">>>")
            if sel == "1": self.member_add()
            elif sel == "2": self.member_login()
            elif sel == "3": self.member_logout()
            elif sel == "4": self.member_modify()
            elif sel == "5": self.member_delete()
            elif sel == "9": run = False
            else:
                print("잘못 입력하셨습니다.")

    def load_members(self):
        if not os.path.isfile(self.file_name):
            self.save_members()
            return
        self.members = []
        with open(self.file_name, "r", encoding="utf-8") as f:
            for line in f:
                self.members.append(Member.from_line(line))
       # print("\n[현재 members 리스트의 통 데이터 모습]")
    #print(self.members)
        #print(f"리스트의 타입: {type(self.members)}")
        #print(f"리스트의 길이: {len(self.members)}개")



    def save_members(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            for member in self.members:
                f.write(member.to_line())
                #       멤버객체의 매서드를 사용하여 1줄씩 기록하겠다.
                #       멤버리스트의 뒷부분에 추가하겠다.

    def main_menu(self):
        print("""
===== 회원관리 프로그램 (Member 객체 기반) =====
1. 회원가입
2. 로그인
3. 로그아웃
4. 회원정보수정
5. 회원탈퇴
9. 종료
""")

    def member_add(self):
        print("\n[회원가입]")
        uid = input("아이디 : ")
        if self.find_member(uid):
            print("이미 존재하는 아이디")
            return
        pw = input("비밀번호 : ")
        name = input("이름 : ")
        role = "user"

        self.members.append(Member(uid, pw, name, role))
        self.save_members()
        self.load_members()


    def member_login(self):
        print("\n[로그인]")
        uid = input("아이디 : ")
        pw = input("비밀번호 : ")
        member = self.find_member(uid)

        if not member:
            print("존재하지 않는 아이디")
            return
        if not member.active:
            print("비활성화 계정")
        if member.pw == pw:
            self.session = member
            print(f"{member.name}님 로그인 성공({member.role})")
            if member.role == "admin":
                self.member_admin()
        else:
            print("비밀번호 오류")

    def member_logout(self):
        pass

    def member_modify(self):
        pass

    def member_delete(self):
        pass



    def find_member(self, uid):
        for member in self.members:
            # members 리스트에서 1개씩member 객체를 가져와
            if member.id == uid: # 가져온 객체.id와 전달받은 id가 같은지
                print(member.name , "님을 찾았습니다.")
                return member #같은게 있으먄 member 객체를 리턴
        return None

    def member_admin(self):
        subrun = True
        while subrun:
            print("\n[관리자메뉴]")
            print("1. 회원 리스트 조회")
            print("2. 비밀번호 변경")
            print("3. 블랙리스트 처리")
            print("4. 권한 변경")
            print("9. 종료")
            #회원 리스트 조회
            sel = input("선택 : ")
            if sel == "1":
                self.show_member_list()
            #비밀번호 변경
            elif sel == "2":
                uid = input("대상 아이디 : ")
                member = self.find_member(uid)
                if member:
                    member.pw = input("새 비밀번호 : ")
                    self.save_members()
            #블랙리스트 처리
            elif sel == "3":
                uid = input("대상 아이디: ")
                member = self.find_member(uid)
                if member:
                    member.active = False
                    self.save_members()
                    print("블랙리스트 처리 완료")
                else:
                    print("회원 없음")
            #권한변경
            elif sel == "4":
                uid = input("대상 아이디 : ")
                member = self.find_member(uid)
                if member:
                    member.role = input("admin / manager / user : ")
                    self.save_members()
                    print("권한 변경 완료")
    def show_member_list(self):
        # 관리자가 볼수 있는 회원 리스트, 인터넷 진흥원에서 검증을 받는다.
        print("\n[회원목록]")
        print("-" * 60)
        print(f"{'ID':10} {'이름':10} {'권한':10} {'상태':10}")

        for member in self.members: #자바 공부와의 호환성이 좋다. 문법만 조금 틀리지 로직이 같다.
            # members 리스트에 있는 객체를 하나씩 가져와 멤버에 넣음
            status = "활성" if member.active else "비활성"
            print(f"{member.id:10} {member.name:10} {member.role:10} {status}")
        print("-" * 60)

