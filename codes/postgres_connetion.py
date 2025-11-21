import psycopg2
import os

# DB 연결 설정
# """PostgreSQL 데이터베이스에 연결합니다."""

# 환경 변수 또는 기본값으로 데이터베이스 연결 정보 설정
db_host = "db_postgresql"
db_port = "5432"
db_name = "main_db"
db_user = "admin"
db_password = "admin123"

conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_user,
    password=db_password
)
print("PostgreSQL 데이터베이스에 성공적으로 연결되었습니다.")
# return conn
# except psycopg2.OperationalError as e:
# print(f"데이터베이스 연결에 실패했습니다: {e}")
# print("연결 정보를 확인하거나 Docker 컨테이너가 실행 중인지 확인하세요.")

with conn.cursor() as cursor:
    # cursor.execute("Insert into users_uuid_name (name) values ('from code')")
    # cursor.execute("""update users_uuid_name
    # set name = 'UpdateName'
    # where id_name = '82f1c950-76f8-49da-80c3-c61aaba6b9d1';""")
    # cursor.execute("""delete from users_uuid_name 
    # "where id_name = '82f1c950-76f8-49da-80c3-c61aaba6b9d1';""")
    cursor.execute("select name, id_name from users_uuid_name;")
    records = cursor.fetchall()
    for record in records:
        print(record) # type(record) = tuple (= list)
        print(f'{record[0]}, {record[1]}')

conn.commit()