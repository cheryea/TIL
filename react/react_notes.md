## onClick과 매개변수 전달

### 문제 상황
```javascript
onClick={todoStatus.removeTodo(todo.id)}
```
위 코드는 클릭할 때 실행되는 것이 아니라 **컴포넌트가 렌더링될 때 바로 실행된다.**

### 이유
React의 `onClick`은 **실행할 “함수 자체”를 전달받는다.**
```javascript
onClick={함수}
```

하지만 아래 코드는
```javascript
handleClick(id)
```

**함수 참조가 아니라 함수 호출**이다.
자바스크립트에서 `()`를 붙이면 **즉시 실행**되기 때문에 렌더링 과정에서 바로 실행된다.


### 올바른 방법

매개변수를 전달하려면 **함수를 새로 만들어 전달한다.**

```javascript
onClick={() => todoStatus.removeTodo(todo.id)}
```

이렇게 하면 클릭했을 때 해당 함수가 실행된다.

### 참고

매개변수가 없는 경우에는 **이미 함수 자체이기 때문에 그대로 전달하면 된다.**

```javascript
onClick={handleClick}
```



---



## 객체 key 활용 (Computed Property)
### 코드
```javascript
setForm({ ...form, [e.target.name]: e.target.value });
```
#### 해석
React에서 form 상태 객체를 복사한 후, 입력된 input의 name에 해당하는 값을 업데이트하는 코드이다.
```javascript
[e.target.name]
```
[]를 사용하면 변수 값을 객체 key로 사용할 수 있다.

### 일반적인 객체 key
```javascript
const user = {
  name: "철수"
};
```
여기서 `name`은 **고정된 key**이다.

### 변수 값을 key로 사용할 때
```javascript
const key = "name";

const user = {
  [key]: "철수"
};
```

#### 결과

```javascript
{ name: "철수" }
```

`[key]`는 **변수 값을 key로 변환**한다.

---

### React에서 사용하는 이유
React의 form에서는 input마다 `name`이 다르기 때문에
어떤 값을 수정할지 **동적으로 결정해야 한다.**
```javascript
setForm({
  ...form,
  [e.target.name]: e.target.value
});
```

#### 예

```html
<input name="email" />
<input name="name" />
```

입력된 input의 `name`에 따라 **업데이트할 key가 자동으로 바뀐다.**

* `name:` → 고정된 key
* `[name]:` → 변수 값을 key로 사용

