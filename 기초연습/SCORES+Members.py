import time
### 전역변수 ###
ids = []
passwords = []
names = []
emails = []
admins = []
sns = []
login_user = None
kors = [] # 국어점수
engs = [] # 영어점수
mats = [] # 수학점수
tots = [] # 총점 빈 배열
avgs = [] # 평균
grades = [] #등급

#추가구현 희망하는 기능 (종합석차[람다랑 리버스 배워야한당])

menu = """
==============================
MBC 아카데미 성적처리
1. 회원가입  |6. 비회원게시판
2. 성적입력  |7. 로그인
3. 성적보기  |8. 회원보기
4. 성적수정  |9. 회원정보수정
5. 회원탈퇴  |0. 프로그램종료
============================="""
run = True # 프로그램 실행중
while run:
    print(menu)
    if login_user is not None:
        if admins[login_user]:
            print(f" >>> 현재접속중: {names[login_user]} | 학번: {sns[login_user]}\n관리자 계정입니다.")
        else:
            print(f" >>> 현재접속중: {names[login_user]} | 학번: {sns[login_user]}\n일반사용자 계정입니다.")
# ===================
#     메 뉴 선 택
# ===================
    select = input("(1~9)값을 눌러 메뉴를 선택하세요. : ")
# ===================
#   1. 회원가입 메뉴
# ===================
    if select == "1":
        print("\n[회원가입 메뉴에 진입하셨습니다.]")
        while True:
            id = input("아이디 : ")
            if id in ids:
                print("\n이미 존재하는 아이디입니다.\n3초뒤 메뉴로 돌아갑니다.")
                time.sleep(3)
                break
            else:
                pw = input("비밀번호 : ")
                name = input("이름 : ")
                email = input("이메일 : ")
                print(f"\n입력하신 정보를 확인하세요\n이름 : {name} | 아이디 : {id} | 이메일 : {email}")
                if input("\n가입하시겠습니까? (y/n)").lower() == "y":
                    if not sns:
                        sn = "320-01" #sn이 비어있을 경우 첫 숫자는 이렇게 부여
                    else:
                        last_sn = sns[-1]
                        last_num = int(last_sn.split("-")[1])
                        new_num = last_num + 1
                        sn = (f"320-{new_num:02d}") # f"(1:02d)" 정수 표현식 전체 두 자리를 만들되 부족한 부분은 0으로 채우고 정수로 해라
                    sns.append(sn)
                    ids.append(id)
                    passwords.append(pw)
                    names.append(name)
                    emails.append(email)
                    kors.append(0)
                    engs.append(0)
                    mats.append(0)
                    tots.append(0)
                    avgs.append(0)
                    grades.append("N/A")
                    if sn == "320-01": #맨 처음 가입한 사람에게 관리자 권한 주기
                        admins.append(True)
                    else:
                        admins.append(False)
                    print("\n회원가입이 완료되었습니다.\n메뉴로 돌아갑니다.")
                    time.sleep(1)
                else:
                    print("\n회원가입이 취소되었습니다.\n메뉴로 돌아갑니다.")
                    time.sleep(1)
            break
# ===================
#   2. 성적입력 메뉴
# ===================
    elif select == "2":
        if login_user is None:
            print("\n로그인 후 이용 가능합니다.\n2초뒤 메뉴로 돌아갑니다.")
            time.sleep(2)
            continue
        print("\n[성적입력 메뉴에 진입하셨습니다.]")
        sn = input("\n'320-00'형식으로 '-'를 포함하여\n본인의 학번 6자리를 입력 :") #몇 자리를 입력해야 하는지 정해주는 표현식 찾기
        idx = sns.index(sn)
        while True:
            kor = int(input("국어 점수를 입력하세요. :")) #키보드로 입력한 숫자는 문자로 인식되므로 int()감사 계산용만듦
            if 1 <= int(kor) <= 100:
                while True:
                    eng = int(input("영어 점수를 입력하세요. :"))
                    if 1 <= int(eng) <= 100:
                        while True:
                            mat = int(input("수학 점수를 입력하세요. :"))
                            if 1 <= int(mat) <= 100:
                                print(f"\n학번 : {sns[idx]} | 이름 : {names[idx]} | 국어 : {kor} | 영어 : {eng} | 수학 : {mat}")
                                if input("\n입력한 성적을 저장하시려면 \n'y'를 누르세요\n취소하시려면 아무키나 누르세요('y'키 제외)").lower() == "y":
                                    kors[idx] = kor
                                    engs[idx] = eng
                                    mats[idx] = mat
                                    tot = kor + eng + mat
                                    tots[idx] = tot
                                    avgs[idx] = (tot / 3)
                                    if (tot / 3) >= 90:
                                        grades[idx] = "A"
                                    elif (tot / 3) >= 80:
                                        grades[idx] = "B"
                                    elif (tot / 3) >= 70:
                                        grades[idx] = "C"
                                    elif (tot / 3) >= 60:
                                        grades[idx] = "D"
                                    else:
                                        grades[idx] = "F"
                                    print("\n성적 입력이 저장되었습니다. \n메뉴로 돌아갑니다.")
                                    time.sleep(1)
                                else:
                                    print("\n성적 입력이 취소되었습니다. \n메뉴로 돌아갑니다.")
                                    time.sleep(1)
                                break
                            else:
                                print("수학점수 입력값을 다시 확인하세요.")
                        break
                    else:
                        print("영어점수 입력값을 다시 확인하세요.")
                break
            else:
                print("국어점수 입력값을 다시 확인하세요.")
# ===================
#  3. 성적 전체 조회
# ===================이것도 관리자만 전체 성적을 확인할 수 있어야 한다. 기능 추가하기
    elif select == "3":
        if login_user is None:
            print("\n로그인 후 이용 가능합니다.\n2초뒤 메뉴로 돌아갑니다.")
            time.sleep(2)
            continue
        if tots[idx] == 0:
            print("\n입력된 성적이 없습니다.\n성적입력을 먼저 진행해주세요.\n2초뒤 메뉴로 돌아갑니다.")
            time.sleep(2)
        else:
            print("\n[학생성적 전체조회 메뉴에 진입하셨습니다.]")
            print("============================================")
            print("[성적목록]")
            for i in range(len(sns)): #리스트의 처음부터 끝까지 반복용
                print("-------------------------------------------")
                print("학번 : " + sns[i] + " |이름 : " + names[i])
                print("국어 : " + str(kors[i]) + " |영어 : " + str(engs[i]) + " |수학 : " + str(mats[i]))
                print("총점 : " + str(tots[i]) + " |평균 : " + str(avgs[i]) + " |등급 : " + str(grades[i]))
            while True:
                if input("\n메인메뉴로 돌아가시려면 \n'Enter'키를 누르세요") == "":
                    print("\n메뉴로 돌아갑니다.")
                    time.sleep(1)
                    break
                else: print("\n메뉴로 돌아가려면 'Enter'키를 정확히 누르세요.")
