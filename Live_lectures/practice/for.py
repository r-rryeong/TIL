#1~3의 세제곱 리스트 만들기
#초기화된 리스트를 만들고 싶을 때

cubic_dict = {}

cubic_dict = {number: number**3 for number in range(1,4)}
print(cubic_dict)