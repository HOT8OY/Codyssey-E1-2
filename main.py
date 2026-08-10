from quiz_controller import QuizController

if __name__ == "__main__":
    app = QuizController()

    try:
        app.run()
    except KeyboardInterrupt:
        # 사용자가 도중에 Ctrl+C (강제 종료)를 눌렀을 때 이곳이 실행
        print("\n\n⚠️ 강제 종료가 감지되었습니다.")
        print("데이터를 안전하게 저장하고 프로그램을 종료합니다.")
        app.manager.save_data() # 종료되기 직전에 저장