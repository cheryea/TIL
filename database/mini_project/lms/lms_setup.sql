SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';

-- =========================
-- 선생님 테이블
-- =========================
CREATE TABLE teacher (
    teacher_id   INT PRIMARY KEY,          -- 선생님 고유 식별자
    teacher_name VARCHAR(50) NOT NULL,      -- 선생님 이름
    intro        TEXT                       -- 선생님 소개
);


# 데이터 추가
INSERT INTO teacher (teacher_id, teacher_name, intro) VALUES
(1, '김선생', 'DB & SQL 전문 강사'),
(2, '이선생', '프론트엔드 전문 강사'),
(3, '박선생', '백엔드 전문 강사'),
(4, '최선생', 'AI & 데이터 분석 강사');


-- =========================
-- 학생 테이블
-- =========================
CREATE TABLE student (
    student_id   INT PRIMARY KEY,           -- 학생 고유 식별자
    student_name VARCHAR(50) NOT NULL        -- 학생 이름
);


# 데이터 추가
INSERT INTO student (student_id, student_name) VALUES
(1, '홍길동'),
(2, '김영희'),
(3, '박철수'),
(4, '최지은');


-- =========================
-- 강좌 테이블
-- =========================
CREATE TABLE course (
    course_id    INT PRIMARY KEY,            -- 강좌 고유 식별자
    teacher_id   INT NOT NULL,                -- 담당 선생님 ID
    course_title VARCHAR(100) NOT NULL,       -- 강좌 제목
    start_date   DATE,                        -- 시작일
    end_date     DATE,                        -- 종료일
    CONSTRAINT fk_course_teacher
        FOREIGN KEY (teacher_id)
        REFERENCES teacher(teacher_id)
);


# 데이터 추가
INSERT INTO course (course_id, teacher_id, course_title, start_date, end_date) VALUES
(1, 1, 'SQL 기초', '2026-01-01', '2026-12-31'), -- 진행중
(2, 1, 'DB 설계 실전', '2025-01-01', '2025-03-01'), -- 종료
(3, 2, 'React 입문', '2026-02-01', '2026-04-01'),
(4, 3, 'Python 기초', '2026-01-15', '2026-06-30'), -- 진행중
(5, 4, '머신러닝 입문', '2026-03-01', '2026-06-01'), -- 진행중
(6, 3, 'Spring Boot 실전', '2025-05-01', '2025-08-01'); -- 종료


-- =========================
-- 강의 테이블
-- =========================
CREATE TABLE lecture (
    lecture_id    INT PRIMARY KEY,           -- 강의 고유 식별자
    course_id     INT NOT NULL,               -- 소속 강좌 ID
    lecture_title VARCHAR(100) NOT NULL,      -- 강의 제목
    lecture_intro TEXT,                       -- 강의 설명
    CONSTRAINT fk_lecture_course
        FOREIGN KEY (course_id)
        REFERENCES course(course_id)
);


# 데이터 추가
INSERT INTO lecture (lecture_id, course_id, lecture_title, lecture_intro) VALUES
(1, 1, 'SELECT 기본', 'SELECT / WHERE'),
(2, 1, 'JOIN 기초', 'INNER / LEFT JOIN'),
(3, 2, '정규화', '1NF ~ 3NF'),
(4, 3, 'React 개요', '컴포넌트란?'),
(5, 4, 'Python 변수/자료형', 'Python 기본 자료형과 변수'),
(6, 4, '조건문과 반복문', 'if / for / while'),
(7, 5, '머신러닝 개념', '지도학습 / 비지도학습 소개'),
(8, 5, '회귀분석 실습', 'Linear Regression 실습'),
(9, 6, 'Spring 프로젝트 생성', 'Spring Boot 기본 프로젝트');



-- =========================
-- 수강평 테이블
-- =========================
CREATE TABLE review (
    review_id      INT PRIMARY KEY,           -- 리뷰 고유 식별자
    course_id      INT NOT NULL,               -- 대상 강좌 ID
    student_id     INT NOT NULL,               -- 작성 학생 ID
    review_content TEXT NOT NULL,              -- 리뷰 내용
    created_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- 작성일시
    CONSTRAINT fk_review_course
        FOREIGN KEY (course_id)
        REFERENCES course(course_id),
    CONSTRAINT fk_review_student
        FOREIGN KEY (student_id)
        REFERENCES student(student_id)
);


# 데이터 추가
INSERT INTO review (review_id, course_id, student_id, review_content) VALUES
(1, 1, 1, 'SQL 기초를 확실히 다질 수 있었어요'),
(2, 2, 2, 'DB 설계 감이 잡혔습니다'),
(3, 3, 1, 'React 입문으로 딱 좋아요'),
(4, 4, 3, 'Python 기초라 따라가기 쉬웠어요'),
(5, 5, 1, '머신러닝 개념이 잘 정리되어있음'),
(6, 6, 2, 'Spring Boot 실전 강의라서 프로젝트 이해에 도움됨');


-- =========================
-- 게시글 테이블
-- =========================
CREATE TABLE post (
    post_id    INT PRIMARY KEY,               -- 게시글 ID
    student_id INT NOT NULL,                  -- 작성자(학생) ID
    title      VARCHAR(200) NOT NULL,         -- 제목
    content    TEXT NOT NULL,                 -- 내용
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- 작성일시
    CONSTRAINT fk_post_student
        FOREIGN KEY (student_id)
        REFERENCES student(student_id)
);


# 데이터 추가
INSERT INTO post (post_id, student_id, title, content) VALUES
(1, 1, 'SQL 질문', 'JOIN이 헷갈려요'),
(2, 1, 'React 후기', '입문자에게 좋아요'),
(3, 2, 'DB 설계 후기', '정규화 설명 굿'),
(4, 3, 'Python 질문', '리스트와 딕셔너리 차이가 궁금합니다'),
(5, 4, '머신러닝 질문', 'KNN이 뭔가요?'),
(6, 3, 'Spring Boot 후기', '실습 위주라 좋았습니다');


-- =========================
-- 댓글 테이블
-- =========================
CREATE TABLE comment (
    comment_id INT PRIMARY KEY,               -- 댓글 ID
    post_id    INT NOT NULL,                  -- 게시글 ID
    student_id INT NOT NULL,                  -- 작성 학생 ID
    content    TEXT NOT NULL,                 -- 댓글 내용
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- 작성일시
    CONSTRAINT fk_comment_post
        FOREIGN KEY (post_id)
        REFERENCES post(post_id),
    CONSTRAINT fk_comment_student
        FOREIGN KEY (student_id)
        REFERENCES student(student_id)
);


# 데이터 추가
INSERT INTO comment (comment_id, post_id, student_id, content) VALUES
(1, 1, 2, 'JOIN은 예제 많이 보세요'),
(2, 1, 1, '감사합니다'),
(3, 3, 1, '저도 도움됐어요'),
(4, 4, 1, '리스트는 순서 O, 딕셔너리는 Key-Value'),
(5, 5, 2, 'KNN은 최근접 이웃 알고리즘'),
(6, 6, 4, '저도 동의합니다. 실습이 핵심');



-- =========================
-- 수강 신청 테이블
-- =========================
CREATE TABLE enrollment (
    student_id  INT NOT NULL,                 -- 학생 ID
    course_id   INT NOT NULL,                 -- 강좌 ID
    enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- 신청일
    PRIMARY KEY (student_id, course_id),      -- 복합 PK
    CONSTRAINT fk_enroll_student
        FOREIGN KEY (student_id)
        REFERENCES student(student_id),
    CONSTRAINT fk_enroll_course
        FOREIGN KEY (course_id)
        REFERENCES course(course_id)
);


# 데이터 추가
INSERT INTO enrollment (student_id, course_id) VALUES
(1, 1),
(1, 3),
(2, 2),
(3, 4),
(4, 5),
(3, 5),
(2, 4);


-- =========================
-- 관심 강좌 테이블
-- =========================
CREATE TABLE favorite_course (
    student_id INT NOT NULL,                  -- 학생 ID
    course_id  INT NOT NULL,                  -- 강좌 ID
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- 등록일
    PRIMARY KEY (student_id, course_id),
    CONSTRAINT fk_fav_course_student
        FOREIGN KEY (student_id)
        REFERENCES student(student_id),
    CONSTRAINT fk_fav_course_course
        FOREIGN KEY (course_id)
        REFERENCES course(course_id)
);


# 데이터 추가
INSERT INTO favorite_course (student_id, course_id) VALUES
(1, 2),
(2, 1),
(3, 5),
(4, 4),
(4, 6),
(2, 5);


-- =========================
-- 관심 선생님 테이블
-- =========================
CREATE TABLE favorite_teacher (
    student_id INT NOT NULL,                  -- 학생 ID
    teacher_id INT NOT NULL,                  -- 선생님 ID
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- 등록일
    PRIMARY KEY (student_id, teacher_id),
    CONSTRAINT fk_fav_teacher_student
        FOREIGN KEY (student_id)
        REFERENCES student(student_id),
    CONSTRAINT fk_fav_teacher_teacher
        FOREIGN KEY (teacher_id)
        REFERENCES teacher(teacher_id)
);


# 데이터 추가
INSERT INTO favorite_teacher (student_id, teacher_id) VALUES
(1, 1),
(1, 2),
(3, 3),
(3, 4),
(4, 1),
(4, 3);


# 선생님 목록 페이지
SELECT teacher_id,
    teacher_name,
    intro
FROM teacher
ORDER BY teacher_id DESC;


