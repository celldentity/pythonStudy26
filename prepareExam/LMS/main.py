import tkinter as tk
from tkinter import messagebox
# 파일 구조에 맞춘 import (사용자님의 현재 경로 반영)
from prepareExam.LMS.service import *
from prepareExam.LMS.common.Session import Session


def get_menu_selection():
    """숫자 타이핑 대신 버튼을 클릭하여 메뉴를 선택하는 GUI 창"""
    root = tk.Tk()
    root.title("MBC 아카데미 관리 시스템")

    # [창 크기 설정] 가로 500, 세로 650으로 시원하게 설정
    root.geometry("500x650+600+150")
    root.resizable(False, False)
    root.configure(bg="#f5f5f5")  # 연한 회색 배경

    # 결과값을 저장할 변수
    selection = [None]

    def on_click(value):
        selection[0] = value
        root.destroy()

    # --- 상단 디자인 ---
    member = Session.login_member
    status_text = f"● {member.name}님 로그인 중" if member else "☆ 로그아웃 상태"
    status_color = "#2ecc71" if member else "#e74c3c"  # 로그인 시 초록, 로그아웃 시 빨강

    tk.Label(root, text="MBC 아카데미", font=("맑은 고딕", 25, "bold"),
             bg="#f5f5f5", pady=10).pack()
    tk.Label(root, text="관리 시스템", font=("맑은 고딕", 18),
             bg="#f5f5f5").pack()
    tk.Label(root, text=status_text, font=("맑은 고딕", 12, "bold"),
             fg=status_color, bg="#f5f5f5", pady=20).pack()

    # --- 버튼 리스트 (텍스트, 반환할 번호) ---
    menu_items = [
        ("1. 회원가입", "1"),
        ("2. 로그인", "2"),
        ("3. 로그아웃", "3"),
        ("4. 회원관리 (관리자)", "4"),
        ("5. 게시판 관리", "5"),
        ("6. 성적 관리", "6"),
        ("9. 프로그램 종료", "9")
    ]

    # --- 버튼 생성 루프 ---
    for text, code in menu_items:
        # 버튼 디자인: 넓은 너비(width), 높은 높이(height), 큰 폰트
        btn = tk.Button(root, text=text, font=("맑은 고딕", 14, "bold"),
                        width=25, height=1,
                        bg="white", fg="#333333",
                        activebackground="#dfe6e9",
                        command=lambda c=code: on_click(c))
        btn.pack(pady=7)

    root.mainloop()
    return selection[0]


def main():
    # 프로그램 시작 시 데이터 로드
    MemberService.load()

    run = True
    while run:
        # 1. 터미널 출력 로직 (기록용으로 유지)
        print("\n" + "=" * 30)
        print(" MBC 아카데미 시스템 가동 중...")
        print("=" * 30)

        member = Session.login_member
        if member is None:
            print("상태: 로그아웃")
        else:
            print(f"상태: {member.name}님 접속 중")

        # 2. GUI 버튼 메뉴 호출 (input 대신 실행)
        sel = get_menu_selection()

        # 3. 비즈니스 로직 실행
        if sel == "1":
            MemberService.signup()
        elif sel == "2":
            MemberService.login()
        elif sel == "3":
            MemberService.logout()
        elif sel == "4":
            MemberService.admin_menu()
        elif sel == "5":
            if hasattr(BoardService, 'run'):
                BoardService.run()
            else:
                print("게시판 서비스가 아직 구현되지 않았습니다.")
        elif sel == "6":
            if hasattr(ScoreService, 'run'):
                ScoreService.run()
            else:
                print("성적 관리 서비스가 아직 구현되지 않았습니다.")
        elif sel in ["9", None]:  # 종료 버튼이나 창 닫기 클릭 시
            print("\n[시스템을 종료합니다. 이용해 주셔서 감사합니다.]")
            run = False


if __name__ == "__main__":
    main()