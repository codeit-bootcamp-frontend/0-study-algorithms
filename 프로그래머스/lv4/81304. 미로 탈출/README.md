# [level 4] 미로 탈출 - 81304 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/81304) 

### 성능 요약

메모리: 70.9 MB, 시간: 146.75 ms

### 구분

코딩테스트 연습 > 2021 카카오 채용연계형 인턴십

### 채점결과

Empty

### 문제 설명

<p>신규 게임 ‘카카오 미로 탈출’이 출시되어, <code>라이언</code>이 베타테스터로 참가했습니다.</p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/0015adcc-d76e-40e3-8004-70dd8deff2ec/Maze.png" title="" alt="Maze.png"></p>

<p>위 예시 그림은 카카오 미로 탈출의 초기 상태를 나타냅니다. 1번부터 3번까지 번호가 붙어있는 3개의 방이 있고, 방과 방 사이를 연결하는 길에는 이동하는데 걸리는 시간이 표시되어 있습니다. 길은 화살표가 가리키는 방향으로만 이동할 수 있습니다. 미로에는 함정이 존재하며, 함정으로 이동하면, 이동한 함정과 연결된 모든 화살표의 방향이 바뀝니다.<br>
출발지점인 <code>1</code>번 방에서 탈출이 가능한 <code>3</code>번 방까지 이동해야 합니다. 탈출하는데 걸리는 최소 시간을 구하려고 합니다.</p>

<ul>
<li>그림의 원은 방을 나타내며 원 안의 숫자는 방 번호를 나타냅니다.

<ul>
<li>방이 <code>n</code>개일 때, 방 번호는 1부터 <code>n</code>까지 사용됩니다.</li>
</ul></li>
<li>화살표에 표시된 숫자는 방과 방 사이를 이동할 때 걸리는 시간을 나타냅니다.

<ul>
<li>화살표가 가리키고 있는 방향으로만 이동이 가능합니다. 즉, 위 그림에서 2번 방에서 1번 방으로는 이동할 수 없습니다.</li>
</ul></li>
<li>그림에 표시된 빨간색 방인 <code>2</code>번 방은 함정입니다.

<ul>
<li>함정 방으로 이동하는 순간, 이동한 함정 방과 연결되어있는 모든 길의 방향이 반대가 됩니다.</li>
<li>위 그림 <code>1</code>번 방에서 <code>2</code>번 방으로 이동하는 순간 <code>1</code>에서 <code>2</code>로 이동할 수 있던 길은 <code>2</code>에서 <code>1</code>로 이동할 수 있는 길로 바뀌고, <code>3</code>에서 <code>2</code>로 이동할 수 있던 길은 <code>2</code>에서 <code>3</code>으로 이동할 수 있는 길로 바뀝니다.</li>
<li>똑같은 함정 방을 두 번째 방문하게 되면 원래 방향의 길로 돌아옵니다. 즉, 여러 번 방문하여 계속 길의 방향을 반대로 뒤집을 수 있습니다.</li>
</ul></li>
<li>미로를 탈출하는데 필요한 최단 시간은 다음과 같습니다.

<ul>
<li>1→2: 2번 방으로 이동합니다. 이동 시간은 2입니다.</li>
<li>함정 발동: 2번 방과 연결된 모든 길의 방향이 반대가 됩니다.</li>
<li>2→3: 3번 방으로 이동합니다. 이동 시간은 3입니다.</li>
<li>탈출에 성공했습니다. 총 이동시간은 5입니다.</li>
</ul></li>
</ul>

<p>방의 개수를 나타내는 정수 <code>n</code>, 출발 방의 번호 <code>start</code>, 도착 방의 번호 <code>end</code>, 통로와 이동시간을 나타내는 2차원 정수 배열 <code>roads</code>, 함정 방의 번호를 담은 정수 배열 <code>traps</code>이 매개변수로 주어질 때, 미로를 탈출하는데 필요한 최단 시간을 return 하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>2 ≤ <code>n</code> ≤ 1,000</li>
<li>1 ≤ <code>start</code> ≤ <code>n</code></li>
<li>1 ≤ <code>end</code> ≤ <code>n</code></li>
<li>1 ≤ <code>roads</code>의 행 길이 ≤ 3,000</li>
<li><code>roads</code>의 행은 [P, Q, S]로 이루어져 있습니다.

<ul>
<li><code>P</code>에서 <code>Q</code>로 갈 수 있는 길이 있으며, 길을 따라 이동하는데 <code>S</code>만큼 시간이 걸립니다.</li>
<li>1 ≤ <code>P</code> ≤ <code>n</code></li>
<li>1 ≤ <code>Q</code> ≤ <code>n</code></li>
<li><code>P</code> ≠ <code>Q</code></li>
<li>1 ≤ <code>S</code> ≤ 3,000</li>
<li>서로 다른 두 방 사이에 직접 연결된 길이 여러 개 존재할 수도 있습니다.</li>
</ul></li>
<li>0 ≤ <code>traps</code>의 길이 ≤ 10

<ul>
<li>1 ≤ <code>traps</code>의 원소 ≤ <code>n</code></li>
<li>시작 방과 도착 방은 함정이 아닙니다.</li>
</ul></li>
<li>항상 미로를 탈출할 수 있는 경우만 주어집니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>start</th>
<th>end</th>
<th>roads</th>
<th>traps</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>3</td>
<td>1</td>
<td>3</td>
<td>[[1, 2, 2], [3, 2, 3]]</td>
<td>[2]</td>
<td>5</td>
</tr>
<tr>
<td>4</td>
<td>1</td>
<td>4</td>
<td>[[1, 2, 1], [3, 2, 1], [2, 4, 1]]</td>
<td>[2, 3]</td>
<td>4</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<p>문제 예시와 같습니다.</p>

<p><strong>입출력 예 #2</strong></p>

<p><img src="https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/c5ab2e6d-9872-42d1-9898-2890b69ce74e/MazeEx2.png" title="" alt="MazeEx2.png"></p>

<p>1 → 2 → 3 → 2 → 4 순서로 이동하면 됩니다. 총 이동시간은 4입니다.</p>

<hr>

<h5>제한시간 안내</h5>

<ul>
<li>정확성 테스트 : 10초</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges