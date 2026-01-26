# 자판기 직접 만들기
import time
import sys
from datetime import datetime

#------------------------------------------------ 제미나이가 알려준 잡기술 (실제로 타이핑 하는 느낌을 줌)
def typewriter(text, speed=0.0008):
    for char in text:
        sys.stdout.write(char) # 한 글자씩 출력
        sys.stdout.flush()     # 버퍼를 비워 즉시 화면에 표시
        time.sleep(speed)      # 다음 글자까지 대기 시간 (초 단위)
    print() # 마지막에 줄바꿈
#--------------------------------------------------
#전역변수 설정
run = True

book_writer = ["마이클 이스터", "유발하라리", "주언규", "요한 하리", "이랑주", "유현준", "최인철", "김상욱", "제임스 클리어"]
book_list = ["편안함의 습격", "넥서스(Nexus)", "슈퍼노멀", "도둑맞은 집중력", "오래가는 것들의 비밀", "공간의 미래", "굿 라이프", "떨림과 울림", "아주 작은 습관의 힘"]
book_quantity = [9, 1, 15, 20, 14, 4, 6, 8, 5]
book_price = [19800, 18000, 19500, 18800, 14220, 14400, 15300, 13500, 14400] #잔돈 거슬러줘야됨 아직 로직 추가전
payment = {
    "1": "카드결제(삼성페이, 애플페이)",
    "2": "현금결제",
    "3": "계좌이체(이체후 010-1234-5678로 연락 필요)"}
paytime = []
paycount = [] #
paycount_book = [] #아래 payno와 대응해서 사람들이 구매한 도서가 하나씩 추가된다.(관리자가 확인가능한 구매내역 버전)
payno = []         #결재가 이뤄진 번호 1에서부터 차례대로 올라간다
# 관리자 메뉴에서 사용할 변수들
ids = ["ksb"]
passwords = ["1234"]
names = ["김수빈"]
cellnums = ["010-7676-6059"]
session = None
adminnum = [1]
# 메뉴 구성
while run:
    mainMenu = f"""
===========================================
MBCA Book Vending Machine V.0112\033[33m
1. 편안함의 습격 - 마이클 이스터 [남은수량 : {book_quantity[0]} 권]
2. 넥서스(Nexus) - 유발하라리 [남은수량 : {book_quantity[1]} 권]
3. 슈퍼노멀 - 주언규 [남은수량 : {book_quantity[2]} 권]
4. 도둑맞은 집중력 - 요한 하리 [남은수량 : {book_quantity[3]} 권]
5. 오래가는 것들의 비밀 - 이랑주 [남은수량 : {book_quantity[4]} 권]
6. 공간의 미래 - 유현준 [남은수량 : {book_quantity[5]} 권]
7. 굿 라이프 - 최인철 [남은수량 : {book_quantity[6]} 권]
8. 떨림과 울림 - 김상욱 [남은수량 : {book_quantity[7]} 권]
9. 아주 작은 습관의 힘 - 제임스 클리어 [남은수량 : {book_quantity[8]} 권]\033[0m
0. 관리자&판매자 메뉴
q. 프로그램 종료
==========================================="""
    typewriter(mainMenu, 0.002)
    select = input("\n구매를 희망하시는 책을 선택해 주세요.")
    if book_quantity[0] == "품절":
        print("\n선택하신 책은 인기가 많아 품절되었습니다.\n빠르게 입고하겠습니다. 불편을 드려 죄송합니다.")
        time.sleep(1)
        continue
    if select == "1":
        typewriter(f'''\033[32m
       ___________________________ ___________________________
     _/                           Y                           \_
    //                            |                            \\
   //      책 제목:                |       글쓴이:                \\
  //       {book_list[0]:<14}     |       {book_writer[0]:<16}   \\
 //                               |                              \\
//_______________________________ | ______________________________\\
`---------------------------------^---------------------------------'\033[0m

마이클 이스터의 『편안함의 습격』은 인류가 생존을 위해 추구해 온 '안락함'이 현대에 이르러 오히려
비만, 우울증, 만성 질환의 원인이 되었다고 경고하며, 유전자에 각인된 야생성을 회복하기 위해 
의도적인 불편함을 삶에 들여야 한다고 강조합니다. 저자는 1년에 한 번 한계에 도전하는 '미소기', 
무거운 배낭을 메고 걷는 '러킹', 그리고 스마트폰 없는 고독과 지루함을 견디는 과정을 통해 
우리가 잃어버린 육체적·정신적 건강과 진정한 삶의 활력을 되찾을 수 있음을 보여줍니다.
''', 0.0008)
        if input("\n구매를 희망하시면 'y'키를,\n이전 메뉴로 돌아가시려면 다른키를 눌러주세요.") == "y":
            print(f'''
--------------------------
책 제목 : {book_list[0]}
저자 : {book_writer[0]}
가격 : {book_price[0]:,}원
남은 수량 : {book_quantity[0]}개''')
            if input("\n결제하시려면 'y'키를, 이전 메뉴로 돌아가려면 다른키를 눌러주세요.") == 'y':
                print("""
-------------------------------------------
1. 카드결제(삼성페이, 애플페이)
2. 현금결제
3. 계좌이제(이체후 010-1234-5678로 이체연락 필요)""")
                subSelect = input("\n결제수단을 선택하세요.")
                if subSelect in payment:
                    if input (f"\n선택하신 {payment[subSelect]}방식으로 결제후\n'Enter'키를 누르세요") == "":
                        pay = payment[subSelect]
                        paycount.append(pay)
                        paycount_book.append(book_list[0])
                        now = datetime.now()
                        formated_time = now.strftime("%Y-%m-%d %H:%M:%S")
                        paytime.append(formated_time)
                        payno += "1"
                        book_quantity[0] -= 1
                        if book_quantity[0] == 0:
                            book_quantity[0] = "품절" #리스트에서 특정 이벤트마다 값을 빼는 건 +=, -=로 거래숫자만큼 빼자
                        print(f'''
-------------------------------------------
선택하신 '{book_list[0]}'가 결제 완료되었습니다.
도서출구에서 도서를 받아주세요.
즐거운 독서 되세요 ^~^
''')
                        time.sleep(2)
                else:
                    print("\n올바른 결제가 아닙니다. 이전 메뉴로 돌아갑니다.")
            else:
                print("\n결제를 취소합니다.")
                time.sleep(1)
        else:
            print("\n이전 메뉴로 돌아갑니다.")
            time.sleep(1)
