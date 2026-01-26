# Member.py는 각 회원의 자료를 담당한다.
# 웹프로그래밍에 백엔드에는 데이터베이스와 결합하는데
# MemberDTO, MemberVO 라는 이름으로 사용된다.
# DTO (Data Transfer Object) 데이타 베이스도 표로 되어있다. 시트처럼 되어있고 컬럼처럼 받아쓴다.
# VO (Value Object) 값 그 자체

# 회원 각각의 자료를 리스트가 아닌 변수에 담아 제공하려 함.

class Member: #클래스명은 무조건 대문자로 시작하세요)
    def __init__(self, uid, pw, name, role="user", active=True):
        self.id = uid
        self.pw = pw
        self.name = name
        self.role = role
        self.active = active

    # 사용법 member = Member()    >   객체를 생성하여 변수에 연결  #온니 클래스하고 파일명만 대문자
    # 이름 : member.id       >
    # 암호 : member.pw

# 파일 저장용 문자열 변환
    def to_line(self):
        return f"{self.id}|{self.pw}|{self.name}|{self.role}|{self.active}\n"

# 사용법 Member = Member()
# member.to_line()    -    kkw|1234|김기원|admin|True
# 이렇게 하면 메모장에 객체가 기록된다.


    # 파일에서 불러온 내용 객체처리
    @classmethod #객체(self)가 아니라 클래스 자체를 (cls)를 다루는 메서드라고 정의 # 가로로 한줄 되어 있던 걸 객화 시켜주는 애
    def from_line(cls, line):  #여기서 line : 메모장의 1줄 문자열 cls를 인수로 집어넣어야 아래 있는 cls에 데이터가 들어감
        data = line.strip().split("|")
        if len(data) < 5:
            return None
        uid, pw, name, role, active = data
        return cls(uid, pw, name, role, active == "True")
        #면접시 물어보는 내용
        #직렬화 = 객체를 저장 가능한 형태로 바꾸는 것 Serialization
        #역직렬화 = 저장된 데이터를 객체로 만드는(@classmethod)역직렬화
        #사용법 : m = Member(uid, pw, name, role, active) - 권장하지 않음 바로넣음
                                #self를 사용하는 방법
        #직렬화 사용법 = member.to_line() Deserialization
        #권장법 : m = Member.from_line(line) - 이게 역직렬화
        #
                                        #cls를 사용하는 방법(클래스 변수)

    def __repr__(self):
        return f"({self.id}, {self.pw}, {self.name}, {self.role}, {self.active})"

