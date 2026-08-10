# 프로젝트 개요
[main 화면]
- 코드 에디터의 Terminal을 사용하여 플레이 할 수 있는 쉬운 퀴즈 게임.
- 개발 환경은 파이썬 3.12.13
- 사용 ide는 Visual Studio Code
- 개발 요구사항에 맞춰서 외부 라이브러리를 사용하지 않고 기본 라이브러리만을 사용하였음.

# 퀴즈 주제와 선정 이유
- 누구나 가볍게 접근 가능하도록 한국의 넌센스 퀴즈를 주제로 선정.

# 실행 방법
[사진]
- VSC에서 main.py 파일을 선택 후 실행 버튼을 클릭.
[사진]
- 또는 터미널에서 해당 프로젝트 폴더로 이동한 뒤, `python3 main.py` 명령어를 입력하여 실행.

# 기능 목록
1. **퀴즈 풀기**: 저장된 퀴즈 중 원하는 문제 수만큼 랜덤으로 출제되며 정답을 맞히면 점수를 획득합. (힌트 사용 시 점수 차감)
2. **퀴즈 추가**: 사용자가 직접 문제, 보기, 정답, 힌트를 입력해 새로운 퀴즈를 등록.
3. **퀴즈 목록**: 현재 등록되어 있는 모든 퀴즈의 문제 목록을 확인합니다.
4. **최고 점수 확인**: 역대 최고 점수와 최근 플레이한 퀴즈 기록(날짜, 문제 수, 점수)을 확인.
5. **퀴즈 삭제**: 목록에 있는 퀴즈 중 불필요한 퀴즈를 선택해 삭제.
6. **종료**: 현재까지의 모든 데이터를 파일에 안전하게 저장하고 게임을 종료.


# 파일 구조
- `quiz_model.py`: 데이터 구조(Quiz 클래스)와 데이터 관리 및 파일 입출력 로직(QuizManager 클래스)을 담당.
- `quiz_view.py`: 사용자에게 보여지는 텍스트 UI 화면 출력과 입력을 담당.
- `quiz_controller.py`: 사용자의 입력을 받아 Model과 View를 연결하고 게임의 전체적인 규칙과 흐름을 통제.
- `main.py`: 프로그램의 진입점(Entry Point)으로, 앱을 실행하고 비정상 종료(Ctrl+C)를 방어.


# 데이터 파일 설명(state.json)
- **경로**: 프로젝트 루트 경로 (`./state.json`)
- **역할**: 프로그램이 종료되어도 퀴즈 목록과 최고 점수, 플레이 기록이 날아가지 않도록 보존.
## 스키마 (구조)
- `quizzes`: 문제(`question`), 선택지 리스트(`choices`), 정답 번호(`answer`), 힌트(`hint`)가 딕셔너리 리스트 형태로 저장.
- `best_score`: 역대 최고 점수가 정수형(int)으로 저장.
- `history`: 플레이 기록이 딕셔너리 리스트 형태(`date`, `played_count`, `score`)로 저장.

---

# Git 명령어 사용 기록

- add, commit, push, checkout(switch)
```
ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ % git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md
        Screenshot/

nothing added to commit but untracked files present (use "git add" to track)


ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ % git add .


ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ % git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   README.md
        new file:   Screenshot/main.png
        new file:   Screenshot/start with command.png
        new file:   Screenshot/start.png


ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ % git commit -m "README.md 파
일 초안 생성"
[main f764b7c] README.md 파일 초안 생성
 4 files changed, 69 insertions(+)
 create mode 100644 README.md
 create mode 100644 Screenshot/main.png
 create mode 100644 Screenshot/start with command.png
 create mode 100644 Screenshot/start.png


ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ % git push origin
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 6 threads
Compressing objects: 100% (7/7), done.
Writing objects: 100% (7/7), 169.06 KiB | 28.18 MiB/s, done.
Total 7 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/HOT8OY/Codyssey-E1-2
   a3e7717..f764b7c  main -> main
```

- switch(checkout), pull(fetch + merge)
```
ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ % git branch -a
  04_quiz-logic-completions
* main
  remotes/origin/01_first-initialize
  remotes/origin/02_quiz-model
  remotes/origin/03_quiz-controller
  remotes/origin/04_quiz-logic-completions
  remotes/origin/HEAD -> origin/main
  remotes/origin/main


ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ % git switch 04_quiz-logic-co
mpletions
Switched to branch '04_quiz-logic-completions'
Your branch is up to date with 'origin/04_quiz-logic-completions'.


ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ % git pull origin main
From https://github.com/HOT8OY/Codyssey-E1-2
 * branch            main       -> FETCH_HEAD
Updating d277305..f764b7c
Fast-forward
 Codyssey-E1-2.code-workspace      |   7 ---
 README.md                         |  69 +++++++++++++++++++++++++
 Screenshot/main.png               | Bin 0 -> 36270 bytes
 Screenshot/start with command.png | Bin 0 -> 30375 bytes
 Screenshot/start.png              | Bin 0 -> 121518 bytes
 main.py                           |  12 -----
 6 files changed, 69 insertions(+), 19 deletions(-)
 delete mode 100644 Codyssey-E1-2.code-workspace
 create mode 100644 README.md
 create mode 100644 Screenshot/main.png
 create mode 100644 Screenshot/start with command.png
 create mode 100644 Screenshot/start.png


ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ % git switch main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
```

- commit 기록
```
ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ % git log --oneline --all
a3e7717 (HEAD -> main, origin/main, origin/HEAD) Refactoring 사용하지 않는 코드 삭제
d277305 (origin/04_quiz-logic-completions, 04_quiz-logic-completions) .gitignore 업데이트 및 기존 파일 추적 해제
ca6053d Feat: 게임 기록(몇 문제 풀었는지, 언제 풀었는지) 저장 형식 변경
00c9ade Feat: 강제 종료 예외 처리
e069163 Feat: 퀴즈 삭제 기능 구현
245f065 Feat: 점수 확인 및 저장 기능 구현
aba2126 Feat: 퀴즈 풀기 기능 구현
ccc80af Feat: 퀴즈 추가 기능 구현
33dc685 Feat: 퀴즈보기 구현
c3a8870 (origin/03_quiz-controller) Feat: 기본 뼈대 완성 + .gitignore 업데이트
bfd69f9 Feat: 메인 view 구성
321d6a7 (origin/02_quiz-model) Feat: 기본 퀴즈 추가 및 퀴즈 로드,세이브 로직 구현
d1c94c8 Feat: quiz_mode에 리스트 변환, json 저장 기능 구현
87d9fb7 -: save
22e971b (origin/01_first-initialize) Feat: main.py 구성 완료
3765a74 Feat: 초기 구조 생성
```