# total = 중간고사(35%) + 기말고사(45%) + 과제(20%)
# 높은 점수의 학생부터 N/10 명씩 성적을 부여한다.
# 전체 학생에게 성적을 부여한 뒤, K번 학생의 성적을 출력해보자!
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
T = int(input())
for tc in range(1, T+1):
    # N은 10의 배수 / 1 <= K <= N
    N, K = map(int, input().split())
    
    # 중간 / 기말 / 과제 순서로 입력
    score = [ list( map( int, input().split() ) ) for _ in range(N) ]
    # 점수의 총계 내림차순
    score_desc = []
    total = []
    for i in range(N):
        total.append(score[i][0]*0.35 + score[i][1]*0.45 + score[i][2]*0.2)
    
    print(total)