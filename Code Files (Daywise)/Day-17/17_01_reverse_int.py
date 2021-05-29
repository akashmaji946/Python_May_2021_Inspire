# 123 =>   321
class Reverse:
    def __init__(self, num):
        self.num = num
    def do_reverse(self):

        num = self.num
        # num => int
        # 

        num_str = str(num) #int->str

        reversed = num_str[::-1]  #reverse
        return reversed

print(Reverse().do_reverse(123))





