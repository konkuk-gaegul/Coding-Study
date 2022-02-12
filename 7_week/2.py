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
    
    total = []
    for i in range(N):
        # 규칙에 의한 점수 산출
        total.append(score[i][0]*0.35 + score[i][1]*0.45 + score[i][2]*0.2)

        # total의 점수를 내림차순 정렬
        for j in range( len(total) ):
            for k in range(1, len(total)):
                # 앞의 값과 비교하여 작은 것을 뒤로 보내자
                if total[k-1] <= total[k]:
                    total[k-1], total[k] = total[k], total[k-1]
    
    # K번 학생의 등수 : index + 1로 보정
    target_score = score[K-1][0]*0.35 + score[K-1][1]*0.45 + score[K-1][2]*0.2
    target_idx   = total.index( target_score )      
    target_idx   = int( target_idx / (N/10) )     # int를 사용해서 10의 배수인 N으로도  
    target_grade = grade[ target_idx ]            # 보정가능!
    
    print(f'#{tc} {grade[target_idx]}')