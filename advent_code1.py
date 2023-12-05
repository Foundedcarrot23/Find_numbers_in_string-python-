import re

file = open("Advent_code1.txt", "r")
lines = file.readlines()

new_list = []
for word in lines:
    word = word.split(",")
   
    new_list.append(word)




arr = []

for i in range(len(new_list)):
    for j in range(len(new_list[i])):
        cheese = new_list[i][j]
        arr.append(cheese)


final_arr = []
for element in arr:
    for index, char in enumerate(element):
        if char.isdigit() or "one" or "two" or "three" or "four" or "five" or "six" or "seven" or "eight" or "nine" in element:
            if char.isdigit():
                final_arr.append(char)
                break
            a = element.find("one")
            b = element.find("two")
            c = element.find("three")
            d = element.find("four")
            e = element.find("five")
            f = element.find("six")
            g = element.find("seven")
            h = element.find("eight")
            i = element.find("nine")
            if a or b or c or d or e or f or g or h == -1:
                if a == -1:
                    a = 10000000000000
                if b == -1:
                    b = 10000000000000
                if c == -1:
                    c = 10000000000000
                if d == -1:
                    d = 10000000000000
                if e == -1:
                    e = 10000000000000
                if f == -1:
                    f = 10000000000000
                if g == -1:
                    g = 10000000000000
                if h == -1:
                    h = 10000000000000
                if i == -1:
                    i = 10000000000000
            
            if a < min([b, c, d, e, f, g, h, i]):
                final_arr.append(1)
                break
            elif b < min([a, c, d, e, f, g, h, i]):
                final_arr.append(2)
                break
            elif c < min([a, b, d, e, f, g, h, i]):
                final_arr.append(3)
                break
            elif d < min([a, b, c, e, f, g, h, i]):
                final_arr.append(4)
                break
            elif e < min([a, c, d, b, f, g, h, i]):
                final_arr.append(5)
                break
            elif f < min([a, c, d, e, b, g, h, i]):
                final_arr.append(6)
                break
            elif g < min([a, c, d, e, f, b, h, i]):
                final_arr.append(7)
                break
            elif h < min([a, c, d, e, f, g, b, i]):
                final_arr.append(8)
                break
            elif i < min([a, c, d, e, f, g, h, b]):
                final_arr.append(9)
                break
'''   
            
for ball in arr:
    reversed_element = ball[::-1]
    for indexi, chari in enumerate(reversed_element):
        if chari.isdigit():
            final_arr.append(chari)
            break


split_index = 10
firsthalf = final_arr[:split_index]
secondhalf = final_arr[split_index:]
maybe_final_arr = []
for l in range(0,len(firsthalf)):
    for m in range(0,len(secondhalf)):
        if l == m:
            maybe_final_arr.append(firsthalf[l]+secondhalf[m])
        else:
            continue

final_arr_arr = []
for n in maybe_final_arr:
    final_arr_arr.append(int(n))

sum_num = sum(final_arr_arr)
'''
print(final_arr)
