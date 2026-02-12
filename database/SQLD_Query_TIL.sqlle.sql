-- DDL: 데이터베이스의 구조(테이블) 를 정의하는 명령어
# 데이터베이스 생성
CREATE DATABASE postgres;


# 기본적인 테이블 생성
-- 전공 테이블
CREATE TABLE major (
    id INT PRIMARY KEY,
    major_name VARCHAR(50)
);


-- 학생 테이블
CREATE TABLE student (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    grade INT,
    major VARCHAR(50),
    major_id INT,
    mentor_id INT
);

# > student 테이블 삭제
DROP TABLE student;
-- student 테이블 자체를 완전히 삭제 (데이터 + 구조 모두 삭제)


# > 존재하면 삭제 (오류 방지)
DROP TABLE IF EXISTS student;
-- student 테이블이 있으면 삭제, 없으면 오류 없이 넘어감


-- DML: 테이블 안의 데이터를 조회·추가·수정·삭제하는 명령어
# - 새로운 데이터 추가
-- 전공 데이터
INSERT INTO major (id, major_name) VALUES
    (1, '컴퓨터공학'),
    (2, '경영학'),
    (3, '수학'),
    (4, '물리학');   -- 학생 없는 전공 (RIGHT / FULL JOIN 확인용)


-- 학생 데이터
INSERT INTO student (id, name, grade, major, major_id, mentor_id) VALUES
    (2024001, '철수', 3, '컴퓨터공학', 1, NULL),     -- 멘토 없음
    (2024002, '영희', 2, NULL,        NULL, 2024001), -- 전공 없음 (LEFT JOIN용)
    (2024003, '민수', 1, '수학',       3, 2024001),
    (2024004, '지은', 2, '컴퓨터공학', 1, 2024003),
    (2024005, '호준', 3, '경영학',     2, 2024001),
    (2024006, '서연', 3, '컴퓨터공학', 1, 2024001);



# ==================================================
# 컬럼이 띄어쓰기가 있는 경우, ""로 감싸서 하나의 컬럼명으로 인식하게 한다.
# 문자의 경우 '' (홑따옴표)를 사용한다.

# SQL 문법 순서
-- SELECT
-- FROM
-- └ JOIN
-- WHERE
-- GROUP BY
-- HAVING
-- ORDER BY
-- LIMIT OFFSET

# ==================================================



# ==================================================
# - SELECT : 데이터 조회
# ==================================================

# > 모든 필드 조회
SELECT * FROM student;
-- student 테이블의 모든 컬럼과 모든 행을 조회한다.


# > 특정 필드 조회
SELECT name, 
    grade 
FROM student;
-- name과 grade 컬럼만 선택하여 조회한다.


# > 테이블 별칭(alias) 사용
SELECT s.name, 
    s.grade
FROM student s;
-- student 테이블에 s라는 별칭을 사용해 name, grade 컬럼 조회


# > 컬럼 별칭(alias) 사용
SELECT name AS 학생명,
    grade AS 학년
FROM student;
-- 컬럼에 별칭을 지정하여 조회 결과의 컬럼명을 변경


# > WHERE : 조건 필터링
SELECT *
FROM student
WHERE grade = 2;
-- grade 값이 2인 행만 조회


# > DISTINCT : 중복 제거
SELECT DISTINCT major 
FROM student;
-- major 컬럼의 중복된 값을 제거하여 조회


# > BETWEEN : 범위 조건
SELECT *
FROM student 
WHERE grade BETWEEN 2 AND 3;
-- grade 값이 2 이상 3 이하인 행 조회


# > IN : 여러 값 조건
SELECT * 
FROM student 
WHERE major IN ('컴퓨터공학', '경영학');
-- major 값이 지정한 목록 중 하나인 행 조회


