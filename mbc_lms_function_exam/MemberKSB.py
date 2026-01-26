import time  # 타입라이터 함수에서 사용하기 위해
import sys

run = True
session = None

ids = ["kkw", "ksb", "wow", "sad"]  # 로그인 아이디 들
pws = ["1234", "5678", "8888", "0000"]  # 암호 둘
names = ["김기원", "김수빈", "개깜놀", "김탈퇴"]  # 사용자 명
roles = ["admin", "manager", "user", "user"]  # 사용자 권한 (admin, manager, user)
active = [True, True, True, False]  # 회원사용중, 탈퇴, 중지, 블랙리스트 등...
# addTime = [0, 0, 0, 0] 마지막 로그아웃 시점을 기준으로 특정 시간이 지나면 자동으로 active에서 False되는 로직 구현중
roletype = {
    "1": "관리자",
    "2": "매니저",
    "3": "일반유저"}  # 딕셔너리를 만들어서 회원가입시 바로 호출

# -------------------------------------------------------------------------------------------
def typewriter(text, speed=0.009):  # 글자가 천천히 타자기처럼 화면에 표시되게끔 만듦
    for char in text:
        sys.stdout.write(char)  # 한 글자씩 출력
        sys.stdout.flush()  # 버퍼를 비워 즉시 화면에 표시
        time.sleep(speed)  # 다음 글자까지 대기 시간 (초 단위)
    print()  # 마지막에 줄바꿈

def session_state():  # 로그인 된 상태에서는 접속하지 못하는 로직을 만들 때 반복적으로 사용
    global session
    if session is not None:
        # is not None 싱글톤이라는 객체가 있는지 비교하는 용
        # if session != None -> 자료형 비교를 위한 표현
        print("\n\033[32m이미 로그인 한 상태입니다.\033[0m")
        print(f"로그인한 사용자는 {names[session]}님 입니다.")
        return

def not_login():  # 로그인 이 안 된 상태에서는 접속하지 못하는 로직을 만들 때 반복적으로 사용
    global session
    if session is None:
        print("\n\033[31m로그인이 되어있지 않습니다.\033[0m")
        return True
    else:
        return False

def member_list():
    global session
    for i in range(len(ids)):
        print(f"순서 : {i + 1} | 아이디 : {ids[i]} | 이름 : {names[i]} | 권한 : {roles[i]} | 활성화 : {active[i]}")
    typewriter("\n\033[32m회원 리스트 출력이 완료되었습니다.\033[0m")

def member_add():
    global session
    if session is not None:
        session_state()
        return
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
            if role.isdigit():  # 입력한 데이터가 숫자가 맞는지 확인 후 맞으면 아래 1,2,3으로 분기
                roleNum = int(role)
                if roleNum == 1:
                    while True:
                        adPass = input("\n관리자 계정을 선택하셨습니다. 관리자 비밀번호를 입력하세요.")
                        if adPass == "1004":
                            print("\033[32m관리자로 계정을 생성합니다.\033[0m")
                            roles.append("admin")  # 계정 권한은 여기에서 바로 추가
                            break
                        else:
                            print("\n비밀번호가 틀렸습니다. 관리자에게 문의하세요.")
                    break
                elif roleNum == 2:
                    print("\033[32m매니저로 계정을 생성합니다.\033[0m")
                    roles.append("manager")  # 계정 권한은 여기에서 바로 추가
                    break
                elif roleNum == 3:
                    print("\033[32m일반사용자로 계정을 생성합니다.\033[0m")
                    roles.append("user")  # 계정 권한은 여기에서 바로 추가
                    break
                else:
                    print("\n\033[31m오류: 1~3숫자만 입력 가능합니다.\033[0m")
            else:
                print("\n\033[31m오류: 1~3숫자만 입력 가능합니다.\033[0m")
        name = input("\n이름을 입력하세요")
        if input(
                f"\n입력된 정보를 확인하세요. \n아이디 : {id}\n패스워드 : {pw}\n이름 : {name}\n계정권한 : {roletype[str(roleNum)]}\n\033[33m저장하시려면 'Enter'키를\033[0m, 취소하려면 다른키를 누르세요") == "":
            names.append(name)
            pws.append(pw)
            ids.append(id)
            active.append(True)
            typewriter("\033[32m회원가입이 완료되었습니다.\033[0m")
            idx = ids.index(id)  # 회원가입 즉시 로그인이 되도록 만듦(시스템상 바로 윗줄에서 만들어진 데이터라 인간 개입 여지가 없음)
            session = idx
            return

