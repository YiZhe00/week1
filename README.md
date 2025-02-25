# week1
"""学生管理系统"""
class_all = []

#功能选择界面
def print_menu():
    print('------------------------')
    print(' 1:添加学生信息')
    print(' 2:查找学生信息')
    print(' 3:修改学生信息')
    print(' 4:删除学生信息')
    print(' 5:显示所有学生信息')
    print(' 6:保存学生信息')
    print(' 7:从文件中读取学生信息')
    print('------------------------')

#功能1
def add_student() :
    global class_all
    number = input('输入学生学号:')
    name = input('输入学生姓名:')
    score_1 = input('输入数学成绩:') 
    score_2 = input('输入英语成绩:')
    score = []
    score.append(score_1)
    score.append(score_2)
    for judement in class_all:
        if judement['学号'] == number:
            print("学号重复，请重新输入")
            return
    student = {
        '学号': number ,
        '姓名': name ,
        '成绩': score ,
    }
    class_all.append(student)
    print('添加成功！')

#功能2
def search_student():
    global class_all
    a = input('请输入要查找的姓名或学号:')
    for judgement in class_all :
        if judgement['姓名'] == a or judgement['学号'] == a :
            print('学号:%s,姓名:%s,成绩:%s'%(judgement['学号'],judgement['姓名'],judgement['成绩']))
            return
        print('您输入的学生信息不存在')

#功能3
def update_student():
    global class_all
    a = input('请输入要修改的学生学号:')
    for judgement in class_all :
        if judgement['学号'] == a :
            score_list = judgement['成绩']
            judgement['姓名'] = input('请输入修改后的学生姓名:')
            score_list[0] = input('请输入修改后的数学成绩:')
            score_list[1] = input('请输入修改后的英语成绩:')
            print('修改成功！')
            return
        print('您输入的学生信息不存在')

#功能4
def del_student():
    global class_all
    a = input('请输入要删除的学生学号:')
    for judgement in class_all :
        if judgement['学号'] == a :
            class_all.remove(judgement)
            print('删除学生信息成功！')
            return
        print('您输入的学生信息不存在')

#功能5
def show_student():
    global class_all
    for student in class_all :
        score = student['成绩']
        score_1 = score[0]
        score_2 = score[1]
        print('学号:',student['学号'],',姓名',student['姓名'],',成绩:[数学:',score_1,',英语:',score_2,']')

#功能6
def cumpute_student():
    global class_all
    sum_1=0
    sum_2=0
    n=0
    list1=[]
    list2=[]
    for student in class_all :
        score = student['成绩']
        sum_1=sum_1+int(score[0])
        sum_2=sum_2+int(score[1])
        n=n+1
    print('数学平均分：',sum_1/n,'英语平均分：',sum_2/n)
    for student in class_all :
        score1 = student['成绩']
        list1.append(int(score1[0]))
        list2.append(int(score1[1]))
    print('数学最高分:',max(list1),'英语最高分:',max(list2))
    print('数学最低分:',min(list1),'英语最低分:',min(list2))

#功能7
def save_student():
    with open("student.txt", "w") as file:
        file.write(str(class_all))
    print('保存成功！')

#功能8
def read_student():
    with open("student.txt", "r") as file:
        content = file.read()
        class_all.append(content)
        print("读取成功！")

#实现函数
def main():
    while True :
        print_menu()
        choose = int(input('请选择所需功能: '))
        if choose == 1:
            add_student()
        elif choose == 2:
            search_student()
        elif choose == 3:
            update_student()
        elif choose == 4:
            del_student()
        elif choose == 5:
            show_student()
        elif choose == 6:
            cumpute_student()
        elif choose == 7:
            save_student()
        elif choose == 8:
            read_student()

main()
