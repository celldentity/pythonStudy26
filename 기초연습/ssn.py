# 주민번호를 입력 받아 생년월일 남녀 구분을 하는 코드
# input() 함수를 사용하면 콘솔로 데이터를 넣을 수 있다.
# 처리0 : 주민번호 입력 검증 -> 14글자인지 6번째에 데쉬가 있는지
# 처리1 : 생년월일을 추출 -> 1.2.5.6 1900년생 나머지는 2000년생 9는 외계인
# 처리2 : 주민번호 8번째 글자를 추출 -> 남여 구분 가능
# 처리3 : 9~10번째 글자를 추출해서 출생지역을 확인할 수 있다.

print("주민번호를 입력하세요!!(-포함 14글자)")
ssn = input(">>>")
# 입력된 주민번호 검증 코드
if len(ssn)==14 : #키보드로 입력된 문자열이 14자?
    print("주민번호 14글자가 잘 입력 되었습니다.")
else :
    print("""주민번호 14글자가 잘못 입력 되었습니다.
    확인 후 다시 입력해 주세요.""")
    exit(0) # 강제 종료 됨!

if ssn[6] == "-" :
    print("주민번호 7번째 구분자 인식 완료")
else:
    print("""주민번호 7번째 구분자가 올바르게 입력되지 않았습니다.
    프로그램을 처음부터 다시 실행하세요.""")
    exit(0) # 강제 종료 됨!

print("입력된주민번호 : "+ssn)
# 주민번호 앞 6자리를 생년월일로 추출 -> 1,2,5,6 1900년생, 나머지는 2000년생

year = ssn[0:2] #생년추출
month = ssn[2:4] #생월추출
day = ssn[4:6] #생일추출

fullyear = "" #if 안쪽에서 변수를 만들면 버그가 생길 수 있다. 미리 만들어 둔다.
#"" 쌍 따옴표 두 개는 null 처리용이다.

if ssn[7] in ["1","2","5","6"] :
    fullyear = "19"+year
elif ssn[7] == "9" :
    print("귀하는 외계인 입니다. 당장 지구를 떠나주세요!!")
    exit(0)
else:
    fullyear = "20"+year
print("귀하의 생년은 :" + fullyear + "년생 입니다.")

#나이 계산도 추가해본다.
age = 2026 - int(fullyear)
print("귀하의 나이는 " + str(age) + "세 입니다.") #괄호안이 사칙연산때문에 최우선이다.
# print는 문자열 + 숫자로 출력 오류가 발생
# 문자열로 변환(강제타입변환) -> str(age)로 진행함
# 웹 개발에서는 요즘 전부 문자로 받고 필요한 부분만 숫자로 변경하는 추세다.

MF = ssn[7] #성별추출
MF = int(MF) #성별정수처리

gender = ""   #성별 null 값
if MF in [0, 2, 4, 6, 8] :   #표 안에 있는 값을 보려면 in을 쓰려면 된다.
    gender = "여자"
elif MF == 9 :
    gender("외계인")
else:
    gender = "남자"
print("귀하는 " + gender + "로 판단됩니다.")

local = ssn[8:10]
local = int(local)
location = ""
if local <= 8 :
    location = "서울"
elif local <= 12 :
    location = "부산"
elif local <= 15 :
    location = "인천"
elif local <= 25 :
    location = "경기"
elif local <= 34 :
    location = "강원"
elif local <= 47 :
    location = "충청"
elif local <= 66 :
    location = "전라"
elif local <= 91 :
    location = "경상"
elif local <= 95 :
    location = "제주"
else:
    location = "외계지역"

print("당신의 생년은 " + year + "년")
print("당신의 생월은 " + month + "월")
print("당신의 생일은 " + day + "일")
print("당신은 " + fullyear[0:2] + "00년대생 이며,")
print(location + "에서 출생한 것으로 보여집니다.")