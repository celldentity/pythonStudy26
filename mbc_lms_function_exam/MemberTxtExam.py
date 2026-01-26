# 회원관리용 더미데이터를 파일(메모장)로 저장하여 관리해보자.
import os
import sys
import time
# import random 회원가입시 고유의 코드를 생성해주기 위함
# import string 회원가입시 고유의 코드를 생성해주기 위함
from datetime import datetime  # 이 줄을 추가하세요

# 회원관리 curd를 사용자 지정 함수로 만들어 보자.
# c : 회원가입
# r : 회원리스트 관리자인경우 회원암호 변경, 블랙리스트로생성, 권한 부여
# r : 로그인 id와 pw를 활용하여 로그인 상태 유지 session
# u : 회원정보 수정
# d : 회원탈퇴, 회원비활성화

# 프로그램에서 사용될 변수들
# 전역변수(global) -> py 파일 안에서 전체적으로 사용되는 변수
# 지역변수(local) -> while, if, for, def안에서 사용되는 변수
run = True # while 에서 전체적으로 사용되는 변수(프로그램 구동)
session = None # 로그인상태 저장용 -> 로그인한 사용자의 리스트 인덱스 기억용
FILE_NAME = "members.txt" # 회원 정보를 저장할 메모장 파일명
FILE_NAME1 = "scores.txt" # 성적 정보를 저장할 메모장 파일명
FILE_NAME2 = "boards.txt" # 게시판 정보를 저장할 메모장 파일명
members = []  # 지금은 비어있지만 좀 있다 메모장에 있는 내용을 가져와 리스트 처리함
scores = []
boards = []

def typewriter(text, speed=0.002):  # 글자가 천천히 타자기처럼 화면에 표시되게끔 만듦
    for char in text:
        sys.stdout.write(char)  # 한 글자씩 출력
        sys.stdout.flush()  # 버퍼를 비워 즉시 화면에 표시
        time.sleep(speed)  # 다음 글자까지 대기 시간 (초 단위)
    print()  # 마지막에 줄바꿈

# #def generate_tag():   #고유값 부여하기
#     # 1. 알파벳 대문자 중 하나를 랜덤으로 선택
#     letter = random.choice(string.ascii_uppercase)
#
#     # 2. 000~999 사이의 숫자를 랜덤으로 생성 (zfill을 사용해 3자리 유지)
#     number = str(random.randint(0, 999)).zfill(3)
#
#     # 3. 두 값을 합쳐서 반환
#     return f"{letter}{number}"

def save_members() : # 메모리상에 리스트를 파일로 저장함!!!
    """
    members 리스트 내용을 members.txt 파일에 저장
    """
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        #     상수     덮어쓰기         한글처리용     파일객체
        #                 a = 추가용
        # 메모리에 있는 리스트를 |로 연결하여 한줄로 저장
        for member in members :
            line = f"{member[0]}|{member[1]}|{member[2]}|{member[3]}|{member[4]}|{member[5]}\n"
            #                kkw|       1234|      김기원|      admin|     True     time
            f.write(line)

def save_scores() :
    """
    scores 리스트 내용을 scores.txt 파일에 저장
    """
    with open(FILE_NAME1, "w", encoding="utf-8") as f:
        for score in scores :
            line = f"{score[0]}|{score[1]}|{score[2]}|{score[3]}|{score[4]}|{score[5]}\n"
            f.write(line)

def save_boards() :
    """
    boards 리스트 내용을 boards.txt 파일에 저장
    """
    with open(FILE_NAME2, "w", encoding="utf-8") as f:
        for board in boards:
            line = f"{board[0]}|{board[1]}|{board[2]}|{board[3]}|{board[4]}|{board[5]}\n"
            f.write(line)

def load_boards() :
    """
    boards.txt 파일을 읽어서 boards 리스트에 저장
    """
    boards.clear()
    # 파일이 없으면 새파일 생성 (암기)
    if not os.path.exists(FILE_NAME2):
        save_boards()
        return
    with open(FILE_NAME2, "r", encoding="utf-8") as f:  #힙 영역에 있는 자료를 스택과 연결하기 위해서 변수에 넣은 거다.
        #    members.txt  읽기전용       한글지원     f라는 변수에 넣어
        for line in f: # f 파일내용을 한줄씩 line 변수에 넣음
            data = line.strip().split("|")
            boards.append(data) #이렇게되면 2차원 배열이 나오고 이걸 가지고 놀거다.

