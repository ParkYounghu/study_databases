-- UUID primary key 사용
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE users_uuid_name (
  id_name UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name VARCHAR(100)
);

insert into users_uuid_name (name) 
values
('Alice'),
('Bob'),
('Charlie');

select * from users_uuid_name;