#2번째 책 구매============================================================================================
    elif select == "2":
        if book_quantity[1] == "품절":
            print("\n선택하신 책은 인기가 많아 품절되었습니다.\n빠르게 입고하겠습니다. 불편을 드려 죄송합니다.")
            time.sleep(1)
            continue
        typewriter(f'''\033[32m
       ___________________________ ___________________________
     _/                           Y                           \_
    //                            |                            \\
   //      책 제목:                |       글쓴이:                \\
  //       {book_list[1]:<15}     |       {book_writer[1]:<17}   \\
 //                               |                              \\
//_______________________________ | ______________________________\\
`---------------------------------^---------------------------------'\033[0m

유발 하라리의 저서 『넥서스(Nexus)』는 인류 역사를 '정보 네트워크'의 관점에서 재해석하며, 
현대의 인공지능(AI)이 과거의 정보 기술(인쇄기, 라디오 등)과 달리 스스로 결정을 내리고 
새로운 아이디어를 창조할 수 있는 '유사 타자(Alien Presence)'라는 점에 주목합니다. 
하라리는 정보가 단순히 진실을 전달하는 수단이 아니라 사람들을 연결해 질서를 만드는 
도구였음을 지적하며, 통제를 벗어난 실리콘 알고리즘이 민주주의의 근간인 대화를 파괴하고 
전체주의적 감시 체계를 강화함으로써 인류 문명에 실존적 위기를 초래할 수 있다고 경고합니다.
''')
        #구매를 희망하면 아래 번호에 맞는 리스트에서 호출
        if input("\n구매를 희망하시면 'y'키를,\n이전 메뉴로 돌아가시려면 다른키를 눌러주세요.") == "y":
            print(f'''
--------------------------
책 제목 : {book_list[1]}
저자 : {book_writer[1]}
가격 : {book_price[1]:,}원
남은 수량 : {book_quantity[1]}개''') #가격의 표현식은 파이썬 3.6부터 지원한다고 하는데, 저렇게 표현하면 알아서 뒤에서 세자리마다 콤마가 찍힌다.
            if input("\n결제하시려면 'y'키를, 이전 메뉴로 돌아가려면 다른키를 눌러주세요.") == 'y':
                print("""
-------------------------------------------
1. 카드결제(삼성페이, 애플페이)
2. 현금결제
3. 계좌이제(이체후 010-1234-5678로 이체연락 필요)""")
                subSelect = input("\n결제수단을 선택하세요.") #전역변수에서 미리 딕셔너리로 결제방식을 만들어 두었다.
                if subSelect in payment: #입력받은 값이 딕셔너리 키에 있으면
                    if input(f"\n선택하신 {payment[subSelect]}방식으로 결제후\n'Enter'키를 누르세요") == "": #그 키에 맞는 밸류를 가져오고
                        pay = payment[subSelect]
                        paycount.append(pay)
                        paycount_book.append(book_list[1])
                        now = datetime.now()
                        formated_time = now.strftime("%Y-%m-%d %H:%M:%S")
                        paytime.append(formated_time)
                        payno += "1"
                        book_quantity[1] -= 1 #구매가 이뤄질경우 -1씩 내려감 품절로 바뀌었을 때 계산을 하지 못하는 로직도 필요
                        print(book_quantity[1])
                        if book_quantity[1] == 0:
                            book_quantity[1] = "품절" #리스트에서 특정 이벤트마다 값을 빼는 건 +=, -=로 거래숫자만큼 빼자
                            print(book_quantity[1])
                        print(f'''
-------------------------------------------
선택하신 '{book_list[1]}'가 결제 완료되었습니다.
도서출구에서 도서를 받아주세요.
즐거운 독서 되세요 ^~^
''')
                        time.sleep(2)
                else:
                    print("\n올바른 결제가 아닙니다. 이전 메뉴로 돌아갑니다.")
            else:
                print("\n결제를 취소합니다.")
                time.sleep(1)
        else:
            print("\n이전 메뉴로 돌아갑니다.")
            time.sleep(1)
# 3번째 책 구매============================================================================================
    elif select == "3":
        if book_quantity[2] == "품절":
            print("\n선택하신 책은 인기가 많아 품절되었습니다.\n빠르게 입고하겠습니다. 불편을 드려 죄송합니다.")
            time.sleep(1)
            continue
        typewriter(f'''\033[32m
       ___________________________ ___________________________
     _/                           Y                           \_
    //                            |                            \\
   //      책 제목:                |       글쓴이:                \\
  //       {book_list[2]:<16}     |       {book_writer[2]:<17}   \\
 //                               |                              \\
//_______________________________ | ______________________________\\
`---------------------------------^---------------------------------'\033[0m

주언규의 저서『슈퍼노멀(Super Normal)』은 평범한 사람이 압도적인 성과를 내는 
'슈퍼노멀'이 되기 위한 구체적인 방법론을 제시하며, 운의 영역을 인정하되 실패의 리스크를 
최소화하는 '확률 게임'의 전략을 강조합니다. 저자는 무모한 도전 대신 성공한 사례를 
철저히 분석하여 핵심 요소를 분해하고, 자신의 상황에 맞게 복제하여 아주 작은 단위로 
여러 번 시도함으로써 성공 확률을 높이는 '돌연변이 전략'을 핵심으로 꼽습니다. 
결과적으로 이 책은 막연한 열정보다는 냉철한 데이터 분석과 반복적인 실행을 통해 
평범함의 범주를 벗어나 경제적 자유와 성취를 얻는 실천적인 로드맵을 제공합니다.
''')
        #구매를 희망하면 아래 번호에 맞는 리스트에서 호출
        if input("\n구매를 희망하시면 'y'키를,\n이전 메뉴로 돌아가시려면 다른키를 눌러주세요.") == "y":
            print(f'''
--------------------------
책 제목 : {book_list[2]}
저자 : {book_writer[2]}
가격 : {book_price[2]:,}원
남은 수량 : {book_quantity[2]}개''') #가격의 표현식은 파이썬 3.6부터 지원한다고 하는데, 저렇게 표현하면 알아서 뒤에서 세자리마다 콤마가 찍힌다.
            if input("\n결제하시려면 'y'키를, 이전 메뉴로 돌아가려면 다른키를 눌러주세요.") == 'y':
                print("""
-------------------------------------------
1. 카드결제(삼성페이, 애플페이)
2. 현금결제
3. 계좌이제(이체후 010-1234-5678로 이체연락 필요)""")
                subSelect = input("\n결제수단을 선택하세요.") #전역변수에서 미리 딕셔너리로 결제방식을 만들어 두었다.
                if subSelect in payment: #입력받은 값이 딕셔너리 키에 있으면
                    if input(f"\n선택하신 {payment[subSelect]}방식으로 결제후\n'Enter'키를 누르세요") == "": #그 키에 맞는 밸류를 가져오고
                        pay = payment[subSelect]
                        paycount.append(pay)
                        paycount_book.append(book_list[2])
                        now = datetime.now()
                        formated_time = now.strftime("%Y-%m-%d %H:%M:%S")
                        paytime.append(formated_time)
                        payno += "1"
                        book_quantity[2] -= 1 #구매가 이뤄질경우 -1씩 내려감
                        if book_quantity[2] == 0:
                            book_quantity[2] = "품절" #리스트에서 특정 이벤트마다 값을 빼는 건 +=, -=로 거래숫자만큼 빼자
                        print(f'''
-------------------------------------------
선택하신 '{book_list[2]}'가 결제 완료되었습니다.
도서출구에서 도서를 받아주세요.
즐거운 독서 되세요 ^~^
''')
                        time.sleep(2)
                else:
                    print("\n올바른 결제가 아닙니다. 이전 메뉴로 돌아갑니다.")
            else:
                print("\n결제를 취소합니다.")
                time.sleep(1)
        else:
            print("\n이전 메뉴로 돌아갑니다.")
            time.sleep(1)