# > LIKE : 문자열 검색
SELECT * 
FROM student
WHERE name LIKE '김%'       -- '김'으로 시작
WHERE name LIKE '%수'       -- '수'로 끝남
WHERE name LIKE '%철%'      -- '철'이 포함
WHERE name NOT LIKE '이%'    -- '이'로 시작하지 않음


# > IS NULL / IS NOT NULL
SELECT * 
FROM student 
WHERE major IS NULL;
-- major 값이 NULL인 행 조회


# > COALESCE: 컬럼 값이 NULL이면 지정한 값으로 대체
# : COALESCE = NVL(Oracle 전용 함수)
SELECT name,
       COALESCE(major, '미정') AS 전공
FROM student;
-- major 컬럼이 NULL이면 '미정'으로 표시


# > COALESCE: 숫자 컬럼에서 NULL이면 0으로 대체
SELECT name,
       COALESCE(mentor_id, 0) AS 멘토
FROM student;
-- mentor_id가 NULL이면 0으로 표시



# ==================================================
# - ORDER BY : 정렬
# : 문자열 내림차순
# : 1. 왼쪽 글자부터 비교
# : 2. 글자가 다르면 그 글자 순서로 결정
# : 3. 글자가 같으면 다음 글자 비교
# : 4. 한쪽 문자열이 끝나면 → 짧은 문자열이 뒤로
# : 'ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ'..
# : '99', '9', '11', '1010', '101', '1000', '100', '10', '1'..
# ==================================================

# > 오름차순 정렬 (기본)
SELECT * 
FROM student 
ORDER BY grade;
-- grade 기준 오름차순으로 정렬


# > 내림차순 정렬
SELECT * 
FROM student 
ORDER BY grade DESC;
-- grade 기준 내림차순으로 정렬


# > 다중 정렬
SELECT * 
FROM student 
ORDER BY grade DESC, name ASC;
-- grade 내림차순, name 오름차순으로 정렬



# ==================================================
# - GROUP BY : 그룹화 (집계)
# : GROUP BY는 “집계 결과를 어떤 단위(= ~별)로 보고 싶은지”를 적는 것
# ==================================================

# > 학년별 학생 수
SELECT grade,
    COUNT(*)
FROM student
GROUP BY grade;
-- 학년별로 학생 수 집계


# > 전공별 평균 학년
SELECT major,
    AVG(grade) 
FROM student 
GROUP BY major;
-- 전공별 평균 학년 계산



# ==================================================
# - HAVING : 그룹 조건
# ==================================================

# > 학생 수가 3명 이상인 전공
SELECT major, 
    COUNT(*) AS student_count 
FROM student 
GROUP BY major 
HAVING COUNT(*) >= 3;
-- 학생 수가 3명 이상인 전공만 조회



# ==================================================
# - 집계 함수 (시험 필수)
# ==================================================

# > 전체 학생 수
SELECT COUNT(*) 
FROM student;
-- student 테이블 전체 학생 수 조회


# > 최고 학년
SELECT MAX(grade) 
FROM student;
-- grade 컬럼의 최대값 조회


# > 최저 학년
SELECT MIN(grade) 
FROM student;
-- grade 컬럼의 최소값 조회


# > 평균 학년
SELECT AVG(grade) 
FROM student;
-- grade 컬럼의 평균값 조회


# > 학년 합계
SELECT SUM(grade) 
FROM student;
-- grade 컬럼의 합계 조회



# ==================================================
# - LIMIT / OFFSET : 페이징 (PostgreSQL)
# ==================================================

# > 상위 5명 조회
SELECT * 
FROM student 
LIMIT 5;
-- 상위 5개 행 조회


# > 6번째부터 5명 조회
SELECT * 
FROM student 
OFFSET 5 LIMIT 5;
-- 6번째 행부터 5개 행 조회



# ==================================================
# - UPDATE : 기존 데이터 수정
# ==================================================

UPDATE student 
SET grade = 2, 
    major = '경제학' 
WHERE id = '2024001';
-- id가 2024001인 학생의 grade와 major 수정



