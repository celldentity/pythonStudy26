import os
from MemberService import MemberService

app = MemberService()
app.run()   #run 자체의 내장함수가 아니라 app이 멤버 서비스가 되었으니. 멤버서비스 안의 run 기능을 호출한거다.


