-- DDL: 데이터베이스의 구조(테이블) 를 정의하는 명령어
# 기본적인 테이블 생성
CREATE TABLE student (
    id VARCHAR(7) PRIMARY KEY,
    name VARCHAR(10),
    grade INT, 
    major VARCHAR(20)
);



-- DML: 테이블 안의 데이터를 조회·추가·수정·삭제하는 명령어
# - 새로운 데이터 추가
INSERT INTO student VALUES 
    ('2024002', '이영희', 2, '경영학'),
    ('2024003', '박민수', 3, '물리학');


# 컬럼이 띄어쓰기가 있는 경우, ""로 감싸서 하나의 컬럼명으로 인식하게 한다.
# 문자의 경우 '' (홑따옴표)를 사용한다.


# - SELECT : 데이터 조회
# > 모든 필드 조회
SELECT * FROM student;

# > 특정 필드 조회
SELECT student.name, student.grade FROM student;
SELECT s.name, s.grade FROM student s;
SELECT name, grade FROM student;

# 컬럼 별칭(alias)을 사용한 SQL DML SELECT 조회 쿼리
SELECT name 학생명, grade 학년 FROM student;

# > WHERE : 데이터 필터링 할 때 사용하는 조건절
SELECT * FROM student WHERE grade = 2;

# > DISTINCT : 중복된 행(row) 제거
SELECT DISTINCT major FROM student;


# - UPDATE : 기존 데이터 수정
UPDATE student 
SET grade = 2, major = '경제학' 
WHERE id = '2024001';


# - DELETE : 데이터 삭제
DELETE FROM student 
WHERE id = '2024003';
