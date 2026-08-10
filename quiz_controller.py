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
                print("\n\n\n\n 💎 퀴즈 게임을 시작합니다!")
                score = 0
                for quiz in self.manager.quizzes:
                    while True:
                        ans = self.view.play_quiz(quiz)

                        if ans == 'h':
                            # 힌트가 있다면
                            if quiz.hint:
                                print(f"\n💡 힌트: {quiz.hint}")
                                score -= 10
                                print("    (점수가 10점 차감되었습니다.)")
                            else :
                                print(f"💡 이 퀴즈에는 힌트가 없습니다.")
                        elif ans.isdigit():
                            answer_num = int(ans)
                            if answer_num == quiz.answer:
                                print("\n ✅ 정답입니다! (+20점)")
                                score += 20
                                print(f"  현재 점수 {score}점")
                            else:
                                print(f"\n\n ❌ 틀렸습니다. 정답은 {quiz.answer}번 이엇습니다.")
                            break # 문제 풀었으면 다음 문제로
                        else:
                            print("⚠️ 숫자 1~4 또는 'h'를 입력하세요.")
                print(f"\n 🎉 퀴즈 종료! 당신의 최종 점수는 {score}점 입니다.")
                input("메뉴로 돌아가려면 엔터를 누르세요.")


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
                print("\n최고 점수 확인 기능개발중")
                input("계속하려면 엔터를 누르세요.")

            elif choice == "5":
                print("\n퀴즈 삭제 기능개발중")
                input("계속하려면 엔터를 누르세요.")

            elif choice == "6":
                print("데이터를 저장하고 종료합니다.")
                self.manager.save_data()
                break 
            
            else: print("🐷 잘못된 입력입니다.\n🐶 1~6 까지의 숫자를 입력하세요.")