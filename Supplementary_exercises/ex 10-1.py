# 문제 10-1 리스트에 항목 추가하기
# 도서제목 입력하면 해당 제목을 도서 목록에 추가하는 기능
# 사용자가 종료 입력할때 까지 반복, 마지막에 전체 도서 목록 출력

books = [] # 빈 리스트 생성

while True: # 무한 반복 
    title = input("도서 제목을 입력하세요 (종료하려면 '종료' 입력): ") # title에 도서 제목입력
    if title == '종료': # 만약 title이 '종료'라면 
        break # 정지
    else:
        books.append(title) # 입력한 title을 books 리스트 안에 추가
    
print("도서 목록:", books) # books 리스트 출력