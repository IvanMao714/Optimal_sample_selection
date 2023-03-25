class Stack:
    def __init__(self):
        self.max = 10000             # 栈的最大容量
        self.elem = [None] * self.max   # 用list数据类型来表示顺序栈
        self.top = 0                    # 栈顶指针
        self.base = 0                   # 栈底指针

    def push(self, elem):
        if self.top - self.base == self.max:  # 判断栈是否已满
            raise Exception("The stack is full!")
        self.elem[self.top] = elem  # 元素入栈
        self.top += 1  # top指针指向栈顶元素的下一个

        def pop(self):
            if self.top == self.base:
                raise Exception("The stack is empty")  # 判断栈是否已空
            self.top -= 1  # top指向栈顶元素（牢记top指针的定义:top始终指向“栈顶元素”的后面）
            e = self.elem[self.top]  # 用e接收弹出的元素
            return e