# 4번째 책 구매============================================================================================
    elif select == "4":
        if book_quantity[3] == "품절":
            print("\n선택하신 책은 인기가 많아 품절되었습니다.\n빠르게 입고하겠습니다. 불편을 드려 죄송합니다.")
            time.sleep(1)
            continue
        typewriter(f'''\033[32m
       ___________________________ ___________________________
     _/                           Y                           \_
    //                            |                            \\
   //      책 제목:                |       글쓴이:                \\
  //       {book_list[3]:<14}     |       {book_writer[3]:<17}   \\
 //                               |                              \\
//_______________________________ | ______________________________\\
`---------------------------------^---------------------------------'\033[0m

요한 하리의 저서 『도둑맞은 집중력』(Stolen Focus)은 현대인이 겪는 집중력 저하가 
개인의 의지력 부족 때문이 아니라, 주의력을 약탈하여 이윤을 남기는 빅테크 기업의 비즈니스 
모델과 만성적인 수면 부족, 과도한 멀티태스킹 등 사회적 시스템에 의해 설계된 '도둑맞은' 
결과라고 지적합니다. 저자는 우리가 몰입(Flow)을 잃어버리고 사소한 자극에 끊임없이 
분산되는 환경에 처해 있음을 강조하며, 이를 해결하기 위해서는 개인적인 디지털 디톡스를 
넘어 테크 기업의 알고리즘 규제와 노동 환경 개선 같은 사회적 차원의 '반격'이 필요하다고 
역설합니다.''')
        # 구매를 희망하면 아래 번호에 맞는 리스트에서 호출
        if input("\n구매를 희망하시면 'y'키를,\n이전 메뉴로 돌아가시려면 다른키를 눌러주세요.") == "y":
            print(f'''
--------------------------
책 제목 : {book_list[3]}
저자 : {book_writer[3]}
가격 : {book_price[3]:,}원
남은 수량 : {book_quantity[3]}개''')  # 가격의 표현식은 파이썬 3.6부터 지원한다고 하는데, 저렇게 표현하면 알아서 뒤에서 세자리마다 콤마가 찍힌다.
            if input("\n결제하시려면 'y'키를, 이전 메뉴로 돌아가려면 다른키를 눌러주세요.") == 'y':
                print("""
-------------------------------------------
1. 카드결제(삼성페이, 애플페이)
2. 현금결제
3. 계좌이제(이체후 010-1234-5678로 이체연락 필요)""")
                subSelect = input("\n결제수단을 선택하세요.")  # 전역변수에서 미리 딕셔너리로 결제방식을 만들어 두었다.
                if subSelect in payment:  # 입력받은 값이 딕셔너리 키에 있으면
                    if input(f"\n선택하신 {payment[subSelect]}방식으로 결제후\n'Enter'키를 누르세요") == "":  # 그 키에 맞는 밸류를 가져오고
                        pay = payment[subSelect]
                        paycount.append(pay)
                        paycount_book.append(book_list[3])
                        now = datetime.now()
                        formated_time = now.strftime("%Y-%m-%d %H:%M:%S")
                        paytime.append(formated_time)
                        payno += "1"
                        book_quantity[3] -= 1  # 구매가 이뤄질경우 -1씩 내려감
                        if book_quantity[3] == 0:
                            book_quantity[3] = "품절"  # 리스트에서 특정 이벤트마다 값을 빼는 건 +=, -=로 거래숫자만큼 빼자
                        print(f'''
-------------------------------------------
선택하신 '{book_list[3]}'가 결제 완료되었습니다.
도서출구에서 도서를 받아주세요.
즐거운 독서 되세요 ^~^
''')
                        time.sleep(2)
                else:
                    print("\n올바른 결제가 아닙니다. 이전 메뉴로 돌아갑니다.")
            else:
                print("\n결제를 취소합니다.")
                time.sleep(1)
        else:
            print("\n이전 메뉴로 돌아갑니다.")
            time.sleep(1)
