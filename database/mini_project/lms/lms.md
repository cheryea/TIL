
# LMS - Data Model
#### Teacher
- teacher_id (PK)
- teacher_name
- intro


#### Review
- review_id (PK)
- course_id (FK)
- student_id   (FK)
- review_content
- created_at


#### Course
- course_id (PK)
- teacher_id (FK)
- course_title
- start_date
- end_date


#### Lecture
- lecture_id (PK)
- course_id (FK)
- lecture_title
- lecture_intro



#### Student
- student_id (PK)
- student_name


#### Post
- post_id     (PK)
- student_id     (FK)
- title
- content
- created_at


#### Comment
- comment_id   (PK)
- post_id      (FK)
- student_id      (FK)
- content
- created_at


#### Enrollment
- student_id   (PK, FK)
- course_id (PK, FK)
- enrolled_at


#### FavoriteCourse
- student_id   (PK, FK)
- course_id (PK, FK)
- created_at


#### FavoriteTeacher
- student_id    (PK, FK)
- teacher_id (PK, FK)
- created_at


```
Teacher 1 ── N Course 1 ── N Lecture
                    └── N Review
student    1 ── N Post  1 ── N Comment
student    N ── M Course (Enrollment)
student    N ── M Course (FavoriteCourse)
student    N ── M Teacher (FavoriteTeacher)
```



# LMS - API Spec
## GET / (메인 페이지)
- GET /teachers (선생님 모음 페이지)
- GET /courses (강좌 모음 페이지)
- GET /search (검색 결과 페이지)
- GET /students/${student.id}/mypage (마이페이지)
- GET /teachers (선생님 목록 페이지)
	#### GET /teachers?size=5 - 선생님 목록 일부
    ``` sql
    SELECT teacher_name,
        intro
    FROM teacher
    ORDER BY teacher_id DESC
    LIMIT :size;
    ```
- GET /courses (강좌 목록 페이지)
	#### GET /courses?size=5 - 강좌 목록 일부
    ```sql
    SELECT 
        t.teacher_name,
        c.course_title,
        c.start_date,
        c.end_date
    FROM course c
    JOIN teacher t
        ON c.teacher_id = t.teacher_id
    ORDER BY c.start_date DESC
    LIMIT :size;
    ```



## GET /teachers — 선생님 모음 페이지
### 선생님 목록
- GET /teachers
```sql
SELECT teacher_id,
    teacher_name,
    intro
FROM teacher
ORDER BY teacher_id DESC;
```



## GET /teachers/{teacher_id} — 선생님 세부 페이지
### 진행중인 강좌 목록
GET /teachers/{teacher_id}/courses/in-progress
```sql
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
```


### 진행했던 강좌 목록
GET /teachers/{teacher_id}/courses?status=finish
```sql
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
```


### 수강평 모음
GET /teachers/{teacher_id}/reviews
```sql
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
```



## GET /courses — 강좌 모음 페이지
### 강좌 목록
GET /courses
```sql
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
```



## GET /courses/{course_id} — 강좌 세부 페이지
### 강의 목록
GET /courses/{course_id}/lectures
```sql
SELECT lecture_id,
    lecture_title,
    lecture_intro
FROM lecture
WHERE course_id = :course_id
ORDER BY lecture_id ASC;
```



## GET /search — 검색 결과 페이지
### 선생님 검색 결과
GET /search?keyword=java&type=teacher
```sql
SELECT teacher_id,
    teacher_name,
    intro
FROM teacher
WHERE teacher_name ILIKE '%' || :keyword || '%'
ORDER BY teacher_name ASC;
```


### 강좌 검색 결과
GET /search?keyword=java&type=course
```sql
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
```



## GET /students/{student_id} — 마이페이지
### 신청한 강좌 목록
GET /students/{student_id}/courses
```sql
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
```


### 내가 관심 등록한 선생님
GET /students/{student_id}/favorite-teachers
```sql
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
```


### 내가 관심 등록한 강좌
GET /students/{student_id}/favorite-courses
```sql
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
```


### 내 게시글 목록
GET /students/{student_id}/posts
```sql
SELECT p.post_id,
    p.title,
    p.created_at
FROM post p
WHERE p.student_id = :student_id
ORDER BY p.created_at DESC;
```


### 내 댓글 목록
GET /students/{student_id}/comments
```sql
SELECT p.post_id,
    p.title,
    c.content,
    c.created_at
FROM comment c
JOIN post p
    ON c.post_id = p.post_id
WHERE c.student_id = :student_id
ORDER BY c.created_at DESC;
```



## GET /posts - 전체 게시판
### 게시글 목록
GET /posts?size=10&page=1
```sql
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
```



## GET /posts/{post_id} - 게시글 상세
### 게시글 내용
GET /posts/{post_id}
```sql
SELECT p.post_id,
    p.created_at,
    s.student_name,
    p.title,
    p.content
FROM post p
JOIN student s
    ON p.student_id = s.student_id
WHERE p.post_id = :post_id;
```


### 댓글 내용
GET /posts/{post_id}/comments
```sql
SELECT s.student_id
    s.student_name,
    c.content,
    c.created_at
FROM comment c
JOIN student s
    ON c.student_id = s.student_id
WHERE c.post_id = :post_id
ORDER BY c.created_at DESC;
```
