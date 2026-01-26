-- Active: 1769144485644@@127.0.0.1@5432@world@public


SELECT * FROM city;
-- | 컬럼명           | 의미(해석)        |
-- | ------------- | ------------- |
-- | `ID`          | 도시 고유 번호 (PK) |
-- | `Name`        | 도시명           |
-- | `CountryCode` | 국가 코드 (FK)    |
-- | `District`    | 주/도           |
-- | `Population`  | 도시 인구         |

SELECT * FROM country;
-- | 컬럼명              | 의미(해석)             |
-- | ---------------- | ------------------ |
-- | `Code`           | 국가 코드 (PK, ISO 코드) |
-- | `Name`           | 국가명                |
-- | `Continent`      | 대륙                 |
-- | `Region`         | 지역                 |
-- | `SurfaceArea`    | 국토 면적              |
-- | `IndepYear`      | 독립 연도              |
-- | `Population`     | 인구 수               |
-- | `LifeExpectancy` | 기대 수명(예상 수명)       |
-- | `GNP`            | 국민총생산              |
-- | `GNPOld`         | 이전 국민총생산           |
-- | `LocalName`      | 현지 국가명             |
-- | `GovernmentForm` | 정부 형태              |
-- | `HeadOfState`    | 국가 원수              |
-- | `Capital`        | 수도 (city 테이블 참조)   |
-- | `Code2`          | 국가 보조 코드           |



# SELECT(데이터 조회) 실습

-- 인구가 800만 이상인 
-- 도시의
-- name, population을 조회하시오
SELECT name, population
FROM city
WHERE population >= 8000000

-- 한국에 있는
-- 도시의
-- name, countycode를 조회하시오
SELECT name, countrycode
FROM city
WHERE countrycode = 'KOR';

-- 유럽 대륙에 속한 
-- 나라들의
-- name과 region을 조회하시오
SELECT name, region
FROM country
WHERE continent = 'Europe';

-- 이름이 'San'으로 시작하는
-- 도시의
-- name을 조회하시오
SELECT name
FROM city
WHERE name LIKE 'San%'

-- 독립 연도(IndepYear)가 1900년 이후인 
-- 나라의
-- name, indepyear를 조회하시오
SELECT name, indepyear
FROM country
WHERE IndepYear <= 1900;

-- 인구가 100만에서 200만 사이인
-- 한국 도시의
-- name을 조회하시오
SELECT name
FROM city
WHERE countrycode = 'KOR'
    AND population BETWEEN 1000000 AND 2000000;

-- 인구가 500만 이상인 
-- 한국, 일본, 중국의 도시의
-- name, countrycode, population 을 조회하시오
SELECT name, countrycode, population
FROM city
WHERE countrycode IN ('KOR', 'JPN', 'CHN')
    AND population >= 5000000;

-- 도시 이름이 'A'로 시작하고 'a'로 끝나는 도시의
-- name을 조회하시오
SELECT name
FROM city
WHERE name LIKE 'A%'
    AND name LIKE '%a';

-- 동남아시아(Southeast Asia) 지역(Region)에 속하지 않는 
-- 아시아(Asia) 대륙 나라들의
-- name, region을 조회하시오
SELECT name, region
FROM country
WHERE continent = 'Asia'
    AND region != 'Southeast Asia';

-- 오세아니아 대륙에서 
-- 예상 수명의 데이터가 없는 나라의
-- name, lifeexpectancy, continent를 조회하시오
SELECT name, lifeexpectancy, continent
FROM country
WHERE continent = 'Oceania'
    AND lifeexpectancy IS NULL;



# ORDER BY(정렬) 실습

-- country 테이블에서
-- 대륙별로 정렬하고,
-- 같은 대륙 내에서는 GNP가 높은 순으로 정렬하여
-- name, continent, GNP을 조회하시오
SELECT name, continent, gnp
FROM country
ORDER BY continent, gnp DESC; 

-- country 테이블에서
-- 기대수명이 높은 순으로 정렬하되,
-- NULL값은 마지막에 나오도록 정렬하여
-- name, lifeexpectancy을 조회하시오
SELECT name, lifeexpectancy
FROM country
ORDER BY LifeExpectancy DESC NULLS LAST;



# LIMIT, OFFSET(개수 제한) 실습

-- city 테이블에서
-- 인구수가 가장 적은 도시 5개를 조회하시오
SELECT name, population
FROM city
ORDER BY population ASC
LIMIT 5;