#5번째 책 구매===============================================================================================
    elif select == "5":
        if book_quantity[4] == "품절":
            print("\n선택하신 책은 인기가 많아 품절되었습니다.\n빠르게 입고하겠습니다. 불편을 드려 죄송합니다.")
            time.sleep(1)
            continue
        typewriter(f'''\033[32m
       ___________________________ ___________________________
     _/                           Y                           \_
    //                            |                            \\
   //      책 제목:                |       글쓴이:                \\
  //       {book_list[4]:<13}     |       {book_writer[4]:<17}   \\
 //                               |                              \\
//_______________________________ | ______________________________\\
`---------------------------------^---------------------------------'\033[0m

이랑주의 저서 『오래가는 것들의 비밀』은 잊히지 않고 오랫동안 살아남는 브랜드와 장소들의 
공통점을 분석하며, 사람의 마음을 끄는 결정적 차이는 화려한 기술이 아닌 
'본질에 집중한 디테일'에 있다고 강조합니다. 저자는 시각적인 연출부터 조명, 색상, 그리고 
고객의 동선에 이르기까지 사람의 오감을 자극하는 구체적인 법칙들을 제시하며, 유행에 민감하게 
반응하기보다 브랜드만의 고유한 철학과 진정성을 시각적으로 어떻게 구현할 것인가에 대한 
실무적인 통찰을 제공합니다. 결국 '오래가는 것'은 단순히 물건을 파는 것이 아니라 고객에게 
잊지 못할 경험과 가치를 전달하는 것임을 일깨워주는 책입니다.''')
        # 구매를 희망하면 아래 번호에 맞는 리스트에서 호출
        if input("\n구매를 희망하시면 'y'키를,\n이전 메뉴로 돌아가시려면 다른키를 눌러주세요.") == "y":
            print(f'''
--------------------------
책 제목 : {book_list[4]}
저자 : {book_writer[4]}
가격 : {book_price[4]:,}원
남은 수량 : {book_quantity[4]}개''')  # 가격의 표현식은 파이썬 3.6부터 지원한다고 하는데, 저렇게 표현하면 알아서 뒤에서 세자리마다 콤마가 찍힌다.
            if input("\n결제하시려면 'y'키를, 이전 메뉴로 돌아가려면 다른키를 눌러주세요.") == 'y':
                print("""
-------------------------------------------
1. 카드결제(삼성페이, 애플페이)
2. 현금결제
3. 계좌이제(이체후 010-1234-5678로 이체연락 필요)""")
                subSelect = input("\n결제수단을 선택하세요.")  # 전역변수에서 미리 딕셔너리로 결제방식을 만들어 두었다.
                if subSelect in payment:  # 입력받은 값이 딕셔너리 키에 있으면
                    if input(f"\n선택하신 {payment[subSelect]}방식으로 결제후\n'Enter'키를 누르세요") == "":  # 그 키에 맞는 밸류를 가져오고
                        pay = payment[subSelect]
                        paycount.append(pay)
                        paycount_book.append(book_list[4])
                        now = datetime.now()
                        formated_time = now.strftime("%Y-%m-%d %H:%M:%S")
                        paytime.append(formated_time)
                        payno += "1"
                        book_quantity[4] -= 1  # 구매가 이뤄질경우 -1씩 내려감
                        if book_quantity[4] == 0:
                            book_quantity[4] = "품절"  # 리스트에서 특정 이벤트마다 값을 빼는 건 +=, -=로 거래숫자만큼 빼자
                        print(f'''
-------------------------------------------
선택하신 '{book_list[4]}'가 결제 완료되었습니다.
도서출구에서 도서를 받아주세요.
즐거운 독서 되세요 ^~^
''')
                        time.sleep(2)
                else:
                    print("\n올바른 결제가 아닙니다. 이전 메뉴로 돌아갑니다.")
            else:
                print("\n결제를 취소합니다.")
                time.sleep(1)
        else:
            print("\n이전 메뉴로 돌아갑니다.")
            time.sleep(1)
# 6번째 책 구매===============================================================================================
    elif select == "6":
        if book_quantity[5] == "품절":
            print("\n선택하신 책은 인기가 많아 품절되었습니다.\n빠르게 입고하겠습니다. 불편을 드려 죄송합니다.")
            time.sleep(1)
            continue
        typewriter(f'''\033[32m
       ___________________________ ___________________________
     _/                           Y                           \_
    //                            |                            \\
   //      책 제목:                |       글쓴이:                \\
  //       {book_list[5]:<15}     |       {book_writer[5]:<17}   \\
 //                               |                              \\
//_______________________________ | ______________________________\\
`---------------------------------^---------------------------------'\033[0m

유현준 교수의 저서 『공간의 미래』는 코로나19 팬데믹 이후 급격하게 변화한 우리의 일상과 
그에 따른 주거, 학교, 오피스, 도시의 변화 방향을 인문학적 시선으로 분석한 책입니다. 
저자는 비대면 기술의 발전이 공간의 기능을 재정의하고 있음을 지적하며, 단순히 기술적인 
대응을 넘어 인간의 존엄성을 지키고 사회적 소통을 활성화할 수 있는 새로운 공간 
디자인(예: 테라스가 있는 아파트, 공원과 연결된 학교 등)이 필요하다고 강조합니다. 
결국 이 책은 미래의 공간이 사람과 사람 사이의 관계를 어떻게 다시 연결하고 권력의 집중을 
분산시켜 더 행복한 공동체를 만들 수 있을지에 대한 실천적인 비전을 제시합니다.
''')# 구매를 희망하면 아래 번호에 맞는 리스트에서 호출
        if input("\n구매를 희망하시면 'y'키를,\n이전 메뉴로 돌아가시려면 다른키를 눌러주세요.") == "y":
            print(f'''
--------------------------
책 제목 : {book_list[5]}
저자 : {book_writer[5]}
가격 : {book_price[5]:,}원
남은 수량 : {book_quantity[5]}개''')  # 가격의 표현식은 파이썬 3.6부터 지원한다고 하는데, 저렇게 표현하면 알아서 뒤에서 세자리마다 콤마가 찍힌다.
            if input("\n결제하시려면 'y'키를, 이전 메뉴로 돌아가려면 다른키를 눌러주세요.") == 'y':
                print("""
-------------------------------------------
1. 카드결제(삼성페이, 애플페이)
2. 현금결제
3. 계좌이제(이체후 010-1234-5678로 이체연락 필요)""")
                subSelect = input("\n결제수단을 선택하세요.")  # 전역변수에서 미리 딕셔너리로 결제방식을 만들어 두었다.
                if subSelect in payment:  # 입력받은 값이 딕셔너리 키에 있으면
                    if input(f"\n선택하신 {payment[subSelect]}방식으로 결제후\n'Enter'키를 누르세요") == "":  # 그 키에 맞는 밸류를 가져오고
                        pay = payment[subSelect]
                        paycount.append(pay)
                        paycount_book.append(book_list[5])
                        now = datetime.now()
                        formated_time = now.strftime("%Y-%m-%d %H:%M:%S")
                        paytime.append(formated_time)
                        payno += "1"
                        book_quantity[5] -= 1  # 구매가 이뤄질경우 -1씩 내려감
                        if book_quantity[5] == 0:
                            book_quantity[5] = "품절"  # 리스트에서 특정 이벤트마다 값을 빼는 건 +=, -=로 거래숫자만큼 빼자
                        print(f'''
-------------------------------------------
선택하신 '{book_list[5]}'가 결제 완료되었습니다.
도서출구에서 도서를 받아주세요.
즐거운 독서 되세요 ^~^''')
                        time.sleep(2)
                else:
                    print("\n올바른 결제가 아닙니다. 이전 메뉴로 돌아갑니다.")
            else:
                print("\n결제를 취소합니다.")
                time.sleep(1)
        else:
            print("\n이전 메뉴로 돌아갑니다.")
            time.sleep(1)
# 7번째 책 구매===============================================================================================
    elif select == "7":
        if book_quantity[6] == "품절":
            print("\n선택하신 책은 인기가 많아 품절되었습니다.\n빠르게 입고하겠습니다. 불편을 드려 죄송합니다.")
            time.sleep(1)
            continue
        typewriter(f'''\033[32m
       ___________________________ ___________________________
     _/                           Y                           \_
    //                            |                            \\
   //      책 제목:                |       글쓴이:                \\
  //       {book_list[6]:<15}     |       {book_writer[6]:<18}   \\
 //                               |                              \\
//_______________________________ | ______________________________\\
`---------------------------------^---------------------------------'\033[0m

최인철 교수의 저서 『굿 라이프』는 행복을 단순한 '기분'이나 '쾌락'으로만 보는 좁은 
관점에서 벗어나, 삶의 의미와 목적, 그리고 성숙한 태도가 조화를 이루는 상태로서의 
행복을 인문학적이고 심리학적인 시선으로 탐구합니다. 저자는 행복한 삶이란 고통이 전혀 
없는 상태가 아니라, 나답게 살 수 있게 해주는 '자기다움'을 실현하고 타인과의 건강한 
관계 속에서 충만함을 느끼는 과정임을 강조합니다. 결국 이 책은 어떻게 하면 순간의 
즐거움을 넘어 우리 삶의 격을 높이고, 자신만의 가치를 실현하는 '좋은 삶'을 설계할 수 
있을지에 대한 실천적이고 지혜로운 지침을 제공합니다.
''')  # 구매를 희망하면 아래 번호에 맞는 리스트에서 호출
        if input("\n구매를 희망하시면 'y'키를,\n이전 메뉴로 돌아가시려면 다른키를 눌러주세요.") == "y":
            print(f'''
--------------------------
책 제목 : {book_list[6]}
저자 : {book_writer[6]}
가격 : {book_price[6]:,}원
남은 수량 : {book_quantity[6]}개''')  # 가격의 표현식은 파이썬 3.6부터 지원한다고 하는데, 저렇게 표현하면 알아서 뒤에서 세자리마다 콤마가 찍힌다.
            if input("\n결제하시려면 'y'키를, 이전 메뉴로 돌아가려면 다른키를 눌러주세요.") == 'y':
                print("""
-------------------------------------------
1. 카드결제(삼성페이, 애플페이)
2. 현금결제
3. 계좌이제(이체후 010-1234-5678로 이체연락 필요)""")
                subSelect = input("\n결제수단을 선택하세요.")  # 전역변수에서 미리 딕셔너리로 결제방식을 만들어 두었다.
                if subSelect in payment:  # 입력받은 값이 딕셔너리 키에 있으면
                    if input(f"\n선택하신 {payment[subSelect]}방식으로 결제후\n'Enter'키를 누르세요") == "":  # 그 키에 맞는 밸류를 가져오고
                        pay = payment[subSelect]
                        paycount.append(pay)
                        paycount_book.append(book_list[6])
                        now = datetime.now()
                        formated_time = now.strftime("%Y-%m-%d %H:%M:%S")
                        paytime.append(formated_time)
                        payno += "1"
                        book_quantity[6] -= 1  # 구매가 이뤄질경우 -1씩 내려감
                        if book_quantity[6] == 0:
                            book_quantity[6] = "품절"  # 리스트에서 특정 이벤트마다 값을 빼는 건 +=, -=로 거래숫자만큼 빼자
                        print(f'''
-------------------------------------------
선택하신 '{book_list[6]}'가 결제 완료되었습니다.
도서출구에서 도서를 받아주세요.
즐거운 독서 되세요 ^~^''')
                        time.sleep(2)
                else:
                    print("\n올바른 결제가 아닙니다. 이전 메뉴로 돌아갑니다.")
            else:
                print("\n결제를 취소합니다.")
                time.sleep(1)
        else:
            print("\n이전 메뉴로 돌아갑니다.")
            time.sleep(1)
