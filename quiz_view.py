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

    # 퀴즈 풀기
    def play_quiz(self, quiz):
        print("\n" + "="*40)
        print(f"❓❓ [문제] {quiz.question}")
        print("-"*40)
        # 보기 출력
        for i, choice in enumerate(quiz.choices, start=1):
            print(f"{i}. {choice}")
        print("-"*40)
        user_input = input("정답을 입력하세요 (힌트를 보려면 'h' 입력) : ").strip().lower()

        return user_input
    
    # 퀴즈 목록 출력
    def show_quizzes(self, quizzes):
        print("\n📋 등록된 퀴즈 목록")
        print("-" * 40)
        for i, quiz in enumerate(quizzes, start=1):
            print(f"[{i}] {quiz.question}")
        print("-" * 40)
        input("계속하려면 엔터를 누르세요.")

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

    # 최고 점수 확인
    def show_best_score(self, best_score, history):
        print("\n\n\n" + "="*40)
        print(f"\n 🏆 현재 최고 점수: {best_score}점 🏆")
        print("\n" + "="*40)
        print("\n 📊 최근 플레이 기록:")

        if not history:
            print("  아직 플레이 기록이 없습니다.")
        else:
            # 리스트에 있는 점수들을 하나씩 꺼내서 보여줌
            for i, s in enumerate(history, start = 1):
                print(f"   {i}회차: {s}점")

        print("-" * 40)
        input("계속하려면 엔터를 누르세요.")