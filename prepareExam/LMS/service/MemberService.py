import os
import tkinter as tk
from tkinter import simpledialog, messagebox

from prepareExam.LMS.common.Session import Session
from prepareExam.LMS.domain import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "..", "data", "member.txt")


class MemberService:
    members = []

    @classmethod
    def load(cls):
        cls.members = []
        if not os.path.exists(FILE_PATH):
            cls.save()
            return
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            for line in f:
                cls.members.append(Member.from_line(line))

    @classmethod
    def save(cls):
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            for m in cls.members:
                f.write(m.to_line() + "\n")

    @classmethod
    def login(cls):
        # 1. 팝업창으로 입력받기
        uid = simpledialog.askstring("로그인", "아이디를 입력하세요:")
        if not uid: return

        pw = simpledialog.askstring("로그인", "비밀번호를 입력하세요:", show='*')
        if not pw: return

        for m in cls.members:
            if m.uid == uid:
                if not m.active:
                    messagebox.showwarning("로그인 제한", "비활성화된 계정입니다.")
                    return

                if m.pw == pw:
                    Session.login(m)
                    messagebox.showinfo("성공", f"{m.name}님 환영합니다!\n권한: {m.role}")
                    return
                else:
                    messagebox.showerror("실패", "비밀번호가 틀렸습니다.")
                    return
        messagebox.showerror("실패", "존재하지 않는 아이디입니다.")

    @classmethod
    def logout(cls):
        if not Session.is_login():
            messagebox.showinfo("알림", "로그인 상태가 아닙니다.")
            return

        if messagebox.askyesno("로그아웃", "정말 로그아웃 하시겠습니까?"):
            Session.logout()
            messagebox.showinfo("알림", "로그아웃 완료되었습니다.")

    @classmethod
    def signup(cls):
        uid = simpledialog.askstring("회원가입", "사용할 아이디를 입력하세요:")
        if not uid: return

        if any(m.uid == uid for m in cls.members):
            messagebox.showerror("중복", "이미 존재하는 아이디입니다.")
            return

        pw = simpledialog.askstring("회원가입", "비밀번호를 입력하세요:", show='*')
        name = simpledialog.askstring("회원가입", "이름을 입력하세요:")

        if uid and pw and name:
            member = Member(uid, pw, name)
            cls.members.append(member)
            cls.save()
            messagebox.showinfo("성공", f"{name}님, 회원가입이 완료되었습니다!")

    @classmethod
    def list_members(cls):
        # 회원 목록을 하나의 문자열로 합쳐서 보여줍니다.
        if not cls.members:
            messagebox.showinfo("목록", "등록된 회원이 없습니다.")
            return

        output = "[회원 목록]\n" + "-" * 30 + "\n"
        for m in cls.members:
            output += f"ID: {m.uid} | 이름: {m.name} | 권한: {m.role}\n"

        # 목록이 길 수 있으므로 별도 창이나 알림창으로 표시
        messagebox.showinfo("회원 관리", output)

    @classmethod
    def admin_menu(cls):
        if not Session.is_login() or not Session.login_member.is_admin():
            messagebox.showerror("권한 오류", "관리자만 접근 가능합니다.")
            return

        while True:
            # 관리자 전용 메뉴 팝업 (버튼 형식 대신 간단히 숫자로 받기)
            sel = simpledialog.askstring("관리자 메뉴",
                                         "1. 회원 목록 조회\n2. 권한 변경\n3. 블랙리스트 처리\n0. 뒤로가기")

            if sel == "1":
                cls.list_members()
            elif sel == "2":
                cls.change_role()
            elif sel == "3":
                cls.block_member()
            elif sel in ["0", None]:
                break

    @classmethod
    def change_role(cls):
        uid = simpledialog.askstring("권한 변경", "대상 아이디를 입력하세요:")
        for m in cls.members:
            if m.uid == uid:
                new_role = simpledialog.askstring("권한 변경", "새 권한 (admin/manager/user):")
                if new_role:
                    m.role = new_role
                    cls.save()
                    messagebox.showinfo("성공", "권한이 변경되었습니다.")
                return
        messagebox.showerror("실패", "회원을 찾을 수 없습니다.")

    @classmethod
    def block_member(cls):
        uid = simpledialog.askstring("블랙리스트", "정지할 아이디를 입력하세요:")
        for m in cls.members:
            if m.uid == uid:
                m.active = False
                cls.save()
                messagebox.showinfo("완료", f"{uid} 계정이 비활성화되었습니다.")
                return
        messagebox.showerror("실패", "회원을 찾을 수 없습니다.")