class Matrix:
    def __init__(self, r=1, c=1):
        self._row = r
        self._column = c
        self.__matrix = []
        '''
        for i in range(self._row):
            self.__matrix.append([])
            for j in range(self._column):
                self.__matrix[i].append(0)
        '''
    def fill_with_value(self, val=0):
        for i in range(self._row):
            self.__matrix.append([])
            for j in range(self._column):
                self.__matrix[i].append(val)


    def get_number(self, r=1, c=1):        # other için işime yaradı
        return self.__matrix[r][c]
    def __add__(self, other):        # __dasf__ bunları kullanma sebebimiz programı çalıştırırken +,- gibi şeyleri kullanabiliceğimiz için mi
        mat_add = []
        for i in range(self._row):
            mat_add.append([])
            for j in range(self._column):
                x = self.__matrix[i][j] + other.get_number(i, j)
                mat_add[i].append(x)
        return mat_add   # böyle yapmakta bir sorun var mı


    def __sub__(self, other):
        mat_sub = []
        for i in range(self._row):
            mat_sub.append([])
            for j in range(self._column):
                x = self.get_number(i, j) - other.get_number(i, j)      #self.__matrix[i][j]
                mat_sub[i].append(x)
        return mat_sub


    def get_row(self, row):
        list_row = []
        for j in range(self._column):
            list_row.append(self.__matrix[row][j])
        return list_row

    def get_column(self, column):
        list_column = []
        for i in range(self._row):
            list_column.append(self.__matrix[i][column])
        return list_column

    def __mul__(self, other):
        mat_mult = []
        for i in range(self._row):
            mat_mult.append([])
            for j in range(self._column):
                sum = 0
                list_mult = []
                for num1, num2 in zip(self.get_row(i), other.get_column(j)):
                    list_mult.append(num1 * num2)
                for l in range(len(list_mult)):
                    sum += list_mult[l]

                mat_mult[i].append(sum)
        return mat_mult


    def __divmod__(self, other):
        '''
        Böyle bir şey var mı emin değilim.
        '''
        pass

    def determinant(self):
        res = 0
        for i in range(self._row):
            for j in range(self._column):
                '''
                * hep 1. satır ve  j. sütunu çıkartıcam matristen geriye 2x2 matris kalacak  (mat_det)
                * geri kalan bana i*i - not(i) * not(i) yi vericek
                * bu sayıyı matrisin 1xj siyle çarpıcam (j 1,3,5... sıralardaysa -j olacak)
                
                * galiba dışardaki for döngüsüne gerek yok
                  j yi 0,1,2 diye dolaşıp aşağıdakileri ona göre yapsam yeticek gibi. 
                '''
            count = self.__matrix[0][j]      #bunun self[i][j] mi olması gerekiyor
            if j % 2 != 0:
                count *= -1

            mat_det = self.__matrix         #böyle direkt eşitleme yok    !!!
            for l in mat_det:
                del l[j]

            num = mat_det[0][0] * mat_det[1][1] - mat_det[0][1] * mat_det[1][0]
            res += num * count
        return res


    def inverse_matrix(self):
        pass

    def trans_matrix(self):
        pass



    def __str__(self):                 #bu kısmı yazmazsak <0x43535b363> li bir şey çıkıyor
        matrix = str(self.__matrix)
        return matrix

m1 = Matrix(3, 3)
m2 = Matrix(3, 3)
m1.fill_with_value(5)
m2.fill_with_value(3)
print("Matrix 1 = ", m1)
print("Matrix 2 = ", m2)

m3 = m1 + m2  # m3 = m1.add(m2)
print("Matrix 3 = ", m3)

m4 = m1 - m2
print("Matrix 4 = ", m4)

m5 = m1 * m2   # m5 = m1.__mult__(m2)
print("Matrix 5 = ", m5)

m6 = m1.determinant()
print("Determinant of m1 is = ", m6)