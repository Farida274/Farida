import pandas



text = "mening natijam\n"

with open(r"C:\Users\xafiz\OneDrive\바탕 화면\한국어 정보처리 (전태희)\git_practice\result.txt",
           "w", encoding='utf-8') as f:
    f.write(text)

'''
class Sonlar:  # klas nomi
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        

    def add(self): # klas metodi(add)
        result = self.num1 + self.num2
        return result

sonlarim = Sonlar(123, 55)  # sonlar degan klasni obyektik
print(sonlarim.num1)
print(sonlarim.add())  
'''


'''
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def greet(self):
        print(f"안녕하세요, 저는 {self.name}이고 {self.age}살입니다.")
        # print("안녕하세요, 저는 ", self.name, "이고 ", self.age, "살입니다." )


def greet(ism, age):
        print(f"안녕하세요, 저는 {ism}이고 {age}살입니다.")
        # print("안녕하세요, 저는 ", self.name, "이고 ", self.age, "살입니다." )

p1 = Person("지민", 25, "janubiy")  # 객체 p1 생성
p2 = Person("민수", 30, "tinchlik")  # 객체 p2 생성


greet("Sohib", 33)
'''
