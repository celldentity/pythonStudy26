import os
import sys
import time
from datetime import datetime

class LMSProgram:
    def __init__(self):
        # 1. 시스템 설정 및 파일명 정의
        self.FILE_MEMBERS = "members.txt"
        self.FILE_SCORES = "scores.txt"
        self.FILE_BOARDS = "boards.txt"

        # 2. 데이터 저장소 (객체의 속성)
        self.members = []
        self.scores = []
        self.boards = []
        self.session = None  # 로그인한 사용자의 인덱스
        self.run_flag = True

        # 3. 초기 데이터 로드
        self.load_all_data()

    # ===============================
    # 기초 시스템 유틸리티
    # ===============================
    def typewriter(self, text, speed=0.002):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        print()

    def load_all_data(self):
        self.members = self._load_file(self.FILE_MEMBERS, is_member=True)
        self.scores = self._load_file(self.FILE_SCORES)
        self.boards = self._load_file(self.FILE_BOARDS)

    def _load_file(self, filename, is_member=False):
        """파일을 읽어 리스트로 반환 (내부용 함수)"""
        data_list = []
        if not os.path.exists(filename):
            with open(filename, "w", encoding="utf-8") as f: pass
            return data_list

        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                data = line.strip().split("|")
                if is_member and len(data) >= 5:
                    data[4] = True if data[4] == "True" else False
                data_list.append(data)
        return data_list

    def save_all(self):
        self._save_file(self.FILE_MEMBERS, self.members)
        self._save_file(self.FILE_SCORES, self.scores)
        self._save_file(self.FILE_BOARDS, self.boards)

    def _save_file(self, filename, data_list):
        with open(filename, "w", encoding="utf-8") as f:
            for item in data_list:
                line = "|".join(map(str, item)) + "\n"
                f.write(line)

    # ===============================
    # 회원 관리 기능 (Member)
    # ===============================
    def member_add(self):
        if self.session is not None:
            print("\n이미 로그인 되어 있습니다.")
            return

        uid = input("아이디 : ")
        for m in self.members:
            if m[0] == uid:
                print("이미 존재하는 아이디입니다.")
                return

        pw = input("비밀번호 : ")
        name = input("이름 : ")
        print("\n1. 관리자  2. 교수님  3. 학생")
        sel = input("권한 선택 : ")
        role = "admin" if sel == "1" else "professor" if sel == "2" else "student"

        if input("저장하려면 y를 누르세요 : ").lower() == 'y':
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.members.append([uid, pw, name, role, True, now])
            self.save_all()
            print("회원가입 완료!")

    def login(self):
        uid = input("아이디 : ")
        for idx, m in enumerate(self.members):
            if m[0] == uid:
                pw = input("비밀번호 : ")
                if m[1] == pw:
                    if not m[4]:
                        print("\n차단된 계정입니다.")
                        return
                    self.session = idx
                    print(f"\n{m[2]}님 환영합니다!")
                    return
                print("\n비밀번호 불일치")
                return
        print("\n아이디를 찾을 수 없습니다.")

    def logout(self):
        if input("\n로그아웃 하시겠습니까? (Enter키 승인) : ") == "":
            self.save_all()
            self.session = None
            print("로그아웃 완료")

    # ===============================
    # 성적 관리 기능 (Score)
    # ===============================
    def score_menu(self):
        while True:
            print(f"\n--- 성적 관리 ({self.members[self.session][3]}) ---")
            print("1. 입력/수정  2. 조회  3. 이전")
            sel = input("선택 : ")
            if sel == "1":
                self.score_input()
            elif sel == "2":
                self.score_list()
            elif sel == "3":
                break

    def score_input(self):
        user = self.members[self.session]
        if user[3] == "student":
            print("권한이 없습니다.")
            return

        self.member_list_summary()
        sid = input("학생 ID 입력 : ")
        target = next((m for m in self.members if m[0] == sid and m[3] == "student"), None)

        if not target:
            print("학생을 찾을 수 없습니다.")
            return

        try:
            pys = int(input("파이썬 : "))
            frs = int(input("프론트 : "))
            www = int(input("웹 : "))
            total = pys + frs + www
            avg = total / 3
            grade = "A" if avg >= 90 else "B" if avg >= 80 else "C" if avg >= 70 else "D" if avg >= 60 else "F"

            new_score = [sid, pys, frs, www, total, grade]

            # 기존 성적 업데이트 또는 추가
            found = False
            for i, s in enumerate(self.scores):
                if s[0] == sid:
                    self.scores[i] = new_score
                    found = True;
                    break
            if not found: self.scores.append(new_score)

            self.save_all()
            print("성적 동기화 완료!")
        except ValueError:
            print("숫자만 입력 가능합니다.")

    def score_list(self):
        user = self.members[self.session]
        if user[3] == "student":
            score = next((s for s in self.scores if s[0] == user[0]), None)
            if score:
                print(f"\n[{user[2]}님 성적] 파이썬:{score[1]} 프론트:{score[2]} 웹:{score[3]} 총점:{score[4]} 등급:{score[5]}")
            else:
                print("\n등록된 성적이 없습니다.")
        else:
            print("\n--- 전체 성적 리스트 ---")
            for s in self.scores:
                print(f"ID: {s[0]} | 총점: {s[4]} | 등급: {s[5]}")

    # ===============================
    # 게시판 기능 (Board)
    # ===============================
    def board_menu(self):
        while True:
            print("\n--- 회원 게시판 ---")
            print("1. 새글작성  2. 목록보기  3. 상세보기  4. 이전")
            sel = input("선택 : ")
            if sel == "1":
                self.board_write()
            elif sel == "2":
                self.board_list()
            elif sel == "3":
                self.board_view()
            elif sel == "4":
                break

    def board_write(self):
        title = input("제목 : ")
        cont = input("내용 : ")
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.boards.append([self.members[self.session][0], title, cont, now, 0, 0])
        self.save_all()
        print("게시글 등록 완료")

    def board_list(self):
        for i, b in enumerate(self.boards):
            print(f"{i + 1}. {b[1]} (작성자: {b[0]}) [조회:{b[4]} 좋아요:{b[5]}]")

    def board_view(self):
        self.board_list()
        try:
            idx = int(input("글 번호 : ")) - 1
            if 0 <= idx < len(self.boards):
                b = self.boards[idx]
                b[4] = int(b[4]) + 1  # 조회수 증가
                print(f"\n제목: {b[1]}\n내용: {b[2]}\n작성시간: {b[3]}")

                sel = input("\n1.좋아요  2.수정(작성자만)  3.이전 : ")
                if sel == "1":
                    b[5] = int(b[5]) + 1
                elif sel == "2" and b[0] == self.members[self.session][0]:
                    b[1] = input("새 제목 : ")
                    b[2] = input("새 내용 : ")
                    print("수정 완료")
                self.save_all()
        except:
            print("잘못된 입력입니다.")

    # ===============================
    # 메뉴 출력 시스템
    # ===============================
    def member_list_summary(self):
        print("\n[현재 회원 리스트]")
        for i, m in enumerate(self.members):
            print(f"{i + 1}. {m[0]}({m[2]}) [{m[3]}] - Active:{m[4]}")

    def start(self):
        while self.run_flag:
            print("\n" + "=" * 45)
            if self.session is None:
                print("1. 회원가입  2. 로그인  3. 종료")
                sel = input(">>> ")
                if sel == "1":
                    self.member_add()
                elif sel == "2":
                    self.login()
                elif sel == "3":
                    self.run_flag = False
            else:
                user = self.members[self.session]
                self.typewriter(f"[{user[2]}님 / 권한: {user[3]}] 접속 중...", 0.001)

                if user[3] == "admin":
                    print("1. 회원리스트  2. 성적관리  3. 게시판  4. 로그아웃  9. 종료")
                else:
                    print("1. 정보수정  2. 성적관리  3. 게시판  4. 로그아웃  9. 종료")

                sel = input(">>> ")
                if sel == "1" and user[3] == "admin":
                    self.member_list_summary()
                elif sel == "2":
                    self.score_menu()
                elif sel == "3":
                    self.board_menu()
                elif sel == "4":
                    self.logout()
                elif sel == "9":
                    self.run_flag = False

        self.save_all()
        print("시스템을 종료합니다.")


# ===============================
# 프로그램 실행 지점
# ===============================
if __name__ == "__main__":
    app = LMSProgram()
    app.start()