class Rational:
    def __init__(self, num=1, denom=1):
        if num < 0 and denom < 0:     # ikisi d enegatifse sayıyı full + çeviriyoeumi twk sıkıntı yazarken sayı +/+ olarak yazılıyor
            self.__numerator = num * -1
            self.__denominator = denom * -1
        else:
            self.__numerator = num
            self.__denominator = denom
        if denom == 0:
            raise ValueError("Denom can not be Zero")
        #self.__sign = 1 if num * denom >= 0 else -1
        #self.__numerator *= self.__sign


    def get_num(self):
        return self.__numerator
    def get_denom(self):
        return self.__denominator
    def get_inverse(self):                   # SOR HOCAYA (self.__numerator ve denom ile yaptığımda olmadı
        x, y = self.__denominator, self.__numerator
        return Rational(x, y)

    def __add__(self, other):
        denom = other.get_denom() * self.get_denom()
        num = other.get_num() * self.get_denom() + self.get_num() * other.get_denom()
        return Rational(num, denom).simplfy()

    def __sub__(self, other):
        denom = other.get_denom() * self.__denominator
        num = self.__numerator * other.get_denom() - other.get_num() * self.__denominator
        return Rational(num, denom).simplfy()

    def __mul__(self, other):
        denom = other.get_denom() * self.__denominator
        num = self.__numerator * other.get_num()
        return Rational(num, denom).simplfy()

    def __divmod__(self, other):
        return self.__mul__(other.get_inverse())    #other'ı yolladıpımda oldu ama self. gönderdiğimde geri doğru dönmüyordu galiba

    def is_maggior(self, other):
        self_num = self.__numerator * other.get_denom()
        other_num = other.get_num() * self.__denominator
        if self_num > other_num:
            return True
        else:
            return False

    def is_minor(self, other):
        return other.is_maggior(self)

    def is_equal(self, other):
        if not self.is_maggior(other) and not self.is_minor(other):
            return True
        else:
            return False


    def simplfy(self):
        if self.__numerator == 0:
            return 0

        while self.__numerator % 2 == 0 and self.__denominator % 2 == 0:
            self.__numerator //= 2
            self.__denominator //= 2

        while self.__numerator % 3 == 0 and self.__denominator % 3 == 0:
            self.__numerator //= 3
            self.__denominator //= 3
        return Rational(self.__numerator, self.__denominator)



    def __str__(self):
        str_rational =  str(self.__numerator) + "/" + str(self.__denominator)
        return str_rational



"""
    //overloaded operators
    *** çıkarma (__sub__)
    *** çarpma
    *** bölme
    float (type conversion)
    int (type conversion)
    *** karşılaştırma operatörleri (comp)
    
    //metots
    *** simplfy()      ilk soru için denedim      ekstra sonucun 0 olma durumunu da denedim
"""



r1 = Rational(-1, -2)
r2 = Rational(3, 4)           # is_equal denemesi için (2, 4) iyi bir örnek

r3 = r1 + r2 #r3 = r1.__add__(r2)
print(r1.__str__(), " + ", r2.__str__(), " = ", r3)     #simplfy ları fonksiyonun bitişine aldım (kullanıcıyı az uğraştırmak bunun gibi mi ?

r4 = r1 - r2 #r3 = r1.__sub__(r2)
print(r1.__str__(), " - ", r2.__str__(), " = ", r4)

r5 = r1.__mul__(r2)
print(r1.__str__(), " * ", r2.__str__(), " = ", r5)

r6 = r1.__divmod__(r2)
print(r1.__str__(), " / ", r2.__str__(), " = ", r6)

print("r1 is maggior (>) verses r2: ", r1.is_maggior(r2))

print("r1 is minor (<) verses r2: ", r1.is_minor(r2))

print("r1 is equal (=) verses r2: ", r1.is_equal(r2))