# ===================
#  4. 성적 수정 메뉴
# ===================
    elif select == "4":
        if login_user is None:
            print("\n로그인 후 이용 가능합니다.\n2초뒤 메뉴로 돌아갑니다.")
            time.sleep(2)
            continue
        print("\n[성적수정 메뉴에 진입하셨습니다.]")
        sn = input("\n'320-00'형식으로 '-'를 포함하여\n수정할 학번을 입력 :")
        if sn in sns:
            idx = sns.index(sn)
            print(f"\n 입력한 학번의 점수는 \n이름 : {names[idx]}\n국어 : {kors[idx]} \n영어 : {engs[idx]}\n수학 : {mats[idx]}")
            time.sleep(1)
            while True:
                kor = int(input("수정할 국어 점수를 입력하세요. :"))  # 키보드로 입력한 숫자는 문자로 인식되므로 int()감사 계산용만듦
                if 1 <= int(kor) <= 100:
                    while True:
                        eng = int(input("수정할 영어 점수를 입력하세요. :"))
                        if 1 <= int(eng) <= 100:
                            while True:
                                mat = int(input("수정할 수학 점수를 입력하세요. :"))
                                if 1 <= int(mat) <= 100:
                                    print(
                                        f"\n학번 : {sns[idx]} | 이름 : {names[idx]} | 국어 : {kor} | 영어 : {eng} | 수학 : {mat}")
                                    if input("\n수정한 성적을 저장하시려면 \n'y'를 누르세요\n취소하시려면 아무키나 누르세요('y'키 제외)\n저장시 기존의 성적은 완전히 덮여쓰여집니다.").lower() == "y":
                                        kors[idx] = kor
                                        engs[idx] = eng
                                        mats[idx] = mat
                                        tot = kor + eng + mat
                                        tots[idx] = tot
                                        avgs[idx] = (tot / 3)
                                        if (tot / 3) >= 90:
                                            grades[idx] = "A"
                                        elif (tot / 3) >= 80:
                                            grades[idx] = "B"
                                        elif (tot / 3) >= 70:
                                            grades[idx] = "C"
                                        elif (tot / 3) >= 60:
                                            grades[idx] = "D"
                                        else:
                                            grades[idx] = "F"
                                        print("\n성적 입력이 저장되었습니다. \n메뉴로 돌아갑니다.")
                                        time.sleep(1)
                                    else:
                                        print("\n성적 입력이 취소되었습니다. \n메뉴로 돌아갑니다.")
                                        time.sleep(1)
                                    break
                                else:
                                    print("수학점수 입력값을 다시 확인하세요.")
                            break
                        else:
                            print("영어점수 입력값을 다시 확인하세요.")
                    break
                else:
                    print("국어점수 입력값을 다시 확인하세요.")
        else:
            print("\n등록된 학번이 없습니다. 메뉴로 돌아갑니다.")
            time.sleep(1)
# ===================
#    5. 회원탈퇴
# ===================
    elif select == "5":
        if login_user is None:
            print("\n로그인 후 이용 가능합니다.\n2초뒤 메뉴로 돌아갑니다.")
            time.sleep(2)
            continue
        print("\n[회원탈퇴 메뉴에 진입하셨습니다.]")
        while True:
            sn = input("\n'320-00'형식으로 '-'를 포함하여\n성적을 탈퇴할 학번을 입력 :")
            if sn in sns:
                idx = sns.index(sn)
                print(f"{names[idx]} 회원의 정보를 영구히 삭제합니다.")
                if input("\n정말 삭제할까요? \n삭제를 희망하시면 'y'키\n메뉴로 돌아가려면 아무키나 누르세요('y'키 제외)") == 'y':
                    self_delete = (idx == login_user) # 본인 계정을 삭제하는지 확인하는 변수
                    ids.pop(idx)
                    passwords.pop(idx)
                    emails.pop(idx)
                    admins.pop(idx)
                    sns.pop(idx)
                    names.pop(idx) #(배열관련 리스트에서 삭제할떄는 Pop이 좋고, "글자를 찾아서 지울 땐 remove를 쓴다.")
                    kors.pop(idx)
                    engs.pop(idx)
                    mats.pop(idx)
                    tots.pop(idx)
                    avgs.pop(idx)
                    grades.pop(idx)
                    print("\n선택한 학생정보가 완전히 삭제되었습니다.")
                    if self_delete:
                        print("\n로그인한 본인의 계정이 삭제되어 로그아웃 됩니다.\n메뉴로 돌아갑니다.")
                        login_user = None
                        if not True in admins:
                            print("\n[잠깐!]관리자가 없습니다.\n자동으로 다음 관리자를 임명합니다.")
                            admins[0] = True
                            print(f"\n{names[0]}님이 관리자가 되었습니다.")
                    elif idx < login_user:
                        login_user -= 1
                    time.sleep(2)
                    break
                else:
                    print("\n학생정보 삭제를 취소합니다.\n2초뒤 메뉴로 돌아갑니다.")
                    time.sleep(2)
                break
            else:
                print("\n입력한 학생 정보를 찾을 수 없습니다.\n2초뒤 메인메뉴로 돌아갑니다.")
                time.sleep(2)
            break
