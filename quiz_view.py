class QuizView:
    def show_menu(self):
        # Header
        print("="*40)
        print("\t\t\t 🐟 동물도 맞출 수 있는 EASY 퀴즈 🐔")
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