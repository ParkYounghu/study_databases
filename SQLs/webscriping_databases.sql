-- CREATE TABLE study_webscripings_database (
--     contents varchar(500),
--     link varchar(500),
--     link_html varchar(500),
--     link_href varchar(500)
-- );

select contents, link, link_html, link_href
from study_webscripings_database

CREATE TABLE study_webscripings_database (
    id varchar(500) PRIMARY KEY,
    contents varchar(500),
    link varchar(500),
    link_html varchar(500),
    link_href varchar(500),
    created_at varchar(500) DEFAULT NOW()
);