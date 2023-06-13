# [level 4] 블록 게임 - 42894 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42894) 

### 성능 요약

메모리: 33.5 MB, 시간: 0.28 ms

### 구분

코딩테스트 연습 > 2019 KAKAO BLIND RECRUITMENT

### 채점결과

Empty

### 문제 설명

<h2>블록게임</h2>

<p>프렌즈 블록이라는 신규 게임이 출시되었고, 어마어마한 상금이 걸린 이벤트 대회가 개최 되었다. </p>

<p>이 대회는 사람을 대신해서 플레이할 프로그램으로 참가해도 된다는 규정이 있어서, 게임 실력이 형편없는 프로도는 프로그램을 만들어서 참가하기로 결심하고 개발을 시작하였다.</p>

<p>프로도가 우승할 수 있도록 도와서 빠르고 정확한 프로그램을 작성해 보자.</p>

<h5>게임규칙</h5>

<p>아래 그림과 같이 1×1 크기의 블록을 이어 붙여 만든 3 종류의 블록을 회전해서 총 12가지 모양의 블록을 만들 수 있다.</p>

<p><img src="https://grepp-programmers.s3.amazonaws.com/files/production/1b22ebaad2/13a37af2-2ed1-4312-aae4-94ba9ef21679.png" title="" alt="blocks_1.png"></p>

<p>1 x 1 크기의 정사각형으로 이루어진 N x N 크기의 보드 위에 이 블록들이 배치된 채로 게임이 시작된다. (보드 위에 놓인 블록은 회전할 수 없다). 모든 블록은 블록을 구성하는 사각형들이 정확히 보드 위의 사각형에 맞도록 놓여있으며, 선 위에 걸치거나 보드를 벗어나게 놓여있는 경우는 없다.</p>

<p>플레이어는 위쪽에서 1 x 1 크기의 검은 블록을 떨어뜨려 쌓을 수 있다. 검은 블록은 항상 맵의 한 칸에 꽉 차게 떨어뜨려야 하며, 줄에 걸치면 안된다. <br>
이때, 검은 블록과 기존에 놓인 블록을 합해 <u><strong>속이 꽉 채워진</strong></u> 직사각형을 만들 수 있다면 그 블록을 없앨 수 있다.</p>

<p>예를 들어 검은 블록을 떨어뜨려 아래와 같이 만들 경우 주황색 블록을 없앨 수 있다.</p>

<p><img src="https://grepp-programmers.s3.amazonaws.com/files/production/d56e9f9068/8ed8b26d-6a1a-4543-b4ee-60f8f287e748.png" title="" alt="blocks_3.png"></p>

<p>빨간 블록을 가로막던 주황색 블록이 없어졌으므로 다음과 같이 빨간 블록도 없앨 수 있다.</p>

<p><img src="https://grepp-programmers.s3.amazonaws.com/files/production/a3ca48b567/010e4297-4499-4ea4-987d-4b42e2fc4c3c.png" title="" alt="blocks_4.png"></p>

<p>그러나 다른 블록들은 검은 블록을 떨어뜨려 직사각형으로 만들 수 없기 때문에 없앨 수 없다.</p>

<p>따라서 위 예시에서 없앨 수 있는 블록은 최대 2개이다.</p>

<p>보드 위에 놓인 블록의 상태가 담긴 2차원 배열 board가 주어질 때, 검은 블록을 떨어뜨려 없앨 수 있는 블록 개수의 최댓값을 구하라.</p>

<h5>제한사항</h5>

<ul>
<li>board는 블록의 상태가 들어있는 N x N 크기 2차원 배열이다.

<ul>
<li>N은 <code>4</code> 이상 <code>50</code> 이하다.</li>
</ul></li>
<li>board의 각 행의 원소는 <code>0</code> 이상 <code>200</code> 이하의 자연수이다.

<ul>
<li>0 은 빈 칸을 나타낸다.</li>
<li>board에 놓여있는 각 블록은 숫자를 이용해 표현한다.</li>
<li>잘못된 블록 모양이 주어지는 경우는 없다.</li>
<li>모양에 관계 없이 서로 다른 블록은 서로 다른 숫자로 표현된다.</li>
<li>예를 들어 문제에 주어진 예시의 경우 다음과 같이 주어진다.</li>
</ul></li>
</ul>

<p><img src="https://grepp-programmers.s3.amazonaws.com/files/production/4d16d87605/9f555cf3-e664-44c4-8567-e01445b9b3b6.png" title="" alt="blocks_6.png"></p>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>board</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]</td>
<td>2</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1<br>
문제에 주어진 예시와 같음</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges