-- [문제 1] 테이블 생성 (students)
-- 실무 Tip: 테이블을 다시 만들 땐 'DROP TABLE IF EXISTS students;'를 먼저 실행하기도 함.
CREATE TABLE students (
    id INT PRIMARY KEY,    -- 고유 식별자 (중복 불가, NULL 불가)
    name VARCHAR(50),      -- 이름
    age INT                -- 나이
);

select id, name, age
from students

-- [문제 2] 데이터 삽입 (INSERT)
-- 한 번에 여러 행을 넣는 것이 성능상 유리할 때가 많네.
INSERT INTO students (id, name, age)
VALUES 
    (1, '홍길동', 23),
    (2, '이영희', 21),
    (3, '박철수', 26);

-- [문제 3] 데이터 조회 (SELECT)
-- 3-1. 전체 데이터 조회
SELECT * FROM students;

-- 3-2. 나이가 22세 이상인 학생 조회
SELECT * FROM students 
WHERE age >= 22;

-- 3-3. 이름이 '홍길동'인 학생 조회
SELECT * FROM students 
WHERE name = '홍길동';

-- [문제 4] 데이터 수정 (UPDATE)
-- id가 2인(이영희) 학생의 나이를 25로 변경
UPDATE students 
SET age = 25 
WHERE id = 2;

-- [문제 5] 데이터 삭제 (DELETE)
-- id가 3인(박철수) 학생 데이터 삭제
DELETE FROM students 
WHERE id = 3;


-- 문제 6번에 대한 설명
1. 질문에 대한 답 (분석)
어떤 에러가 발생하는가?

Unique Constraint Violation (고유 제약 조건 위반) 또는 Duplicate Entry 에러가 발생한다.

(예: Error Code: 1062. Duplicate entry '1' for key 'books.PRIMARY')

왜 발생하는가?

book_id는 **PRIMARY KEY(기본키)**로 설정되어 있다.

첫 번째 INSERT 문에서 이미 book_id가 1인 데이터를 넣었다.

그런데 두 번째 INSERT 문에서 또다시 book_id를 1로 설정해서 넣으려고 했기 때문에, **"이미 1번이라는 ID를 가진 책이 있는데 또 1번을 넣을 수 없다"**며 DB가 거부한 것이다.

PRIMARY KEY의 규칙

Unique (유일성): 테이블 내의 모든 행은 서로 다른 PK 값을 가져야 한다 (중복 불가).

Not Null (최소성): PK 컬럼은 비어있는 값(NULL)을 허용하지 않는다.

2. 해결 방법 및 최종 형태
이 문제를 해결하려면 두 번째 책('책 B')의 book_id를 **1이 아닌 다른 숫자(예: 2)**로 변경해서 넣어야 한다. PK는 사람의 주민등록번호와 같아서 겹치면 안 되기 때문이지.

-- 1. 테이블 생성
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(100),
    price INT
);

-- 2. 첫 번째 데이터 삽입 (성공)
INSERT INTO books (book_id, title, price)
VALUES (1, '책 A', 10000);

-- 3. 두 번째 데이터 삽입 (수정됨)
-- 해결책: book_id를 1에서 2로 변경하여 중복을 피함
INSERT INTO books (book_id, title, price)
VALUES (2, '책 B', 15000);

-- 확인용 조회
SELECT * FROM books;