# ==================================================
# - DELETE : 데이터 삭제
# ==================================================

DELETE FROM student 
WHERE id = '2024003';
-- id가 2024003인 학생 삭제



# ==================================================
# - JOIN : 테이블 연결 (시험 핵심)
# ==================================================

# > 학생 + 전공 테이블 INNER JOIN
SELECT s.name, 
    m.major_name 
FROM student s 
JOIN major m 
    ON s.major_id = m.id;
-- student 테이블과 major 테이블을 조인하여 학생 이름과 전공명 조회 (공통값만)


# > 학생 + 전공 테이블 LEFT JOIN
SELECT s.name, 
       m.major_name 
FROM student s 
LEFT JOIN major m 
    ON s.major_id = m.id;
-- student 테이블의 모든 행과 일치하는 major 값 조회, 없는 경우 NULL


# > 학생 + 전공 테이블 RIGHT JOIN
SELECT s.name, 
       m.major_name 
FROM student s 
RIGHT JOIN major m 
    ON s.major_id = m.id;
-- major 테이블의 모든 행과 일치하는 student 값 조회, 없는 경우 NULL

-- LEFT JOIN → 모든 학생 포함
-- | name | major_name |
-- |------|------------|
-- | 철수 | 컴퓨터공학 |
-- | 영희 | NULL |
-- | 민수 | 수학 |

-- RIGHT JOIN → 모든 전공 포함
-- | name | major_name |
-- |------|------------|
-- | 철수 | 컴퓨터공학 |
-- | 민수 | 수학 |
-- | NULL | 물리 |


# > 학생 테이블 SELF JOIN (선배-후배 관계)
SELECT s1.name AS student_name,
       s2.name AS mentor_name
FROM student s1
JOIN student s2
    ON s1.mentor_id = s2.id;
-- student 테이블을 자기 자신과 조인하여 학생과 멘토(선배) 관계 조회


# > 학생 + 전공 테이블 FULL OUTER JOIN
SELECT s.name, 
       m.major_name 
FROM student s 
FULL OUTER JOIN major m 
    ON s.major_id = m.id;
-- student와 major 테이블의 모든 행 조회, 없는 값은 NULL


# > 학생 + 전공 테이블 CROSS JOIN
SELECT s.name,
       m.major_name
FROM student s
CROSS JOIN major m;
-- student와 major의 모든 조합 생성 (조건 없음)



# ==================================================
# - VIEW : 가상의 테이블 생성
# : 뷰(View) = 실제 테이블 데이터를 SELECT문을 기반으로 만든 가상 테이블
# : 실제 데이터는 저장되지 않고, 조회 시 계산되어 보여짐
# : 복잡한 SELECT, JOIN, GROUP BY, 집계 함수 등을 단순화 가능
# : 하나 이상의 테이블을 조합한 복합뷰 생성 가능하지만 DML 제약이 생김
# ==================================================


# > 학생 이름과 학년만 조회하는 뷰 생성 (복합뷰)
CREATE VIEW student_view AS
SELECT name, grade
FROM student;
-- student 테이블에서 name, grade 컬럼만 뽑아 student_view라는 가상 테이블 생성


# > 뷰에서 데이터 조회
SELECT * 
FROM student_view;
-- student_view 뷰를 조회하면 name과 grade 컬럼만 나온다


# > 뷰에 조건 걸어 조회
SELECT * 
FROM student_view
WHERE grade = 3;
-- student_view에서 학년이 3인 학생만 조회


# > 뷰를 이용해 정렬
SELECT * 
FROM student_view
ORDER BY name ASC;
-- student_view에서 이름 기준 오름차순 정렬



# ==================================================
# - 서브쿼리 (SQLD 단골)
# ==================================================

# > 평균 학년보다 높은 학생 조회
SELECT * FROM student 
WHERE grade > (
    SELECT AVG(grade) FROM student
);
-- 전체 학생 평균 학년보다 높은 학생 조회

