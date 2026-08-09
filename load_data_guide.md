# 📚 load_data() 구현을 위한 파이썬 핵심 개념 가이드

`QuizManager`의 `load_data()` 메서드를 완성하기 위해 필요한 개념들을 정리했습니다. `save_data()`의 반대 과정이라고 생각하시면 쉽습니다!

---

## 1. 파일 불러오기 (`json.load`)

### 💡 개념
JSON 형식으로 저장된 텍스트 파일을 읽어서 파이썬의 **딕셔너리(`dict`)** 형태로 변환합니다.

### 📝 문법
```python
with open(self.filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)
```
* **`'r'` (Read 모드)**: 파일을 읽기 전용으로 엽니다.

---

## 2. 딕셔너리를 다시 `Quiz` 객체로 변환 (복원)

### 💡 개념
`save_data()`에서는 `Quiz` 객체를 딕셔너리로 변환해 저장했습니다. 반대로 불러올 때는 **딕셔너리의 데이터를 꺼내어 다시 `Quiz` 클래스의 인스턴스(객체)로 만들어야** 합니다.

### 📝 딕셔너리의 `.get()` 메서드 활용
과거 버전의 게임에는 `hint` 데이터가 없었을 수도 있습니다. 안전하게 가져오기 위해 `.get()`을 사용합니다.
```python
# data["quizzes"] 에는 딕셔너리들이 들어있습니다.
for q_dict in data["quizzes"]:
    question = q_dict["question"]
    choices = q_dict["choices"]
    answer = q_dict["answer"]
    
    # "hint" 키가 없으면 빈 문자열("")을 기본값으로 가져옵니다.
    hint = q_dict.get("hint", "") 
    
    # 읽어온 데이터로 Quiz 객체를 생성하여 리스트에 추가합니다.
    quiz_obj = Quiz(question, choices, answer, hint)
    self.quizzes.append(quiz_obj)
```

---

## 3. 다양한 예외(에러) 분기 처리

요구사항 중 가장 중요한 부분입니다. **"파일이 없거나 손상되었을 때 기본 퀴즈 데이터로 복구/초기화한다"**
에러의 종류에 따라 `except`를 여러 개 나눌 수 있습니다.

### 💡 처리해야 할 주요 에러
1. **`FileNotFoundError`**: 프로그램을 처음 실행해서 아직 `state.json` 파일이 없을 때 발생합니다.
2. **`json.JSONDecodeError`**: 파일은 있는데 안에 내용이 망가져서(JSON 문법 오류) 읽을 수 없을 때 발생합니다.
3. **`Exception`**: 기타 알 수 없는 에러 방어.

### 📝 구조 예시
```python
try:
    with open(self.filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        # TODO: data에서 퀴즈, 최고점수, 히스토리 복원하는 로직
        
except FileNotFoundError:
    print("저장된 데이터 파일이 없습니다. 기본 퀴즈를 로드합니다.")
    self.set_default_quizzes() # 별도로 만들 기본 퀴즈 세팅 메서드
    
except json.JSONDecodeError:
    print("데이터 파일이 손상되었습니다. 기본 퀴즈로 초기화합니다.")
    self.set_default_quizzes()
    
except Exception as e:
    print(f"데이터를 불러오는 중 오류가 발생했습니다: {e}")
    self.set_default_quizzes()
```
