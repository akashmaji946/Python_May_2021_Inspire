
class StringReverse:
    def __init__(self, string):
        self.string = string
    
    def reverse(self):
        old_string = self.string
        new_string = ""

        for ch in old_string:
            new_string = ch + new_string

        return new_string

        # abc => cba
        # a + "" = a
        # b  + a = ba
        # c + b a = cba

        #  def   => f + ed => fed

sr = StringReverse("abcdef")
reversed_string = sr.reverse()
print(reversed_string)




