# 초보자를 위한 파이썬 300제
print("Hello Workld")
print("'Mary's cosmetics'")
print('신씨가 소리질렀다. "도둑이야"')
print('신씨가 소리질렀다. "도둑이야"')
print('신씨가 소리질렀다. "도둑이야"')
print('신씨가 소리질렀다. "도둑이야"')
print('신씨가 소리질렀다. "도둑이야"')
print('신씨가 소리질렀다. "도둑이야"')
print('"C:\Windows"')
print("안녕하세요.\n만나서\t\t반갑습니다.")
# # \n =줄바꿈 \t = 탭
# \n = 줄바꿈 \t = 탭
# \n = 줄바꿈 \t = 탭
# \n = 줄바꿈 \t = 탭
# \n = 줄바꿈 \t = 탭
# \n = 줄바꿈 \t = 탭
long = 'python'
print(long[0], long[2])
print(long[0], long[2])
print(long[0], long[2])
print(long[2], long[3])
license_plate = "38구 8247"
print(license_plate[-4:])
phone_number = '01054760926'
print(phone_number[-8:])
today = '20210325'
print(today[-4:])
tring = "홀짝홀짝홀짝"
print(tring[::2])
a = "가나다라마바사아자차카타파하"
print(a[::5])
english = "abcdefghijklmnop"
print(english[::3])
string = "python"
print(string[::-1])
first_name = "kim"
print(first_name[::-2])
# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
phone_number = '010-5476-0926'
phone_number1 = phone_number.replace("-","")
print(phone_number1) #  replace 메서드를 사용하면 문자열을 일부를 치환할 수 있습니다. 
#문자열은 수정할 수 없는 자료형이므로 기존 문자열은 그대로 두고 치환된 새로운 문자열이 리턴됩니다.
license_number = "38구-8247"
license_number1 = license_number.replace("-","")
print(license_number1)
#url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
url = "http://sharebook.kr"
url1 = "http://sharebook.kr".replace("http://sharebook.","")
print(url1)
url_split = url.split('.')
print(url_split[-1])
string = 'abcdfe2a354a32a'
print(string.replace('a','A'))
name = 'kim joo hyeong'
print(name.replace('k','K').replace('j','J').replace('h','H'))
string ='abcd'
string.replace('b','B')
print(string)
# abcd가 그대로 출력됩니다. 왜냐하면 문자열은 변경할 수 없는 자료형이기 때문입니다. 
# replace 메서드를 사용하면 원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴해줍니다.

# 리스트의 연산
a = [1,2,3]
b = [4,5,6]
print(a + b) # 리스트의 덧셈

a = [1,2,3]
b = [4,5,6]
print(a * 2) # 리스트의 곱셈

# print(a - b) print(a / b) 리스트간 뺄셈, 나눗셈을 불가능

# 리스트 길이 구하기
a = [1,2,3,4,5,6,7,123]
b= []
print(len(a))
print(len(b))
# print(a[2]+ "hi") 숫자와 문자는 덧셈 불가
# 리스트 값 수정
a = [1,2,3]
a[1] = 20
print(a)

# a[10] = 10 # 오류 : 인덱스 범위를 벗어남
b = [1,2,3,4,5,6]
b[2]=30
print(b)

#리스트 값 삭제
del b[3]
print(b)
del b[:]
print(b)

#리스트 관련 함수
a = [1,2,3]
a.append(4)
print(a)
a.append([10,20])
print(a) # 리스트 하나가 추가됨

#리스트 정렬
a = [1,4,3,2,-99,100,0]
a.sort() # 오름차순 정렬
print(a)

# 리스트 역순으로 재배치
a = [1,4,3,2]
a.reverse()
print(a)
#내림차순은 따로 없기 때문에 오름차순 정렬 후 역순으로 재배치
a = [1,4,3,2,-99,100,0]
a.sort()
a.reverse()
print(a)

a = [1,4,3,2]
print(a.sort())  #sort()는 정렬만 하고 값을 반환하지 않음(None)

#위치(인덱스 번호) 반환
a =[1,2,3,4]
print(a.index(4))
print(a.index(1))
# print(a.index(100)) # 없는 값을 찾으면 오류 발생
# "abc".find('z') --> -1 ##
# 'abc'.index'('z') --> 오류

