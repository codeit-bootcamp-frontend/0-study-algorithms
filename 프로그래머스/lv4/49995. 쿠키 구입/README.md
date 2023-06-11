# [level 4] 쿠키 구입 - 49995 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/49995) 

### 성능 요약

메모리: 36.4 MB, 시간: 8.28 ms

### 구분

코딩테스트 연습 > Summer／Winter Coding（～2018）

### 채점결과

Empty

### 문제 설명

<p>과자를 바구니 단위로 파는 가게가 있습니다. 이 가게는 1번부터 N번까지 차례로 번호가 붙은 바구니 N개가 일렬로 나열해 놨습니다.</p>

<p>철수는 두 아들에게 줄 과자를 사려합니다. 첫째 아들에게는 l번 바구니부터 m번 바구니까지, 둘째 아들에게는 m+1번 바구니부터 r번 바구니까지를 주려합니다. 단, 두 아들이 받을 과자 수는 같아야 합니다(1 &lt;= l &lt;= m, m+1 &lt;= r &lt;= N). 즉,  A[i] 를 i번 바구니에 들어있는 과자 수라고 했을 때, <code>A[l]+..+A[m] = A[m+1]+..+A[r]</code> 를 만족해야 합니다.</p>

<p>각 바구니 안에 들은 과자 수가 차례로 들은 배열 cookie가 주어질 때, 조건에 맞게 과자를 살 경우 한 명의 아들에게 줄 수 있는 가장 많은 과자 수를 return 하는 solution 함수를 완성해주세요. (단, 조건에 맞게 과자를 구매할 수 없다면 0을 return 합니다)</p>

<h5>제한사항</h5>

<ul>
<li>cookie의 길이는 1 이상 2,000 이하입니다.</li>
<li>cookie의 각각의 원소는 1 이상 500 이하인 자연수입니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>cookie</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[1,1,2,3]</td>
<td>3</td>
</tr>
<tr>
<td>[1,2,4,5]</td>
<td>0</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<p>첫째 아들에게 2, 3번 바구니를, 둘째 아들에게 4번 바구니를 사주면 두 아들은 각각 과자 3개를 받습니다.</p>

<p>입출력 예 #2</p>

<p>주어진 조건에 맞게 과자를 살 방법이 없습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges