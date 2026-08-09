# 📚 save_data() 구현을 위한 파이썬 핵심 개념 가이드

`QuizManager`의 `save_data()` 메서드를 완성하기 위해 필요한 **4가지 핵심 파이썬 개념과 사용법**을 정리한 문서입니다.

---

## 1. 리스트 내포 (List Comprehension) 및 데이터 변환 과정

### 💡 개념
기존 리스트의 요소들을 바탕으로 **새로운 리스트를 간결하게 생성하는 파이썬 고유의 직관적인 문법**입니다.

### ❓ 데이터가 어떻게 변환되어 리스트에 들어갈까요? (상세 구조 예시)

`self.quizzes` 안에는 `Quiz` 객체들이 들어 있습니다. 메모리상에서 데이터의 모습과 변환 과정을 단계별로 살펴봅시다.

#### 1단계: 변환 전 `self.quizzes` 상태
`self.quizzes`는 `Quiz` 클래스의 인스턴스(객체)들이 모인 리스트입니다.
```python
# self.quizzes 메모리 모습 (객체 들의 리스트)
[
    <Quiz 객체 1: question="파이썬의 창시자는?", choices=["Guido", "Linus", ...], answer=1, hint="G... ">
    <Quiz 객체 2: question="HTML은 언어인가?", choices=["예", "아니오"], answer=2, hint="마크업...">
]
```
> ⚠️ **이 상태로는 `json.dump()`로 바로 저장할 수 없습니다.** (파이썬 클래스 객체는 JSON 포맷으로 직렬화할 수 없기 때문입니다.)

#### 2단계: `to_dict()`가 하는 일
개별 `Quiz` 객체 `q`에서 `q.to_dict()`를 호출하면 아래처럼 **파이썬 딕셔너리(`dict`)**가 반환됩니다.
```python
{
    "question": "파이썬의 창시자는?",
    "choices": ["Guido", "Linus", "Bjarne", "James"],
    "answer": 1,
    "hint": "G로 시작합니다"
}
```

#### 3단계: 리스트 내포 `[q.to_dict() for q in self.quizzes]` 동작 과정
1. `self.quizzes`에서 1번째 `Quiz` 객체를 꺼냄 ➡️ `to_dict()` 실행 ➡️ 1번째 딕셔너리 완성
2. `self.quizzes`에서 2번째 `Quiz` 객체를 꺼냄 ➡️ `to_dict()` 실행 ➡️ 2번째 딕셔너리 완성
3. 이것들을 모아서 **새로운 딕셔너리 리스트**를 만듭니다!

```python
# 변환 후 결과 (JSON 저장 가능한 딕셔너리 리스트)
[
    {
        "question": "파이썬의 창시자는?",
        "choices": ["Guido", "Linus", "Bjarne", "James"],
        "answer": 1,
        "hint": "G로 시작합니다"
    },
    {
        "question": "HTML은 프로그래밍 언어인가?",
        "choices": ["예", "아니오"],
        "answer": 2,
        "hint": "마크업 언어입니다"
    }
]
```

### 📝 코드 비교
* **기존 for문 방식:**
  ```python
  quiz_dicts = []
  for q in self.quizzes:
      # Quiz 객체 q를 딕셔너리로 바꿔서 quiz_dicts 리스트에 하나씩 추가(append)
      quiz_dicts.append(q.to_dict())
  ```
* **리스트 내포 방식 (추천):**
  ```python
  quiz_dicts = [q.to_dict() for q in self.quizzes]
  ```

---

## 2. 안전한 파일 입출력 (`with open`)

### 💡 개념
파이썬에서 파일을 다룰 때는 `open()` 함수로 파일을 열고 사용이 끝나면 `close()`로 닫아줘야 합니다. `with` 구문을 사용하면 파일 작업을 마친 후 **자동으로 파일을 닫아주므로 메모리 누수나 데이터 손실을 방지**할 수 있습니다.

### 📝 문법 및 옵션
```python
with open(파일경로, 모드, encoding='utf-8') as f:
    # 파일 작업 수행
```

* **`self.filepath`**: 저장할 파일 경로 (`'state.json'`)
* **`'w'` (Write 모드)**: 파일에 내용을 새로 쓰거나 덮어씁니다.
* **`encoding='utf-8'`**: 한글 깨짐을 방지하기 위해 필수적입니다.
* **`as f`**: 열린 파일 객체를 변수 `f`라는 이름으로 다루겠다는 의미입니다.

---

## 3. JSON 파일 저장 (`json.dump`)

### 💡 개념
파이썬의 딕셔너리/리스트 데이터를 JSON 형식의 파일로 저장할 때 `json.dump()` 함수를 사용합니다.

### 📝 주요 매개변수 (Option)
```python
json.dump(저장할_데이터, 파일_객체, ensure_ascii=False, indent=4)
```

1. **`저장할_데이터`**: 딕셔너리(`dict`) 형태의 전체 데이터 (`quizzes`, `best_score`, `history` 포함)
2. **`파일_객체`**: `with open`에서 지정한 파일 변수 (`f`)
3. **`ensure_ascii=False`**: 기본값 `True`로 두면 한글이 `\u1100...` 과 같은 유니코드 코드로 저장됩니다. `False`로 설정해야 텍스트 그대로 한글이 예쁘게 저장됩니다.
4. **`indent=4`**: JSON 파일의 들여쓰기 간격을 지정합니다. 사람이 읽기 좋은 형태로(Pretty Print) 포맷팅됩니다.

---

## 4. 예외 처리 (`try - except`)

### 💡 개념
디스크 용량 부족, 파일 접근 권한 문제 등 예상치 못한 파일 저장 오류가 발생했을 때 **프로그램이 갑자기 튕기거나 비정상 종료되는 것을 방지**합니다.

### 📝 기본 구조
```python
try:
    # 파일 저장 실행 코드
    ...
    print("성공 메시지")
except Exception as e:
    # 에러 발생 시 처리 코드
    print(f"저장 중 오류가 발생했습니다: {e}")
```

---

## 🛠 종합 적용 예시 요약 (의도 파악용 참고)

위 4가지 개념을 합치면 `save_data()` 메서드의 전체적인 흐름은 다음과 같습니다.

```python
# 1. 저장할 데이터 묶기 (리스트 내포 활용)
data = {
    "quizzes": [q.to_dict() for q in self.quizzes],
    "best_score": self.best_score,
    "history": self.history
}

# 2. try-except 와 with open, json.dump 조합하여 파일 쓰기
try:
    with open(self.filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("📂 데이터가 성공적으로 저장되었습니다.")
except Exception as e:
    print(f"⚠️ 데이터 저장 실패: {e}")
```
