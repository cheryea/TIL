// ===============================================================
// if문 실습
// ===============================================================


// 1번: score가 80 이상이면 "합격입니다" 출력
console.log("1번 문제");

const score = 85;

if (score >= 80) {
  console.log("합격입니다");
}

console.log("-----------------");

// 2번: age가 20 이상이면 "성인입니다", 아니면 "미성년자입니다"
console.log("2번 문제");

const age = 18;
const ageMessage = age >= 20 ? "성인입니다" : "미성년자입니다";

console.log(ageMessage);

console.log("-----------------");

// 3번: number가 양수/음수/0 판별
console.log("3번 문제");

const number = -5;
let numberType;

if (number > 0) {
  numberType = "양수";
} else if (number < 0) {
  numberType = "음수";
} else {
  numberType = "0";
}

console.log(numberType);

console.log("-----------------");

// 4번: gold 또는 platinum이면 VIP 혜택
console.log("4번 문제");

const memberLevel = "gold";
const isVip =
  memberLevel === "gold" || memberLevel === "platinum";

console.log(
  isVip
    ? "VIP 혜택을 받을 수 있습니다"
    : "일반 혜택만 가능합니다"
);

console.log("-----------------");

// 5번: 20 이상이면서 학생이면 "성인 학생", 20 이상이면 "성인", 미만이면 "미성년자"
console.log("5번 문제");

const userAge = 25;
const isStudent = true;

let userCategory;

if (userAge < 20) {
  userCategory = "미성년자입니다";
} else if (isStudent) {
  userCategory = "성인 학생입니다";
} else {
  userCategory = "성인입니다";
}

console.log(userCategory);

console.log("-----------------");

// 6번: 25 미만이면 시원, 25 이상이면서 습도 70 이상이면 더움, 아니면 따뜻
console.log("6번 문제");

const temperature = 28;
const humidity = 10;

let weatherCondition;

if (temperature < 25) {
  weatherCondition = "시원한 날씨입니다";
} else if (humidity >= 70) {
  weatherCondition = "더운 날씨입니다";
} else {
  weatherCondition = "따뜻한 날씨입니다";
}

console.log(weatherCondition);

console.log("-----------------");

// 7번: point가 1000 이상이면 "VIP", 아니면 "일반"
console.log("7번 문제");

const point = 1500;
const membershipGrade = point >= 1000 ? "VIP" : "일반";

console.log(membershipGrade);

console.log("-----------------");

// 8번: 100000 이상이면 10% 할인 적용 후 출력
console.log("8번 문제");

const purchaseAmount = 150000;
const finalPrice =
  purchaseAmount >= 100000
    ? purchaseAmount * 0.9
    : purchaseAmount;

console.log(
  `구매금액: ${purchaseAmount}, 최종금액: ${finalPrice}`
);

console.log("-----------------");

// 9번: 비활성이면 "비활성 계정", 활성일 경우 조건에 따라 등급 출력
console.log("9번 문제");

const userType = "premium";
const userPoints = 2500;
const isActive = true;

let accountGrade;

if (!isActive) {
  accountGrade = "비활성 계정";
} else if (userPoints >= 3000) {
  accountGrade = "VIP";
} else if (userType === "premium") {
  accountGrade = "프리미엄";
} else if (userPoints >= 1000) {
  accountGrade = "일반";
} else {
  accountGrade = "신규";
}

console.log(accountGrade);

console.log("-----------------");

// 10번: 비가 오면 "우산을 챙기세요", 아니면 "날씨가 맑습니다"
console.log("10번 문제");

const isRaining = true;
const weatherMessage =
  isRaining ? "우산을 챙기세요" : "날씨가 맑습니다";

console.log(weatherMessage);

console.log("-----------------");
