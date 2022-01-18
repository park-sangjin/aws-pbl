import pymysql

conn = pymysql.connect(host="database-1.cadmrpn9o8fp.ap-northeast-2.rds.amazonaws.com",db='pbldb',port=3306,passwd="qkrtkdstar1!",user='admin')
cursor = conn.cursor()

query = '''
insert into test values(5,'이상민')
'''
cursor.execute(query)
conn.commit()

query2 = '''
select * from test
'''
cursor.execute(query2)
cursor.close()
conn.close()