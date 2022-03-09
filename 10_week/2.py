# 1
# ti
# Starteatingwellwiththeseeighttipsforhealthyeating,whichcoverthebasicsofahealthydietandgoodnutrition
# 문장 속에서 해당 단어가 몇 개 들어있는지 출력하자
## 전략
# 원하는 문자의 첫 문자를 찾은 다음,
# 그 뒤로 len(원하는 문자)-1 만큼 검사
for tc in range(1, 11):
    
    word = input()
    sentence = input()
    n = 0
    for i in range(len(sentence)-len(word)):
        if sentence[i] == word[0]:
            w = 0   # 일치하는 갯수
            for j in range(1, len(word)):
                if sentence[i+j] == word[j]:
                    w += 1
            if w == len(word) - 1:
                n += 1
                
    print(f'#{tc} {n}')
