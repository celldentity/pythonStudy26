#성적 처리용 프로그램을 개발해보자!!!

# C : 성적입력
# R : 성적보기
# U : 성적수정
# D : 성적삭제

# 필요한 변수는?
import os
import time
import datetime

#배열의 처음이 숫자로 되어 있으면 숫자로 들어간다.
#더미 데이터를 날려본다.
sns = []
#          0         1         2         3         4
names = []
kors = [] # 국어점수
engs = [] # 영어점수
mats = [] # 수학점수
tots = [] # 총점 빈 배열
avgs = [] # 평균
grades = [] #등급
admins = [False, False, False, True, False]
login_user = None

menu = """
==============================
MBC 아카데미 성적처리
1. 회원가입    |6. 
2. 성적보기    |7. 
3. 성적수정    |8.
4. 성적삭제    |9. 프로그램종료
5. 종합석차
============================="""
run = True # 프로그램 실행중
while run:
    print(menu)
    if login_user is not None:
        if admins[idx]:
            print(f" >>> 현재접속중: {names[login_user]}님\n관리자 계정입니다.")
        else:
            print(f" >>> 현재접속중: {names[login_user]}님\n일반사용자 계정입니다.")


    select = input("(1~9)값을 눌러 메뉴를 선택하세요. : ") # select 변수에 숫자를 넣는다.

    # 1. 성적입력
    if select == "1":
        print("\n[성적입력 메뉴에 진입하셨습니다.]")
        sn = input("학번을 입력하세요. :")
        name = input("이름을 입력하세요. :")
        while True:
            kor = int(input("국어 점수를 입력하세요. :")) #키보드로 입력한 숫자는 문자로 인식되므로 int()감사 계산용만듦
            if 1<= int(kor) <= 100:
                while True:
                    eng = int(input("영어 점수를 입력하세요. :"))
                    if 1<= int(eng) <= 100:
                        while True:
                            mat = int(input("수학 점수를 입력하세요. :"))
                            if 1<= int(mat) <= 100:
                                print(f"\n학번 : {sn} | 이름 : {name} | 국어 : {kor} | 영어 : {eng} | 수학 : {mat}")
                                if input("\n입력한 성적을 저장하시려면 \n'y'를 누르세요\n취소하시려면 아무키나 누르세요('y'키 제외)") == "y":
                                    sns.append(sn)
                                    names.append(name)
                                    kors.append(kor)
                                    engs.append(eng)
                                    mats.append(mat)
                                    tot = kor + eng + mat
                                    tots.append(tot)
                                    avgs.append(tot / 3)
                                    if (tot / 3) >= 90:
                                        grades.append("A")
                                    elif (tot / 3) >= 80:
                                        grades.append("B")
                                    elif (tot / 3) >= 70:
                                        grades.append("C")
                                    elif (tot / 3) >= 60:
                                        grades.append("D")
                                    else:
                                        grades.append("F")
                                    print("\n성적 입력이 저장되었습니다. \n3초뒤 메뉴로 돌아갑니다.")
                                    time.sleep(3)
                                else:
                                    print("\n성적 입력이 취소되었습니다. \n3초뒤 메뉴로 돌아갑니다.")
                                    time.sleep(3)
                                break
                            else:
                                print("수학점수 입력값을 다시 확인하세요.")
                        break
                    else:
                        print("영어점수 입력값을 다시 확인하세요.")
                break
            else:
                print("국어점수 입력값을 다시 확인하세요.")


    elif select == "2": #전체보기를 알려준다.
        print("\n[학생들의 성적출력 메뉴에 진입하셨습니다.]")
        print("========================================")
        print("[성적목록]")
        for i in range(len(sns)): #리스트의 처음부터 끝까지 반복용
        # #len(sns) : 리스트의 길이를 가져옴 : 5
        # range(5) : 0~5 까지 증가
        # i in 5 : i값에 0 반복 1반복 2 반복 3 반복 4 반복 5 반복 끝
        # 결론 : i 값이 인덱스로 사용함
            tots.append(kors[i] + engs[i] + mats[i])
            avgs.append(tots[i] / 3)
            #grades.append([i] = avgs[i] / 5)  #내가 만들어보쟈
            print("--------------------------------------")
            print("학번 : " + sns[i] + " |이름 : " + names[i])
            print("국어 : " + str(kors[i]) + " |영어 : " + str(engs[i]) + " |수학 : " + str(mats[i]))
            print("총점 : " + str(tots[i]) + " |평균 : " + str(avgs[i]) + " |등급 : " + str(grades[i]))
        while True:
            if input("\n메인메뉴로 돌아가시려면 \n'y'를 누르세요") == "y":
                print("\n3초뒤 메뉴로 돌아갑니다.")
                time.sleep(3)
                break
            else: print("\n메뉴로 돌아가려면 'y'키를 정확히 누르세요.")


    #오류발생으로 주석처리 : index out of range
    #비어 있는 리스트는 주소가 없다.
    #해결방법 .append()를 사용한다.

    elif select == "3":
        print("\n[성적수정 메뉴에 진입하셨습니다.]")
        sn = input("\n 수정할 학번을 입력하세요")
        if sn in sns:
            idx = sns.index(sn)
            print(f"\n 입력한 학번의 정보는 \n이름 : {names[idx]}\n국어 : {kors[idx]} \n영어 : {engs[idx]}\n수학 : {mats[idx]}")

            kors[idx] = int(input("\n수정할 국어 점수를 입력하세요 :"))
            engs[idx] = int(input("\n수정할 영어 점수를 입력하세요 :"))
            mats[idx] = int(input("\n수정할 수학 점수를 입력하세요 :"))

        else:
            print("\n등록된 학번이 없습니다. 3초뒤 메뉴로 돌아갑니다.")
            time.sleep(3)

            #수정된 값을 바탕으로 평균 등급 다시 등록 숙제
        #등록된 학생의 점수를 가져온다.
        #등록된 학생의 점수를 수정한다.
        #수정된 값을 기준으로 총점과 평균과 등급을 다시 등록한다.

    elif select == "4":
        print("\n[학생성적 삭제메뉴에 진입하셨습니다.]")
        while True:
            sn = input("\n삭제할 학번을 입력하세요.")
            if sn in sns:
                idx = sns.index(sn)
                print(f"{names[idx]} 학생의 정보를 학제합니다.")
                if input("\n정말 삭제할까요? \n삭제를 희망하시면 'y'키\n메뉴로 돌아가려면 아무키나 누르세요('y'키 제외)").lower() == 'y':
                    sns.pop(idx)
                    names.pop(idx)
                    kors.pop(idx)
                    engs.pop(idx)
                    mats.pop(idx)
                    print("\n선택한 학생정보가 완전히 삭제되었습니다.\n3초뒤 메뉴로 돌아갑니다.")
                    time.sleep(3)
                else:
                    print("\n학생정보 삭제를 취소합니다.\n3초뒤 메뉴로 돌아갑니다.")
                    time.sleep(3)
                break
            else:
                print("\n입력한 학생 정보를 찾을 수 없습니다.\n3초뒤 메인메뉴로 돌아갑니다.")
                time.sleep(3)
            break

    elif select.lower() == "q":
        run = False
        print("\n[3초뒤 프로그램을 종료합니다.]")
        time.sleep(3)

    else:
        print("1~9, q값만 허용합니다. 입력값을 확인하세요.")
