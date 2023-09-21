number = int(input("정수:"))

if number > 0 :
  print("양")
else if number < 0 :
  print("음")
else :
  print("0")

if number > 0:
  print("양수")
else:
  if number < 0:
    print("음수")
  else:
    print("0")

reg_num = input("주민등록번호")
gen_num = int(reg_num[0])

if gen_num % 2 == 1:
  print("남자")
else:
  print("여지")
