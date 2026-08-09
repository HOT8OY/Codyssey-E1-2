from quiz_model import Quiz
from quiz_view import QuizView
from quiz_controller import QuizController

def main():

    model = QuizModel()

    view = QuizView()

    controller = QuizController(model, view)

    controller.run()

if __name__ == "__main__":
    app = QuizController()
    app.run()