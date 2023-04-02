n = int(input()) #과목의 개수
score = list(map(int, input().split())) #각 과목의 점수를 받음
m = max(score) #최댓값 찾기

newScore = [] #조작한 점수 배열 

for i in score:
    newScore.append(i / m * 100) #조작한 각 점수를 newScore 배열에 추가

averageNewScore = sum(newScore) / n
print(averageNewScore)