# 리스트에 요소 삽입 ##
a = [1,2,3]
a.insert(3, 100)
print(a)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# 리스트 요소 제거 ##
a =[1,2,3,4]
a.remove(2) # 값을 직접 삭제
# a.remove(2) # 값을 직접 삭제 # 오류 : 값이 없음
del a[1] # 2번 인덱스 값을 삭제
print(a)
print('!!!!!')
#리스트 요소 꺼내오기
a = [1,2,3]
print(a.pop())
print(a)

a = [1,2,3]
print(a.pop(1)) # 해당 인덱스의 값 개념

print('~~~~~~~~~~~~~~~~')
# 리스트에 있는 요소의 개수 세기
a = [1,2,3,1]
print(a.count(1))
print(a.count(2))
print(a.count(3))
print(a.count(4))

print('~~~~~~~~~~~~~~~~')

# 조건문
if True:
    print(123)
    print(123)
else:
    print('aaa')

if False:
    print(123)
    print(123)
else:
    print('aaa')
print('~~~~~~~~~~~~~~~~~~~~~~~')
money = True
if money:
     print("택시를 타고 가라")
else:
     print("걸어 가라")

money = False
if money:
         print("택시를 타고 가라")
else:
     print("걸어 가라")
print('~~~~~~~~~~~~~~~~~~~~~~~')

money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

money = 20000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")
print('~~~~~~~~~~~~~~~~~~~~~~~')
#and, or, not
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

card = False
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")
print('~~~~~~~~~~~~~~~~~~~~~~~')
# x in s, x not in s
# "만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라."
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")
print('~~~~~~~~~~~~~~~~~~~~~~~')
pocket = ['paper', 'cellphone', ]
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

pocket = ['money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")
print('~~~~~~~~~~~~~~~~~~~~~~~')
# [조건문에서 아무 일도 하지 않게 설정하고 싶다면?]
# "주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라."
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass 
else:
    print("카드를 꺼내라") # 돈이 있어서 출력 x

pocket = ['paper', 'cellphone']
if 'money' in pocket:
    pass  # 아무것도 하지 말아라(반드시 적어주어야 함)# pass를 지우면 오류
else:
    print("카드를 꺼내라")

print('~~~~~~~~~~~~~~~~~~~~~~~')
# 다양한 조건을 판단하는 elif
# "주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어 가라."
pocket = ['paper', 'handphone']
card = False
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
        print("택시를 타고가라")
    else:
        print("걸어가라")

pocket = ['paper', 'handphone','money']
card = False
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
        print("택시를 타고가라")
    else:
        print("걸어가라")
print('~~~~~~~~~~~~~~~~~~~~~~~')  #elif
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
     print("택시를 타고가라")
elif card: 
     print("택시를 타고가라")
else: # 그 밖의 경우
     print("걸어가라")

print('-' * 20)

'''
수 : 90점 이상
우 : 80점 이상
미 : 70점 이상
양 : 60점 이상
가 : 60점 미만
'''
score = 85
if score >= 90:
    print('수')
elif score >= 80:
    print('우')
elif score >= 70:
    print('미')
elif score >= 60:
    print('양')
else: 
    print('가')
print('-' * 60)
score = 85
if score >= 90:
    print('수')
if score >= 80:
    print('우')
if score >= 70:
    print('미')
if score >= 60:
    print('양')
else: 
    print('가')
print('-' * 60)
score = 100
if score >= 90:
    print('수')
if score >= 80:
    print('우')
if score >= 70:
    print('미')
if score >= 60:
    print('양')
else: 
    print('가')

print('-' * 60)
score = 80
if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)

# 조건부 표현식
score = 59
message = "success" if score >= 60 else "failure"
print(message)
print('-' * 60)
# Up& Down 게임
'''
correct 1~10 사이의 정수 값 : 5
1 --> Up 정답이 응답보다 크면 Up 출력
7 --> Down 정답이 응답보다 작으면 Down 출력
5 --> Correct 정답이 응답과 같으면 Correct 출력
'''
Correct = 5
Answer = 2
if Correct > Answer:
    print("Up")
elif Correct < Answer:
    print("Down")
elif Correct == Answer:
    print("Coorect")
print('-' * 60)
#2단계
# Correct = 5 # 정답
# Answer = int(input('숫자입력'))  #input결과는  
# if Correct > Answer:
#     print("Up")
# elif Correct < Answer:
#     print("Down")
# elif Correct == Answer:
#     print("Coorect")
