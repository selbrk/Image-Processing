inp_filename, operation, out_filename = input().split()


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
def read_imagefile(f):

    a = f.readline().rstrip()
    b = a.split()

    width, height = int(b[1]), int(b[2])
    rest = f.read()
    values = rest.split()
    mylist = list()
    counter = 0
    for j in range(height):
        for i in range(width):
            mylist.append(int(values[counter]))
            counter+=1
    mynewlist = list()
    for i in range(height):
        mynewlist.append(mylist[i*width:i*width+width])

    return mynewlist



def write_imagefile(fp, img_matrix):
    width = len(img_matrix[0])
    height = len(img_matrix)
    fp.write(f'P2 {width} {height} 255\n')
    for r in range(height):
        for c in range(width):
            fp.write(str(img_matrix[r][c]) + ' ')
        fp.write('\n')





def misalign(img_matrix):
    mylist = list()
    for i in range(len(img_matrix)):
        for j in range(len(img_matrix[i])):
            if j % 2 == 0:
                mylist.append(img_matrix[i][j])
            else:
                mylist.append(img_matrix[len(img_matrix) - i - 1][j])

    mylist2 = list()
    for i in range(len(img_matrix)):
        mylist2.append(mylist[i * len(img_matrix[0]) : i * len(img_matrix[0]) + len(img_matrix[0])])

    return mylist2



def sort_columns(img_matrix):
    y7 = list()
    for i in range(len(img_matrix[0])):
        y = []
        for j in range(len(img_matrix)):
            y.append(img_matrix[j][i])
        y.sort()
        y7.append(y)

    y8 = list()
    for i in range(len(y7[0])):
        y = []
        for j in range(len(y7)):
            y.append(y7[j][i])
        y8.append(y)

    return y8



def sort_rows_border(img_matrix):
    values=list()
    for i in range(len(img_matrix)):
        for j in range(len(img_matrix[i])):
           values.append(img_matrix[i][j])

    y = []
    for i in range(len(img_matrix)):
        y1 = []
        consecutive_zeros = []

        for j in range(len(img_matrix[0])):
            if img_matrix[i][j] == 0:
                consecutive_zeros.append(i * len(img_matrix[0]) + j)
            else:
                if consecutive_zeros:
                    y1.append(consecutive_zeros)
                    consecutive_zeros = []

        if consecutive_zeros:
            y1.append(consecutive_zeros)
        y.append(y1)
    y1234 = []
    for i in range(len(y)):
        y123 = []

        if len(y[i]) == 0:
            aaa = values[i * len(img_matrix[0]):i * len(img_matrix[0]) + len(img_matrix[0])]
            aaa.sort()
            y123.append(aaa)
        else:
            for j in range(len(y[i])):
                y12 = []
                if j == 0:
                    if len(y[i][j]) == 1:
                        a = y[i][j][0]
                        b = values[i * len(img_matrix[0]):a]
                        b.sort()
                        c = b + [0]
                        y12.append(c)

                    else:
                        a = y[i][j][0]
                        b = values[i * len(img_matrix[0]):a]
                        b.sort()
                        l = len(y[i][j])
                        c2 = '0 ' * l
                        c3 = c2.split()
                        c = b + c3
                        y12.append(c)

                else:
                    if len(y[i][j]) == 1:
                        a = y[i][j][0]
                        if len(y[i][j - 1]) == 1:
                            a2 = y[i][j - 1][-1] + 1
                        else:
                            a2 = y[i][j - 1][-1] + 1
                        b = values[a2:a]
                        b.sort()
                        c = b + [0]
                        y12.append(c)

                    else:
                        a = y[i][j][0]
                        if len(y[i][j - 1]) == 1:
                            a2 = y[i][j - 1][-1] + 1
                        else:
                            a2 = y[i][j - 1][-1] + 1
                        b = values[a2:a]
                        b.sort()
                        l = len(y[i][j])
                        c2 = '0 ' * l
                        c3 = c2.split()
                        c = b + c3
                        y12.append(c)
                y123.append(y12)
            y123.append([values[y[i][-1][-1] + 1:i * len(img_matrix[0]) + len(img_matrix[0])]])
        y1234.append(y123)

    counter = []
    for i in range(len(y1234)):
        for j in range(len(y1234[i])):
            for k in range(len(y1234[i][j])):
                for m in range(len(y1234[i][j][k])):
                    counter.append(y1234[i][j][k][m])

    counter2 = []
    for i in counter:
        counter2.append(int(i))
    mynewlist1234 = list()
    for i in range(len(img_matrix)):
        mynewlist1234.append(counter2[i * len(img_matrix[0]):i * len(img_matrix[0]) + len(img_matrix[0])])
    return mynewlist1234



def convolution(img_matrix,kernel):
    k=list()
    for i in range(len(kernel)):
        for j in range(i):
            k.append(kernel[i][j])

    yy = list()
    a = (len(img_matrix) + 2) * '0'
    b = list(a)
    yy.append(b)
    for i in img_matrix:
        yy.append([0] + i + [0])
    yy.append(b)

    yyy = list()
    for i in range(len(img_matrix)):
        for j in range(len(img_matrix[0])):
            yyy.append(yy[i][j:j + 3] + yy[i + 1][j:j + 3] + yy[i + 2][j:j + 3])

    yyyy = list()
    for j in range(len(img_matrix[0]) * len(img_matrix)):
        a = 0
        for i in range(1, 10):
            a += int(yyy[j][i]) * k[i-1]

        if a > 255:
            yyyy.append(255)
        elif a < 0:
            yyyy.append(0)
        else:
            yyyy.append(a)

    yyyyy = list()
    for j in range(len(img_matrix)):
        yyyyy.append(yyyy[j * len(img_matrix[0]):j * len(img_matrix[0]) + len(img_matrix[0])])

    return yyyyy



# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
f = open(inp_filename, "r")
img_matrix = read_imagefile(f)
f.close()

if operation == "misalign":
    img_matrix = misalign(img_matrix)

elif operation == "sort_columns":
    img_matrix = sort_columns(img_matrix)

elif operation == "sort_rows_border":
    img_matrix = sort_rows_border(img_matrix)

elif operation == "highpass":
    kernel = [
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
    ]
    img_matrix = convolution(img_matrix, kernel)

f = open(out_filename, "w")
write_imagefile(f, img_matrix)
f.close()