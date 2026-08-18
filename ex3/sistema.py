class I:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class P:
    def __init__(self):
        self.a = ""
        self.b = ""
        self.c = []

    def x(self):
        s = 0.0
        d = 0.0

        for i in self.c:
            v = i.b * i.c
            s = s + v

            if i.a == "LIVRO":
                d = d + v * 0.05
            elif i.a == "ELETRONICO":
                d = d + v * 0.02
            elif i.a == "OUTRO":
                d = d + 0

        r = s - d

        if self.a == "PREMIUM":
            z = r * 0.10
            d = d + z
            r = r - z

        f = 0.0

        if self.b == "RETIRADA":
            f = 0.0
        elif self.b == "NORMAL":
            if r >= 150.0:
                f = 0.0
            else:
                f = 12.0
        elif self.b == "EXPRESSA":
            f = 25.0

        t = r + f

        print(f"SUBTOTAL={s:.2f}")
        print(f"DESCONTO={d:.2f}")
        print(f"FRETE={f:.2f}")
        print(f"TOTAL={t:.2f}")


def main():
    p = P()

    p.a = input().strip()
    p.b = input().strip()

    n = int(input().strip())

    for _ in range(n):
        x = input().split()
        p.c.append(I(x[0], float(x[1]), int(x[2])))

    p.x()


if __name__ == "__main__":
    main()