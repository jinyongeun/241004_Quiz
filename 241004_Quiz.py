# Quiz 1
def add(a, b, c, d):
    return a + b + c + d

def multiply(a, b, c, d):
    return a * b * c * d

num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))
num3 = int(input("세 번째 숫자를 입력하세요: "))
num4 = int(input("네 번째 숫자를 입력하세요: "))

result1 = add(num1, num2, num3, num4)
result2 = multiply(num1, num2, num3, num4)

print(f"4개 숫자의 합: {result1}")
print(f"4개 숫자의 곱: {result2}")

# Quiz 2
def odd_or_even(number):
    if number % 2 == 0:
        return "짝수"
    else:
        return "홀수"

num = int(input("숫자를 입력하세요: "))

result = odd_or_even(num)
print(f"입력한 숫자는 {result}입니다.")

# Quiz 3
def calculate_average(numbers):
    total = 0
    count = 0

    for num in numbers:
        total += num
        count += 1

    average = total / count
    return average

numbers = [10, 20, 30, 40, 50]

avg = calculate_average(numbers)
print(f"리스트의 평균값: {avg}")

# Quiz 4
class GameCharacter:
    def __init__(self, character_id, gender, job):
        self.character_id = character_id
        self.gender = gender
        self.job = job

    def attack(self):
        print("공격!")

character_id = input("캐릭터의 아이디를 입력하세요: ")
gender = input("캐릭터의 성별을 입력하세요: ")
job = input("캐릭터의 직업을 입력하세요: ")

character = GameCharacter(character_id, gender, job)

print(f"캐릭터 정보: 아이디={character.character_id}, 성별={character.gender}, 직업={character.job}")

character.attack()

# Quiz 5
class RealEstate:
    def __init__(self, location, size, building_type, price, year_built):
        self.location = location
        self.size = size
        self.building_type = building_type
        self.price = price
        self.year_built = year_built

    def show_info(self):
        print(f"부동산 정보")
        print(f"위치: {self.location}")
        print(f"평수: {self.size}평")
        print(f"건물 종류: {self.building_type}")
        print(f"가격: {self.price} 원")
        print(f"건축 연도: {self.year_built}년")

location = input("부동산 위치를 입력하세요: ")
size = input("평수를 입력하세요: ")
building_type = input("건물 종류를 입력하세요: ")
price = input("가격을 입력하세요: ")
year_built = input("건축 연도를 입력하세요: ")

property1 = RealEstate(location, size, building_type, price, year_built)

property1.show_info()