def load_scores() : # 텍스트파일을 전체 불러와 리스트로 만듬!!! 왜?!?!?!?? 중간수정이 안됨
    """
    scores.txt 파일을 읽어서 scores 리스트에 저장
    """
    scores.clear()
    # 파일이 없으면 새파일 생성 (암기)
    if not os.path.exists(FILE_NAME1): # 지금 디렉토리에 FILE_NAME이 없으면!!!
        #  os.path 는 현재 위치 -> os는 내부 라이브러리지만 기본적으로 포함되지 않아 import 해야 함
        save_scores()   # 빈 파일이 members.txt로 생성됨
        return
    with open(FILE_NAME1, "r", encoding="utf-8") as f:  #힙 영역에 있는 자료를 스택과 연결하기 위해서 변수에 넣은 거다.
        #    members.txt  읽기전용       한글지원     f라는 변수에 넣어
        for line in f: # f 파일내용을 한줄씩 line 변수에 넣음
            data = line.strip().split("|")
            scores.append(data) #이렇게되면 2차원 배열이 나오고 이걸 가지고 놀거다.

def load_members():  # 텍스트파일을 전체 불러와 리스트로 만듬!!! 왜?!?!?!?? 중간수정이 안됨
    """
    members.txt 파일을 읽어서 members 리스트에 저장
    """
    members.clear()
    # 파일이 없으면 새파일 생성 (암기)
    if not os.path.exists(FILE_NAME):  # 지금 디렉토리에 FILE_NAME이 없으면!!!
        #  os.path 는 현재 위치 -> os는 내부 라이브러리지만 기본적으로 포함되지 않아 import 해야 함
        save_members()  # 빈 파일이 members.txt로 생성됨
        return

    # 있으면 파일을 열어서 한 줄씩 읽기
    with open(FILE_NAME, "r", encoding="utf-8") as f:  #힙 영역에 있는 자료를 스택과 연결하기 위해서 변수에 넣은 거다.
        #    members.txt  읽기전용       한글지원     f라는 변수에 넣어
        for line in f: # f 파일내용을 한줄씩 line 변수에 넣음
            #print(f"변조전 데이터 : {line}")
            # kkw|1234|김기원|admin|True
            # 줄끝에 엔터 제거, |로 분류된거 리스트로 나눠서 넣음
            data = line.strip().split("|")
            #         맨뒤에 엔터제거
            #                   |를 기준으로 나눔
            # 변조 후 데이터를 확인해보면 모두다~ 문자열로 취급됨
            # 숫자로 들어오는 애들이나 불대수는 전부 원래대로 표현해줘야 한다.
            data[4] = True if data[4] == "True" else False   #패션 코딩이라고 하는데 두 줄로 늘어트려도 맞으나 이렇게도 작동한다.
            # if data[4] == "True":
            #   data[4] = True
            # else:
            #   data[4] = False
            #print(f"변조 후 데이터 : {data}")
            #print("-" * 60)
            # 마지막 members 리스트에 넣는다.
            members.append(data) #이렇게되면 2차원 배열이 나오고 이걸 가지고 놀거다.

# 프로그램에서 사용될 함수들
def member_add():
    global session
    if session is not None:
        print("\n이미 로그인 되어 있습니다.")
    # 회원가입용 함수
    print("member_add 함수로 진입합니다.")
    # 회원가입에 필요한 기능을 넣음
    uid = input("아이디 : ")

    # 아이디 중복검사
    for member in members :
        if member[0] == uid: # {member[0]}|{member[1]}|{member[2]}|{member[3]}|{member[4]|{member[4]
            #                      uid         pw         name        role       active     time
            print("이미 존재하는 아이디 입니다.")
            return # 메인 메뉴로 들어감
    pw = input("비밀번호 : ")
    name = input("이름 : ")
    # 권한 선택
    member_add_menu()
    roleselect = input("권한 선택 : ")
    role = "student" # 잘못 클릭해도 user권한으로 기본값
    if roleselect == "1":
        role = "admin"
    elif roleselect == "2":
        role = "professor"
    # ====== 입력 종료 =======
    print(f"아이디 : {uid}  이름 : {name} ")
    print(f"권한 : {role}    암호 : {pw} ")
    # ====== 입력값 확인

    save_true = input("저장하려면 y를 누르세요 :")
    if save_true == "y" :
        # 저장 시작!!!
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        members.append([uid, pw, name, role, True, now]) # 리스트로 만듬
        save_members() # 리스트를 파일에 저장
        session = len(members) - 1
        print("회원가입완료")
        return

