CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE students (
  id UUID,
  name VARCHAR(50),
  age INT
);

select  id, name, age
from students;