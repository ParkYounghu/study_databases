
CREATE TABLE news_articles (
    title VARCHAR(500),
    url VARCHAR(500),
    author VARCHAR(500),
    published_at INT
);


INSERT INTO new_articles (title, url, author, published_at)
VALUES ('AI 시대 도래', 'https://news.com/ai', '홍길동', 20250101);

INSERT INTO new_articles (title, url, author, published_at)
VALUES ('경제 성장률 상승', 'https://news.com/economy', '이영희', 20250105);


SELECT title, url, author, published_at
FROM new_articles;


SELECT * FROM new_articles 
WHERE author = '홍길동';

UPDATE new_articles
SET title = 'AI 시대의 새로운 지평'
WHERE title = 'AI 시대 도래';

DELETE FROM new_articles
WHERE title = '경제 성장률 상승';