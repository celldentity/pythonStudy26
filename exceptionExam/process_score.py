# 오류 회피하기 : 코드를 작성하다보면 특정오류가 발생해도 그냥 통과시켜야 할 때가 있다.
# 여러 파일을 처리하는 중 일부 파일이 없더라도 프로그램을 계속 실행하고 싶을 경우 등등...

students = ["김기원", "조정화", "이재정", "김수빈",]

for student in students:
    try :
        with open(f"{student}_성적.txt", "r", encoding="utf8") as f:
            score = f.read() # 파일에 있는 내용을 불러와 score에 넣음
            print(f"{student}의 성적 : {score}") #score 변수에 있는 내용을 출력
    except FileNotFoundError:
        print(f"{student}의 성적 파일이 없습니다.")
        print("다음 학생으로 넘어갑니다.")
        continue # 다음 학생으로 for 문