# 파이썬 라스트를 사용하여 쇼핑 품목을 관리하는 프로그램 작성

shopping_list = []

shopping_list.append('milk')
shopping_list.append('bread')
shopping_list.append('eggs')
shopping_list.append('apple')
print("현재 쇼핑 리스트:",shopping_list)
shopping_list.insert(0, 'toilet paper')
shopping_list.insert(1, 'orange juice')
extra = ['chicken', 'rice']
shopping_list.extend(extra)
print("최종 쇼핑 리스트:",shopping_list)