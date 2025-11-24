import psycopg2
from psycopg2.extras import DictCursor

# 1. 데이터베이스 연결 설정
db_host = "db_postgresql"
db_port = "5432"
db_name = "main_db"
db_user = "admin"
db_password = "admin123"

def get_db_connection():
    """데이터베이스 연결을 생성하여 반환하는 헬퍼 함수"""
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
    return conn

# 📌 문제 1 — 테이블 생성 함수
def create_books_table():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            # UUID 생성을 위한 확장 기능 활성화 (필수)
            cur.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')
            
            # 기존 테이블이 있다면 삭제 (실습용)
            cur.execute("DROP TABLE IF EXISTS books;")
            
            # 테이블 생성 쿼리
            create_query = """
            CREATE TABLE books (
                id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                title VARCHAR(100),
                price INT
            );
            """
            cur.execute(create_query)
            conn.commit()
            print("books 테이블이 생성되었습니다.")
    except Exception as e:
        print(f"테이블 생성 중 오류 발생: {e}")
        conn.rollback()
    finally:
        conn.close()

# 📌 문제 2 — INSERT 함수
def insert_books():
    conn = get_db_connection()
    data = [
        ("파이썬 입문", 19000),
        ("알고리즘 기초", 25000),
        ("네트워크 이해", 30000)
    ]
    
    try:
        with conn.cursor() as cur:
            insert_query = "INSERT INTO books (title, price) VALUES (%s, %s);"
            # executemany를 사용하여 효율적으로 다중 삽입
            cur.executemany(insert_query, data)
            conn.commit()
            print(f"{cur.rowcount}개 도서가 삽입되었습니다.")
    except Exception as e:
        print(f"데이터 삽입 중 오류 발생: {e}")
        conn.rollback()
    finally:
        conn.close()

# 📌 문제 3 — SELECT 함수들
def get_all_books():
    conn = get_db_connection()
    try:
        # DictCursor를 사용하여 딕셔너리 형태로 결과를 받음 (가독성 향상)
        with conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute("SELECT * FROM books;")
            rows = cur.fetchall()
            print("\n[전체 도서 목록]")
            for row in rows:
                print(dict(row))
            return rows
    except Exception as e:
        print(f"전체 조회 중 오류 발생: {e}")
    finally:
        conn.close()

def get_expensive_books():
    conn = get_db_connection()
    try:
        with conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute("SELECT * FROM books WHERE price >= 25000;")
            rows = cur.fetchall()
            print("\n[25000원 이상 도서 목록]")
            for row in rows:
                print(dict(row))
    except Exception as e:
        print(f"가격 조건 조회 중 오류 발생: {e}")
    finally:
        conn.close()

def get_book_by_title(title):
    conn = get_db_connection()
    try:
        with conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute("SELECT * FROM books WHERE title = %s;", (title,))
            row = cur.fetchone()
            print(f"\n['{title}' 검색 결과]")
            if row:
                print(dict(row))
            else:
                print("검색된 도서가 없습니다.")
    except Exception as e:
        print(f"제목 검색 중 오류 발생: {e}")
    finally:
        conn.close()

# 📌 문제 4 — UPDATE 함수
def update_second_book_price():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            # 1. 두 번째 도서의 UUID 조회 (저장된 순서를 보장하기 위해 OFFSET 사용)
            # 주의: 실제 운영 DB에서는 ORDER BY 없이 순서를 보장하지 않으나, 실습을 위해 단순 조회
            cur.execute("SELECT id FROM books ORDER BY title LIMIT 1 OFFSET 1;")
            result = cur.fetchone()
            
            if result:
                target_id = result[0]
                # 2. UPDATE 수행
                cur.execute("UPDATE books SET price = 27000 WHERE id = %s;", (target_id,))
                conn.commit()
                print("두 번째 도서 가격이 27000으로 수정되었습니다.")
            else:
                print("수정할 두 번째 도서가 존재하지 않습니다.")
    except Exception as e:
        print(f"데이터 수정 중 오류 발생: {e}")
        conn.rollback()
    finally:
        conn.close()

# 📌 문제 5 — DELETE 함수
def delete_third_book():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            # 1. 세 번째 도서의 UUID 조회 (0부터 시작하므로 OFFSET 2)
            cur.execute("SELECT id FROM books ORDER BY title LIMIT 1 OFFSET 2;")
            result = cur.fetchone()
            
            if result:
                target_id = result[0]
                # 2. DELETE 수행
                cur.execute("DELETE FROM books WHERE id = %s;", (target_id,))
                conn.commit()
                print("세 번째 도서가 삭제되었습니다.")
            else:
                print("삭제할 세 번째 도서가 존재하지 않습니다.")
    except Exception as e:
        print(f"데이터 삭제 중 오류 발생: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == '__main__':
    # 실행 순서대로 함수 호출
    create_books_table()
    insert_books()
    
    # 조회 테스트
    get_all_books()
    get_expensive_books()
    get_book_by_title("파이썬 입문")
    
    # 수정 및 삭제 테스트
    update_second_book_price()
    delete_third_book()
    
    # 최종 결과 확인
    print("\n=== 최종 결과 확인 ===")
    get_all_books()
