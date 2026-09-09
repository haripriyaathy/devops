class T:
    def show(self):
        print('this is T')
class R(T):
    def show(self):
        print('this is R')
t1=R()
print(t1.show())