# 회원가입용 함수 종료

def member_login() :
    global session
    # 가입된 회원을 확인하여 로그인 처리 후 session 변수에 인덱스를 넣음
    if session is not None:
        "\n이미 로그인 되어 있습니다."
        return
    uid = input("아이디를 입력하세요 : ")
    for idx, member in enumerate(members) : #이뉴머레이트
        if member[0] == uid: # {member[0]}|{member[1]}|{member[2]}|{member[3]}|{member[4]
            #                        uid        pw          name        role        active
            pw = input("패스워드를 입력하세요 : ")
            if member[1] == pw:
                if member[4] == False :
                    print("\n차단된 회원입니다. 관리자에게 문의하세요.\n메인 메뉴로 돌아갑니다.")
                    return
                else:
                    session = idx
                    return
            else:
                print("\n\033[31m입력한 비밀번호가 맞지 않습니다.\n메인메뉴로 돌아갑니다.\033[0m")
                return
    else:
        print("\n\033[31m입력한 회원정보를 찾을 수 없습니다.\n메인메뉴로 돌아갑니다.\033[0m")
        return

def member_logout():
    global session
    if session is None:
        print("\n아직 로그인되지 않았습니다.")
        return
    elif input("\n\033[31m로그아웃 하시려면 'Enter'키를\n취소하시려면 다른 키를 누르세요\033[0m") == "":
        save_scores()
        save_members()
        session = None
    else:
        print("\n\033[32m로그아웃이 취소되었습니다.\033[0m")
    return

def member_modify():
    global session
    old_time = members[session][5]
    pw = input(f"\n{members[session][2]}님 회원정보 수정을 위해 패스워드를 입력하세요")
    if members[session][1] == pw:
        id = input("변경하려는 ID를 입력하세요")
        pw = input("변경하려는 pw를 입력하세요")
        name = input("변경하려는 이름을 입력하세요")
        member_add_menu()
        roleSelect = input("권한 선택 : ")
        role = "student"  # 잘못 클릭해도 user권한으로 기본값
        if roleSelect == "1":
            role = "admin"
        elif roleSelect == "2":
            role = "professor"
        # ====== 입력 종료 =======
        print(f"아이디 : {id}  이름 : {name} ")
        print(f"권한 : {role}    암호 : {pw} ")
        # ====== 입력값 확인
        save_True = input("\n변경할 정보를 저장하려면 y를 누르세요 :")
        if save_True == "y":
            # 저장 시작!!!
            members[session] = [id, pw, name, role, True, old_time]  # 리스트로 만듬
            save_members()  # 리스트를 파일에 저장
            print("회원정보 수정 완료!")
        else:
            print("회원정보 수정을 취소합니다.")
    else:
        print("\n비밀번호가 틀렸습니다.")

def admin_modify():
    global session
    member_list()
    old_time = members[session][5]
    try:
        ddx = int(input("\n회원수정 메뉴에 진입합니다.\n수정 하려는 회원 번호를 입력하세요: "))
        idx = ddx - 1  # 리스트 인덱스로 변환

        # 1. 입력한 번호가 유효한지 확인 (0보다 크고 전체 개수보다 작아야 함)
        if 0 <= idx < len(members):
            target_member = members[idx]
            if input(f"\n선택한 회원의 정보는\n{target_member}입니다.\n수정하시려면 'Enter'키를 누르세요.") == "":
                id = input("변경하려는 ID를 입력하세요")
                pw = input("변경하려는 pw를 입력하세요")
                name = input("변경하려는 이름을 입력하세요")
                member_add_menu()
                roleSelect = input("권한 선택 : ")
                role = "student"  # 잘못 클릭해도 user권한으로 기본값
                if roleSelect == "1":
                    role = "admin"
                elif roleSelect == "2":
                    role = "professor"
                # ====== 입력 종료 =======
                print(f"아이디 : {id}  이름 : {name} ")
                print(f"권한 : {role}    암호 : {pw} ")
                # ====== 입력값 확인
                save_True = input("\n변경할 정보를 저장하려면 y를 누르세요 :")
                if save_True == "y":
                    # 저장 시작!!!
                    members[session] = [id, pw, name, role, True, old_time]  # 리스트로 만듬
                    save_members()  # 리스트를 파일에 저장
                    print("\n수정이 완료되었습니다.")
                else:
                    print("회원정보 수정을 취소합니다.")
        else:
            # 리스트 범위를 벗어난 번호를 입력했을 때 한 번만 출력
            print("\n입력한 번호에 해당하는 사용자를 찾을 수 없습니다.")
    except ValueError:
        print("\n숫자만 입력 가능합니다.")

