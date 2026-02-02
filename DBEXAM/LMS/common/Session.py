# 세션에서 db 접속도 관리하자!!!
# 현재 세션으로 상태관리를 하는데 차후에 프론트를 배우면 웹브라우져에서 세션을 처리한다.
# HTML + CSS + JS : W3C라고 부른다. 웹표준!!!
# 차후에는 이곳이 db관리하는 connection 영역으로 활용될 수 있다.
# 파이참에도 db를 관리하는 메뉴가 있다.
# 오른쪽 버튼에 db 선택함 → mysql 워크밴치 대타용

import pymysql # pip install pymysql 터미널 설치 필수

class Session:

    login_member = None

    @staticmethod
    def get_connection():
        print("get_connection() 메서드 호출 - mysql에 접속됩니다.")

        return pymysql.connect(
            host='localhost',
            user='mbc',
            password='1234',
            db='lms',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
            # dict 타입으로 처리함 (딕셔너리타입 k : v)
        )
    @classmethod
    def login(cls, member): # 멤버서비스에서 로그인시 객체를 담아놓음
        cls.login_member = member

    @classmethod
    def logout(cls):
        cls.login_member = None

    @classmethod
    def is_login(cls):
        return cls.login_member is not None

    @classmethod
    def is_admin(cls):
        return cls.is_login() and cls.login_member.role == "admin"

    @classmethod
    def is_manager(cls):
        return cls.is_login() and cls.login_member.role in == ("manager", "admin")