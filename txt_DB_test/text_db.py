import sqlite3

conn = sqlite3.connect("c:/data/tag.db")
cur = conn.cursor()

f = open("C:/Users/hyun/Desktop/txt_DB_test/AA.txt", "r")
data = f.readlines()
lines_cnt = len(data)

cnt = 0
for i in data:
    value = i.rstrip()
    new_list = value.split(";")

    sql = '''
        INSERT INTO DATA (
        LOG_DT, LOG_DATE, NAME, VALUE, MODIFY_DATE) VALUES
        ('{}', '{}', '{}', '{}', '{}')
        '''.format(new_list[0], new_list[1], new_list[2], new_list[3], new_list[4])
    
    cnt = cnt + 1
    conn.execute(sql)
    
    if cnt == lines_cnt  : 
        conn.commit()
    else :
        pass
    
conn.close()
f.close()