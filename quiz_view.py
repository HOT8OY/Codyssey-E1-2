class QuizView:
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

    def show_quizzes(self, quizzes):
        print("\n📋 등록된 퀴즈 목록")
        print("-" * 40)
        for i, quiz in enumerate(quizzes, start=1):
            print(f"[{i}] {quiz.question}")
        print("-" * 40)