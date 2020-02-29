from faker import Faker

myfake = Faker()

# Faker의 메소드를 통해 어떤 종류의 가짜데이터를 뽑아낼지 결정 가능

Faker.seed(1)

print(myfake.name()) #가짜 이름
print(myfake.address()) #가짜 주소
#print(myfake.text())
#print(myfake.state())
#print(myfake.sentence())
print(myfake.random_number(1))
