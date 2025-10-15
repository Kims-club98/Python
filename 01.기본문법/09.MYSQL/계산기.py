def calculator():
    print("🔢 사칙연산 계산기입니다. 종료하려면 'exit' 또는 '종료'를 입력하세요.")

    while True:
        user_input = input("\n계산식을 입력하세요 (예: 3 + 4): ")

        if user_input.lower() in ['exit', '종료']:
            print("👋 계산기를 종료합니다.")
            break

        try:
            # 공백 기준으로 분리: 숫자1, 연산자, 숫자2
            parts = user_input.split()
            if len(parts) != 3:
                print("❌ 형식 오류: '숫자 연산자 숫자' 형식으로 입력해주세요.")
                continue

            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("❌ 0으로 나눌 수 없습니다.")
                    continue
                result = num1 / num2
            else:
                print("❌ 지원하지 않는 연산자입니다.")
                continue

            print(f"✅ 결과: {num1} {operator} {num2} = {result}")

        except ValueError:
            print("❌ 숫자를 정확히 입력해주세요.")

# 실행
if __name__ == "__main__":
    calculator()

