-- Active: 1769144485644@@127.0.0.1@5432@dvdrental@public


-- 배우가 출연한 / 영화의 / 제목을 조회
SELECT f.title,
    a.first_name,
    a.last_name
FROM actor a
JOIN film_actor fa
    ON a.actor_id = fa.actor_id
JOIN film f
    ON fa.film_id = f.film_id

-- first_name이 `PENELOPE` 인 배우가 출연한 / 영화의 / 제목을 조회
SELECT f.title
FROM actor a
JOIN film_actor fa
    ON a.actor_id = fa.actor_id
JOIN film f
    ON fa.film_id = f.film_id
WHERE a.first_name = 'Penelope';
    
-- 영화 별 / 출연 배우의 수를 조회
SELECT f.title,
       COUNT(fa.actor_id) AS actor_count
FROM film f
JOIN film_actor fa
    ON f.film_id = fa.film_id
GROUP BY f.title;

-- 영화 별 / 출연 배우의 수가 5가 넘는 데이터를 / 배우의 수가 큰순으로 조회
SELECT f.title,
       COUNT(fa.actor_id) AS actor_count
FROM film f
JOIN film_actor fa
    ON f.film_id = fa.film_id
GROUP BY f.title
HAVING COUNT(fa.actor_id) > 5
ORDER BY actor_count DESC;

-- 고객의 대여 정보 조회
SELECT c.customer_id,
       c.first_name,
       c.last_name,
       r.rental_date,
       r.return_date
FROM customer c
JOIN rental r
    ON c.customer_id = r.customer_id
ORDER BY c.customer_id;

-- 고객이 대여한 영화 정보 조회
SELECT c.customer_id,
       c.first_name,
       c.last_name,
       f.title,
       r.rental_date,
       r.return_date
FROM customer c
JOIN rental r
    ON c.customer_id = r.customer_id
JOIN inventory i
    ON r.inventory_id = i.inventory_id
JOIN film f
    ON i.film_id = f.film_id;

-- `YENTL IDAHO` 영화를 대여한 고객 정보 조회
SELECT DISTINCT
       c.customer_id,
       c.first_name,
       c.last_name
FROM film f
JOIN inventory i
    ON f.film_id = i.film_id
JOIN rental r
    ON i.inventory_id = r.inventory_id
JOIN customer c
    ON r.customer_id = c.customer_id
WHERE f.title = 'Yentl Idaho';

-- 각 직원이 일하는 매장의 주소와 도시를 조회
SELECT s.first_name,
       s.last_name,
       a.address,
       c.city
FROM staff s
JOIN store st ON s.store_id = st.store_id
JOIN address a ON st.address_id = a.address_id
JOIN city c ON a.city_id = c.city_id;

-- 고객별로 대여한 영화 제목과 지불한 금액, 날짜를 조회
SELECT c.first_name,
       c.last_name,
       f.title,
       p.amount,
       p.payment_date
FROM customer c
JOIN rental r
  ON c.customer_id = r.customer_id
JOIN payment p
  ON r.rental_id = p.rental_id
JOIN inventory i
  ON r.inventory_id = i.inventory_id
JOIN film f
  ON i.film_id = f.film_id;

-- 국가별 고객 수를 조회
SELECT co.country,
       COUNT(c.customer_id) AS customer_count
FROM customer c
JOIN address a
  ON c.address_id = a.address_id
JOIN city ci
  ON a.city_id = ci.city_id
JOIN country co
  ON ci.country_id = co.country_id
GROUP BY co.country;

-- `Action` 카테고리에 출연한 배우 조회
SELECT DISTINCT a.first_name,
                a.last_name
FROM actor a
JOIN film_actor fa
  ON a.actor_id = fa.actor_id
JOIN film f
  ON fa.film_id = f.film_id
JOIN film_category fc
  ON f.film_id = fc.film_id
JOIN category c
  ON fc.category_id = c.category_id
WHERE c.name = 'Action';

-- 재고(inventory)가 없는 영화 찾기
SELECT f.title
FROM film f
LEFT JOIN inventory i
  ON f.film_id = i.film_id
WHERE i.inventory_id IS NULL;

-- 카테고리별 평균 대여료
SELECT c.name AS category,
       AVG(f.rental_rate) AS avg_rental_rate
FROM category c
JOIN film_category fc
  ON c.category_id = fc.category_id
JOIN film f
  ON fc.film_id = f.film_id
GROUP BY c.name;