# 선생님 세부 페이지
-- 진행중인 강좌 목록
SELECT t.teacher_name,
    t.intro,
    c.course_title,
    c.start_date,
    c.end_date
FROM teacher t
JOIN course c
    ON t.teacher_id = c.teacher_id
WHERE t.teacher_id = :teacher_id
  AND CURRENT_DATE BETWEEN c.start_date AND c.end_date
ORDER BY c.start_date ASC;


-- 진행 했던 강좌 목록
SELECT t.teacher_name,
    t.intro,
    c.course_title,
    c.start_date,
    c.end_date
FROM teacher t
JOIN course c
    ON t.teacher_id = c.teacher_id
WHERE t.teacher_id = :teacher_id
  AND c.end_date < CURRENT_DATE
ORDER BY c.start_date DESC;


-- 수강평 모음
SELECT c.course_title,
    s.student_name,
    r.review_content,
    r.created_at
FROM review r
JOIN course c
    ON r.course_id = c.course_id
JOIN student s
    ON r.student_id = s.student_id
WHERE c.teacher_id = :teacher_id
ORDER BY r.created_at DESC;



# 강좌 모음 페이지
-- 강좌 목록
SELECT c.course_id,
    c.course_title,
    t.teacher_id,
    t.teacher_name,
    c.start_date,
    c.end_date
FROM course c
JOIN teacher t
    ON c.teacher_id = t.teacher_id
ORDER BY c.start_date DESC;



# 강좌 세부 페이지
-- 강의 목록
SELECT lecture_id,
    lecture_title,
    lecture_intro
FROM lecture
WHERE course_id = :course_id
ORDER BY lecture_id ASC;



# keyword에 관련된 검색 결과 페이지
-- 선생님 검색 결과
SELECT teacher_id,
    teacher_name,
    intro
FROM teacher
WHERE teacher_name ILIKE '%' || :keyword || '%'
ORDER BY teacher_name ASC;


-- 강좌 검색 결과
SELECT c.course_id,
    c.course_title,
    t.teacher_id,
    t.teacher_name,
    c.start_date,
    c.end_date
FROM course c
JOIN teacher t
    ON c.teacher_id = t.teacher_id
WHERE c.course_title ILIKE '%' || :keyword || '%'
ORDER BY c.start_date DESC;


# 마이페이지
-- 신청한 강좌 목록
SELECT c.course_id,
    c.course_title,
    t.teacher_id,
    t.teacher_name,
    c.start_date,
    c.end_date,
    e.enrolled_at
FROM enrollment e
JOIN course c
    ON e.course_id = c.course_id
JOIN teacher t
    ON c.teacher_id = t.teacher_id
WHERE e.student_id = :student_id
ORDER BY e.enrolled_at DESC;


-- 내가 관심 등록한 선생님 목록 
SELECT t.teacher_id,
       t.teacher_name,
       t.intro,
       ft.created_at
FROM favorite_teacher ft
JOIN student s
    ON ft.student_id = s.student_id
JOIN teacher t
    ON ft.teacher_id = t.teacher_id
WHERE s.student_id = :student_id
ORDER BY ft.created_at DESC;


-- 내가 관심 등록한 강좌 목록
SELECT c.course_id,
       c.course_title,
       t.teacher_id,
       t.teacher_name,
       c.start_date,
       c.end_date,
       fc.created_at
FROM favorite_course fc
JOIN course c
    ON fc.course_id = c.course_id
JOIN teacher t
    ON c.teacher_id = t.teacher_id
WHERE fc.student_id = :student_id
ORDER BY fc.created_at DESC;


-- 내 게시글 목록
SELECT p.post_id,
    p.title,
    p.created_at
FROM post p
WHERE p.student_id = :student_id
ORDER BY p.created_at DESC;


-- 내 댓글 목록
SELECT p.post_id,
    p.title,
    c.content,
    c.created_at
FROM comment c
JOIN post p
    ON c.post_id = p.post_id
WHERE c.student_id = :student_id
ORDER BY c.created_at DESC;



# 전체 게시판
-- 게시글 목록
SELECT p.post_id,
       s.student_name,
       p.title,
       p.content,
       p.created_at
FROM post p
JOIN student s
    ON p.student_id = s.student_id
ORDER BY p.created_at DESC, p.post_id DESC
LIMIT :size OFFSET :offset;



# 1번 게시글 세부 페이지
-- 게시글 내용
SELECT p.post_id,
    p.created_at,
    s.student_name,
    p.title,
    p.content
FROM post p
JOIN student s
    ON p.student_id = s.student_id
WHERE p.post_id = :post_id;


-- 댓글 내용
SELECT s.student_id,
    s.student_name,
    c.content,
    c.created_at
FROM comment c
JOIN student s
    ON c.student_id = s.student_id
WHERE c.post_id = :post_id
ORDER BY c.created_at DESC;
