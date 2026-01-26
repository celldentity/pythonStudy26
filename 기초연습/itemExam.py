# 상품에 대한 CRUD를 구현해보자
# C - 신상품 등록
# R - 전체상품 목록
# R - 단일상품 자세히 보기
# U - 상품 수정
# D - 상품 품절(매진)

run = True

items = ["노트북", "모니터", "공기청정기", "텀블러"] # 상품명
unit_prices = ["1200000", "400000", "350000", "250000"] # 단가 현재 문자열로 입력을 받기 때문에 표현식에서 정수 변환이 필요
quantity = [40, 25, 30, 20] # 수량
product_infor = ["AI용 삼성노트북", "LG24인치 LED", "LG퓨리케어", "스탠리"] #상품정보
category = ["가전", "잡화", "가전", "잡화"]
# 사용할 함수(메서드)
def new_item():
 #   print("new_item() 함수 호출 완료")
    print("새상품 추가용 함수로 진입합니다.")
    name = input("상품명 : ")
    price = int(input("단가 : "))
    qty = int(input("수량 : "))
    info = input("상품 설명 : ")
# 입력한 값을 바로 리스트에 추가(리스트는 글로벌 변수여도 함수 안에서 값 변화 가능)
    items.append(name)
    unit_prices.append(price)
    quantity.append(qty)
    product_infor.append(info)
    item_add_menu()
    while True:
        cat_num = input("카테고리 선택 : ")
# 카테고리 선택후에 바로 카테고리 리스트에 추가
        if cat_num == "1":
            cat = "가전"
            category.append(cat)
            print(f"{cat}카테고리로 상품 등록이 완료되었습니다.")
            return
        elif cat_num == "2":
            cat = "잡화"
            category.append(cat)
            print(f"{cat}카테고리로 상품 등록이 완료되었습니다.")
            return
        elif cat_num == "3":
            cat = "음식"
            category.append(cat)
            print(f"{cat}카테고리로 상품 등록이 완료되었습니다.")
            return
        elif cat_num == "4":
            cat = "패션"
            category.append(cat)
            print(f"{cat}카테고리로 상품 등록이 완료되었습니다.")
            return
        else:
            print("잘못된 카테고리 선택")
    # 새상품 추가용 실행문
def item_list():
   # print("item_list() 함수 호출 완료")
    print("현재 판매중인 상품 리스트 입니다.")
    print("-" * 30)
    for i in range(len(items)): #숫자표현식이 되도록 정수 표현 필요
        print(f"번호 : {i+1} | 품명 : {items[i]} | 가격 : {int(unit_prices[i]):,}원 | 수량 : {quantity[i]} | 카테고리 : {category[i]}")
    print("상품 리스트 출력이 완료되었습니다.")
    # 리스트 출력용 for item in item_names:
def item_view():
    #print("item_view() 함수 호출 완료") #완료되면 주석처리 하면 된다.
    item_list()
    subSelect = int(input("자세히 보려는 상품의 번호를 선택해 주세요.: ")) - 1
    if 0 <= int(subSelect) <= int(len(items)):
        print("\n[ 상품 상세 정보 ]")
        print("상품명 :", items[subSelect])
        print("가격 :", unit_prices[subSelect])
        print("수량 :", quantity[subSelect])
        print("카테고리 :", category[subSelect])
        print("설명 :", product_infor[subSelect])
        print(f"{subSelect+1}번 상품 조회가 완료되었습니다.")
    else:
        print("❌존재하지 않는 상품입니다.")
    # 상품에 대한 상세 정보 표시
def item_update():
    #print("item_update() 함수 호출 완료")
    item_list()
    subSelect = int(input("수정을 원하시는 상품 번호를 입력하세요")) - 1
    if 0 <= int(subSelect) <= int(len(items)):
        print("기존상품명 :", items[subSelect])
        name = input("바꿀상품명 : ")
        items[subSelect] = name
        print(f"가격 :, {int(unit_prices[subSelect]):,}원")
        price = input("바꿀상품단가 : ")
        unit_prices[subSelect] = price
        print("수량 :", quantity[subSelect])
        qty = input("바꿀상품갯수 : ")
        quantity[subSelect] = qty
        print("카테고리 :", category[subSelect])
        item_add_menu()
        while True:
            cat_num = input("\n수정할 카테고리 선택 : ")
            # 카테고리 선택후에 바로 카테고리 리스트에 추가
            if cat_num == "1":
                cat = "가전"
                category[subSelect] = cat
                print(f"{cat}카테고리로 상품 등록이 완료되었습니다.")
                return
            elif cat_num == "2":
                cat = "잡화"
                category[subSelect] = cat
                print(f"{cat}카테고리로 상품 등록이 완료되었습니다.")
                return
            elif cat_num == "3":
                cat = "음식"
                category[subSelect] = cat
                print(f"{cat}카테고리로 상품 등록이 완료되었습니다.")
                return
            elif cat_num == "4":
                cat = "패션"
                category[subSelect] = cat
                print(f"{cat}카테고리로 상품 등록이 완료되었습니다.")
                return
            else:
                print("잘못된 카테고리 선택")
    else:
        print("\n❌존재하지 않는 상품입니다.")
def item_delete():
    #print("item_delete() 함수 호출 완료")
    item_list()
    subSelect = int(input("\n삭제를 원하시는 상품 번호를 입력하세요")) - 1
    if 0 <= int(subSelect) <= int(len(items)):
        print("\n삭제할상품명 :", items[subSelect])
        print("가격 :", unit_prices[subSelect])
        print("수량 :", quantity[subSelect])
        print("카테고리 :", category[subSelect])
        print("설명 :", product_infor[subSelect])
        if input("삭제를 원하시면 'Enter'키를\n취소하려면 다른 키를 누르세요.") == "":
            items.pop(subSelect)
            unit_prices.pop(subSelect)
            quantity.pop(subSelect)
            category.pop(subSelect)
            product_infor.pop(subSelect)
            print("상품이 전산에서 삭제되었습니다.")
        else:
            print("상품 삭제를 취소합니다.")
    else:
        print("\n❌존재하지 않는 상품입니다.")
def main_menu():
    print("""
===========================
엠비씨 아카데이 쇼핑몰 입니다.
1. 상품등록
2. 상품리스트
3. 상품자세히
4. 상품수정하기
5. 상품 삭제하기
9. 프로그램 종료
    """)
def item_add_menu():
    print("""
==== 등록한 상품의 카테고리를 정해주세요. ====
1. 가전
2. 잡화
3. 음식
4. 패션
9. 종료
""")
#프로그램 주 실행
while run:
    main_menu()
    select = input("숫자입력 : ")
    if select == "1":
        new_item()
    elif select == "2":
        item_list()
    elif select == "3":
        item_view()
    elif select == "4":
        item_update()
    elif select == "5":
        item_delete()
    elif select == "9":
        run = False
    else:
        print("\n잘못된 숫자를 입력하셨습니다.\n다시 입력하세요")