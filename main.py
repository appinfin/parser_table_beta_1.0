#!/usr/bin/python3

import datetime
from module import *
from m_chek_file import *

def main():
    table_h = ['№','команда','И','В','Н','П','З.м.','П.м.','О','%очков']
    table_all = []
    list_row = []
    res = []
    
    if chek_file()==False:
        save_html()
        print('CHEKED FILE')
    
    with open('index.html', 'r') as file:
        html = file.read()
        soup = BeautifulSoup(html, 'lxml')
        list_tr = soup.find_all('tr') #список строк таблицы

    for tr in list_tr:
        list_td = tr.find_all('td') #список ячеек в строке
        list_td = [td.text.strip() for td in list_td[:9]]#список ячеек кроме последней
        res.append(list_td) #res[ [],[] ] список строк с чистыми данными

    for s in res: #распарсим строку мячи (21-4) на 21, 4
        idx = 0
        i = s[6].index('-')
        s.insert(6, s[6][:i])
        s[7] = s[7][i+1:]

    list_len_str = [0]*len(res[0])#указываем длину списка
    for s in res:
        for item in s:
            idx = s.index(item) #получаем индекс эл-та по порядку
            if list_len_str[idx] < len(item): #сравниваем эл-ты списков
                list_len_str[idx] = len(item)+3 #указываем макс.ширину ячеек

    current_time = datetime.datetime.today().strftime('%Y-%m-%d_%H.%M.%S')
    print(current_time) #текущая дата и время

#номер[0], название команды[1], игры[2], выигрышей[3], ничьи[4], проигрышей[5]
    for c, i in zip(list_len_str, table_h):
        st = i.ljust(c)
        list_row.append(st)
    table_all.append(list_row)

    for s in res:
        list_row = []
        for c, i in zip(list_len_str, s):
            st = i.ljust(c)
            list_row.append(st)
        table_all.append(list_row)  #создаем полный список таблицы

    for s in table_all: #печать всей таблицы
        print(' '.join(s))

    with open('table_1.txt', 'w+') as file: #SAVE FILE
        file.write(current_time+'\n')
        for s in table_all:
            st = ' '.join(s[:6])+'\n' #'№','команда','И','В','Н','П'
            file.write(st)
            print(' '.join(s[:6]))

#номер[0], название команды[1], кол-во забитых мячей[6], кол-во пропущенных мячей[7]
    with open('table_2.txt', 'w+') as file: #SAVE FILE
        file.write(current_time+'\n')
        for s in table_all:
            st = ' '.join(s[:2])+' '.join(s[6:8])+'\n' #'№','команда','И','В','Н','П','З.м.'
            file.write(st)
            print(' '.join(s[:2])+' '.join(s[6:8]))

#отсортированными по убыванию количества забитых мячей  
    sort_list = sorted(table_all[1:], key=lambda ball: int(ball[6]), reverse=True)
    sort_list.insert(0, table_all[0])

    with open('table_3.txt', 'w+') as file: #SAVE FILE
        file.write(current_time+'\n')
        for s in sort_list:
            st = ' '.join(s[:7])+'\n' #'№','команда','И','В','Н','П','З.м.'
            file.write(st)
            print(' '.join(s[:7]))
        
if __name__ == "__main__": main()
    
