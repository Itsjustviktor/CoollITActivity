import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from PIL import Image

def lin_reg(X, y, im):
    predicted = np.zeros([im.height, im.width])
    for i in range(im.height):
    lm = linear_model.LinearRegression()
    lm.fit(X, y[i])
    predicted[i] = lm.predict(X)
    return predicted

def ImWork(data, im, h):

    x = np.arange(0, im.width)
    X = np.array([x, x**2.0, x**3.0, x**4.0, x**5.0]).transpose()

    y_red = data[0, :, 0]
    y_green = data[0, :, 1]
    y_blue = data[0, :, 2]

    plt.plot(x, y_red, 'r-')
    plt.plot(x, y_green, 'g-')
    plt.plot(x, y_blue, 'b-')
    plt.title('Цветовые каналы первой строки изображения')
    plt.grid()
    plt.show()

    y_red = data[:, :, 0]
    y_green = data[:, :, 1]
    y_blue = data[:, :, 2]

    predicted_red = lin_reg(X, y_red, im)
    predicted_green = lin_reg(X, y_green, im)
    predicted_blue = lin_reg(X, y_blue, im)
    

    # кодирование разностей
    raz_red = y_red - predicted_red
    raz_green = y_green - predicted_green
    raz_blue = y_blue - predicted_blue

    bits_per_channel = h
    threshold = (2 ** (bits_per_channel-1)) - 1
    # для кодирование 8 (2^3, так как один бит определяет знак) оттенков от 0 до 7

    diff_red = np.clip(raz_red, -threshold, threshold)
    diff_green = np.clip(raz_green, -threshold, threshold)
    diff_blue = np.clip(raz_blue, -threshold, threshold)

    y_r = predicted_red + diff_red
    y_g = predicted_green + diff_green
    y_b = predicted_blue + diff_blue

    # Подмена пикселов в исходном изображении
    pix = im.load()
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            l = list(pix[i, j])
            l[0] = int(y_r[j, i])
            l[1] = int(y_g[j, i])
            l[2] = int(y_b[j, i])
            pix[i, j] = tuple(l)
    tr = 'pract6\\ready'+str(h)+'.png'
    im.save(tr)
    return True, tr

im = Image.open('D:\\visual studio\\laba Python\\LR1\\pract6\\image.jpg')
data = np.array(im.getdata()).reshape([im.height, im.width, 3])
h = int(input("Введите кол-во бит: "))
ch, way = ImWork(data, im, h)
if ch:
    print('Сжатие выполнено. Путь к файлу: ', way)









