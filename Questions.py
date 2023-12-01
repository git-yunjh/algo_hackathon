import pandas as pd
import random

# CSV 파일에서 데이터 읽기
df = pd.read_csv('questions.csv')

# 각 카테고리의 총합을 저장할 딕셔너리
category_scores = {category: 0 for category in set(df['Category'])}

# 사용자에게 질문하고 점수 부여
user_scores = {}
questions = list(df['Question'])  # 질문 목록 가져오기

while questions:
    # 랜덤하게 질문 선택
    random_question = random.choice(questions)
    category = df[df['Question'] == random_question]['Category'].values[0]

    # 선택된 질문 및 해당 카테고리 출력
    print("\nQ:", random_question)

    while True:
        # 사용자에게 점수 부여
        user_input = input("1부터 5까지 점수를 입력하세요. (5가 매우 그렇다): ")

        # 예외 처리: 유효한 숫자가 입력되었는지 확인
        try:
            score = int(user_input)
            if 1 <= score <= 5:
                user_scores[random_question] = score
                # 선택된 질문은 다음에 나오지 않도록 제거
                questions.remove(random_question)

                # 해당 카테고리의 총합에 점수 추가
                category_scores[category] += score
                break  # 유효한 입력이 들어온 경우 반복문 탈출
            else:
                print("1부터 5까지 입력하세요.")
        except ValueError:
            print("Please enter a numeric value.")

# 카테고리별 총합이 가장 높은 상위 3개의 카테고리 출력
top_categories = sorted(category_scores, key=category_scores.get, reverse=True)[:3]
print("\n상위 3개의 계열:")
for category in top_categories:
    print(f"{category}: {category_scores[category]} 점")
