1.py
#열기
#file = open("c:\\test_c\\test01.txt","w") #쓰기모드
file = open("c:\\test_c\\test01.txt","a") #추가모드

#작업
#print(file)
file.write("김인하\n")
file.write("컴퓨터정보\n")
file.write("1학년\n")
file.write("이인하|컴퓨터시스템|2학년\n")

#닫기
file.close()

2.py
file = open("c:\\test_c\\test02.txt","w")

scores = {"math": 90, "kor": 100, "eng": 40}
for k,v in scores.items():
    data = f"{k},{v}\n"
    file.write(data)

file.close()

3.py
file = open("c:\\test_c\\test01.txt","r")


#1
# while True:
#     line = file.readline()
#     if not line:
#         break
#     line = line.strip
#     print(line)

#2
# lines = file.readlines()
# print(lines)
# lines = [v.strip() for v in lines]

#3
datas = file.read()
print(datas)


file.close()

4.py
scores = [
    ["김인하", "2", "컴퓨터정보"],
    ["이인하", "1", "컴퓨터시스템"],
    ["박인하", "3", "컴퓨터정보"]
]

with open("c:\\test_c\\test03.txt","w") as file:  #이건 간편한 방법이지만 파이썬에서만 가능, with로 오픈하면 close 안써도 됨
#file = open("c:\\test_c\\test03.txt","w") #이게 전통적인 방식
    for score in scores:
        file.write("|".join(score) + "\n")
    #file.close()

file = open("c:\\test_c\\test03.txt","r")
result = []

for line in file:
    result.append(line.strip().split("|"))

file.close()
