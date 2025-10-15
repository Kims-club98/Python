num = input('숫자>')
num = int(num)



while True:
#예외처리
    try:
        num = input('숫자>')
        if num =="": break
        num = int(num)
    except Exception as err: # 오류가 났을 때
        print('숫자를 입력하세요')

# Try를 계속 진행하다가 오류(문자열) 입력 시
# 숫자를 입려하세요 문구 등장(오류 시)

# while True:
#         num = input('숫자>')
#         if num =="": break
#         num = int(num)


# 결론: Try를 계속 진행하다가
 # 오류가 발생
  # execpt Exception(오류에 대한 정보)으로 이동함
   # 오류문구 필요 시 print로 기입