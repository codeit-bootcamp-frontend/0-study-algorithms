# 0-study-algorithms

코드잇 FE 부트캠프 0기 알고리즘 스터디!

## 가이드 라인

1.  코드잇 organization에 있는 upstream repo의 main 브랜치에서 본인 브랜치를 생성한다(나는 henry라는 이름으로 활동 중이다).
2.  upstream repo를 fork 한 뒤, origin repo를 로컬에서 clone한다. (백준 허브를 사용하면 로컬 환경을 사용할 필요 없다)
3.  어쨌든 origin main 브랜치에서 알고리즘 풀이들을 관리한다.
4.  upstream repo의 본인 브랜치에 PR(마감기한 : 일요일 자정)을 한다.

## 스터디 방식

1.  코드잇 정규 커리큘럼을 소화하기도 벅차며, 각자 알고리즘 실력의 편차가 다르므로 "기록"을 최우선 목표로 설정했다.
2.  매주 본인이 정한 알고리즘 문제 개수만큼 풀고 공유한다.

## PR 시 주의 사항

백준허브에서 fork origin main repo에 자동으로 push까지 해주므로,<br>
그대로 fork origin main repo에서 upstream henry repo로 PR 날리고 merge해주면 된다.

그리고 나서 upstream henry의 local repo에서 `git pull origin henry`를 해주고,<br>
fork main의 local repo에서도 `git pull upstream henry`를 해주면 된다.
