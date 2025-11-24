### json으로 변경 프롬프트 [Gemini]

```

너는 20년 간 코딩을 한 베테랑 개발자야.
python 문제를 풀어줘, 문제에 적혀있는 출력 예는 실행 시에 terminal에 출력되는 문자야.
prompts 폴더 안에 02_DMLs_functions.py 파일로 만들어져서 결과물이 나오게 해주고
함수 call은 아래 코드 안에서 실행할 수 있게 해줘
if __name__=='__main__':

[데이터 연결 설정]
import psycopg2

# 1. 데이터베이스 연결 설정
db_host = "db_postgresql"
db_port = "5432"
db_name = "main_db"
db_user = "admin"
db_password = "admin123"

visual studio code에서 terminal에서 gemini CLI를 쓸거니까 지금 내가 주는 프롬프트 요구사항을 json 형식으로 바꿔줘

📌 문제 1 — 테이블 생성 함수 만들기
아래 요구사항에 맞게 **Python 함수(create_books_table())**를 작성하시오.
 함수 실행 시 PostgreSQL에 books 테이블이 생성되어야 한다.
✔ 요구사항
테이블명: books
컬럼명
자료형
id
UUID PRIMARY KEY DEFAULT uuid_generate_v4()
title
VARCHAR(100)
price
INT
✨ 출력 예
books 테이블이 생성되었습니다.

📌 문제 2 — INSERT 함수 만들기
아래 데이터를 books 테이블에 추가하는 insert_books() 함수를 작성하시오.
✔ 테스트용 데이터
id
title
price
1
파이썬 입문
19000
2
알고리즘 기초
25000
3
네트워크 이해
30000
🔥 id는 자동 UUID이므로 INSERT 시 제외
✨ 출력 예
3개 도서가 삽입되었습니다.

📌 문제 3 — SELECT 함수 만들기
아래 조건을 만족하는 조회용 Python 함수들을 작성하시오.
✔ 요구 함수
전체 조회 함수

함수명: get_all_books()

가격이 25000원 이상인 데이터 조회 함수

함수명: get_expensive_books()

title 이 “파이썬 입문”인 데이터 조회 함수

함수명: get_book_by_title()

parameter: title

📌 문제 4 — UPDATE 함수 만들기
저장된 순서에서 두 번째 도서의 가격을 27000으로 변경하는 함수를 만드시오.
함수명: update_second_book_price()

옵션:

두 번째 도서의 UUID를 SELECT 로 먼저 가져온 후

UPDATE 를 수행한다.

✨ 출력 예
두 번째 도서 가격이 27000으로 수정되었습니다.

📌 문제 5 — DELETE 함수 만들기
저장된 순서에서 세 번째 도서 데이터를 삭제하는 Python 함수를 작성하시오.
함수명: delete_third_book()

옵션:

SELECT로 UUID 조회 후 DELETE 수행

✨ 출력 예
세 번째 도서가 삭제되었습니다.

```

### CLI prompt

```

{
  "persona": "You are a veteran developer with 20 years of experience in Python and Database management.",
  "task": "Create a Python script named '02_DMLs_functions.py' inside the 'prompts' folder to solve PostgreSQL problems using psycopg2.",
  "constraints": [
    "Use 'psycopg2' library for database connection.",
    "Ensure all function calls and execution logic are placed inside 'if __name__ == \"__main__\":'.",
    "Handle database connections and cursors properly (commit/close).",
    "Ensure the 'uuid-ossp' extension is enabled for UUID generation if necessary."
  ],
  "database_config": {
    "host": "db_postgresql",
    "port": "5432",
    "dbname": "main_db",
    "user": "admin",
    "password": "admin123"
  },
  "problems": [
    {
      "id": 1,
      "title": "Create Table",
      "function_name": "create_books_table",
      "requirements": {
        "table_name": "books",
        "columns": [
          {"name": "id", "type": "UUID PRIMARY KEY DEFAULT uuid_generate_v4()"},
          {"name": "title", "type": "VARCHAR(100)"},
          {"name": "price", "type": "INT"}
        ]
      },
      "expected_output": "books 테이블이 생성되었습니다."
    },
    {
      "id": 2,
      "title": "Insert Data",
      "function_name": "insert_books",
      "requirements": "Insert data excluding the ID column (auto-generated).",
      "data": [
        {"title": "파이썬 입문", "price": 19000},
        {"title": "알고리즘 기초", "price": 25000},
        {"title": "네트워크 이해", "price": 30000}
      ],
      "expected_output": "3개 도서가 삽입되었습니다."
    },
    {
      "id": 3,
      "title": "Select Data",
      "functions": [
        {
          "name": "get_all_books",
          "description": "Retrieve all records."
        },
        {
          "name": "get_expensive_books",
          "description": "Retrieve books with price >= 25000."
        },
        {
          "name": "get_book_by_title",
          "parameter": "title",
          "description": "Retrieve book where title matches the parameter (e.g., '파이썬 입문')."
        }
      ]
    },
    {
      "id": 4,
      "title": "Update Data",
      "function_name": "update_second_book_price",
      "logic": "Fetch the 2nd book's UUID via SELECT first, then UPDATE its price to 27000.",
      "expected_output": "두 번째 도서 가격이 27000으로 수정되었습니다."
    },
    {
      "id": 5,
      "title": "Delete Data",
      "function_name": "delete_third_book",
      "logic": "Fetch the 3rd book's UUID via SELECT first, then DELETE it.",
      "expected_output": "세 번째 도서가 삭제되었습니다."
    }
  ]
}

```