def member_login():  # 가입된 회원을 확인하여 로그인 처리 후 session 변수에 인덱스를 넣음
    typewriter("로그인 메뉴로 진입합니다.")
    global session
    if session is not None:
        session_state()
        return
    else:
        user_id = input("로그인 ID")
        user_pw = input("비밀번호")
        if user_id in ids:
            idx = ids.index(user_id)
            if active[idx] == False:
                print("\n\033[31m비활성화/차단된 계정입니다.\033[0m")
                return
            else:
                if user_pw == pws[idx]:
                    session = idx
                    typewriter("\n로그인이 완료되었습니다.", 0.05)
                else:
                    print("\n\033[31m비밀번호가 다릅니다.\033[0m")
        else:
            print("\n\033[31m입력한 회원정보가 존재하지 않습니다.\033[0m")

def member_modify():
    global session
    typewriter("\n회원정보 수정 메뉴로 진입합니다.")
    if not_login():
        return
    elif not_login() == False:
        typewriter(f"\n변경 전 이름 :{names[session]}")
        name = input("변경하려는 이름을 입력하세요. :")
        typewriter(f"변경 전 패스워드 : {pws[session]}")
        pw = input("변경하려는 패스워드를 입력하세요.:")
        typewriter(f"변경 전 아이디 : {ids[session]}")
        id = input("변경하려는 ID를 입력하세요")
        typewriter(f"변경 전 계정 권한 : {roles[session]}")
        print(roletype)
        while True:
            role = input("변경하시려는 권한을 선택하세요.")
            if role.isdigit():  # 입력한 데이터가 숫자가 맞는지 확인 후 맞으면 아래 1,2,3으로 분기
                roleNum = int(role)
                if roleNum == 1:
                    while True:
                        adPass = input("\n관리자 계정을 선택하셨습니다. 관리자 비밀번호를 입력하세요.")
                        if adPass == "1004":
                            print("\033[32m관리자로 계정을 변경합니다.\033[0m")
                            roles[session] = "admin"  # 계정 권한은 여기에서 바로 추가
                            break
                        else:
                            print("\n비밀번호가 틀렸습니다. 관리자에게 문의하세요.")
                    break
                elif roleNum == 2:
                    print("\033[32m매니저로 계정을 변경합니다.\033[0m")
                    roles[session] = "manager"  # 계정 권한은 여기에서 바로 추가
                    break
                elif roleNum == 3:
                    print("\033[32m일반사용자로 계정을 변경합니다.\033[0m")
                    roles[session] = "user"  # 계정 권한은 여기에서 바로 추가
                    break
                else:
                    print("\n\033[31m오류: 1~3숫자만 입력 가능합니다.\033[0m")
            else:
                print("\n\033[31m오류: 1~3숫자만 입력 가능합니다.\033[0m")
        names[session] = name
        ids[session] = id
        pws[session] = pw
        typewriter(f"""
아이디 : {ids[session]}
이름 : {names[session]}
비밀번호 : {pws[session]}
계정권한 : {roles[session]}
으로 변경 완료되었습니다. 수정사항이 있을경우 다시 변경해 주세요.""")
        return

