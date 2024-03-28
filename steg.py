from PIL import Image
import re

def decode_message(image_path):
    img = Image.open(image_path)  
    width, height = img.size  #получение размеров изображения
    binary_data = ""  #переменная для хранения бинарных данных изображения

    #проход по каждому пикселю изображения
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))  #получение цвета пикселя
            r, g, b = pixel
            #извлечение двух последних бит каждой цветовой компоненты
            r_bin = format(r, '08b')[-2:]
            g_bin = format(g, '08b')[-2:]
            b_bin = format(b, '08b')[-2:]
            #объединение каждых двух битов в одну строку
            combined_bin = r_bin + g_bin + b_bin
            binary_data += combined_bin  #добавление бинарных данных в общую строку

    decoded_message = ""  #переменная для хранения декодированного сообщения
    #проход по бинарным данным по 8 бит (1 байт) за раз и декодирование в символы ASCII
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        decoded_message += chr(int(byte, 2))

    decoded_message = re.sub(r'[^\x20-\x7E]', '', decoded_message)  #удаление неотображаемых символов

    return decoded_message.strip()  #удаление лишних символов

#вывод декодированного сообщения
image_path = "1023.png"
decoded_message = decode_message(image_path)
decoded_message = ''.join(c for c in decoded_message if c.isalpha() or c.isspace()) #удаление лишних символов
print("Декодированное сообщение:", decoded_message)
