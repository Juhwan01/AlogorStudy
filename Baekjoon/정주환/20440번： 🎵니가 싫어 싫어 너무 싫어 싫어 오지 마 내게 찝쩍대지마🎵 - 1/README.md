# 20440번: 🎵니가 싫어 싫어 너무 싫어 싫어 오지 마 내게 찝쩍대지마🎵 - 1 - <img src="https://static.solved.ac/tier_small/13.svg" style="height:20px" /> Gold III

<!-- performance -->

<!-- 문제 제출 후 깃허브에 푸시를 했을 때 제출한 코드의 성능이 입력될 공간입니다.-->

<!-- end -->

## 문제

[문제 링크](https://boj.kr/20440)


<blockquote>
<p>🎵니가 싫어 싫어 너무 싫어 싫어 오지마 내게 찝쩍대지마🎵 - 유자, 모기송 中</p>
</blockquote>

<p>모기를 싫어하는 지동이는 어느 날 문득 자신의 방에 모기가 가장 많이 있는 시간대가&nbsp;언제인지 궁금해졌다. 다행히 지동이 방은 최첨단 시스템이 갖춰져 있어 어떤 모기가 방에 언제 입장했고&nbsp;언제 퇴장했는지를 기록할 수 있다.</p>

<p>지동이를 도와 모기들의 방 입장, 퇴장 시각이 주어졌을 때 모기들이 가장 많이 있는 시간대와&nbsp;해당 시간대에 모기가 몇 마리가 있는지 구하는 프로그램을 만들어보자.&nbsp;</p>



## 입력


<p>첫째 줄에 지동이의 방에 출입한 모기의 마릿수&nbsp;<em>N</em>(1 ≤ <em>N</em> ≤ 1,000,000)가 주어진다.</p>

<p>다음 <em>N</em>개의 줄에 모기의 입장 시각&nbsp;<em>T<sub>E</sub></em>과 퇴장 시각&nbsp;<em>T<sub>X</sub></em>이 주어진다. (0 ≤&nbsp;<em>T<sub>E</sub>&nbsp;&lt;&nbsp;T<sub>X</sub>&nbsp;</em>≤ 2,100,000,000)</p>

<p>모기는 <em>[T<sub>E</sub>, T<sub>x</sub>)</em>동안 존재한다.</p>

<p>&nbsp;</p>



## 출력


<p>첫째 줄에 지동이 방에 모기가 가장 많이 있는&nbsp;시간대의 모기 마릿수를 출력한다.</p>

<p>지동이 방에 모기가 가장 많이 있는 시간대의 연속 구간 전체를 <em>[T<sub>Em</sub>, T<sub>Xm</sub>)</em>이라고 할 때,</p>

<p>둘째 줄에 <em>T<sub>Em</sub>, T<sub>Xm</sub></em>을&nbsp;공백으로 구분하여 출력한다. 단, 여러 가지 방법이 있으면&nbsp;가장 빠른 시작 시각을 기준으로 출력한다.</p>



## 소스코드

[소스코드 보기](🎵니가%20싫어%20싫어%20너무%20싫어%20싫어%20오지%20마%20내게%20찝쩍대지마🎵%20-%201.py)