# ===================
#   6. 비회원 게시판
# ===================
    elif select == "6":
        run = True  # while문 프로그램 구동중!!
        board_no = []  # 중복되지 않는 유일한 값, not null(0이라도 집어넣어야 한다.)
        board_title = []  # 게시글의 제목
        board_content = []  # 게시글의 내용
        board_writer = []  # 글쓴이
        board_password = []  # 게시글의 암호(수정, 삭제용)
        board_hit = []  # 좋아요(이걸 영어에서 hit 라고 부른다.)
        board_visitcount = []  # 조회수
        last_no = 0
        sub_menu = """
        ============================
        MBC 아카데미 비회원 게시판입니다.
        6-1. 게시글 생성
        6-2. 게시글 리스트 보기
        6-3. 게시글 자세히 보기
        6-4. 게시글 수정하기
        6-5. 게시글 삭제하기
        6-6. 회원메뉴로 돌아가기
        ==========================="""
        while run:
            print(sub_menu)
            select = input(
                "\n1~6사이의 메뉴를 선택하세요. : ")  # select는 while문 안에서만 사용이 가능하기 때문에 지역변수다 for문 안에서 사용되는 i, k들도 들여쓰기가 끝나면 사라진다.
            if select == "1":
                print("\n[게시글 등록 메뉴]")  # 게시글 번호는 컴터가 직접 입력
                title = input("제목을 입력하세요: ")
                content = input("내용을 입력하세요: ")
                writer = input("작성자명을 입력하세요: ")
                password = input("게시물 암호를 입력하세요: ")
                print(f"\n제목 : {title}\n내용 : {content}\n작성자 : {writer}\n암호 : {password}\n")
                choose = input("저장하려면 'Enter'키를 누르세요")  # 번호 순차적으로 증가하는 것 확인하기
                # ===================
                #   1. 게시글 등록
                # ===================
                if choose == "":
                    last_no += 1
                    no = last_no  # 글을 쓸 때마다 무조건 1씩 증가
                    board_title.append(title)
                    board_content.append(content)
                    board_writer.append(writer)
                    board_password.append(password)
                    # 제목의 리스트에서 인덱스를 추출하여 +1 한 값이 넘버가 된다.
                    # 제목을 이용해서 번호를 생성하면 중복 제목 문제가 생긴다. (중간 게시물을 지웠을때의 문제는 어떻게 해결함?)
                    board_no.append(no)
                    board_hit.append(0)  # 좋아요
                    board_visitcount.append(0)  # 조회수
                    print(f"\n{no}번째 게시물이 등록 되었습니다.")
            # ===================
            #  2. 게시글 전체 보기
            # ===================
            elif select == "2":
                print("\n[게시글 전체 목록 출력]")
                print("----------------------------------------")
                print("\n번호\t   [제목]\t 내용\t [작성자]\t 조회수\t [좋아요]")
                print("----------------------------------------")
                if len(board_no) == 0:
                    print("\n 등록된 게시물이 없습니다.")
                    continue
                for i in range(len(board_no)):  # 게시물의 개수만큼 반복
                    print(
                        f"{board_no[i]}\t[{board_title[i]}]\t{board_content[i]}\t[{board_writer[i]}]\t{board_visitcount[i]}\t[{board_hit[i]}]")
                    #          게시물번호          제목               내용               작성자                 조회수               좋아요
                print("출력이 완료되었습니다.")
                time.sleep(2)
            # ===================
            # 3. 게시글 자세히 보기
            # ===================
            elif select == "3":
                print("\n[게시글 자세히 보기]")
                bno = int(input("\n조회를 원하는 게시물 번호를 입력하세요"))
                if bno in board_no:
                    idx = board_no.index(bno)
                    print(f"{board_no[idx]}번 게시물을 조회합니다.")
                    board_visitcount[idx] += 1  # 조회수 / 진리표를 그려가면서 생각해봐야 한다.
                    print("====================================")
                    print(f"번호: {board_no[idx]}")
                    print(f"제목: {board_title[idx]}")
                    print(f"내용: {board_content[idx]}")
                    print(f"작성자: {board_writer[idx]}")
                    print(f"조회수: {board_visitcount[idx]}")
                    print(f"좋아요: {board_hit[idx]}")
                    print("====================================")
                    if input("좋아요 = (y)키 누르기 : \n메뉴로 돌아가려면 (y)를 제외한 아무키나 입력하세요 : ") == "y":
                        board_hit[idx] += 1
                        print("좋아요 +1\n메뉴로 돌아갑니다.")
                        time.sleep(1)
                    else:
                        print("\n아쉽습니다. 다음에 더 좋은 게시물로 만나요.\n메뉴로 돌아갑니다.")
                        time.sleep(1)
                else:
                    print("\n해당 번호의 게시글이 없습니다.\n메뉴로 돌아갑니다.")
                    time.sleep(1)
            # ===================
            #  4. 게시글 수정 메뉴
            # ===================
            elif select == "4":
                print("\n[게시글 등록 메뉴]")
                bno = int(input("\n수정을 원하는 게시물 번호를 입력하세요"))
                if bno in board_no:
                    idx = board_no.index(bno)
                    bpw = input("게시물 비밀번호를 입력하세요. : ")
                    if board_password[idx] == bpw:
                        print("=========본인인증이 완료되었습니다==========")
                        print(f"번호: {board_no[idx]}")
                        print(f"제목: {board_title[idx]}")
                        print(f"내용: {board_content[idx]}")
                        print(f"작성자: {board_writer[idx]}")
                        if input("\n작성한 위 내용을 수정하시려면 'Enter'키를\n메뉴로 돌아가려면 아무키나 눌러주세요.") == "":
                            title = input("수정할 제목을 입력하세요: ")
                            content = input("수정할 내용을 입력하세요: ")
                            writer = input("수정할 작성자명을 입력하세요: ")
                            password = input("수정할 게시물 암호를 입력하세요: ")
                            print(f"\n제목 : {title}\n내용 : {content}\n작성자 : {writer}\n암호 : {password}\n")
                            if input("\n수정한 내용을 저장하시려면 'Enter'키를\n메뉴로 돌아가려면 아무키나 눌러주세요.") == "":
                                board_title[idx] = title
                                board_content[idx] = content
                                board_writer[idx] = writer
                                board_password[idx] = password
                                print("\n저장이 완료되었습니다.")
                                time.sleep(1)
                            else:
                                print("\n수정을 취소하고 메뉴로 돌아갑니다.")
                                time.sleep(1)
                        else:
                            print("메뉴로 돌아갑니다.")
                            time.sleep(1)
                    else:
                        print("\n비밀번호가 일치하지 않습니다.\n메뉴로 돌아갑니다.")
                    time.sleep(1)
                else:
                    print("\n해당 번호의 게시글이 없습니다.\n메뉴로 돌아갑니다.")
                    time.sleep(1)
            # ===================
            #  5. 게시글 삭제 메뉴
            # ===================
            elif select == "5":
                print("\n[게시글 삭제]")
                bno = int(input("\n삭제를 원하는 게시물 번호를 입력하세요"))
                if bno in board_no:
                    idx = board_no.index(bno)
                    bpw = input("게시물 비밀번호를 입력하세요. : ")
                    if board_password[idx] == bpw:
                        print("==========본인인증이 완료되었습니다.==========")
                        print(
                            f"\n제목 : {board_title[idx]}\n내용 : {board_content[idx]}\n작성자 : {board_writer[idx]}\n암호 : {board_password[idx]}\n")
                        if input(
                                "\n선택한 본인 게시물의 삭제를 희망하면 'Enter'키를\n취소하고 메뉴로 돌아가려면 아무키나 누르세요.\n삭제시 모든 데이터는 복구가 불가능합니다.") == "":
                            board_no.pop(idx)
                            board_title.pop(idx)
                            board_content.pop(idx)
                            board_writer.pop(idx)
                            board_password.pop(idx)
                            board_hit.pop(idx)
                            board_visitcount.pop(idx)
                            print("\n선택한 게시글이 삭제되었습니다.")
                            time.sleep(1)
                        else:
                            print("\n메인 메뉴로 돌아갑니다.")
                            time.sleep(1)
                    else:
                        print("\n비밀번호가 일치하지 않습니다.\n메뉴로 돌아갑니다.")
                        time.sleep(1)
            elif select == "6":
                print("\n[메인 회원 메뉴로 돌아갑니다.]")
                time.sleep(1)
                break
            else:
                print("\n[1~6사이 메뉴번호를 정확히 입력하세요.]")
                time.sleep(1)
