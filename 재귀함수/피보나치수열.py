# n번째 피보나치 수를 리턴
def fib(n):
    # 여기에 코드를 작성하세요
    if n <= 1: return n
    return fib(n - 1) + fib(n - 2)
# 테스트 코드: fib(1)부터 fib(10)까지 출력
for i in range(1, 11):
    print(fib(i))
    