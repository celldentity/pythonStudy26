class Member:  #이 함수 자체가 다섯개의 인자를 포함한 하나의 객체를 찍어내는 틀.
    # member = Member("id", "pw", "name", "role")
    def __init__(self, uid, pw, name, role="user", active=True):
    #            주체 /  인자1 인자2 인자3 인자4      인자5 (이론상 갯수제한없음)
    #            셀프를 배놓고 작성하면 uid를 주체인자로 간주하는데, 그럼 아이디가 날아버려서 누구의 비번, 이름, 권한, 액티브인지 모름
            self.uid = uid
            self.pw = pw
            self.name = name
            self.role = role
            self.active = active

    def __str__(self): # print(member) 처리되는 테스트용
        status = "활성" if self.active else "비활성"
        return(f"{self.uid} | {self.name} | {self.role} | {status}")

    def to_line(self):
        # 파일 저장용 (직렬화) : 메모리에 있는 객체를 메모장에 저장할 문자열로 변환
        return(f"{self.uid}|{self.name}|{self.pw}|{self.role}|{self.active}")

    @staticmethod #객체화는 같으나 일반함수처럼 인수를 line을 받았고, 추후 상속이 진행되어도 Member(~~)값이 계속 등장
    # 만약 스태틱 메서드를 안썼으면
    #           1. 이건 클래스 내부 함수니까 파이썬은 주체(클래스)를 챙겨줘야지 하고 앞에 Member를 집어넣음
    #           2. 결과적으로 받은 데이터가 Member와 line 두 개의 인자가 도착함 (처리공간은 하나인데, 인자 2개 오류)
    #           3. 본질적으로 line 자리에는 Member의 클래스라는 설계도가 앉아버림
    # 만약 메서드를 안쓰고 이 방법을 해결하려면
    #           1. 프롬라인을 메서드가 아닌 클래스 밖의 펑션으로 빼내는 방법
    #               But 코드가 길어지면 좋지 못하고 가독성도 떨어진다.
    # 만약 클래스메서드를 썼다면?
    #           1.리턴값에 cls가 아닌 Member클래스로 집어넣어버린다는 선언이 있어서 다른 클래스로는 값이 가지 않아야 한다.
    # Member 클래스에서 프롬 라인을 호출한 경우면 상관이 없는데, 이걸 상속한 다른 클래스에서 프롬라인 리턴값을 받으려면 오류가 난다.
    # 결과적으로 스태틱 메서드는(받을 인자를 파이썬에서 신경쓰지 않으려고함)
    # 클래스매서드와 일반 메서드는 파이썬에서 인자를 최대한 챙겨주려고 함
    # 다른곳에서의 범용성까지 생각한다면 클래스매서드로 선언하고 맨 아래 Member를 cls로 변경해도 좋음
    def from_line(line: str):  #self도 cls도 인자로 받지 않을 땐 스태티스틱 매서드를 쓴다.
        # 스태틱 메서드를 쓴 순간 이 메서드는 일반 함수랑 똑같다는 선언,
        uid, pw, name, role, active = line.strip().split("|")
        return Member(uid, pw, name, role, active=(active == "True")) #불리언 타입변환 기법
  #             멤버상수                                              결과가 참이면 True을, 거짓이면 False를 반환
  #             여기서 무조건 Member라는 상수를 써야 하는 이유는 이걸 안쓰면 튜플 타입으로 결과값이 반환되는데, 그럼
  #
    def is_admin(self):
        return(self.role == "admin") # 지금 객체가 admin??? 불리언 값 리턴

    def is_manager(self):
        return(self.role == "manager") #지금 객체가 manager?? 불리언 값 리턴
