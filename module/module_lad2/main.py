import sys 
import os


#비표준 경로 추가 : 개인 환경에 맞게 수정
module_path = os.getcwd() + '\extrenal' # 외부의 모듈의 주소를 추가

# print(module_path)

if module_path not in sys.path:
    sys.path.append(module_path)
    
#  모듈 임포트
import extrenal_module

def main():
    greeting = extrenal_module.greet("Python User")
    print(greeting)
    
if __name__ == "__main__":
    main()

