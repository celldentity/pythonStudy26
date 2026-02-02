# opp 기반의 Member 객체용

class Member:
    def __init__(self, id, uid, pw, name, role="user", active=True):
        self.id = id
        self.uid = uid
        self.pw = pw
        self.name = name
        self.role = role
        self.active = active

    @classmethod
    def from_db(cls, row: dict):
        """
        DictCursor로부터 전달받은 딕셔너리 데이터를 Member 객체로 변환합니다.
        """
        if not row:
            return None

        # return cls(
        #     id=row.get['id'],
        #     uid=row.get['uid'],
        #     pw=row.get['password'],
        #     name=row.get['name'],
        #     role=row.get['role'],
        #     active=bool(row.get('active')),
        # )

    def is_admin(self):
        return self.role == "admin"

    def __str__(self): #member 객체를 문자열로 출력할 때 사용(테스트용)
        return f"{self.name}({self.uid}:{self.pw}) [{self.role}]"