# 8번째 책 구매===============================================================================================
    elif select == "8":
        if book_quantity[7] == "품절":
            print("\n선택하신 책은 인기가 많아 품절되었습니다.\n빠르게 입고하겠습니다. 불편을 드려 죄송합니다.")
            time.sleep(1)
            continue
        typewriter(f'''\033[32m
       ___________________________ ___________________________
     _/                           Y                           \_
    //                            |                            \\
   //      책 제목:                |       글쓴이:                \\
  //       {book_list[7]:<15}     |       {book_writer[7]:<18}   \\
 //                               |                              \\
//_______________________________ | ______________________________\\
`---------------------------------^---------------------------------'\033[0m

김상욱 교수의 저서 『떨림과 울림』은 차갑게만 느껴지는 물리학의 법칙들을 통해 
인간과 세상을 바라보는 따뜻하고 인문학적인 시선을 담은 책입니다. 
저자는 빛, 시공간, 원자, 엔트로피 등 물리학의 핵심 개념들이 단순히 수식에 머무는 것이 아니라, 
존재의 근원을 설명하고 타인과의 소통(울림)을 이해하는 도구가 될 수 있음을 보여줍니다. 
결국 이 책은 우주의 무심한 법칙 속에서도 의미를 찾아내려는 인간의 노력을 '떨림'으로 정의하며, 
과학이 어떻게 우리의 삶을 더 깊이 있게 이해하고 위로할 수 있는지를 아름다운 문체로 풀어냅니다.
''')  # 구매를 희망하면 아래 번호에 맞는 리스트에서 호출
        if input("\n구매를 희망하시면 'y'키를,\n이전 메뉴로 돌아가시려면 다른키를 눌러주세요.") == "y":
            print(f'''
--------------------------
책 제목 : {book_list[7]}
저자 : {book_writer[7]}
가격 : {book_price[7]:,}원
남은 수량 : {book_quantity[7]}개''')  # 가격의 표현식은 파이썬 3.6부터 지원한다고 하는데, 저렇게 표현하면 알아서 뒤에서 세자리마다 콤마가 찍힌다.
            if input("\n결제하시려면 'y'키를, 이전 메뉴로 돌아가려면 다른키를 눌러주세요.") == 'y':
                print("""
-------------------------------------------
1. 카드결제(삼성페이, 애플페이)
2. 현금결제
3. 계좌이제(이체후 010-1234-5678로 이체연락 필요)""")
                subSelect = input("\n결제수단을 선택하세요.")  # 전역변수에서 미리 딕셔너리로 결제방식을 만들어 두었다.
                if subSelect in payment:  # 입력받은 값이 딕셔너리 키에 있으면
                    if input(f"\n선택하신 {payment[subSelect]}방식으로 결제후\n'Enter'키를 누르세요") == "":  # 그 키에 맞는 밸류를 가져오고
                        pay = payment[subSelect]
                        paycount.append(pay)
                        paycount_book.append(book_list[7])
                        now = datetime.now()
                        formated_time = now.strftime("%Y-%m-%d %H:%M:%S")
                        paytime.append(formated_time)
                        payno += "1"
                        book_quantity[7] -= 1  # 구매가 이뤄질경우 -1씩 내려감
                        if book_quantity[7] == 0:
                            book_quantity[7] = "품절"  # 리스트에서 특정 이벤트마다 값을 빼는 건 +=, -=로 거래숫자만큼 빼자
                        print(f'''
-------------------------------------------
선택하신 '{book_list[7]}'가 결제 완료되었습니다.
도서출구에서 도서를 받아주세요.
즐거운 독서 되세요 ^~^''')
                        time.sleep(2)
                else:
                    print("\n올바른 결제가 아닙니다. 이전 메뉴로 돌아갑니다.")
            else:
                print("\n결제를 취소합니다.")
                time.sleep(1)
        else:
            print("\n이전 메뉴로 돌아갑니다.")
            time.sleep(1)
# 9번째 책 구매===============================================================================================
    elif select == "9":
        if book_quantity[8] == "품절":
            print("\n선택하신 책은 인기가 많아 품절되었습니다.\n빠르게 입고하겠습니다. 불편을 드려 죄송합니다.")
            time.sleep(1)
            continue
        typewriter(f'''\033[32m
       ___________________________ ___________________________
     _/                           Y                           \_
    //                            |                            \\
   //      책 제목:                |       글쓴이:                \\
  //       {book_list[8]:<13}     |       {book_writer[8]:<16}   \\
 //                               |                              \\
//_______________________________ | ______________________________\\
`---------------------------------^---------------------------------'\033[0m

제임스 클리어의 저서 『아주 작은 습관의 힘』(Atomic Habits)은 거대한 변화를 
목표로 삼기보다 매일 '1%의 성장'을 만드는 사소한 습관의 반복이 어떻게 삶을 근본적으로 
바꾸는지를 과학적 근거와 함께 설명합니다. 저자는 습관을 형성하는 
4단계 법칙(신호, 갈망, 반응, 보상)을 통해 의지력에만 의존하지 않고 시스템을 설계하여 
좋은 습관은 '하기 쉽게', 나쁜 습관은 '하기 어렵게' 만드는 구체적인 전략을 제시합니다. 
결국 이 책은 원자(Atomic)만큼 작은 습관들이 쌓여 복리 효과를 낼 때, 평범한 개인도 
놀라운 정체성의 변화와 실질적인 성취를 이룰 수 있음을 강조합니다.
''')  # 구매를 희망하면 아래 번호에 맞는 리스트에서 호출
        if input("\n구매를 희망하시면 'y'키를,\n이전 메뉴로 돌아가시려면 다른키를 눌러주세요.") == "y":
            print(f'''
--------------------------
책 제목 : {book_list[8]}
저자 : {book_writer[8]}
가격 : {book_price[8]:,}원
남은 수량 : {book_quantity[8]}개''')  # 가격의 표현식은 파이썬 3.6부터 지원한다고 하는데, 저렇게 표현하면 알아서 뒤에서 세자리마다 콤마가 찍힌다.
            if input("\n결제하시려면 'y'키를, 이전 메뉴로 돌아가려면 다른키를 눌러주세요.") == 'y':
                print("""
-------------------------------------------
1. 카드결제(삼성페이, 애플페이)
2. 현금결제
3. 계좌이제(이체후 010-1234-5678로 이체연락 필요)""")
                subSelect = input("\n결제수단을 선택하세요.")  # 전역변수에서 미리 딕셔너리로 결제방식을 만들어 두었다.
                if subSelect in payment:  # 입력받은 값이 딕셔너리 키에 있으면
                    if input(f"\n선택하신 {payment[subSelect]}방식으로 결제후\n'Enter'키를 누르세요") == "":  # 그 키에 맞는 밸류를 가져오고
                        pay = payment[subSelect]
                        paycount.append(pay)
                        paycount_book.append(book_list[8])
                        now = datetime.now()
                        formated_time = now.strftime("%Y-%m-%d %H:%M:%S")
                        paytime.append(formated_time)
                        payno += "1"
                        book_quantity[8] -= 1  # 구매가 이뤄질경우 -1씩 내려감
                        if book_quantity[8] == 0:
                            book_quantity[8] = "품절"  # 리스트에서 특정 이벤트마다 값을 빼는 건 +=, -=로 거래숫자만큼 빼자
                        print(f'''
-------------------------------------------
선택하신 '{book_list[8]}'가 결제 완료되었습니다.
도서출구에서 도서를 받아주세요.
즐거운 독서 되세요 ^~^''')
                        time.sleep(2)
                else:
                    print("\n올바른 결제가 아닙니다. 이전 메뉴로 돌아갑니다.")
            else:
                print("\n결제를 취소합니다.")
                time.sleep(1)
        else:
            print("\n이전 메뉴로 돌아갑니다.")
            time.sleep(1)
