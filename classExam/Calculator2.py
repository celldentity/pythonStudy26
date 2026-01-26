# 클래스는 대부분 파일명을 대문자로 만드는 것이 관례이다.
# 클래스는 인스턴스를 목적으로 만듦.

# 파일명과 클래스명도 대문자로 시작.

    # 내부에 함수(메서드)를 생성한다.

        # 초기화 메서드
        # 클래스 선언시 기본적으로 실행되는 문법

        # 셀프는 간단하게 주소다 어려울 게 없다.
        # 스택&힙 영역이 있는데,힙 영역에 생성된 객체의 주소 자신을 지칭하는 말이다.
        # 그래서 모든 변수는 self 안에다가 만들어주면 된다. 그 안에 다른 변수가 들어 있거나 주소가 점유중일 수 있으니
        # 초기화 하기 위해서 맨 처음에 이니셜 함수가 정의되고 들어간다.

# class 선언 종료

 #(멤버였다면 멤버, 스코어였다면 스코어)
# 변수에 객체를 연결(대문자로 시작했으니 클래스다.)

# 클래스를 사용하려면 변수에 연결(스택과 힙영역에 그래야 연결된다.)
# 이때 사용하는 주소가 self
# 클래스는 스택영역의 변수와 힙 영역에
# 아무리 많은 사람이 클래스를 사용하더라도 변수만 다르게 연결하면 얼마든지 이용이 가능하다.


class Calculator:
    def __init__(self):
        # 1. 반드시 __init__ (언더바 2개씩)이어야 합니다.
        # 2. 여기서 self.result를 0으로 초기화해줘야 합니다.
        self.result = 0

    def add(self, num):
        self.result += num  # 이제 self.result가 존재하므로 에러가 나지 않습니다.
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

    def mul(self, num):
        self.result *= num
        return self.result

    def div(self, num):
        if num == 0:
            print("0으로 나눌 수 없습니다.")
        self.result /= num
        return self.result

# 실행부
cal1 = Calculator()
kkwresult = cal1.add(5)
print(kkwresult)

cal2 = Calculator()
ksbresult = cal2.add(7)
print(ksbresult)


print(cal1.sub(10))
print(cal2.mul(9))
print(cal2.div(9))