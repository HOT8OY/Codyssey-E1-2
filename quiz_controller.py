from quiz_model import QuizManager
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
                print("\n기능개발중")
            elif choice == "3":
                print("\n기능개발중")
            elif choice == "4":
                print("\n기능개발중")
            elif choice == "5":
                print("\n기능개발중")
            elif choice == "6":
                print("데이터를 저장하고 종료합니다.")
                self.manager.save_data()
                break 
            else: print("🐷 잘못된 입력입니다.\n🐶 1~6 까지의 숫자를 입력하세요.")