class A:
    def b(self, x, y):
        return x + y

if __name__ == '__main__':
    a = A()
    n1=14
    n2=10
    print(f"{n1} + {n2} = {a.b(n1,n2)}")