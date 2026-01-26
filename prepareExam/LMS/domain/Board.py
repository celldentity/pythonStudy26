class Board:
    def __init__(self, no, title, content, writer, active="True"):
        self.no = no
        self.title = title
        self.content = content
        self.writer = writer
        self.active = active

    def to_line(self):
        return f"{self.no}|{self.title}|{self.content}|{self.writer}|{self.active}"

    @staticmethod #파일 업로드 역직렬화
    def from_line(line):
        no, title, content, writer, active = line.strip().split("|")
        return Board(int(no), title, content, writer, active == "True")  #여기서도 불리언 값으로 변경해서 받아야 되지 않나