-- country 테이블에서
-- 면적(SurfaceArea)이 가장 넓은 순서대로 
-- 11위부터 20위까지의 국가를 조회하시오
SELECT name, surfacearea
FROM country
ORDER BY surfacearea DESC
LIMIT 10 OFFSET 10;

-- country 테이블에서
-- 기대수명이 높은 순서대로
-- 1위부터 5위까지의 국가를 조회하시오
SELECT name, lifeexpectancy
FROM country
ORDER BY lifeexpectancy DESC NULLS LAST
LIMIT 5;



# GROUP BY(그룹화, 집계 함수) 실습

-- 대륙별 총 인구수를 구하시오.
SELECT
    continent,
    SUM(population) AS total_population
FROM country
GROUP BY continent;

-- 대륙별 평균 GNP와
-- 평균 인구를 구하시오.
SELECT
    continent,
    AVG(gnp) AS avg_gnp,
    AVG(population) AS avg_population
FROM country
GROUP BY continent;

-- 인구가 50만에서 100만 사이인
-- 도시들에 대해,
-- District별 도시 수를 구하시오.
SELECT
    District,
    COUNT(*) AS city_count
FROM city
WHERE population BETWEEN 500000 AND 1000000
GROUP BY District;

-- 아시아 대륙
-- 국가들의
-- Region별
-- 총 GNP를 구하세요.
SELECT
    region,
    SUM(gnp) AS total_gnp
FROM country
WHERE Continent = 'Asia'
GROUP BY region;

-- 대륙 별
-- 국가 수가 많은 순서대로
-- Continent, 국가 수를 조회하시오.
SELECT
    Continent,
    COUNT(*) AS country_count
FROM country
GROUP BY continent
ORDER BY country_count DESC;

-- 독립년도가 있는 
-- 국가들의 
-- 대륙 별 평균 기대수명이 높은 순서대로 
-- Continent, 평균 기대수명을 조회하시오.
SELECT
    continent,
    AVG(lifeexpectancy) AS avg_lifeexpectancy
FROM country
WHERE indepyear IS NOT NULL
GROUP BY continent
ORDER BY avg_lifeexpectancy DESC;

-- GNP가 가장 높은 Region를 찾으시오.(GNP : 국민 총 생산)
SELECT 
    region,
    SUM(gnp) AS sum_gnp
FROM country
GROUP BY region
ORDER BY sum_gnp DESC
LIMIT 1;



# HAVING (그룹화 결과 필터링) 실습

-- 각 국가별
-- 도시가 10개 이상인 국가의 
-- CountryCode, 도시 수를 조회하시오.
SELECT
    CountryCode,
    COUNT(*) AS city_count
FROM city
GROUP BY CountryCode
HAVING COUNT(*) >= 10;

-- District별
-- 평균 인구가 100만 이상이면서
-- 도시 수가 3개 이상인
-- District,  도시 수, 총 인구를 구하시오
SELECT
    district,
    COUNT(*) AS city_count,
    SUM(population) AS total_population
FROM city
GROUP BY district
HAVING AVG(population) >= 1000000
   AND COUNT(*) >= 3;

-- 아시아 대륙의
-- 국가들 중에서,
-- Region별 평균 GNP가 1000 이상인
-- Region,  평균 GNP를 조회하시오
SELECT
    region,
    AVG(gnp) AS avg_gnp
FROM country
WHERE continent = 'Asia'
GROUP BY region
HAVING AVG(gnp) >= 1000;

-- 독립년도가 1900년 이후인
-- 국가들 중에서,
-- 대륙별 평균 기대수명이 70세 이상인
-- Continent, 평균 기대수명을 조회하시오.
SELECT
    continent,
    AVG(lifeexpectancy) AS avg_lifeexpectancy
FROM country
WHERE indepyear >= 1900
GROUP BY continent
HAVING AVG(lifeexpectancy) >= 70;

-- 도시 평균 인구가 100만 이상이고, 
-- 도시 최소 인구가 50만 이상인 
-- 국가의
-- countrycode, 총 도시수, 총 인구수를 조회하시오.
SELECT
    countrycode,
    COUNT(*) AS city_count,
    SUM(population) AS total_population
FROM city
GROUP BY countrycode
HAVING AVG(population) >= 1000000
   AND MIN(population) >= 500000;

-- 인구가 50만 이상인 city들의
-- 평균 인구가 100만 이상 인
-- 국가의
-- CountryCode, 총 도시수, 총 인구수를 조회하시오.
SELECT
    countrycode,
    COUNT(*) AS city_count,
    SUM(population) AS total_population
FROM city
WHERE population >= 500000
GROUP BY countrycode
HAVING AVG(population) >= 1000000;