# 관리자 메뉴===============================================================================================
    elif select == "0":
        subrun = True
        while subrun:
            print(f'''
관리자 메뉴에 진입하셨습니다.
원하는 메뉴를 선택하세요.
1. 관리자 회원가입
2. 관리자 로그인
3. 재고관리
4. 거내래역 보기
9. 관리자 메뉴 나가기
''')
            if session is not None:
                print(f"\033[33m{names[session]}님 관리자 계정으로 로그인중\033[0m")
            subSelect = input("\n이용하시려는 메뉴를 선택하세요.")
# 0 - 1 회원가입 메뉴--------------------------------------------------------------------------------------
            if subSelect == "1":
                print("\n관리자 회원가입 메뉴에 진입하셨습니다.")
                while True:
                    id = input("아이디 : ")
                    if id in ids:
                        print("\n이미 존재하는 아이디입니다.\n회원 메뉴로 돌아갑니다.")
                        time.sleep(1)
                        break
                    else:
                        pw = input("비밀번호 : ")
                        name = input("이름 : ")
                        cellnum = input("연락처 : 000-0000-0000 '-'포함 14자리") #정확하게 입력하지 않으면 돌아가는 로직 만들기
                        print(f"\n입력하신 정보를 확인하세요\n이름 : {name} | 아이디 : {id} | 연락처 : {cellnum}")
                        if input("가입하시겠습니까? (y/n)").lower() == "y":
                            names.append(name)
                            ids.append(id)
                            cellnums.append(cellnum)
                            passwords.append(pw)
                            if not adminnum:
                                an = 1
                                print("\n회원가입이 완료되었습니다.\n메뉴로 돌아갑니다. 로그인 해주세요.")
                                time.sleep(1)
                                break
                            else:
                                last_an = an[-1]   #마지막 가입한 회원 번호 찾아서
                                anx = last_an + 1   #변수 하나 만들고 마지막번호에 +1 해라
                                adminnum.append(anx)  #+1한 값을 관리자번호에 추가해라
                                print("\n회원가입이 완료되었습니다.\n메뉴로 돌아갑니다. 로그인해주세요.")
                                time.sleep(1)
                                break
# 0-2 회원로그인 메뉴 -----------------------------------------------------------------------------------
            elif subSelect == "2":
                print("\n로그인 메뉴에 진입하셨습니다.")
                while True:
                    id = input("아이디를 입력하세요 :")
                    if id in ids:
                        idx = ids.index(id)
                        while True:
                            pw = input("패스워드를 입력하세요 :")
                            if passwords[idx] == pw:
                                session = idx
                                print(f"\n{names[idx]}님 로그인 성공")
                                time.sleep(1)
                                break
                            else:
                                print("\n입력한 패스워드가 맞지 않습니다.\n다시 입력하세요.")
                    else:
                        print("\n입력한 ID는 회원가입 되어있지 않습니다.")
                        time.sleep(1)
                    break
