import time
# 게시물 번호가 일정하게 빠지려면(중간에 글이 삭제되더라도) 전역변수에 last_no = 0 으로 설정해주고 그 뒤에 1번 지역에서 글을 작성할 때마다
# last_no += 1 로 설정해서 몇 번 글이 삭제되든 상관없이 게시물 번호는 일정하게 앞으로 나아가도록 해야한다.

### 비회원용 게시판 ###
# C 게시글 등록
# R 게시글 전체 보기(리스트)
# R 게시글 자세히 보기
# U 게시글 수정
# D 게시글 삭제
#사용할 전역 변수 리스트 = 프로그램 전반적으로 사용한다.
run = True # while문 프로그램 구동중!!
board_no = [] # 중복되지 않는 유일한 값, not null(0이라도 집어넣어야 한다.)
board_title = [] # 게시글의 제목
board_content = [] # 게시글의 내용
board_writer = [] # 글쓴이
board_password = [] # 게시글의 암호(수정, 삭제용)
board_hit = [] # 좋아요(이걸 영어에서 hit 라고 부른다.)
board_visitcount = [] # 조회수
last_no = 0
#게시판을 생성할 줄 알면 모든 걸 다 할 수 있다.
menu = """
============================
MBC 아카데미 비회원 게시판입니다.
1. 게시글 생성
2. 게시글 리스트 보기
3. 게시글 자세히 보기
4. 게시글 수정하기
5. 게시글 삭제하기
6. 프로그램 종료
==========================="""
while run:
    print(menu)
    select = input("\n1~6사이의 메뉴를 선택하세요. : ")#select는 while문 안에서만 사용이 가능하기 때문에 지역변수다 for문 안에서 사용되는 i, k들도 들여쓰기가 끝나면 사라진다.
    if select == "1":
        print("\n[게시글 등록 메뉴]") #게시글 번호는 컴터가 직접 입력
        title = input("제목을 입력하세요: ")
        content = input("내용을 입력하세요: ")
        writer = input("작성자명을 입력하세요: ")
        password = input("게시물 암호를 입력하세요: ")
        print(f"\n제목 : {title}\n내용 : {content}\n작성자 : {writer}\n암호 : {password}\n")
        choose = input("저장하려면 'Enter'키를 누르세요") #번호 순차적으로 증가하는 것 확인하기
# ===================
#   1. 게시글 등록
# ===================
        if choose == "":
            last_no += 1
            no = last_no # 글을 쓸 때마다 무조건 1씩 증가
            board_title.append(title)
            board_content.append(content)
            board_writer.append(writer)
            board_password.append(password)
            # 제목의 리스트에서 인덱스를 추출하여 +1 한 값이 넘버가 된다.
            # 제목을 이용해서 번호를 생성하면 중복 제목 문제가 생긴다. (중간 게시물을 지웠을때의 문제는 어떻게 해결함?)
            board_no.append(no)
            board_hit.append(0) # 좋아요
            board_visitcount.append(0) # 조회수
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
        for i in range (len(board_no)): #게시물의 개수만큼 반복
            print(f"{board_no[i]}\t[{board_title[i]}]\t{board_content[i]}\t[{board_writer[i]}]\t{board_visitcount[i]}\t[{board_hit[i]}]")
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
            board_visitcount[idx] += 1 # 조회수 / 진리표를 그려가면서 생각해봐야 한다.
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
                print(f"\n제목 : {board_title[idx]}\n내용 : {board_content[idx]}\n작성자 : {board_writer[idx]}\n암호 : {board_password[idx]}\n")
                if input ("\n선택한 본인 게시물의 삭제를 희망하면 'Enter'키를\n취소하고 메뉴로 돌아가려면 아무키나 누르세요.\n삭제시 모든 데이터는 복구가 불가능합니다.") == "":
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
                print("\n비밀번호가 일치하지 않습니다.\n메인 메뉴로 돌아갑니다.")
                time.sleep(1)
    elif select == "6":
        print("\n[비회원 게시판 프로그램이 종료됩니다.]")
        time.sleep(2)
        run = False
    else:
        print("\n[1~6사이 메뉴번호를 정확히 입력하세요.메뉴로 돌아갑니다.]")
        time.sleep(2)

