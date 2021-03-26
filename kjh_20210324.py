'''
다음의 문자열을 year, month, day, weather 로
나누어 각각 출력해보세요.
'''
a = '20210323Sunny'

print (a[0:4])
print (a[4:6])
print (a[6:8])
print (a[8:13])


a = '20210323Cloudy'
print (a[:4])
print (a[4:6])
print (a[6:8])
print (a[8:])

# 문자열 포맷팅
'''
%d: 정수형
%s: 문자열/숫자형 모두 가능
'''
# 'I eat 3 apples' 만들기
print (' I eat %d apples' % 5)
print('_________________')
# # 2개 이상의 값 넣기
# 'I ate 10 apples. so I was sick for three days.' 만들기
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))
#print("I eat %d apples." % 'four') # TypeError : %d 자리에는 숫자만 입력 가능
# I eat 3 apples.
# I eat 5 apples. 문장 만들기
'''
%d: 정수형
%s: 문자열/숫자형 모두 가능
'''
# print("I eat %d apples" %3)
# print("I eat %d apples" %5)

# print("I eat %s apples." % 'four')
# print("I eat %s apples." % 5)

# number = 10
# day = "three"
# print("I ate %d apples. so I was so sick for %s days."% (5, 'three'))
# print("I ate %d appls. so I was sick for %s days"%(5,3))

# print("Error is %d%%" %98) # %글자 출력시 %%사용
# format 함수를 이용한 포맷팅
# print("I ate {0} apples".format(3))
# print("I ate {0} apples".format(4))
# print("I ate {0} apples".format(5))
#문자열 함수 + format 함수 혼합
#2개 이상의 값 넣기
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))
#이름으로 넣기
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))
#  {name} 형태를 사용할 경우 format 함수에는 반드시 name=value 와 같은 형태의 입력값이 있어야만 한다. 
# 위 예는 문자열의 {number}, {day}가 format 함수의 입력값인 number=10, day=3 값으로 각각 바뀌는 것을 보여 주고 있다.
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))
# 인덱스 항목과 name=value 형태를 혼용하는 것도 가능하다.

# 문자열 포맷팅(f-string)
# 파이썬 3.6 버전부터는 f 문자열 포매팅 기능을 사용할 수 있다. 
# 파이썬 3.6 미만 버전에서는 사용할 수 없는 기능이므로 주의해야 한다.
# 다음과 같이 문자열 앞에 f 접두사를 붙이면 f 문자열 포매팅 기능을 사용할 수 있다.
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
# f 문자열 포매팅은 표현식을 지원하기 때문에 다음과 같은 것도 가능하다.
age = 30
print(f'나는 내년이면 {age+1}살이 된다.')

# 문자열 자료형은 자체적으로 함수를 가지고 있다. 
# 이들 함수를 다른 말로 문자열 내장 함수라 한다.
#  이 내장 함수를 사용하려면 문자열 변수 이름 뒤에 ‘.’를 붙인 다음에 함수 이름을 써주면 된다. 
# 이제 문자열의 내장 함수에 대해서 알아보자.
''' 문자 개수 세기(count)'''
a = "hobby"
print(a.count('b'))
'''위치 알려주기1(find)'''
a = "Python is the best choice"
print(a.find('b')) # 문자열 중 문자 b가 처음으로 나온 위치를 반환한다.
                   # 파이썬은 숫자를 0부터 세기 때문에 b의 위치는 15가 아닌 14가 된다.
print(a.find('x')) # 만약 찾는 문자나 문자열이 존재하지 않는다면 -1을 반환한다.
'''위치 알려주기2(index)'''
a = "Life is too short"
print(a.index('t')) # 문자열 중 문자 t가 맨 처음으로 나온 위치를 반환한다.
'''print(a.index('k'))''' # 만약 찾는 문자나 문자열이 존재하지 않는다면 오류를 발생시킨다
'''문자열 삽입(join)'''
print(','.join('abcd')) #''사이에 ,넣기
print('/'.join('abcd')) #''사이에 /넣기
print(''.join('a')) # ''사이에 지정 글자 넣기
print('\n'.join('abcd')) # 줄바꿈으로 한글자씩 넣기
# 소문자 --> 대문자
a ="hi"
print(a.upper())
# 대문자 --> 소문자
a = 'HELLO'
print(a.lower())

a = 'Hello Python'
print(a.upper())
print(a.lower())
# 공백 지우기
a = '         hi         '
print(a)            
print(a.lstrip())   # 왼쪽 공백 제거
print(a.rstrip())   # 오른쪽 공백 제거
print(a.strip())    # 양쪽 공백 제거

a = '         Hello Python       '
print(a.strip())   
print(a.lstrip())  
print(a.rstrip())




                   