def member_delete():
    global session
    print("\n회원탈퇴 메뉴로 진입합니다.")
    if input(f"\n{members[session][2]}님\n\033[31m본인의 계정을 진짜로 삭제하려면 'Enter'키를\033[0m\n아니면 다른키를 눌러주세요.") == "":
        members.pop(session)
        print("\n\033[32m회원탈퇴가 완료되었습니다. 다음에 또 만나길 바래요.\033[0m")
        save_members()
        session = None
    else:
        print("\n회원탈퇴를 취소합니다.")

def admin_delete():
    global session
    member_list()
    try:
        ddx = int(input("\n회원탈퇴 메뉴에 진입합니다.\n탈퇴처리 하려는 회원 번호를 입력하세요: "))
        idx = ddx - 1  # 리스트 인덱스로 변환
        # 1. 입력한 번호가 유효한지 확인 (0보다 크고 전체 개수보다 작아야 함)
        if 0 <= idx < len(members):
            target_member = members[idx]
            # 본인 삭제 방지
            if idx == session:
                print("\n[경고] 본인 계정은 삭제할 수 없습니다.")
                return
            if input(f"\n선택한 회원의 정보는\n{target_member}입니다.\n삭제하시려면 'Enter'키를 누르세요.") == "":
                members.pop(idx)
                save_members()
                print("\n삭제가 완료되었습니다.")
            else:
                print("\n회원삭제를 취소합니다.")
        else:
            # 리스트 범위를 벗어난 번호를 입력했을 때 한 번만 출력
            print("\n입력한 번호에 해당하는 사용자를 찾을 수 없습니다.")
    except ValueError:
        print("\n숫자만 입력 가능합니다.")

def admin_blacklist():
    global session
    member_list()
    try:
        ddx = int(input("\nPNG메뉴에 진입합니다.\n관리 하려는 회원 번호를 입력하세요: "))
        idx = ddx - 1  # 리스트 인덱스로 변환
        # 1. 입력한 번호가 유효한지 확인 (0보다 크고 전체 개수보다 작아야 함)
        if 0 <= idx < len(members):
            target_member = members[idx]
            # 본인 삭제 방지
            if idx == session:
                print("\n[경고] 본인 계정은 차단&해제 할 수 없습니다.")
                return
            if input(f"\n선택한 회원의 정보는\n{target_member}입니다.\n차단&해제 하려면 'Enter'키를 누르세요.") == "":
                members[idx][4] = not members[idx][4] #불리언 방식의 값을 토글시킨다. 차단이면 해제, 해제면 차단
                save_members()
                print("\n변경이 완료되었습니다.")
            else:
                print("\n회원차단을 취소합니다.")
        else:
            # 리스트 범위를 벗어난 번호를 입력했을 때 한 번만 출력
            print("\n입력한 번호에 해당하는 사용자를 찾을 수 없습니다.")
    except ValueError:
        print("\n숫자만 입력 가능합니다.")

def member_list():
    global session
    print("\n전체 회원 리스트를 출력합니다.")
    for idx, member in enumerate(members) :
        typewriter(f"{idx + 1}번 유저 아이디 : {member[0]} 패스워드 : {member[1]} 이름 : {member[2]} 권한 : {member[3]} 액티브 : {member[4]} 시간 : {member[5]}")
    print("회원 출력이 완료되었습니다.")