# ===================
#   7. 계정 로그인
# ===================
    elif select == "7":
        print("\n[로그인 메뉴에 진입했습니다.]")
        while True:
            id = input("아이디를 입력하세요 :")
            if id in ids:
                idx = ids.index(id)
                while True:
                    pw = input("패스워드를 입력하세요 :")
                    if passwords[idx] == pw:
                        login_user = idx
                        print(f"\n{names[idx]}님 로그인 성공\n메인화면으로 이동합니다.")
                        time.sleep(1)
                        break
                    else:
                        print("\n입력한 패스워드가 맞지 않습니다.\n다시 입력하세요.")
            else:
                print("\n입력한 ID는 회원가입 되어있지 않습니다.\n2초뒤 메인화면으로 이동합니다.")
                time.sleep(2)
            break
# ===================
#   8. 회원정보 확인
# ===================
    elif select == "8":
        if login_user is None:
            print("\n로그인 후 이용 가능합니다.\n2초뒤 메뉴로 돌아갑니다.")
            time.sleep(2)
            continue
        if admins[login_user]:
            print("\n[전체 회원 목록]")
            for i in range(len(ids)):
                print(f"{i+1} | 이름: {names[i]} | 계정: {ids[i]} | 이메일: {emails[i]} | 학번: {sns[i]} | 관리자 권한: {admins[i]}")
            print("\n" + "="*52)
            while True:
                if input("조회가 완료되었습니다. 'Enter'키를 누르면 메뉴로 돌아갑니다.") == "":
                    print("\n메뉴로 돌아갑니다.")
                    time.sleep(1)
                    break
                else:
                    print("\n[알림] 'Enter'키를 정확히 누르셔야 합니다.")
        else:
            print(f"\n[내 정보 보기]\n이름: {names[login_user]}\n계정: {ids[login_user]}\n이메일: {emails[login_user]}\n학번: {sns[login_user]}\n관리자 권한: {admins[login_user]}")
            while True:
                if input("\n메인메뉴로 돌아가시려면 \n'y'를 누르세요") == "y":
                    print("\n메뉴로 돌아갑니다.")
                    time.sleep(1)
                    break
                else: print("\n메뉴로 돌아가려면 'y'키를 정확히 누르세요.")
# ===================
#   9. 회원정보 수정----------------------------------------------------
# ===================
    elif select == "9":
        if login_user is None:
            print("\n로그인 후 이용 가능합니다.\n1초뒤 메뉴로 돌아갑니다.")
            time.sleep(1)
            continue
        print("\n[회원정보 수정 메뉴에 진입했습니다.]")
        time.sleep(3)
# ===================
#  0. 프로그램 종료하기
# ===================
    elif select.lower() == "q":
        run = False
        print("\n[2초뒤 프로그램을 종료합니다.]")
        time.sleep(2)
# ===================
#   메뉴버튼 오기입
# ===================
    else:
        print("\n1~5, 'q'값만 허용합니다.\n입력값을 다시 확인하세요.")
