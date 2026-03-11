## onClick과 매개변수 전달

### 문제 상황

```javascript
onClick={todoStatus.removeTodo(todo.id)}
```

위 코드는 클릭할 때 실행되는 것이 아니라 **컴포넌트가 렌더링될 때 바로 실행된다.**

---

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

---

### 올바른 방법

매개변수를 전달하려면 **함수를 새로 만들어 전달한다.**

```javascript
onClick={() => todoStatus.removeTodo(todo.id)}
```

이렇게 하면 클릭했을 때 해당 함수가 실행된다.

---

### 참고

매개변수가 없는 경우에는 **이미 함수 자체이기 때문에 그대로 전달하면 된다.**

```javascript
onClick={handleClick}
```
