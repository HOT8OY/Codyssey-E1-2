import json


class Quiz:
    def __init__(self, question, choices, answer, hint = ""):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # quiz를 리스트 형식의 객체로 만드는 함수
    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint
        }

class QuizManager:
    def __init__(self):
        self.filepath = 'state.json'
        self.quizzes = []
        self.best_score = 0
        self.history = []

    # json 파일에 퀴즈, 스코어, 기록을 추가하는 함수
    def save_data(self):
        data = {
            "quizzes" : [q.to_dict() for q in self.quizzes],
            "best_score" : self.best_score,
            "history" : self.history
        }
        
        try:
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(e)
    
    def set_default_quizzes(self):
        # 1번 문제
        self.quizzes.append(Quiz(
            "세상에서 가장 학벌이 좋은 물고기는?",
            ["오징어", "연어", "고등어", "송어"],
            3,
            "학교 이름과 비슷합니다."
        ))
        # 2번 문제
        self.quizzes.append(Quiz(
            "왕이 넘어지면 뭐가 될까?",
            ["킹카", "킹콩", "왕자", "왕뚜껑"],
            2,
            "왕(King) + '쿵' 하고 넘어지는 소리"
        ))
        # 3번 문제
        self.quizzes.append(Quiz(
            "도둑이 가장 싫어하는 아이스크림은?",
            ["돼지바", "바밤바", "스크류바", "누가바"],
            4,
            "누가 훔쳐가는 걸 볼까 봐..."
        ))
        # 4번 문제
        self.quizzes.append(Quiz(
            "타이타닉의 구명보트에는 몇 명이 탈 수 있을까?",
            ["5명", "9명", "10명", "100명"],
            2,
            "단어 발음에 정답이 있습니다."
        ))
        # 5번 문제
        self.quizzes.append(Quiz(
            "사람들이 가장 싫어하는 거리는?",
            ["먹거리", "볼거리", "걱정거리", "웃음거리"],
            3,
            "마음이 무거워지는 거리입니다."
        ))

    def load_data(self):
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                data =json.load(f)
                # data에서 퀴즈, 최고점수, 히스토리를 복원
                for q_dict in data["quizzes"]:
                    question = q_dict["question"]
                    choices = q_dict["choices"]
                    answer = q_dict["answer"]
                    hint = q_dict.get("hint", "") # hint는 없을수도 있으니 .get으로

                    # 읽어온 데이터로 Quiz 객체를 생성하여 리스트에 추가
                    quiz_obj = Quiz(question, choices, answer, hint)
                    self.quizzes.append(quiz_obj)
                    
                self.best_score = data.get("best_score", 0)
                self.history = data.get("history", [])

        except FileNotFoundError :
            print("저장된 데이터 파일이 없습니다. 기본 퀴즈를 로드합니다.")
            self.set_default_quizzes()
        
        except json.JSONDecodeError:
            print("데이터 파일이 손상되었습니다. 기본 퀴즈로 초기화합니다.")
            self.set_default_quizzes()

        except Exception as e:
            print(f"데이터를 불러오는 중 오류가 발생했습니다: {e}")
            self.set_default_quizzes()