# 0-3 재고관리 메뉴 -----------------------------------------------------------------------------------
            elif subSelect == "3":
                if session is None:
                    print(f"\033[33m로그인 후 이용가능한 서비스입니다.\033[0m")
                    time.sleep(1)
                    continue
                elif session is not None:
                    print(f"\033[33m{names[session]}님 관리자 계정으로 로그인중\033[0m")
                print("\n재고관리 메뉴에 진입하셨습니다.")
                print(f"""
1. 편안함의 습격 \033[33m[남은수량 : {book_quantity[0]} 권]\033[0m
2. 넥서스(Nexus) \033[33m[남은수량 : {book_quantity[1]} 권]\033[0m
3. 슈퍼노멀 \033[33m[남은수량 : {book_quantity[2]} 권]\033[0m
4. 도둑맞은 집중력 \033[33m[남은수량 : {book_quantity[3]} 권]\033[0m
5. 오래가는 것들의 비밀 \033[33m[남은수량 : {book_quantity[4]} 권]\033[0m
6. 공간의 미래 \033[33m[남은수량 : {book_quantity[5]} 권]\033[0m
7. 굿 라이프 \033[33m[남은수량 : {book_quantity[6]} 권]\033[0m
8. 떨림과 울림 \033[33m[남은수량 : {book_quantity[7]} 권]\033[0m
9. 아주 작은 습관의 힘 \033[33m[남은수량 : {book_quantity[8]} 권]\033[0m""")
                sn = input("\n재고를 수정하려는 도서를 선택하세요(1~9)")
                if sn == "1": # 1번 도서 수정
                    print(f"{book_list[0]} 도서를 수정합니다.")
                    while True:
                        try:
                            fixquantity = int(input("\n보충하려는 갯수를 입력하세요."))
                            new_quantity = fixquantity + book_quantity[0]
                            if new_quantity > 0:
                                book_quantity[0] = new_quantity
                                print(f"\n{book_list[0]}번 도서\n{fixquantity}개 보충되어\n최종{book_quantity[0]}개 잔량입니다.")
                                time.sleep(1)
                                break
                            else:
                                print("\n입력한 값이 잘못 되었거나 재고가 없습니다.\n입력값을 확인해주세요.")
                        except ValueError:
                            print("\n숫자가 아닌 값이 입력되었습니다. 양의 정수를 입력해주세요.")
                elif sn == "2": # 2번 도서 수정
                    print(f"{book_list[1]} 도서를 수정합니다.")
                    while True:
                        try:
                            fixquantity = int(input("\n보충하려는 갯수를 입력하세요."))
                            new_quantity = fixquantity + book_quantity[1]
                            if new_quantity > 0:
                                book_quantity[1] = new_quantity
                                print(f"\n{book_list[1]}번 도서\n{fixquantity}개 보충되어\n최종{book_quantity[1]}개 잔량입니다.")
                                time.sleep(1)
                                break
                            else:
                                print("\n입력한 값이 잘못 되었거나 재고가 없습니다.\n입력값을 확인해주세요.")
                        except ValueError:
                            print("\n숫자가 아닌 값이 입력되었습니다. 양의 정수를 입력해주세요.")
                elif sn == "3": # 3번 도서 수정
                    print(f"{book_list[2]} 도서를 수정합니다.")
                    while True:
                        try:
                            fixquantity = int(input("\n보충하려는 갯수를 입력하세요."))
                            new_quantity = fixquantity + book_quantity[2]
                            if new_quantity > 0:
                                book_quantity[2] = new_quantity
                                print(f"\n{book_list[2]}번 도서\n{fixquantity}개 보충되어\n최종{book_quantity[2]}개 잔량입니다.")
                                time.sleep(1)
                                break
                            else:
                                print("\n입력한 값이 잘못 되었거나 재고가 없습니다.\n입력값을 확인해주세요.")
                        except ValueError:
                            print("\n숫자가 아닌 값이 입력되었습니다. 양의 정수를 입력해주세요.")
                elif sn == "4": # 4번 도서 수정
                    print(f"{book_list[3]} 도서를 수정합니다.")
                    while True:
                        try:
                            fixquantity = int(input("\n보충하려는 갯수를 입력하세요."))
                            new_quantity = fixquantity + book_quantity[3]
                            if new_quantity > 0:
                                book_quantity[3] = new_quantity
                                print(f"\n{book_list[3]}번 도서\n{fixquantity}개 보충되어\n최종{book_quantity[3]}개 잔량입니다.")
                                time.sleep(1)
                                break
                            else:
                                print("\n입력한 값이 잘못 되었거나 재고가 없습니다.\n입력값을 확인해주세요.")
                        except ValueError:
                            print("\n숫자가 아닌 값이 입력되었습니다. 양의 정수를 입력해주세요.")
                elif sn == "5": # 5번 도서 수정
                    print(f"{book_list[4]} 도서를 수정합니다.")
                    while True:
                        try:
                            fixquantity = int(input("\n보충하려는 갯수를 입력하세요."))
                            new_quantity = fixquantity + book_quantity[4]
                            if new_quantity > 0:
                                book_quantity[4] = new_quantity
                                print(f"\n{book_list[4]}번 도서\n{fixquantity}개 보충되어\n최종{book_quantity[4]}개 잔량입니다.")
                                time.sleep(1)
                                break
                            else:
                                print("\n입력한 값이 잘못 되었거나 재고가 없습니다.\n입력값을 확인해주세요.")
                        except ValueError:
                            print("\n숫자가 아닌 값이 입력되었습니다. 양의 정수를 입력해주세요.")
                elif sn == "6": # 6번 도서 수정
                    print(f"{book_list[5]} 도서를 수정합니다.")
                    while True:
                        try:
                            fixquantity = int(input("\n보충하려는 갯수를 입력하세요."))
                            new_quantity = fixquantity + book_quantity[5]
                            if new_quantity > 0:
                                book_quantity[5] = new_quantity
                                print(f"\n{book_list[5]}번 도서\n{fixquantity}개 보충되어\n최종{book_quantity[5]}개 잔량입니다.")
                                time.sleep(1)
                                break
                            else:
                                print("\n입력한 값이 잘못 되었거나 재고가 없습니다.\n입력값을 확인해주세요.")
                        except ValueError:
                            print("\n숫자가 아닌 값이 입력되었습니다. 양의 정수를 입력해주세요.")
                elif sn == "7": # 7번 도서 수정
                    print(f"{book_list[6]} 도서를 수정합니다.")
                    while True:
                        try:
                            fixquantity = int(input("\n보충하려는 갯수를 입력하세요."))
                            new_quantity = fixquantity + book_quantity[6]
                            if new_quantity > 0:
                                book_quantity[6] = new_quantity
                                print(f"\n{book_list[6]}번 도서\n{fixquantity}개 보충되어\n최종{book_quantity[6]}개 잔량입니다.")
                                time.sleep(1)
                                break
                            else:
                                print("\n입력한 값이 잘못 되었거나 재고가 없습니다.\n입력값을 확인해주세요.")
                        except ValueError:
                            print("\n숫자가 아닌 값이 입력되었습니다. 양의 정수를 입력해주세요.")
                elif sn == "8": # 8번 도서 수정
                    print(f"{book_list[7]} 도서를 수정합니다.")
                    while True:
                        try:
                            fixquantity = int(input("\n보충하려는 갯수를 입력하세요."))
                            new_quantity = fixquantity + book_quantity[7]
                            if new_quantity > 0:
                                book_quantity[7] = new_quantity
                                print(f"\n{book_list[7]}번 도서\n{fixquantity}개 보충되어\n최종{book_quantity[7]}개 잔량입니다.")
                                time.sleep(1)
                                break
                            else:
                                print("\n입력한 값이 잘못 되었거나 재고가 없습니다.\n입력값을 확인해주세요.")
                        except ValueError:

                            print("\n숫자가 아닌 값이 입력되었습니다. 양의 정수를 입력해주세요.")
                elif sn == "9": # 9번 도서 수정
                    print(f"{book_list[8]} 도서를 수정합니다.")
                    while True:
                        try:
                            fixquantity = int(input("\n보충하려는 갯수를 입력하세요."))
                            new_quantity = fixquantity + book_quantity[8]
                            if new_quantity > 0:
                                book_quantity[8] = new_quantity
                                print(f"\n{book_list[8]}번 도서\n{fixquantity}개 보충되어\n최종{book_quantity[8]}개 잔량입니다.")
                                time.sleep(1)
                                break
                            else:
                                print("\n입력한 값이 잘못 되었거나 재고가 없습니다.\n입력값을 확인해주세요.")
                        except ValueError:
                            print("\n숫자가 아닌 값이 입력되었습니다. 양의 정수를 입력해주세요.")
            elif subSelect == "4":
                if session is None:
                    print(f"\033[33m로그인 후 이용가능한 서비스입니다.\033[0m")
                    time.sleep(1)
                    continue
                elif session is not None:
                    print(f"\033[33m{names[session]}님 관리자 계정으로 로그인중\033[0m")
                if not paycount_book:
                    print("현재 거래 내역이 없습니다.")
                else:
                    print("번호 | 결제시간 | 도서명 | 결제수단")
                    print("-" * 30)
                    # enumerate를 사용하면 번호(i)를 1부터 자동으로 매길 수 있습니다.
                    for i, (p_time, book, method) in enumerate(zip(paytime, paycount_book, paycount), 1):
                        print(f"{i}. [{p_time}] {book} | {method}") #짚을 쓰면 리스트의 내용들을 하나로 묶어준다./enumerate는 자동으로 순번을 매겨준다.
                        time.sleep(1)
            elif subSelect == "9":
                print("\n도서 구매 메뉴로 돌아갑니다.")
                time.sleep(1)
                subrun = False
# 관리자 메뉴===============================================================================================
    elif select == "q":
        print("\n자판기 프로그램을 종료합니다.")
        time.sleep(2)
        run = False