import tkinter as click
from tkinter import messagebox

def select_job(job):
    messagebox.showinfo("선택 완료", f"{job}을(를) 선택하셨습니다.")
    # 여기서 다음 프로세스로 job 값을 전달

root = click.Tk()
root.title("직업 선택")

click.Label(root, text="아래 중 맞는 걸 선택하세요:").pack(pady=10)

# 버튼 생성 및 값 전달 (lambda 사용)
click.Button(root, text="1번 학생", command=lambda: select_job("학생")).pack(fill='x')
click.Button(root, text="2번 직장인", command=lambda: select_job("직장인")).pack(fill='x')
click.Button(root, text="3번 무직", command=lambda: select_job("무직")).pack(fill='x')

root.mainloop()