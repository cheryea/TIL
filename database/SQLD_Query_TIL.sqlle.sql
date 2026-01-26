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

# ==================================================
# 컬럼이 띄어쓰기가 있는 경우, ""로 감싸서 하나의 컬럼명으로 인식하게 한다.
# 문자의 경우 '' (홑따옴표)를 사용한다.


# SQL 문법 순서
-- SELECT
-- FROM
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



# ==================================================
# - ORDER BY : 정렬
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

# > 학생 + 전공 테이블 조인
SELECT s.name, 
    m.major_name 
FROM student s 
JOIN major m ON s.major_id = m.id;
-- student 테이블과 major 테이블을 조인하여 학생 이름과 전공명 조회



# ==================================================
# - 서브쿼리 (SQLD 단골)
# ==================================================

# > 평균 학년보다 높은 학생 조회
SELECT * FROM student 
WHERE grade > (
    SELECT AVG(grade) FROM student
);
-- 전체 학생 평균 학년보다 높은 학생 조회



