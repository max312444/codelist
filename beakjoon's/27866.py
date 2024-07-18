# 문제 27866
# 단어 S와 정수 i가 주어졌을 때, S의 i번째 글자를 출력하는 프로그램을 작성하시오.

word = input()
find_letter = int(input())
find_letter_index = word[find_letter - 1]
print(find_letter_index)
