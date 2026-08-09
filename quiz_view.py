class QuizView:
    # 메뉴 출력
    def show_menu(self):
        # Header
        print("\n\n")
        print("="*40)
        print("   🐟 동물도 맞출 수 있는 EASY 퀴즈 🐔")
        print("="*40 + "\n")
        # 메뉴
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 최고 점수 확인")
        print("5. 퀴즈 삭제")
        print("6. 종료\n")
        # 선택
        choice = input("선택: ").strip()
        return choice
    
    # 퀴즈 목록 출력
    def show_quizzes(self, quizzes):
        print("\n📋 등록된 퀴즈 목록")
        print("-" * 40)
        for i, quiz in enumerate(quizzes, start=1):
            print(f"[{i}] {quiz.question}")
        print("-" * 40)

    # 퀴즈 추가
    def get_new_quiz(self):
        print("\n📥 새로운 퀴즈를 추가합니다.")
        question = input("문제를 입력하세요: ").strip()

        c1 = input("선택지 1: ").strip()
        c2 = input("선택지 2: ").strip()
        c3 = input("선택지 3: ").strip()
        c4 = input("선택지 4: ").strip()
        choices = [c1, c2, c3, c4]

        answer = int(input("정답 번호 (1~4): ").strip())
        hint = input("힌트 (없으면 엔터): ").strip()

        # 4개의 데이터를 한번에 반환
        return question, choices, answer, hint