run = True

menu = """
===========================
MBC 아카데미 회원 관리 프로그램
===========================
1. 회원가입
2. 로그인
3. 회원보기 (R)
4. 내정보수정 (U)
5. 프로그램종료
"""
# 초기 데이터
sns = [1, 2]
ids = ["kkw", "lhj"]
passwords = ["1234", "4321"]
names = ["관리자", "임효정"]
emails = ["admin@mbc.com", "lhj@mbc.com"]
admins = [True, False]
login_user = None



while run:
    print(menu)
    if login_user is not None:
        role_str = "관리자" if admins[login_user] else "일반회원"
        print(f" >>> 현재 접속 중: {names[login_user]}님 ({role_str})")

    select = input("메뉴를 선택하세요: ")

    # 1. 회원가입 (C)
    if select == "1":
        print("\n[회원가입]")
        sn = input("사번: ")
        new_id = input("아이디: ")
        pw = input("비밀번호: ")
        name = input("이름: ")
        email = input("이메일: ")

        if input("가입하시겠습니까? (y/n): ").lower() == 'y':
            sns.append(sn);
            ids.append(new_id);
            passwords.append(pw)
            names.append(name);
            emails.append(email);
            admins.append(False)
            print("회원가입 완료!")

    # 2. 로그인
    elif select == "2":
        print("\n[로그인]")
        input_id = input("아이디: ")
        input_pw = input("비밀번호: ")

        if input_id in ids:
            idx = ids.index(input_id)
            if passwords[idx] == input_pw:
                login_user = idx
                print(f"{names[idx]}님, 환영합니다!")
            else:
                print("비밀번호가 틀렸습니다.")
        else:
            print("존재하지 않는 아이디입니다.")

    # 3. 회원보기 (R) - 관리자와 일반 회원 분리
    elif select == "3":
        if login_user is None:
            print("로그인 후 이용 가능합니다.")
            continue

        if admins[login_user]:  # 관리자일 경우
            print("\n" + "=" * 50)
            print(f"{'No':<4} | {'이름':<10} | {'ID':<10} | {'Email':<20} | {'관리자'}")
            print("-" * 50)
            for i in range(len(ids)):
                print(f"{i + 1:<4} | {names[i]:<10} | {ids[i]:<10} | {emails[i]:<20} | {admins[i]}")
            print("=" * 50)
        else:  # 일반 회원일 경우
            print("\n[내 정보 보기]")
            print(f"- 이름: {names[login_user]}")
            print(f"- 아이디: {ids[login_user]}")
            print(f"- 이메일: {emails[login_user]}")

    # 4. 정보수정 (U)
    elif select == "4":
        if login_user is None:
            print("로그인 후 이용 가능합니다.")
            continue

        if admins[login_user]:
            print("\n[관리자 모드: 회원 정보 관리]")
            target_id = input("수정/관리할 회원의 ID를 입력하세요: ")
            if target_id in ids:
                t_idx = ids.index(target_id)
                print(f"1. 차단(미구현) 2. 등업 3. 암호초기화")
                # 여기에 관리자 전용 로직 추가 가능
            else:
                print("해당 ID를 찾을 수 없습니다.")
        else:
            print("\n[내 정보 수정]")
            names[login_user] = input(f"새 이름(기존:{names[login_user]}): ")
            passwords[login_user] = input("새 비밀번호: ")
            print("수정이 완료되었습니다.")

    # 5. 종료
    elif select == "5":
        print("프로그램을 종료합니다.")
        run = False# ===============================
# 회원 관리 프로그램
# ===============================

run = True
login_user = None  # 현재 로그인한 사용자 인덱스

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

# 회원 데이터
sns = [1, 2]
ids = ["kkw", "lhj"]
passwords = ["1234", "4321"]
names = ["관리자", "임효정"]
emails = ["admin@mbc.com", "lhj@mbc.com"]
admins = [True, False]


while run:
    print(menu)
    select = input("1~5 숫자를 입력하세요 : ")

    # ===============================
    # 1. 회원가입
    # ===============================
    if select == "1":
        print("회원가입 메뉴")

        sn = input("사번 : ")
        id = input("아이디 : ")

        if id in ids:
            print("이미 존재하는 아이디입니다.")
            continue

        pw = input("비밀번호 : ")
        name = input("이름 : ")
        email = input("이메일 : ")

        print("\n입력 정보 확인")
        print(f"이름 : {name}")
        print(f"아이디 : {id}")
        print(f"이메일 : {email}")

        if input("가입하시겠습니까? (y/n) : ") == "y":
            sns.append(sn)
            ids.append(id)
            passwords.append(pw)
            names.append(name)
            emails.append(email)
            admins.append(False)
            print("회원가입 완료")
        else:
            print("회원가입 취소")

    # ===============================
    # 2. 로그인
    # ===============================
    elif select == "2":
        print("로그인 메뉴")

        id = input("아이디 : ")
        pw = input("비밀번호 : ")

        if id in ids:
            idx = ids.index(id)
            if passwords[idx] == pw:
                login_user = idx
                print(f"{names[idx]}님 로그인 성공")

                if admins[idx]:
                    print("▶ 관리자 계정입니다.")
                else:
                    print("▶ 일반 회원 계정입니다.")
            else:
                print("비밀번호가 틀렸습니다.")
        else:
            print("존재하지 않는 아이디입니다.")

    # ===============================
    # 3. 회원보기
    # ===============================
    elif select == "3":
        if login_user is None:
            print("로그인 후 이용 가능합니다.")
            continue

        # 관리자
        if admins[login_user]:
            print("\n[전체 회원 목록]")
            for i in range(len(ids)):
                print(f"{i+1}. {names[i]} | {ids[i]} | {emails[i]} | 관리자:{admins[i]}")
        else:
            # 일반회원
            print("\n[내 정보]")
            print(f"이름 : {names[login_user]}")
            print(f"아이디 : {ids[login_user]}")
            print(f"이메일 : {emails[login_user]}")

    # ===============================
    # 4. 내정보수정
    # ===============================
    elif select == "4":
        if login_user is None:
            print("로그인 후 이용 가능합니다.")
            continue

        print("\n내정보 수정")
        print("1. 이름 변경")
        print("2. 이메일 변경")
        print("3. 비밀번호 변경")

        choice = input("선택 : ")

        if choice == "1":
            names[login_user] = input("새 이름 : ")
            print("이름 변경 완료" + names[login_user])

        elif choice == "2":
            emails[login_user] = input("새 이메일 : ")
            print("이메일 변경 완료" + emails[login_user])

        elif choice == "3":
            passwords[login_user] = input("새 비밀번호 : ")
            print("비밀번호 변경 완료" + passwords[login_user])

        else:
            print("잘못된 선택")

    # ===============================
    # 5. 종료
    # ===============================
    elif select == "5":
        print("프로그램을 종료합니다.")
        run = False

    else:
        print("1~5 사이 숫자를 입력하세요.")
