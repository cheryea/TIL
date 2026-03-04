// ===============================================================
// 배열 고차 메서드 실습
// ===============================================================


// 1번. 변수 animals에 저장된 각 동물 이름을 한 줄씩 출력한다.
const animals = ["자", "축", "인", "묘", "진", "사", "오", "미", "신", "유", "술", "해"];
console.log("1번 문제");
animals.forEach(animal => console.log(animal))

console.log("-----------------");

// 2번. 변수 fruits에 저장된 각 과일 이름을 "맛있는 [과일명]" 형식으로 변환하여 새로운 배열을 만들고 출력한다.
const fruits = ["사과", "바나나", "오렌지"];
console.log("2번 문제");
let result = fruits.map(fruit => "맛있는 "+ fruit)
console.log(result);

console.log("-----------------");

// 3번. 변수 numbers에 저장된 각 숫자와 인덱스를 "인덱스: 숫자" 형식으로 한 줄씩 출력한다.
const numbers1 = [10, 20, 30, 40];
console.log("3번 문제");
numbers1.forEach((num,idx) => console.log(`${idx}:${num}`))

console.log("-----------------");

// 4번. 변수 numbers에 저장된 각 숫자를 제곱한 데이터를 모아서 새로운 배열을 만들고 출력한다.
const numbers2 = [1, 2, 3, 4, 5];
console.log("4번 문제");
result = numbers2.map(num => num ** 2)
console.log(result);

console.log("-----------------");

// 5번. 변수 numbers에 저장된 1부터 10까지의 숫자 중 짝수만 필터링한 새로운 배열을 만들고 출력한다.
const numbers3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.log("5번 문제");
result = numbers3.filter(num => num % 2 === 0)
console.log(result);

console.log("-----------------");

// 6번. 변수 people 배열에서 나이(age)가 20세 이상인 사람만 필터링하여 새로운 객체 배열을 만들고 출력한다.
const people = [
  { name: "김철수", age: 25 },
  { name: "이영희", age: 30 },
  { name: "박민수", age: 18 },
];
console.log("6번 문제");
result = people.filter(person => person.age >= 20)
console.log(result);

console.log("-----------------");

// 7번. 변수 numbers에 저장된 [1, 2, 3, 4, 5] 각 숫자의 합계를 계산하여 출력한다.
const numbers4 = [1, 2, 3, 4, 5];
console.log("7번 문제");
let sum = numbers4.reduce((acc, cur) => acc + cur, 0)
console.log(sum)

console.log("-----------------");

// 8번. 변수 users 배열에서 id가 2인 객체 하나만 찾아 출력한다.
const users = [
  { id: 1, name: "김철수" },
  { id: 2, name: "이영희" },
  { id: 3, name: "박민수" },
];
console.log("8번 문제");
result = users.find(user => user.id === 2)
console.log(result);

console.log("-----------------");

// 9번. products 배열에서 '전자제품' 카테고리만 필터링한 후, 그 결과물에서 다시 "상품명: 가격원" 형태의 문자열 배열을 만들어 출력한다.
const products = [
  { name: "노트북", price: 1200000, category: "전자제품" },
  { name: "마우스", price: 25000, category: "전자제품" },
  { name: "책상", price: 150000, category: "가구" },
  { name: "키보드", price: 80000, category: "전자제품" },
  { name: "의자", price: 200000, category: "가구" },
];
console.log("9번 문제");
result = products
  .filter((product) => product.category === "전자제품")
  .map((product) => `${product.name}:${product.price}`)
console.log(result);

console.log("-----------------");

// 10번. students 배열에서 점수가 70점 이상인 학생을 뽑아 "이름(등급)" 형태의 문자열 배열로 변환하여 출력한다.
const students = [
  { name: "김철수", score: 85, grade: "A" },
  { name: "이영희", score: 92, grade: "A" },
  { name: "박민수", score: 78, grade: "B" },
  { name: "최지영", score: 88, grade: "A" },
  { name: "정수현", score: 65, grade: "C" },
];
console.log("10번 문제");
result = students
  .filter((student) => student.score >= 70)
  .map((student) => `${student.name}(${student.grade})`)
console.log(result);

console.log("-----------------");

// 11번. 장바구니 배열에서 각 품목의 결제 금액(수량 * 가격)을 모두 더한 총액을 계산하여 출력한다.
const cart = [
  { name: "사과", quantity: 2, price: 1000 },
  { name: "바나나", quantity: 3, price: 1500 },
  { name: "포도", quantity: 1, price: 5000 },
];
console.log("11번 문제");
result = cart.reduce((acc, product) => acc + product.quantity * product.price,0)

console.log(result);


console.log("-----------------");

// 12번. 게시글 목록(posts)에서 '공지'인 글만 필터링한 뒤, 제목(title)만 추출하여 가나다순으로 정렬한 배열을 출력한다.
const posts = [
  { id: 1, title: "공지: 정기 점검 안내", isNotice: true },
  { id: 2, title: "오늘 점심 뭐 먹지?", isNotice: false },
  { id: 3, title: "공지: 이용 약관 변경", isNotice: true },
  { id: 4, title: "리액트 공부 너무 재밌어요", isNotice: false },
  { id: 5, title: "공지: 이벤트 당첨자 발표", isNotice: true },
];
console.log("12번 문제");

result = posts
  .filter((post) => post.isNotice)
  .map((post) => post.title)
  .sort((a, b) => a.localeCompare(b, 'ko'))

console.log(result);

console.log("-----------------");
