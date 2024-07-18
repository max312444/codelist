# 문제 10807
# 총 n 개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오

n = input()
n_list = list(map(int,input().split())) # list를 사용해 목록을 만들고 목록 내용은 입력값을 차례대로 들어가게 
# map(int,input(split())) 을 사용한다
v = int(input())
# v 는 갯수를 세고 싶은 값을 입력하고 출력할 때 count를 사용한다.
print(n_list.count(v))