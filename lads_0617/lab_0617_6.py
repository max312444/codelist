# 태그 이름과 내용을 매개변수로 받아, 해당 태그로 감싸진 HTML 요소를 반환하는 함수 wrap_in_tag를 작성
def wrap_in_tag(tag, text):
    return f"<{tag}>{text}</{tag}>"

print(wrap_in_tag('p', 'hello'))
print(wrap_in_tag('b', 'world'))