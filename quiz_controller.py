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
                self.manager.history.append(score) # 플레이 기록에 추가
                # 최고 점수 갱신 확인
                if score > self.manager.best_score:
                    print("\n🏆 축하합니다! 최고 점수를 갱신했습니다!")
                    self.manager.best_score = score
                input("메뉴로 돌아가려면 엔터를 누르세요.")


            elif choice == "2":
                # question, choices, answer, hint
                q, c, a, h = self.view.get_new_quiz()
                # 새로운 퀴즈 객체를 만들어 모델에 추가
                new_quiz = Quiz(q,c,a,h)
                self.manager.quizzes.append(new_quiz)
                print("\n❤️ 퀴즈가 성공적으로 추가되었습니다!")
                print(f"추가된 퀴즈 : {q}")
                input("메뉴로 돌아가려면 엔터를 누르세요.")

            elif choice == "3":
                self.view.show_quizzes(self.manager.quizzes)

            elif choice == "4":
                # 매니저(Model)이 가진 최고 점수와 기록 데이터를 View에게 넘겨줌
                self.view.show_best_score(self.manager.best_score, self.manager.history)

            elif choice == "5":
                if not self.manager.quizzes:
                    print("\n⚠️ 등록된 퀴즈가 없습니다.")
                    input("메뉴로 돌아가려면 엔터를 누르세요.")
                    continue # 등록된 퀴즈가 없으면 메뉴로
                
                #get_quiz_index_to_delete로 삭제할 퀴즈의 index를 받아옴
                target_str = self.view.get_quiz_index_to_delete(self.manager.quizzes)

                if target_str == "0":
                    print("\n 🤚🏻 삭제를 취소합니다.")
                elif target_str.isdigit():
                    target_idx = int(target_str)
                    # 입력한 번호가 1번부터 전체 퀴즈 개수 사이에 있는지 확인
                    if 1 <= target_idx <= len(self.manager.quizzes):
                        # 파이썬 리스트의 시작점은 0이므로 -1
                        delete_quiz = self.manager.quizzes.pop(target_idx - 1)
                        print(f"\n✅ '{delete_quiz.question}' 퀴즈가 삭제되었습니다.")
                        input("메뉴로 돌아가려면 엔터를 누르세요.")
                    else:
                        print("\n⚠️ 목록에 없는 번호입니다.")
                        input("메뉴로 돌아가려면 엔터를 누르세요.")
                else:
                    print("\n⚠️ 숫자를 입력해주세요.")
                    input("메뉴로 돌아가려면 엔터를 누르세요.")

            elif choice == "6":
                print("데이터를 저장하고 종료합니다.")
                self.manager.save_data()
                break 
            
            else: print("🐷 잘못된 입력입니다.\n🐶 1~6 까지의 숫자를 입력하세요.")