"""
기본적인 계산 연산자
+: 더하기
-: 빼기
*: 곱하기
/: 나누기(몫)
%: 나누기(나머지)
**:거듭제곱 ex) print(2 ** 3) = 8

변수명 = 변수값
변수명은 변수에 맞는 이름이나 자기가 지어주고 싶은 변수명 사용하면 됩니다.
변수값은 필요한 값을 넣어주거나 입력을 받게 할 수도 있다.

예시) 
n = 3
설명) "n"이라는 변수명을 가진 변수에 숫자 3을 넣음
여기서 변수값은 3이 된다.

# a에 10을 넣어주는 코드
a = 10
# b에 3을 넣어주는 코드
b = 3

#a에 들어가 있는 값을 출력
print(a)
#b에 들어가 있는 값을 출력
print(b)

#a 와 b를 더한 값을 출력하는 코드 a + b = ?
print(a + b)

#a에서 b를 뺀 값을 출력하는 코드 a - b = ?
print(a - b)

#a 와 b를 곱한 값을 출력하는 코드 a * b = ?
print(a * b)

#a 와 b를 나눈 몫을 출력하는 코드 a / b = ?
print(a / b)

#a 와 b를 나눈 후 나온 나머지을 출력하는 코드 a % b = ?
print(a % b)

int : 정수.
str : 문자.
float : 실수.
chr : 정수값 -> 문자.
ord : 문자 -> 정수값.
split : 나누다 구분하다. 
for : 반복문.(반복의 횟수가 명확하게 정해져 있을 때)
range : 범위. ex) for i in range()
while : 1을 붙이면 계속 반복. (반복문의 횟수가 예측하지 못할 때)
if : 만약에.
elif : ~도 아니면.
else : 그 외. 
1) if(조건 하나일 경우), 
2) if - else(두 조건 중 무조건 하나 선택일 경우), 
3) if - elif...(조건 중 하나를 선택할 수 있고 선택 안할 수 있는 경우),
4) if- elif...- else(여러 조건 중 무조건 하나를 선택하는 경우)
5) if 시리즈 중에 선택의 최소는 0개 최대는 1개이다 

format : (수,".2f")원하는 자리(f) 까지 반올림. 
map : 여러가지 데이터를 받아서 각각의 요소에 함수를 적용한 결과를 반환하는 내장함수.
max : 정수 중 가장 큰수.
min : 정수 중 가장 작은수.
import : 다른 모듈(외부 라이브러리)의 기능을 현재 모듈에서 사용하기 위해 필요. 
rstrip : 문자열에서 오른쪽에 있는 연속된 모든 공백을 삭제한다.
f {}: {} 안에 변수나 표현식을 쉽게 삽일할 수 있도록 해준다.
list : 목록 작성에 쓰임
count : 몇개인지 갯수를 셀 때 사용
len : 리스트의 길이를 구할 때 사용
del : 리스트 요소 삭제. x 번째 값을 삭제
append : 리스트 요소 추가.
sort : 리스트 요소 순서대로 정렬. ex) a = [1, 4, 2, 3]. a.sort() => a = [1, 2, 3, 4] 
reverse : 현재 리스트를 역순으로 뒤집는다.
index : 리스트에 x 값이 있으면 위치 값을 돌려준다. ex) a = [1, 2, 3]. a.index(3) = 2 와 같이 index 값이 몇번째에 있는지 나타냄
insert : 리스트에 요소 삽입. ex) a = [1, 2, 3]. a.insert(0, 4). a = [4, 1, 2, 3] 0의 자리에 4를 삽입하라는 뜻이다.
remove : 리스트에 나오는 첫 번째 x 값을 제거. 중복 값이 더 있으면 다시 remove를 입력해 삭제한다.
def : 함수를 하나 정의 해놓고 정의 된 함수를 호출해 쓴다. 자주 사용하는 코드를 함수로 묶어 사용(간결하게 됨, 수정 유지보수 편의) 
return : 지정된 변수값을 다시 가져온다.(retrun(넘겨줄 값))= 현재 함수의 실행을 종료하고 Return 우항 값을 함수 호출 쪽으로 반환한다.
output을 전달함. return을 만나면 계산 했다면 계산 값을 가지고 호출 됐던 항으로 돌아가 그대로 실행한다. 
현재 함수의 실행을 종료하십시오. return값을 함수 호출한 쪽으로 넘겨라.
def 함수를 사용할 때 가장 설명이 잘되는 유형이 stack 형이다.
함수를 호출할때 집어 넣어주는 값 = 인자값
매개변수 : 입력받는 값을 저장하기 위함
문자열에 비교연산자는 사전적 순서를 기준으로 비교된다.
논리 연산자에는 and or not 이 있는데. 여기서 and 와 or은 이항 연산자로 
연산자를 중심으로 좌항 우항이 있는 것을 의미한다. not은 단항 연산자로 항이 1개만 있다.
코드를 짤 때 우선 적으로 예외 조건을 제외하고 코드를 짠다. 정상적으로 작동하는 것을 확인 후 예외 조건들을 대입한다.
continue : 제어문으로 반복문 내에서 사용되며, 해당 반복문의 반복을 중단하고 다음 반복을 시행 하라는 뜻이다.
break와 비슷한 효과를 내지만 break는 반복문을 아에 종료를 시키고 continue는 다음 반복으로 넘긴다. 반복은 계속 하는데 특정 조건에는 시행하지 말라.
end = 줄바꿈 없애고 출력 ex) print("*",end="") 그냥 print를 하면 따로 한줄씩 별이 출력이 되지만
이렇게 하면 별을 연속적으로 붙여서 출력이 가능하다.  
print(bar.pop(2)) : del과 같은 건데 해당 리스트의 값(좌표 : 인덱스 번호)을 가져오고 삭제한다.
bar = {'key' : 'value', 'key2' : 'value2'} : 딕셔너리 생성
새로운 값을 할당하려면 그냥 지정해주기만하면 되고 삭제는 del key값 하면 삭제 된다.
모든 키와 해당 값 삭제 : bar.clear()
for key in person: - key 값을 순회
for key in bar.keys(): - key 값을 출력
for key in bar.values(): - value 값을 출력
for key in bar.items(): - key, value 값 출력

"""