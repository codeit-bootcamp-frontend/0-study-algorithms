# 0-study-algorithms
## 가이드라인
준비물 : [백준 허브](https://chrome.google.com/webstore/detail/%EB%B0%B1%EC%A4%80%ED%97%88%EB%B8%8Cbaekjoonhub/ccammcjdkpgjmcpijpahlehmapgmphmk?hl=ko)
![image](https://user-images.githubusercontent.com/81355590/229982626-bc2b3740-e23c-4004-a2c4-4b296c0f7048.png)

1. upstream repo의 main에서 본인 이름(ex.eva) 브랜치를 생성한다.
2. fork를 한후 fork된 origin 레포를 clone한다.
4. 로컬에서 main브랜치에서 작업 후 origin 레포의 main에 push한다. `git push origin main`
5. upstream repo의 본인 이름 브랜치에 pr을 날린다~

## ✅ commit 규칙
commit 메세지: [문제 출처(플랫폼)] 문제이름 / 난이도 / 걸린시간
description: 문제 주소 (option)
터미널에서 작성법:
git commit -m "[BOJ] Hello World / 브론즈5 / 1분" -m "https://www.acmicpc.net/problem/2557"
플랫폼 작성법 통일:
[BOJ] - 백준
[PGS] - 프로그래머스
[FSC] - 패스트캠퍼스
[LTC] - 리트코드
[CFS] - 코드포스
[SEA] - 삼성SW Expert Academy
[ETC] - 그외


## ✅ PR 규칙
PR 제목: 이름 / 주차 / 몇 문제
shynnn / 1주차 / 4문제 
comment는 자유이나 가능하다면, 이번주에 풀었던 문제의 알고리즘 분류가 어떻게 되는지,
어떤 문제가 어려웠는지 회고를 작성한다면 개인에게도 도움되고 다른 코드 리뷰어가 참고하기 좋을 것 같습니다 :)
