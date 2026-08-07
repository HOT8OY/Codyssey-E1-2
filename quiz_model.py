
# 2단계: 데이터 구조 설계 및 Model 기초 구현
# Quiz 객체를 설계합니다. (보너스 과제를 위해 hint 속성을 미리 포함시킵니다.)

# state.json의 스키마를 정의합니다. (아래 '데이터 구조' 섹션 참고)

# JSON 파일을 읽고(load), 쓰는(save) 파일 입출력 로직을 구현합니다. 파일이 없거나 손상되었을 때 기본 데이터를 반환하는 예외 처리에 집중합니다.

# Commit: Feat: Quiz 모델 및 JSON 파일 입출력 기능 구현

# Model 계층은 프로그램의 '데이터'와 그 데이터를 다루는 '비즈니스 로직(규칙)'을 전담하는 곳입니다.
# Model은 화면에 어떻게 출력될지(print), 사용자로부터 어떻게 입력을 받을지(input)에 대해서는 전혀 알지 못해야 하며,
# 오직 데이터의 상태를 관리하고 파일에 저장/불러오는 역할만 충실히 수행해야 합니다.

class Quiz:
    def __init__(self, question, choices, answer, hints, is_hint_used=False, is_solved=False):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hints = hints
        self.is_hint_used = is_hint_used
        self.is_solved = is_solved

    def to_dict(self):
        return {
            ""
        }


#   Quiz Data 입출력
class QuizModel:

    def load_data(self):
        pass

    def save_data(self):
        pass

