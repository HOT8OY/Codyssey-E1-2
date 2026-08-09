from quiz_model import QuizManager, Quiz
from quiz_view import QuizView

class QuizController:
    def __init__(self):
        self.manager = QuizManager()
        self.view = QuizView()
        # 데이터 로드
        self.manager.load_data()

    def run(self):
        while True:
            choice = self.view.show_menu()
            if choice == "1":
                print("\n기능개발중")

            elif choice == "2":
                # question, choices, answer, hint
                q, c, a, h = self.view.get_new_quiz()
                # 새로운 퀴즈 객체를 만들어 모델에 추가
                new_quiz = Quiz(q,c,a,h)
                self.manager.quizzes.append(new_quiz)
                print("\n❤️ 퀴즈가 성공적으로 추가되었습니다!")
                print(f"추가된 퀴즈 : {q}")

            elif choice == "3":
                self.view.show_quizzes(self.manager.quizzes)

            elif choice == "4":
                print("\n기능개발중")

            elif choice == "5":
                print("\n기능개발중")

            elif choice == "6":
                print("데이터를 저장하고 종료합니다.")
                self.manager.save_data()
                break 
            
            else: print("🐷 잘못된 입력입니다.\n🐶 1~6 까지의 숫자를 입력하세요.")