def score_input():
    global session
    if members[session][3] == "student":
        print("\n성적 입력 권한이 없습니다. 권한을 확인하세요.")
        return #권한이 없으면 돌아가는 로직

    print("\n성적 입력 메뉴에 진입하셨습니다.")
    member_list()
    sid = input("\n성적을 입력하려는 학생의 아이디를 입력하세요.") #그 외에 교수나 관리자의 경우는 여기서 수정하는 학생의 아이디를 입력받음

    target_student = None #함수 안에서 변수 선언의 경우if문이 끝나도 원하는 답을 찾지 못할시 오류가 나는 걸 방지해준다.
    for s in members:
        if s[0] == sid and s[3] == "student": #입력받은 학생이 등록된 학생이고 신분도 학생인지 재차 확인
            target_student = s                #위에는 로그인 한 사람의 권한을 묻는거고 아래는 바꾸려는 사람의 권한을 물음
# 멤버스 리스트를 한줄씩 뽑아와서 s에 넣고
# s의 0번 칸이 sid와 같고, s의 3번 칸이 스튜던트와 같으면
# 타겟 스튜던트는 s행 전체를 가져온다.

    if not target_student:
        print("\n\033[31m해당 아이디의 학생을 찾을 수 없습니다.\033[0m") #수정하려는 사람이 학생이 아니면 돌아감
        return

    existing_score_idx = -1        #여기서부터 살짝 고급기술인데, 이뉴머레이트에서 인덱스 값이 없는 경우를 대비해서
    for i, s in enumerate(scores):      #미리 -1값을 넣어두는 기술이다. 만약
        if s[0] == target_student[0]:
            existing_score_idx = i
            break
    if existing_score_idx != -1:
        print(f"\n[알림] {target_student[0]} 학생은 이미 성적이 등록되어 있습니다. 수정을 진행합니다.")
    while True:
        try:
            pys = int(input("파이썬 점수 (0~100): "))
            frs = int(input("프론트 점수 (0~100): "))
            www = int(input("웹 점수 (0~100): "))

            if all(0 <= s <= 100 for s in [pys, frs, www]): #if 와 for를 같이 쓰면서 모든 조건이 참이어야 트루를 반환
                total = pys + frs + www     #세 변수 값을 전부 조건식에 대입해서 셋다 트루면 트루 반환, 거짓이면 False반환
                avg = total / 3

                # 학점 계산
                if avg >= 90:
                    grade = "A"
                elif avg >= 80:
                    grade = "B"
                elif avg >= 70:
                    grade = "C"
                elif avg >= 60:
                    grade = "D"
                else:
                    grade = "F"

                new_data = [target_student[0], pys, frs, www, total, grade]

                if existing_score_idx != -1:
                    # 기존 데이터 교체 (수정)
                    scores[existing_score_idx] = new_data
                    print(f"\n[수정 완료] {target_student[0]} 학생의 성적이 업데이트되었습니다.")
                    return
                else:
                    # 새 데이터 추가 (입력)
                    scores.append(new_data)
                    print(f"\n[입력 완료] {target_student[0]} 학생의 성적이 새로 등록되었습니다.")
                    return

                save_scores()
                break  # 입력 성공시 while 루프 탈출
            else:
                print("⚠️ 점수는 0~100 사이여야 합니다.")
        except ValueError:
            print("⚠️ 숫자만 입력해주세요.")

def score_list():  #학생이 접속하면 본인의 성적만 보여주고, 관리자나 교수가 들어오면 입력된 학생의 성적을 리스트로 보여준다.
    global session
    if members[session][3] == "student":
        print("\n개인 성적조회 메뉴에 진입했습니다.")
        pos = members[session][0]
        for idx, who in enumerate(scores):
            if who[0] == pos:
                stuscore = who
                print(f"\033[35m{members[session][2]} 학생의 점수는\n파이썬 : {stuscore[1]}\n프론트 : {stuscore[2]}\n웹 : {stuscore[3]}\n등급 : {stuscore[5]}\n입니다.\033[0m")
                return
        else:
            print("\n\033[31m교수님이 점수를 입력하기 전 입니다.\n교수님께 관심의 독촉전화를 드려보세요.\033[0m")
            return
    else:
        print("\n전체 성적조회 메뉴에 진입했습니다.\n전체 회원과 입력된 학생의 성적 리스트를 표시합니다.")
        member_list()
        for pos in scores:
            typewriter(f"\n\033[35m이름 : {pos[0]}\n파이썬 : {pos[1]}\n프론트 : {pos[2]}\n웹 : {pos[3]}\n등급 : {pos[5]}\n==========\033[0m")
    return