def member_admin():
    global session
    if not_login():
        return
    elif session is not None:
        if roles[session] == "admin":
            admin_menu()
            subSelect = input("\n이용하시려는 메뉴를 선택하세요.")
            if subSelect == "1":
                print("\n전체 회원 목록을 조회합니다.")
                member_login()
                member_list()
                member_admin()
            elif subSelect == "2":
                member_list()
                mn = int(input("\n정보를 변경하려면 회원 번호를 입력하세요")) - 1
                if 0 <= int(mn) <= len(ids):
                    typewriter(f"\n변경 전 이름 :{names[mn]}")
                    name = input("변경하려는 이름을 입력하세요. :")
                    typewriter(f"변경 전 패스워드 : {pws[mn]}")
                    pw = input("변경하려는 패스워드를 입력하세요.:")
                    typewriter(f"변경 전 아이디 : {ids[mn]}")
                    id = input("변경하려는 ID를 입력하세요")
                    typewriter(f"변경 전 계정 권한 : {roles[mn]}")
                    print(roletype)
                    while True:
                        role = input("변경하시려는 권한을 선택하세요.")
                        if role.isdigit():  # 입력한 데이터가 숫자가 맞는지 확인 후 맞으면 아래 1,2,3으로 분기
                            roleNum = int(role)
                            if roleNum == 1:
                                while True:
                                    adPass = input("\n관리자 계정을 선택하셨습니다. 관리자 비밀번호를 입력하세요.")
                                    if adPass == "1004":
                                        print("\033[32m관리자로 계정을 변경합니다.\033[0m")
                                        roles[mn] = "admin"  # 계정 권한은 여기에서 바로 추가
                                        break
                                    else:
                                        print("\n비밀번호가 틀렸습니다. 관리자에게 문의하세요.")
                                break
                            elif roleNum == 2:
                                print("\033[32m매니저로 계정을 변경합니다.\033[0m")
                                roles[mn] = "manager"  # 계정 권한은 여기에서 바로 추가
                                break
                            elif roleNum == 3:
                                print("\033[32m일반사용자로 계정을 변경합니다.\033[0m")
                                roles[mn] = "user"  # 계정 권한은 여기에서 바로 추가
                                break
                            else:
                                print("\n\033[31m오류: 1~3숫자만 입력 가능합니다.\033[0m")
                        else:
                            print("\n\033[31m오류: 1~3숫자만 입력 가능합니다.\033[0m")
                else:
                    print("\n\033[31m입력한 회원정보를 찾을 수 없습니다.\033[0m")
                names[mn] = name
                ids[mn] = id
                pws[mn] = pw
                typewriter(f"""
아이디 : {ids[mn]}
이름 : {names[mn]}
비밀번호 : {pws[mn]}
계정권한 : {roles[mn]}
으로 변경 완료되었습니다. 수정사항이 있을경우 다시 변경해 주세요.""")
                member_admin()
            elif subSelect == "3":
                member_list()
                mn = int(input("\n블랙리스트 처리하려는 회원 번호를 입력하세요")) - 1
                if 0 <= int(mn) <= len(ids):
                    idx = mn
                    if input (f"\n{names[mn]}님을 서버에서 차단(혹은 해제)하시려면 'Enter'키를\n취소하시려면 다른 키를 눌러주세요.") == "":
                        active[idx] = not active[idx] #토글기능
                        if ids[session] == ids[mn]:
                            session = None
                        print("\n차단처리(혹은 해제)가 완료되었습니다.")
                    else:
                        print("\n\033[31m차단 처리를 취소합니다.\033[0m")
                else:
                    print("\n\033[31m입력한 회원정보를 찾을 수 없습니다.\033[0m")
                member_admin()
            elif subSelect == "9":
                print("\n\033[31m메인메뉴로 돌아갑니다.\033[0m")
                return
            else:
                print("\n\033[31m잘못된 입력입니다. 메인메뉴로 돌아갑니다.\033[0m")
        else:
            print(f"\n\033[31m관리자만 이용 가능한 메뉴입니다.\033[0m")

def member_logout():
    global session
    if not_login():
        return
    elif input("\n로그아웃 하시려면 'Enter'키를\n취소하시려면 다른 키를 누르세요") == "":
        session = None
    else:
        print("\n\033[32m로그아웃이 취소되었습니다.\033[0m")
    return

def member_delete():
    global session
    if not_login():
        return
    typewriter("\n회원탈퇴 메뉴로 진입합니다.")
    if input(
            f"\n{names[session]}, {ids[session]}, {roles[session]}님\n\033[31m본인의 계정을 진짜로 삭제하려면 'Enter'키를\033[0m\n아니면 다른키를 눌러주세요.") == "":
        ids.pop(session)
        names.pop(session)
        pws.pop(session)
        roles.pop(session)
        active.pop(session)
        session = None
        typewriter("\n\033[32m회원탈퇴가 완료되었습니다. 다음에 또 만나길 바래요.\033[0m")
        return
    else:
        typewriter("\n회원탈퇴를 취소합니다.")

def main_menu():
    print(f"""
    \033[33m====== MBC아카데미 회원관리 프로그램입니다. ======
    1. 회원가입     2. 로그인      3. 회원정보수정
    4. 관리자 메뉴    5. 로그아웃       6.회원탈퇴
    9. 프로그램 종료
    =============================================\033[0m""")

def admin_menu():
    print(f"""
    \033[33m------ 관리자 메뉴에 접속하셨습니다. ------
    1. 전체회원보기       2. 회원정보수정
    3. 회원PNG        9. 이전메뉴로 돌아가기\033[0m""")


while run:
    main_menu()
    session_state()
    select = input("\n이용하시려는 메뉴를 선택해 주세요")
    if select == "1":
        member_add()
    elif select == "2":
        member_login()
    elif select == "3":
        member_modify()
    elif select == "4":
        member_admin()
    elif select == "5":
        member_logout()
    elif select == "6":
        member_delete()
    elif select == "9":
        run = False
    else:
        print("\n\n\033[31m잘못된 입력입니다. 메뉴번호를 확인하세요.\033[0m")