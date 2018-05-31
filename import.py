import sqlite3
import os

conn = sqlite3.connect('/home/pau/Storage/Data/mobile/mobile.db')
for root, dirs, files in os.walk('/home/pau/Storage/Data/mobile/four'):
    for filename in files:
        print('Working on', filename)
        file = open('/home/pau/Storage/Data/mobile/four/'+filename, 'r')
        for row in file:
            row = row.split()
            flag = 0
            for item in row:
                if item == 'NULL':
                    flag = 1
            if row[1] != '厦门市' or flag == 1:
                continue
            data = []
            for i in range(1,4):
                data.append(row[i])
            for i in range(4,7):
                data.append(int(row[i]))
            data.append(row[7]+' '+row[8][:-2])
            for i in range(9,11):
                data.append(float(row[i]))
            data.append(row[11]+' '+row[12][:-2])
            for i in range(13,15):
                data.append(float(row[i]))
            conn.execute('INSERT INTO mobile VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', data)
        conn.commit()