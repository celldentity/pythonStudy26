# ===============================
# MBC 아카데미 LMS
# ===============================

run = True
session = None   # 로그인한 회원 index

# ===============================
# 회원 데이터
# ===============================
sns = [1]
ids = ["admin"]
pws = ["1234"]
groups = ["admin"]  # admin, prof, staff, stu, parent

# ===============================
# 성적 데이터
# ===============================
stuIdx = []
pythonScore = []
dbScore = []
webScore = []

# ===============================
# 게시판 데이터
# ===============================
board_no = []
board_title = []
board_content = []
board_writer = []

# ===============================
# 메뉴
# ===============================
mainMenu = """
==========================
엠비씨아카데미 LMS

1. 로그인 / 회원가입
2. 성적관리
3. 게시판
4. 관리자메뉴
9. 프로그램종료
"""

memberMenu = """
---------------------------
회원관리 메뉴

1. 로그인
2. 회원가입
9. 뒤로가기
"""

scoreMenu = """
----------------------------
성적관리 메뉴

1. 성적입력 (교수)
2. 성적보기 (학생)
9. 뒤로가기
"""

boardMenu = """
-----------------------------
게시판 메뉴

1. 글쓰기
2. 글목록
9. 뒤로가기
"""

adminMenu = """
-----------------------------
관리자 메뉴

1. 회원목록
2. 회원강제삭제
9. 뒤로가기
"""

# ===============================
# 메인 루프
# ===============================
while run:
    print(mainMenu)
    select = input(">>> ")

    # ===========================
    # 1. 로그인 / 회원가입
    # ===========================
    if select == "1":
        subRun = True
        while subRun:
            print(memberMenu)
            sub = input(">>> ")

            # ---------- 로그인 ----------
            if sub == "1":
                uid = input("ID : ")
                upw = input("PW : ")

                if uid in ids:
                    idx = ids.index(uid)
                    if pws[idx] == upw:
                        session = idx
                        print(f"로그인 성공 / 권한 : {groups[idx]}")
                        subRun = False
                    else:
                        print("비밀번호 오류")
                else:
                    print("존재하지 않는 ID")

            # ---------- 회원가입 ----------
            elif sub == "2":
                print("[회원가입]")
                uid = input("새 ID : ")
                if uid in ids:
                    print("이미 존재하는 ID")
                    continue

                upw = input("PW : ")

                # ===== ROLE 분기 =====
                if session is None:
                    print("회원 유형 선택")
                    print("1. 학생")
                    print("2. 부모")

                    r = input("선택 : ")
                    if r == "1":
                        role = "stu"
                    elif r == "2":
                        role = "parent"
                    else:
                        print("잘못된 선택")
                        continue

                elif groups[session] == "admin":
                    print("권한 선택")
                    print("1. 관리자(admin)")
                    print("2. 교수(prof)")
                    print("3. 행정(staff)")
                    print("4. 학생(stu)")
                    print("5. 부모(parent)")

                    role_map = {
                        "1": "admin",
                        "2": "prof",
                        "3": "staff",
                        "4": "stu",
                        "5": "parent"
                    }

                    r = input("선택 : ")
                    if r in role_map:
                        role = role_map[r]
                    else:
                        print("잘못된 선택")
                        continue
                else:
                    print("관리자만 회원을 추가할 수 있습니다.")
                    continue

                sns.append(len(sns) + 1)
                ids.append(uid)
                pws.append(upw)
                groups.append(role)

                print(f"회원가입 완료 (권한 : {role})")

            elif sub == "9":
                subRun = False

    # ===========================
    # 2. 성적관리
    # ===========================
    elif select == "2":
        if session is None:
            print("로그인이 필요합니다.")
            continue

        subRun = True
        while subRun:
            print(scoreMenu)
            sub = input(">>> ")

            # 성적입력 (교수)
            if sub == "1":
                if groups[session] != "prof":
                    print("교수만 입력 가능")
                    continue

                sid = int(input("학생 회원번호 : "))
                py = int(input("Python : "))
                db = int(input("DB : "))
                web = int(input("Web : "))

                stuIdx.append(sid)
                pythonScore.append(py)
                dbScore.append(db)
                webScore.append(web)

                print("성적 입력 완료")

            # 성적보기 (학생)
            elif sub == "2":
                if groups[session] != "stu":
                    print("학생만 조회 가능")
                    continue

                myNo = sns[session]
                if myNo in stuIdx:
                    i = stuIdx.index(myNo)
                    total = pythonScore[i] + dbScore[i] + webScore[i]
                    avg = total / 3

                    print("==== 내 성적 ====")
                    print("Python :", pythonScore[i])
                    print("DB     :", dbScore[i])
                    print("Web    :", webScore[i])
                    print("평균   :", avg)
                else:
                    print("등록된 성적이 없습니다.")

            elif sub == "9":
                subRun = False

    # ===========================
    # 3. 게시판
    # ===========================
    elif select == "3":
        if session is None:
            print("로그인이 필요합니다.")
            continue

        subRun = True
        while subRun:
            print(boardMenu)
            sub = input(">>> ")

            if sub == "1":
                title = input("제목 : ")
                content = input("내용 : ")

                board_no.append(len(board_no) + 1)
                board_title.append(title)
                board_content.append(content)
                board_writer.append(sns[session])

                print("게시글 등록 완료")

            elif sub == "2":
                print("번호 | 제목 | 작성자")
                for i in range(len(board_no)):
                    print(board_no[i], board_title[i], board_writer[i])

            elif sub == "9":
                subRun = False

    # ===========================
    # 4. 관리자 메뉴
    # ===========================
    elif select == "4":
        if session is None or groups[session] != "admin":
            print("관리자만 접근 가능")
            continue

        subRun = True
        while subRun:
            print(adminMenu)
            sub = input(">>> ")

            if sub == "1":
                print("번호 | ID | 권한")
                for i in range(len(ids)):
                    print(sns[i], ids[i], groups[i])

            elif sub == "2":
                uid = input("삭제할 ID : ")
                if uid in ids:
                    i = ids.index(uid)
                    sns.pop(i)
                    ids.pop(i)
                    pws.pop(i)
                    groups.pop(i)
                    print("삭제 완료")
                else:
                    print("ID 없음")

            elif sub == "9":
                subRun = False

    # ===========================
    # 종료
    # ===========================
    elif select == "9":
        print("프로그램 종료")
        run = False

    else:
        print("잘못된 선택")