from operators import add, nul
from logic import and_, or_


def main():
    print "my application starts..."
    a = 2
    b = 3
    x = True
    y = False
    print add(a, b)
    print mul(x, y)
    print and_(x, y)
    print or_(x, y)

if __name__ == "__main__":
    main()
