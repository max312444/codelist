# 문제 9-1 평균 속도 계산기
# 차량이 이동하는 데 걸린 시간과 이동 거리를 바탕으로 평균 속도 계산.
# 출발 시간과 도착시간(시와 분으로 별도 입력), 그리고 이동거리를 입력받음
# 차량의 평균 속도를 km/h 단위로 계산, 속도가 느림, 보통, 빠름 중에 어느것에 해당하는지 출력. 

# 입력 출발 시간(시), 출발시간(분), 도착시간(시), 도착시간(분), 이동거리(km)
# 출력은 이동거리, 출발시간, 도착시간, 평균속도, 속도 상태 순으로 출력
# 평군 속도 = 이동거리 / 이동 시간 -> 분 단위로 환산하여 계산
# 60km 미만이면 느림, 60이상 90미만이면 보통, 90이상이면 빠름으로 분류
'''
start_timeH = int(input("출발 시 (시간)을 입력하세요: "))
start_timeM = int(input("출발 시 (분)을 입력하세요: "))
end_timeH = int(input("도착 시 (시간)을 입력하세요: "))
end_timeM = int(input("도착 시 (분)을 입력하세요: "))
distance = float(input("이동 거리 (km)를 입력하세요: "))

def time1(start_timeH):
    time = start_timeH * 60
    return time

def time2(end_timeH):
    time = end_timeH * 60
    return time

speed = distance / (((end_timeM + time2(end_timeH)) - (start_timeM + time1(start_timeH))) / 60)
print("    ")
print(f"이동 거리: {distance}km")
print(f"출발 시간: {start_timeH}시 {start_timeM}분")
print(f"도착 시간: {end_timeH}시 {end_timeM}분")
print(f"평균 속도: ",format(speed,".2f"),"km/h")

if speed < 60 :
    print("속도 상태: 느림")
elif 60<= speed < 90:
    print("속도 상태: 보통")
else:
    print("속도 상태: 빠름")
'''
start_timeH = int(input("출발 시 (시간)을 입력하세요: "))
start_timeM = int(input("출발 시 (분)을 입력하세요: "))
end_timeH = int(input("도착 시 (시간)을 입력하세요: "))
end_timeM = int(input("도착 시 (분)을 입력하세요: "))
distance = float(input("이동 거리 (km)를 입력하세요: "))

def time(start_timeH, start_timeM, end_timeH, end_timeM):
    time = (((end_timeM + (end_timeH * 60)) - (start_timeM + (start_timeH * 60))) / 60)
    return time
speed = distance / time(start_timeH, start_timeM, end_timeH, end_timeM)
print("    ")
print(f"이동 거리: {distance}km")
print(f"출발 시간: {start_timeH}시 {start_timeM}분")
print(f"도착 시간: {end_timeH}시 {end_timeM}분")
print(f"평균 속도:",format(speed,".2f"),"km/h")

if speed < 60 :
    print("속도 상태: 느림")
elif 60<= speed < 90:
    print("속도 상태: 보통")
else:
    print("속도 상태: 빠름")
