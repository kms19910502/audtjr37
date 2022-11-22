class Person:
    name=""
    id=""
    age=0
    height=0
    weight=0

    def __init__(self,name,id,age,height,weight):
        self.name = name
        self.id= id
        self.age = age
        self.height = height
        self.weight = weight
        
    def __str__(self):
        return "이름: " + self.name +  "  나이: " + str(self.age) + "  키: " + str(self.height) + "  몸무게: " + str(self.weight)
    






def main():
    manyperson = [Person("을지문덕","1",20,60,174),Person("계백","2",23,80,194),Person("김유신","3",18,59,174),Person("강감찬","4",25,78,180),Person("이순신","5",24,67,184)]
    for i in range(0,5):
        print(manyperson[i])


if  __name__ == "__main__":
    main()