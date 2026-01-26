import os
# MemberManager
#  ├─ file_name 변수
#  ├─ members
#  ├─ session
#  ├─ load_members() 메서드
#  ├─ save_members()
#  ├─ member_add()
#  ├─ member_login()
#  ├─ member_admin()
#  ├─ member_logout()
#  ├─ member_modify()
#  ├─ member_delete()
#  ├─ main_menu()
#  └─ run()

class MemberManager: # 객체를 담당하는 클래스 사용법은 변수 = MemberManager()
    def __init__(self, file_name="members.txt"):  #객체생성시 만드는 기본값 (생성자) 클래스 만들때는 필수
        self.file_name = file_name  # 객체에 파일이름을 넣는다.
        self.members = []           # 객체에 members 리스트를 만든다.
        self.session = None         # 객체에 세션변수를 만들고 기본값으로 None 처리한다. (정수타입)
        self.load_members()         # 아래에 선언된 load_members()메서드를 호출한다.

    # ===============================
    # 파일 로드
    # ===============================
    def load_members(self): # 앞으로만들 메서드는 ()괄호 안에 self가 필수다
        self.members = []   # 빈배열로 생성 (이전에 리스트가 남아 있을 수 있어서 지우고 생성함)

        if not os.path.exists(self.file_name):    #설정된 디렉토리에 파일명이 없으면
            self.save_members()                   # save_members()메서드를 호출 (open()으로 파일생성)
            return                                # load_members()메서드를 빠져나와라

        with open(self.file_name, "r", encoding="utf-8") as f:
            for line in f:        #읽기전용           #한글처리필수                   ->f라는 변수에 넣어라
                data = line.strip().split("|")
                #1줄 읽은 값을 엔터제거, | 기준으로 잘라서 1차원 리스트로 생성해라.
                #["kkw", "1234", "김기원", "admin", "True"]
                #Ture 값의 쌍 따옴표를 제거한채로 불타입으로 가져와라
                data[4] = True if data[4] == "True" else False
                self.members.append(data) #for문이 종료될 때 까지 멤버스에 값을 추가해라.

    # ===============================
    # 파일 저장
    # ===============================
    def save_members(self): # 2차원 리스트 값을 파일로 덮어쓴다.
        # 왜? 파일처리는 수정기능을 지원하지 않기 때문에 임시리스트은 리스트에 추가만 해서 가지고 있다가 최종적으로 세이브때 파일로 넘어간다.
        with open(self.file_name, "w", encoding="utf-8") as f:
            for m in self.members: # 메모리에 있는 멤버스s 2차원 리스트를 한 줄씩 가져와서
                #m 변수 에 넣어라.
                f.write(f"{m[0]}|{m[1]}|{m[2]}|{m[3]}|{m[4]}\n")

    # ===============================
    # 회원가입
    # ===============================
    def member_add(self): #메서드는 항상 클래스 밖에 작성되어야 한다.
        print("\n[회원가입]")
        uid = input("아이디 : ") # 키보드로 입력한 값을 uid 변수에 넣는다.

        for m in self.members: # 2차원 배열인 멤버스에 1차원 리스트를 가져와 (1줄)
            if m[0] == uid: #프린트로 입력한거랑 m의 0번지랑 같냐
                print("이미 존재하는 아이디입니다.")
                return

        pw = input("비밀번호 : ")
        name = input("이름 : ")

        print("1.admin  2.manager  3.user")
        r = input("권한 선택 : ")

        role = "user"
        if r == "1":
            role = "admin"
        elif r == "2":
            role = "manager"

        self.members.append([uid, pw, name, role, True])
        self.save_members()
        self.load_members()
        print("회원가입 완료")

    # ===============================
    # 로그인
    # ===============================
    def member_login(self):
        print("\n[로그인]")
        uid = input("아이디 : ")
        pw = input("비밀번호 : ")

        for i, m in enumerate(self.members):  # members에 2차원 배열을 반복
            if m[0] == uid:
                if not m[4]:
                    print("비활성화된 계정입니다.")
                    return

                if m[1] == pw:
                    self.session = i
                    print(f"{m[2]}님 로그인 성공 ({m[3]})")

                    if m[3] == "admin":
                        self.member_admin()
                    return
                else:
                    print("비밀번호 오류")
                    return

        print("존재하지 않는 아이디")  # for문에 return이 안걸리면 여기까지 온다.

    # ===============================
    # 관리자 기능
    # ===============================
    def member_admin(self): #로그인시 admin = role 이면 진입
        print("\n[관리자 메뉴]")
        print("1. 비밀번호 변경")
        print("2. 블랙리스트")
        print("3. 권한 변경")
        print("0. 종료")

        sel = input("선택 : ")   # 관리자 메뉴 선택용
        uid = input("대상 아이디 : ") # 대싱 id 찾는 입력

        for m in self.members:
            if m[0] == uid:
                if sel == "1":
                    m[1] = input("새 비밀번호 : ")
                elif sel == "2":
                    m[4] = False
                elif sel == "3":
                    m[3] = input("admin / manager / user : ")

                self.save_members()
                print("관리자 작업 완료")
                return

        print("대상 회원 없음")

    # ===============================
    # 로그아웃
    # ===============================
    def member_logout(self):
        self.session = None # 세션값에 있는 인덱스를 None 처리하면 된다.
        print("로그아웃 완료")

    # ===============================
    # 내정보 수정
    # ===============================
    def member_modify(self): # 현재 세션의 값이 None이면??
        if self.session is None:
            print("로그인 필요")
            return

        print("\n[내 정보 수정]")
        print("1. 이름 변경")
        print("2. 비밀번호 변경")

        sel = input("선택 : ")

        if sel == "1":
            self.members[self.session][2] = input("새 이름 : ")
                # 2차원배열        로그인인덱스          이름
        elif sel == "2":
            self.members[self.session][1] = input("새 비밀번호 : ")
                # 2차월배열         로그인인데긋          이름

        self.save_members()
        self.load_members()
        print("수정 완료")

    # ===============================
    # 회원탈퇴
    # ===============================
    def member_delete(self):
        if self.session is None:
            print("로그인 필요")
            return

        print("\n[회원 탈퇴]")
        print("1. 완전 탈퇴")
        print("2. 계정 비활성화")

        sel = input("선택 : ")

        if sel == "1":
            self.members.pop(self.session)
        elif sel == "2":
            self.members[self.session][4] = False

        self.session = None
        self.save_members()
        self.load_members()
        print("처리 완료")

    # ===============================
    # 메뉴
    # ===============================
    def main_menu(self):
        print("""
==== 회원관리 프로그램 (Class 기반) ====
1. 회원가입
2. 로그인
3. 로그아웃
4. 회원정보수정
5. 회원탈퇴
9. 종료
""")

    # ===============================
    # 실행
    # ===============================
    def run(self):
        while True:
            self.main_menu()
            sel = input(">>> ")

            if sel == "1":
                self.member_add()
            elif sel == "2":
                self.member_login()
            elif sel == "3":
                self.member_logout()
            elif sel == "4":
                self.member_modify()
            elif sel == "5":
                self.member_delete()
            elif sel == "9": break


# ===============================
# 프로그램 시작
# ===============================
app = MemberManager() # 지금까지 만든 클래스를 객체로 만들고
app.run() # 객체에 있는 .run()메서드를 실행한다.
