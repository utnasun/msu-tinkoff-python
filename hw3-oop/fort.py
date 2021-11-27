class Fort:
    def __init__(self, filename):
        self.stack = []
        self.size = 0
        self.output = filename

    def error(self):
        result = open(self.output, 'w')
        result.write('ERROR')
        result.close()
        exit()

    def add(self, number):
        self.stack.append(number)
        self.size += 1
        pass

    def drop(self):
        if self.size >= 1:
            self.stack.pop()
            self.size -= 1
            pass
        else:
            self.error()

    def swap(self):
        if self.size >= 2:
            self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]
            pass
        else:
            self.error()

    def dup(self):
        if self.size >= 1:
            self.stack.append(self.stack[-1])
            self.size += 1
            pass
        else:
            self.error()

    def over(self):
        if self.size >= 2:
            self.stack.append(self.stack[-2])
            self.size += 1
            pass
        else:
            self.error()

    def plus(self):
        if self.size >= 2:
            self.stack[-2] += self.stack[-1]
            self.stack.pop()
            self.size -= 1
        else:
            self.error()

    def minus(self):
        if self.size >= 2:
            self.stack[-2] -= self.stack[-1]
            self.stack.pop()
            self.size -= 1
            pass
        else:
            self.error()

    def multiply(self):
        if self.size >= 2:
            self.stack[-2] *= self.stack[-1]
            self.stack.pop()
            self.size -= 1
            pass
        else:
            self.error()

    def div(self):
        if self.size >= 2:
            if self.stack[-1] == 0:
                self.error()
            self.stack[-2] //= self.stack[-1]
            self.stack.pop()
            self.size -= 1
            pass
        else:
            self.error()

    def answer(self):
        result = open(self.output, "w", encoding='utf-8')
        if self.size == 0:
            result.write("EMPTY")
            result.close()
            return
        else:
            for num in self.stack:
                f.write(str(num) + " ")
            f.close()
            pass


k = Fort("output.txt")
f = open('input.txt', 'r', encoding='utf-8')
text = f.read().splitlines()
f.close()
for cmd in text:
    if cmd.isdigit():
        k.add(int(cmd))
    if cmd == 'DROP':
        k.drop()
    if cmd == 'SWAP':
        k.swap()
    if cmd == 'DUP':
        k.dup()
    if cmd == 'OVER':
        k.over()
    if cmd == '+':
        k.plus()
    if cmd == '-':
        k.minus()
    if cmd == '*':
        k.multiply()
    if cmd == '/':
        k.div()
k.answer()
