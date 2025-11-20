-- DELETE Syntax
-- DELETE FROM table_name WHERE condition;

DELETE FROM new_articles WHERE title = 'AI 시대 도래';

UPDATE persons
SET firstname = 'Hu', lastname = 'Bread'
WHERE personid = 2;