def board_write():
    global session
    print(f"{members[session][2]}님 안녕하세요\n새글 작성을 진행합니다.")
    title = input("제목을 입력해주세요.")
    content = input("내용을 입력해주세요")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if input("\n내용을 저장하시겠습니까? 저장하시려면 'Enter'키를,\n아니면 다른키를 눌러주세요.") == "":
        boards.append([members[session][0], title, content, now, 0, 0])
        save_boards()
        return
    else:
        print("\n게시글 작성을 취소합니다.")
        return

def board_list():
    print("\n전체 게시글을 조회합니다.")
    for idx, l in enumerate(boards):
        typewriter(f"""
번호: {idx + 1}
\033[32m작성자: {l[0]} | 제목: {l[1]:.10}
내용: {l[2]:.10}
조회수: {boards[idx][4]} | 좋아요: {boards[idx][5]}
작성시간: {l[3]}\033[0m
=================================================""")
    print("전체 게시글 조회가 완료되었습니다.")

def board_view():
    global session
    print("\n게시글 자세히 보기 및 수정 메뉴에 진입했습니다.")
    board_list()
    sn = int(input("\n자세히 보거나 수정하려는 \033[35m게시글 번호\033[0m를 선택해 주세요.")) - 1
    print(int(len(boards)))
    if 0 <= sn < int(len(boards)): #랭스 함수는 보드리스트 안에 1차원 배열이 몇 개가 있는지 확인한다.
        view = boards[sn]          #이미 sn값에 -1을 했기 때문에 마지막 값은 작거나 같다가 아닌 작다만 가능
        view_board = int(view[4]) + 1
        boards[sn][4] = view_board
        print(f"""
        번호: {sn + 1}\033[32m
        작성자: {view[0]} | 제목: {view[1]}
        내용: {view[2]}
        작성시간: {view[3]}
        조회수: {int(view[4])} | ♥: {view[5]}\033[0m""")
        select =  input("\n\033[32m좋아요를 표현하려면 'Enter'키를\033[0m,\n\033[33m게시글을 수정하려면 'y'키를\033[0m\n이전 메뉴로 복귀하려면 다른키를 누르세요.")
        if select == "":
            print("\033[34m♥+1 완료\033[0m")
            view_like = int(view[5]) + 1
            boards[sn][5] = view_like
            return
        elif select == "y":
            while True:
                if members[session][0] == view[0]:
                    print("\n게시물을 수정합니다.")
                    title = input("제목을 입력해주세요.")
                    content = input("내용을 입력해주세요")
                    if input("\n내용을 저장하시겠습니까? 저장하시려면 'Enter'키를,\n아니면 다른키를 눌러주세요.") == "":
                        boards[sn][1] = title
                        boards[sn][2] = content
                        print("게시물 수정이 완료되었습니다.")
                        return
                    else:
                        print("\n게시물 수정을 취소합니다.")
                        return
                else:
                    print("\n\033[31m본인이 작성한 게시글만 수정할 수 있습니다.\033[0m")
                    return
        else:
            print("\n이전 메뉴로 돌아갑니다.")
            return
    else:
        print("\n\033[31m선택한 번호의 게시물이 없습니다. 번호를 확인해주세요.\033[0m")
        return

def save_quit():
    save_members()
    save_boards()
    save_scores()
    return



# --------------------- 기능에 대한 함수 생성 끝----------------
def member_add_menu() : # 회원가입에서 사용할 메뉴
    print(f"""
    --------- 회원권한을 확인하세요.---------
    1. 관리자       2. 교수님        3. 학생 
    """)

def main_menu():
    print(f"""
    ==== 엠비씨아카데미 LMS 프로그램입니다======
    1. 회원가입     2. 로그인       3. 프로그램 종료
    """)

def loged_menu():
    global session
    typewriter(f"""
    ==== 엠비씨아카데미 LMS 프로그램입니다======
    1. 개인정보수정   2. 회원탈퇴    3. 로그아웃
    4. \033[31m성적관리메뉴\033[0m
    5. \033[32m회원게시판\033[0m
    9. 프로그램종료
    """, 0.002)
    print(f"\n{members[session][2]}님 {members[session][3]}권한으로 접속하셨습니다.")

