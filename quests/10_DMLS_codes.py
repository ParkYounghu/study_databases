import psycopg2

# 1. 데이터베이스 연결 설정
db_host = "db_postgresql"
db_port = "5432"
db_name = "main_db"
db_user = "admin"
db_password = "admin123"

try:
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
    
    with conn.cursor() as cursor:
        
        # ====================================================================
        # 📌 문제 1 — 테이블 생성 (PRIMARY KEY 기초)
        # ====================================================================
        # 설명: UUID 기능을 사용하기 위해 확장기능을 먼저 활성화하고 테이블을 생성합니다.
        
        # UUID 확장 기능 활성화
        cursor.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')

        # 테이블 생성 (이미 존재할 경우 에러 방지를 위해 IF NOT EXISTS 사용)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                name VARCHAR(50),
                age INT
            );
        """)
        
        # 단계별 저장 (Break)
        conn.commit()


        # ====================================================================
        # 📌 문제 2 — CREATE (INSERT) 기초
        # ====================================================================
        # 설명: UUID 컬럼은 정수(1, 2, 3)를 직접 받을 수 없으므로, 
        # ID는 자동생성(DEFAULT) 되도록 두고 이름과 나이만 입력합니다.
        
        students_data = [
            ('홍길동', 23),
            ('이영희', 21),
            ('박철수', 26)
        ]
        
        cursor.executemany("INSERT INTO students (name, age) VALUES (%s, %s);", students_data)
        
        # 단계별 저장 (Break)
        conn.commit()


        # ====================================================================
        # 📌 문제 3 — READ (SELECT) 기본 조회
        # ====================================================================
        # 설명: fetchall()을 사용하여 데이터를 가져옵니다.
        
        # 3-1. 전체 데이터 조회
        cursor.execute("SELECT * FROM students;")
        # print(f"전체 조회 결과: {cursor.fetchall()}")

        # 3-2. 나이가 22세 이상인 학생 조회
        cursor.execute("SELECT * FROM students WHERE age >= 22;")
        # print(f"22세 이상 조회 결과: {cursor.fetchall()}")

        # 3-3. 이름이 '홍길동'인 학생 조회
        cursor.execute("SELECT * FROM students WHERE name = '홍길동';")
        # print(f"홍길동 조회 결과: {cursor.fetchall()}")

        # (조회는 데이터 변경이 아니므로 commit 불필요하지만, 습관상 작성 가능)
        conn.commit()


        # ====================================================================
        # 📌 문제 4 — UPDATE 연습
        # ====================================================================
        # 설명: 문제의 요구사항(id=2)을 해결하기 위해, 
        # 먼저 '이영희'의 실제 UUID를 조회한 뒤 해당 ID로 나이를 수정합니다.
        
        # 1. 이영희의 UUID 찾기
        cursor.execute("SELECT id FROM students WHERE name = '이영희';")
        target_row = cursor.fetchone()
        
        if target_row:
            target_uuid = target_row[0]
            # 2. 찾은 UUID로 나이 업데이트 (21 -> 25)
            cursor.execute("UPDATE students SET age = 25 WHERE id = %s;", (target_uuid,))
        
        # 단계별 저장 (Break)
        conn.commit()


        # ====================================================================
        # 📌 문제 5 — DELETE 연습
        # ====================================================================
        # 설명: '박철수'(id=3 가정)를 삭제하기 위해 이름을 통해 UUID를 찾고 삭제합니다.
        
        # 1. 박철수의 UUID 찾기
        cursor.execute("SELECT id FROM students WHERE name = '박철수';")
        target_row = cursor.fetchone()
        
        if target_row:
            target_uuid = target_row[0]
            # 2. 찾은 UUID로 데이터 삭제
            cursor.execute("DELETE FROM students WHERE id = %s;", (target_uuid,))
        
        # 단계별 저장 (Break)
        conn.commit()


#         # ====================================================================
#         # 📌 문제 6 — PRIMARY KEY 이해 문제 (주석 답변)
#         # ====================================================================
#         """
#         [질문]
#         INSERT INTO books (book_id, title, price) VALUES (1, '책 A', 10000);
#         INSERT INTO books (book_id, title, price) VALUES (1, '책 B', 15000);
        
#         위 쿼리 실행 시 발생하는 문제에 대한 답변입니다.

#         1. 어떤 에러가 발생하는가?
#            - 첫 번째 에러: Data Type Mismatch Error 
#              (UUID 타입 컬럼에 정수 '1'을 넣으려 해서 형식이 맞지 않음)
#            - 두 번째 에러(타입이 맞다고 가정 시): Unique Constraint Violation Error 
#              (중복된 키값 에러)

#         2. 왜 발생하는가?
#            - books 테이블의 book_id는 UUID 타입으로 설정되었으나, 
#              입력값은 Integer(정수) 타입이므로 호환되지 않습니다.
#            - 만약 타입이 맞더라도 Primary Key는 유일해야 하는데, 
#              두 번째 INSERT 문에서 똑같은 ID(1)를 다시 넣으려 했기 때문에 충돌합니다.

#         3. PRIMARY KEY 의 규칙
#            - UNIQUE: 테이블 내의 모든 행(Row)은 서로 다른 유일한 값을 가져야 합니다 (중복 불가).
#            - NOT NULL: 비어있는 값(Null)을 가질 수 없습니다.
#         """

# except Exception as e:
#     print(f"에러 발생: {e}")
#     conn.rollback() # 에러 발생 시 이전 상태로 되돌림

# finally:
#     if conn:
#         conn.close()