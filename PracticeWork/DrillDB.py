import sqlite3

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

conn = sqlite3.connect('drillTXT.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_fname TEXT \
                )")
    conn.commit()

conn = sqlite3.connect('drillTXT.db')
with conn:

    for file in fileList:
        cur = conn.cursor()
        if file.find(".txt", len(file) - 4) > -1:
            strSQL = 'INSERT INTO tbl_files(col_fname) VALUES (\'' + f'{file}' + '\')'
            # print(strSQL)
            cur.execute(strSQL)
            print("{}".format(file))
            conn.commit()

conn.close()