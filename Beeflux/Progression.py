class Progression:

    def __init__(self, start=0):
        self.current = start

    def advance(self):
        self.current += 1

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            answer = self.current
            self.advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(", ".join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):
    def __init__(self, x, start=0):
        super(ArithmeticProgression,self).__init__(start)
        self.x=x

    def advance(self):
        self.current += self.x


class GeometricProgression(Progression):
    def __init__(self,x,start=1):
        super(GeometricProgression,self).__init__(start)
        self.x=x   
    def advance(self):
        self.current *= self.x


class FibonacciProgression(ArithmeticProgression):
    def advance(self):
        self.current, self.x = self.x, self.current+self.x


if __name__ == '__main__':
    print('Default Progression')

    Progression().print_progression(10)

    ArithmeticProgression(2).print_progression(20)

    GeometricProgression(3).print_progression(10)
    FibonacciProgression(4,6).print_progression(10)