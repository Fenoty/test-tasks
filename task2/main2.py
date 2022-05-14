#Чтение файлов
text1 = open('task2/text1.txt', 'r')
text2 = open('task2/text2.txt', 'r')

first_row_array = text1.readline().split()

#Коорды центра окружности
circle_x = int(first_row_array[0])
circle_y = int(first_row_array[1])

#Радиус круга
radius = int(text1.readline())

text1.close()

while True:
    file_line = text2.readline()
    if not file_line:
        break
    else:
        file_array = file_line.split()
        
        #Коорды точек
        point_x = int(file_array[0])
        point_y = int(file_array[1])
        hypotenuse = (point_x - circle_x)**2 / radius**2 + (point_y - circle_y)**2 / radius**2
        if hypotenuse <= 1:
            print("1")
        elif hypotenuse == 1:
            print("0")
        else:
            print("2")

text2.close()


 

