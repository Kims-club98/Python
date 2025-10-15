file_name = 'data/juso.txt'

with open(file_name, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(lines, type(lines), len(lines))
    for line in lines:
        print(line, end='')
        items = line.split(",") # ,를 기준으로 데이터를 나눠줌
        print(f"이름:{items[0]}, 전화:{items[1]}, 주소:{items[2]}", end='')
