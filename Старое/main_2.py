
from utils import load_questions, count_correct_answers, count_points


def main():

    questions = load_questions()

    for question in questions:
        print(question.build_question())

        user_answer = input()
        question.user_answer = user_answer

        if question.is_correct():
            print(question.build_positive_feedback())
        else:
            print(question.build_negative_feedback())

    correct_counter = count_correct_answers(questions)
    points = count_points(questions)


    print('Вот и всё!')
    print(f'Отвечено {correct_counter} вопросd из {len(questions)}')
    print(f'Набрано баллов:{points}')


main()