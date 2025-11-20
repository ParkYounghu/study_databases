-- 테이블명: web_links
--  컬럼:
-- link_text


-- link_url


-- category


-- 데이터:
-- "네이버", "https://naver.com", "portal"


-- "구글", "https://google.com", "portal"


-- "깃허브", "https://github.com", "dev"


-- 👉 요구:
-- 데이터 3개를 생성하는 INSERT문 작성


-- category가 "portal"인 링크만 조회


-- "깃허브"의 category를 "code" 로 수정


-- "네이버" 데이터 삭제

CREATE TABLE web_links (
    link_text varchar(500),
    link_url varchar(500),
    category varchar(500)
);


SELECT link_text, link_url, category
FROM web_links;

INSERT INTO web_links (link_text, link_url, category)
VALUES ('네이버', 'http://naver.com', 'portal');

INSERT INTO web_links (link_text, link_url, category)
VALUES ('구글', 'https://google.com', 'portal');

INSERT INTO web_links (link_text, link_url, category)
VALUES ('깃허브', 'https://github.com', 'dev')

SELECT * FROM web_links
WHERE category = 'portal';

UPDATE web_links
SET category = 'code'
WHERE link_text = '깃허브';

DELETE FROM web_links WHERE link_text = '네이버';