
class FourCal:
    # pass # 아무동작 안하고 넘어감
    # 변수 선언부)__init__
    def __init__(self): #생성자 객체를 생성할때 쓰는 자료다(변수들 모아놓고 생성할때 사용)
        self.first = 0 #first라는 변수를 선언한거다.
        self.second = 0 #second라는 변수를 선언함.

    def add(self):
        return self.first + self.second
        return result

    def div(self):
        return self.first / self.second #사람은 나누는 값이 0이면 0이지만 컴퓨터는 0을 나누라고 한면 오류뜬다.
        result = result

    # 이것은 취약한 코드
    # 세터와 게터를 이용해 구현해야 한다.
    def setdata(self,first,second): #메서드를 통해서 값을 검증하고 받아 넣을 수 있다.
        # a. first와 a. second를 직접 가서 처리 가능하지만
        # 하지만 검증해서 값을 처리하는 게 보안상 안전하다.
        # 데이터를 넣는 메서드를 세터라고 한다.
        if first <= 0 :
            self.first = 0
        else:
            self.first = first
        if second <= 0 :
            self.second = 0
        else:
            self.second = second

    # 메서드 선언부

a = FourCal()
#a.first = 100 #객체 변수에 바로 입력이 됨
#a.second = 200 #객체 변수에 바로 출력이 됨
a.setdata(-10, 10)
result1 = a.add()
print(f"=-10+10을 : add 메서드 실행결과 = {result1}")

print(a.first)
print(a.second)
# a변수에 FourCal()클래스를 연결한다.
# 이런 방법은 개발자들이 취약한 코드라고 판단한다.
print(type(a))
# <class '__main__.FourCal'>
# __maon__ = 모듈의 이름을 담고 있는 파이썬 내장변수
# 최상위 코드가 실행되는 환경의 의름(주 실행코드)
# 건물에는 무조건 1층 입구가 있듯이 프로그램 실행은 main으로 판단


class MoreFourCal(FourCal):
    def __init__(self):  # 생성자 객체를 생성할때 쓰는 자료다(변수들 모아놓고 생성할때 사용)
        self.first = 0  # first라는 변수를 선언한거다.
        self.second = 0
        #부모객체의 모든 기능을 사용하면서 추가 메서드를 만듦

    def pow(self):
        result = self.first ** self.second
                    #부모에다가 추가 메서드
        return result

    def div(self): #부모와 같은 메서드 명
        if self.second == 0:
            #나누는 뒷값이 0이면 나눌필요도 없이 0을 리턴

            return 0
        else:
            return self.first / self.second

c = MoreFourCal()
c.add()
c.pow()

#메서드 오버라이딩 (부모가 만든 메서드를 튜닝할 때)
#d = FourCal()
#d.setdata(first=8, second=0)
#d.div()
#result = d.div()
#print(result)

e = MoreFourCal()
e.setdata(first=9, second=0)
result = e.div() # 자식에게서 개선된 자식 div()를 실행한다. (자식의 객체를 사용하고 그 안의 메서드를 쓰면 부모껀 사용하지 못한다.)
print(result)

# 클래스 변수(필드) : __init__ 나 일반 메서드의 바깥족 변수

class Family :
    lastname = "김" #얘는 전역변수가 되어버려서 클래스를 쓰는 이유가 없어진다.
    #클래스 바로 아래에 선언된 변수들을 클래스 변수 및 필드라고 부른다.

print(Family.lastname)
a = Family()
b = Family()
a.lastname = "최" #클래스에 변수를 쓸땐 이렇게 쓰는데 대부부은 인잇 안에 넣고 시작한다.
print(a.lastname)
print(b.lastname)