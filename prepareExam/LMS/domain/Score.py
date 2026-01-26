class Score:

    def __init__(self, uid, kor, eng, math):
        self.uid = uid
        self.kor = kor
        self.eng = eng
        self.math = math

    @property
    def total(self): # 변수처럼 사용하기 s.total
        return self.kor + self.eng + self.math

    @property
    def avg(self): # 변수처럼 사용하기 s.total
        return (self.total / 3, 2)  # 오류가능성이 높아서 라운드로 덮어야 될 가능성 농후 round 사용 대비

    @property
    def grade(self):
        if self.avg >= 90:
            return 'A'
        elif self.avg >= 80:
            return 'B'
        elif self.avg >= 70:
            return 'C'
        else:
            return 'F'

    def to_line(self):
        return f"{self.uid},{self.kor},{self.eng},{self.math}"

    @classmethod
    def from_line(cls, line):
        uid, kor, eng, math = line.strip().split(',')
        return cls(uid, int(kor), int(eng), int(math))
