import os
# 결국에 멤버py의 멤버 클래스는 멤버 서비스의 세이브, 로드에서 호출되기 위해서 작성된다.
# 로드를 하기 위해서는 텍스트 파일을 여기 클래의 형태로 모습을 갖추고 멤버서비스의 멤버스 리스트로 가져와 가 되는거고
# 저장을 하기 위해서는 멤버스에 있는 리스트들을 텍스트파일에 아래에 적힌 모습으로 저장해! 라는 부분을 위해서 필요하다.
# 결국 맴버라는 클래스는 저장과 불러오기 기능을 위해서 존재한다.
# 만약 어떤식으로 저장되고 어떤식으롤 불러올지에 대한 표현을 멤버 서비스에서 했다면, 여기에 있는 맴버 클래스는 호출되지 않는다.
# 다른말로 객체화가 되지 않기 때문에 여전히 인덱스를 구해야하는 상황이 된다.


class Member:
    def __init__(self, uid, pw, name, role="user", active=True):
        self.id = uid
        self.pw = pw
        self.name = name
        self.role = role
        self.active = active

    # 메인파일에서 먼저 run 이 실행되면, 그 다음으로 멤버 서비스의 로드_멤버스 데이터가 작동한다.
    # 로드_멤버스 안에서 아래의 프롬 투 라인을 호출한다. 어디에서 어떤 파일을 사용할지는 멤버 서비스에 정의되어 있고
    # 거기서 호출한 파일을 아래처럼 다듬는 다는 의미만 가진다. 그래서 어떻게 전환하고 어디에 넣을지만 작성한다.
    # 파일을 켜고 쓰고 닿는건 멤버 서비스에서 전담한다.
    def to_line(self):
        return f"{self.id}|{self.pw}|{self.name}|{self.role}|{self.active}"
    # 투 라인이라는게 호출되면 받은 데이터를

    @classmethod
    def from_line(cls, line):   #프롬 투 파인이라는 함수는 클래스메서드라는 데코레이터를 통해서 앞으로 작동하게 된다는 뜻.
        data = line.strip().split("|")
        uid, pw, name, role, active = data
        return cls(uid, pw, name, role, active)




        # MemberService 안에서 직접 처리 (cls 안 씀)
        #def load_members(self):
         #   with open(self.file_name, "r") as f:
          #      for line in f:
           #         data = line.strip().split("|")
                    # 밖에서 일일이 다 쪼개서 Member()에 집어넣음
            #        new_member = Member(data[0], data[1], data[2], data[3], data[4] == "True")
             #       self.members.append(new_member)
