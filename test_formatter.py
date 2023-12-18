current = False


class Question:
    def __init__(self, title):
        self.title = title
        self.right = []
        self.wrong = []
    def add_right(self, answer):
        self.right.append(answer)
    def add_wrong(self, answer):
        self.wrong.append(answer)
    def __str__(self):
        if 0 == len(self.right) or 0 == len(self.wrong):
            return "\n"

        res = f"{self.title}" + "{\n"
        for wrong in self.wrong:
            res += f"~{wrong}\n" 
        if 1 == len(self.right):
            res += f"={self.right[0]}\n"
        else:
            for right in self.right:
                res += f"~%{100/len(self.right):.2f}%{right}\n"
        res += "}\n"

        return res


def dump():
    global current
    res = str(current) if current else ""
    current = None
    return res


def process(line):
    global current

    line = line.strip()

    if line.startswith("V2:"):
        return f"{dump()}\n$CATEGORY: {line[3:].strip()}\n"

    if line.startswith("S:"):
        res = dump()
        current = Question(line[2:].strip())
        return res

    if line.startswith("+:"):
        current.add_right(line[2:].strip())

    if line.startswith("-:"):
        current.add_wrong(line[2:].strip())
    
    return ""

if __name__ == "__main__":
    while True:
        try:
            line = input()
            print(process(line))
        except EOFError:
            print(dump())
            break