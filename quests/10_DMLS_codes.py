import psycopg2


"""PostgreSQL 데이터베이스에 연결합니다."""
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


with conn.cursor() as cursor:
    cursor.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS students (
        id UUID,
        name VARCHAR(50),
        age INT
    );
    """
    cursor.execute(create_table_sql)
    print("✅ 'students' 테이블이 성공적으로 생성되었습니다.")

conn.commit()

with conn.cursor() as cursor:
    cursor.execute("""INSERT INTO students (name, age)
     VALUES
     ('홍길동', 23),
     ('이영희', 21),  
     ('박철수', 26);""")
#     # cursor.execute("""UPDATE users_uuid_name
#     #                 SET name = 'code Name'
#     #                 WHERE id_name = '9a328b2c-f195-499e-a3d0-c76ca59be4dd';""")
#     # cursor.execute("SELECT name, id_name FROM users_uuid_name;")
#     # cursor.execute("INSERT INTO users_uuid_name (name) VALUES ('from code');")
#     # records = cursor.fetchall()
#     # for record in records :
#     #     print(record)
#     #     print(f'{record[0]} : {record[1]}')
conn.commit()

with conn.cursor() as cursor:
        
        # ==========================================
        # 📌 문제 3 — READ (SELECT)
        # ==========================================
        # 1. 전체 조회
        cursor.execute("SELECT * FROM students;")
        for row in cursor.fetchall():
            print(row)

        # 2. 나이가 22세 이상인 학생 조회
        cursor.execute("SELECT * FROM students WHERE age >= 22;")
        for row in cursor.fetchall():
            print(row)
conn.commit

        # 3. 이름이 '홍길동'인 학생 조회
with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM students WHERE name = '홍길동';")
        hong_gildong = cursor.fetchone() # 한 명만 가져오기
        print(hong_gildong)
conn.commit


        # ==========================================
        # 📌 문제 4 — UPDATE (UUID 검색 후 수정)
        # ==========================================
        # 시나리오: '이영희'(가정상 2번)의 UUID를 찾아서 나이를 25로 변경

        # 1단계: 이름으로 UUID 찾기 (Option 수행)
with conn.cursor() as cursor:
        cursor.execute("SELECT id FROM students WHERE name = '이영희';")
        target_student = cursor.fetchone()

        if target_student:
            target_uuid = target_student[0]
            
            # 2단계: 찾은 UUID로 나이 수정
            update_sql = "UPDATE students SET age = 25 WHERE id = %s;"
            cursor.execute(update_sql, (target_uuid,))
            print(f"✅ '이영희'({target_uuid})의 나이를 25세로 수정했습니다.")
        else:
            print("⚠ 수정할 대상('이영희')을 찾지 못했습니다.")
conn.commit


# ==========================================
# 📌 문제 5 — DELETE (UUID 검색 후 삭제)
# ==========================================
#  시나리오: '박철수'(가정상 3번)의 UUID를 찾아서 삭제
        # 1단계: 이름으로 UUID 찾기 (Option 수행)
with conn.cursor() as cursor:
        cursor.execute("SELECT id FROM students WHERE name = '박철수';")
        target_student = cursor.fetchone()

        if target_student:
            target_uuid = target_student[0]
            
            # 2단계: 찾은 UUID로 삭제
            delete_sql = "DELETE FROM students WHERE id = %s;"
            cursor.execute(delete_sql, (target_uuid,))
            print(f"✅ '박철수'({target_uuid})의 데이터를 삭제했습니다.")
        else:
            print("⚠ 삭제할 대상('박철수')을 찾지 못했습니다.")


conn.commit()

# 2. 개념 문제 풀이 (문제 6)
# UUID를 PK로 사용하는 테이블에 정수 1을 넣으려 할 때 발생하는 상황에 대한 답안입니다.

# Q1. 어떤 에러가 발생하는가?
# A. 타입 불일치 에러 (Invalid Input Syntax)

# PostgreSQL 에러 메시지 예시: ERROR: invalid input syntax for type uuid: "1"

# 만약 1을 억지로 UUID 형식(000...001)으로 변환해서 넣는 데 성공했다면, 두 번째 INSERT에서는 duplicate key value violates unique constraint (PK 중복 에러)가 발생합니다. 하지만 주어진 쿼리(VALUES (1...)) 그대로 실행하면 타입 에러가 먼저 뜹니다.

# Q2. 왜 발생하는가?
# A. 데이터 타입이 다르기 때문입니다.

# 테이블을 정의할 때 book_id의 타입을 UUID로 지정했습니다.

# 하지만 INSERT 문에서는 정수(Integer)인 1을 넣으려고 했습니다.

# UUID는 550e8400-e29b... 같은 32자리 16진수-하이픈 문자열 형식만 허용하므로, 단순 숫자 1은 받아들여지지 않습니다.

# Q3. PRIMARY KEY(기본키)의 규칙을 쓰시오.
# A. 다음 두 가지 조건을 반드시 만족해야 합니다.

# UNIQUE (유일성): 테이블 내에서 중복된 값을 가질 수 없습니다. (모든 행을 식별할 수 있어야 함)

# NOT NULL (빈 값 불가): 비어있는 값(Null)을 허용하지 않습니다.