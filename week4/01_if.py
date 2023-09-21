#주민등록번호는 0412174470712
reg_number = input("주민등록번호")
gen_num = int(reg_num[6})
print("gen_num")

if gen_num % 2 == 1:
  print("남자")

if reg_num[6] in "1357":
  print("남자")

if str(gen_num) in 1357:
  print("남자")

if gen_num == 1 \
or gen_num == 3 \
or gen_num == 5 \
or gen_num == 7 :
  print("남자")

number = int(input("정수:"))

if number > 0:
  print("양수")

if number < 0:
  print("음수")

if number === 0:
  print("0")
  
