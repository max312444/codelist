def bar():
    msg1 = "<<" + name
    
    msg2 = foo(msg1)
    msg2 += " "
    
    msg3 = pos(msg2)
    msg3 += " "
    
    return msg3

def foo(argF):
    msg = argF + "님"
    return msg

def pos(argP):
    msg = argP + "안녕하세요"
    return msg

name = "홍길동"

result = bar()

print(result)