def admin_menu():
    global session
    typewriter(f"""
        =================관리자 메뉴입니다.=================
        1. 전체회원보기     2. 회원탈퇴         3. PNG
        4. 회원정보수정    5. 로그아웃    6. \033[31m성적관리메뉴\033[0m
        7. \033[32m회원 게시판\033[0m    9. 프로그램종료
        """)
    print(f"\n{members[session][2]}님 {members[session][3]}권한으로 접속하셨습니다.")

def score_menu():
    global run, session
    while True:
        print(f"""
        ========== 성적 관리 메뉴입니다. ==========
        1. 성적입력&수정
        2. 성적조회(교수는 전체 학생은 개인)         
        3. 이전메뉴 
        4. 로그아웃
        9. 프로그램 종료
        """)
        select = input("\n이용하려는 게시판을 선택하세요")
        if select == "1":
            score_input()
        elif select == "2":
            score_list()
        elif select == "3":
            return
        elif select == "4":
            session = None
            return
        elif select == "9":
            save_quit()
            run = False
        else:
            print("\n\033[31m이용하시려는 게시판 번호를 정확히 입력하세요.\n관리자 메뉴로 돌아갑니다.\033[0m")

def board_menu():
    global session, run
    while True: #이전메뉴를 누르기 전까지는 회원게시판에 계속 머무르도록
        print("""
        ===========회원 게시판에 접속하셨습니다.===========
        \033[35m1. 새글 작성하기         2. 게시글 전체보기
        3. 게시글 조회 및 수정하기\033[0m
        4. 이전 메뉴            5. 로그아웃
        9. 프로그램 종료
        """)
        select = input("\n이용하려는 게시판을 선택하세요")

        if select == "1":
            board_write()
        elif select == "2":
            board_list()
        elif select == "3":
            board_view()
        elif select == "4":
            return
        elif select == "5":
            session = None
            return
        elif select == "9":
            save_quit()
            run = False
        else:
            print("\n\033[31m이용하시려는 게시판 번호를 정확히 입력하세요.\033[0m")

# ------------------ 메뉴 함수 끝 ------------------

# 프로그램 시작!!!!
load_members()  # 프로그램 시작시 파일을 불러오기!!!
load_scores()
load_boards()
print(scores)
while run : # 메인 프로그램 실행 코드
    print("\n" + "=" * 40)
    if not members:
        print(" 현재 가입된 회원이 없습니다.")
    else:
        print(" [현재 가입된 회원 요약 리스트]")
        for m in members:
            # m[0]은 아이디, m[2]는 이름입니다.
            print(f"\033[34m ID: {m[0]} ({m[2]}) ({m[3]}) ({m[5]})\033[0m", end="\n")
        print()  # 줄바꿈
    print("=" * 40)
    # --------------------------
    if session is None:
        main_menu() # 위에서 만든 메인 메뉴함수를 실행
        print("\n\033[32m아직 로그인 되지 않았습니다. 다른 메뉴를 이용하시려면 로그인하세요.\033[0m")
        select = input("\n진입하시려는 메뉴를 선택하세요.") # 키보드로 메뉴 선택
        if select == "1" : member_add()   # 회원가입용 함수 호출
        elif select == "2" : member_login() # 로그인용 함수 호출
        elif select == "3" :
            save_quit()
            run = False
    else:
        user_role = members[session][3]
        if user_role == "admin":
            admin_menu()
            select = input("\n진입하시려는 메뉴를 선택하세요.")
            if select == "1":
                member_list()
            elif select == "2":
                admin_delete()
            elif select == "3":
                admin_blacklist()
            elif select == "4":
                admin_modify()
            elif select == "5":
                member_logout()
            elif select == "6":
                score_menu()
            elif select == "7":
                board_menu()
            elif select == "9":
                save_quit()
                run = False
            else:
                print("\n메뉴를 똑바로 선택하세요.")
        else:
            loged_menu()
            select = input("\n진입하시려는 번호를 선택하세요.")
            if select == "1":
                member_modify()
            elif select == "2":
                member_delete()
            elif select == "3":
                member_logout()
            elif select == "4":
                score_menu()
            elif select == "5":
                board_menu()
            elif select == "9":
                save_quit()
                run = False
            else:
                print("\n\033[31m메뉴를 똑바로 선택하세요.\033[0m")
# while문 종료

# 변수를 추가하려면 save, load, modify 를 자세히 봐야 한다.