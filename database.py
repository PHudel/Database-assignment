available_commands = ['A', 'D', 'M']
available_courses = ['ART', 'COMPSCI', 'ENGLISH', 'FRENCH', 'HISTORY', 'MATH', 'MUSIC']
layout = ['num', 'alpha', 'alpha', 'alpha', 'alpha', 'num', 'alpha', 'num', 'alpha', 'num']
commands = []
objects = {}
master = []
f1 = open('transaction.txt', 'w')
f3 = open('error.txt', 'w')


class Student:
    def __init__(self):
        self.id_num = 0
        self.f_name = ''
        self.l_name = ''
        self.name = ''
        self.courses = [['null', -1], ['null', -1], ['null', -1]]
        self.average = 0
        self.report = ' '

    def create(self, id_num, l_name, f_name):
        self.id_num = id_num
        self.f_name = f_name
        self.l_name = l_name
        self.name = self.f_name + ' ' + self.l_name

    def get_average(self):
        total = 0
        numcourses = 0
        for x in range(3):
            if self.courses[x][1] != -1:
                total += self.courses[x][1]
                numcourses += 1
        if numcourses > 0:
            self.average = int(total/numcourses)
        else:
            self.average = -1

    def display(self):
        print('ID Number: ', self.id_num)
        print('Name: ', self.name)
        print('Courses: ', self.courses)
        print('Average: ', self.average)

    def generate_report(self):
        for c in self.courses:
            for i in range(7):
                if c[0] == available_courses[i]:
                    courses[i].students.append([self.id_num, c[1]])
        self.get_average()
        self.report = 'ID: %s   Name: %s %s         Courses: %s           Average: %s\n' % (self.id_num, self.f_name, self.l_name, self.courses, self.average)
        return self.report
    

class Course:
    def __init__(self):
        self.students = []
        self.average = 0

    def display(self):
        print('Students:')
        print(self.students)

    def sort(self):
        for x in range(1, len(self.students)):
            current = self.students[x][1]
            pos = x
            while pos > 0 and self.students[pos - 1][1] < current:
                self.students[pos][1] = self.students[pos - 1][1]
                pos -= 1
                self.students[pos][1] = current

    def getaverage(self):
        c = 0
        total = 0
        for x in self.students:
            total += x[1]
            c += 1
        self.average = int(total/c)
        return self.average


def bubble(lst):
    changed = False
    for x in range(1, len(lst)):
        for y in range(len(lst) - x):
            if lst[y] < lst[y + 1]:
                changed = True
                temp = lst[y + 1]
                lst[y + 1] = lst[y]
                lst[y] = temp
        if changed is False:
            break
    print('Bubble Sort:', lst)


def selection(lst):
    for x in range(len(lst) - 1, 0, -1):
        counter = 0
        for y in range(1, x + 1):
            if lst[y] > lst[counter]:
                counter = y
        temp_val = lst[x]
        lst[x] = lst[counter]
        lst[counter] = temp_val
    print('Selection Sort:', lst)


def insertion(lst):
    for x in range(1, len(lst)):
        current = lst[x]
        pos = x
        while pos > 0 and lst[pos - 1] > current:
            lst[pos] = lst[pos - 1]
            pos -= 1
        lst[pos] = current
    return lst


def quick(lst):
    quick_helper(lst, 0, len(lst) - 1)
    print('Quick Sort:', lst)


def quick_helper(lst, first, last):
    if first > last:
        split = quick_body(lst, first, last)
        quick_helper(lst, first, split - 1)
        quick_helper(lst, split + 1, last)


def quick_body(lst, first, last):
    pivot = lst[first]
    left = first + 1
    right = last
    done = False

    while not done:
        while left <= right and lst[left] <= pivot:
            left += 1

        while lst[right] >= pivot and right >= left:
            right -= 1

        if right < left:
            done = True
        else:
            temp = lst[left]
            lst[left] = lst[right]
            lst[right] = temp

    temp = lst[first]
    lst[first] = lst[right]
    lst[right] = temp
    return right


def initialize(file, file2, file3):
    lines = []
    with open(file) as f, open(file2) as f4, open(file3) as f5:
        lines.append(f.readlines())
        lines.append(f4.readlines())
        lines.append(f5.readlines())
    for x in lines:
        for y in x:
            y = y.strip()
            commands.append(y.split(','))

    for x in commands:
        correct = 0
        for c in range(len(x)):
            x[c] = x[c].replace(' ', '')
            if c < 10:
                if layout[c] == 'num':
                    if x[c].isdigit() or x[c] == '':
                        correct += 1
                if layout[c] == 'alpha':
                    if x[c].isalpha() or x[c] == '':
                        correct += 1

            if x[c].isalpha() is True:
                x[c] = x[c].upper()

        if x[1] in available_commands:
            if len(x) <= 10:
                if correct is len(x):
                    if len(x) > 3:
                        if x[1] == 'A':
                            if x[1].isalpha and x[2].isalpha():
                                add(x)
                            else:
                                f3.write('ERROR: names missing   %s \n' % x)
                        elif x[1] == 'M':
                            modify(x)
                        else:
                            delete(x)
                    elif len(x) == 2:
                        delete(x)
                else:
                    f3.write('ERROR: not all alpha fields = alpha   %s \n' % x)
            else:
                f3.write('ERROR: too many fields   %s \n' % x)
        else:
            f3.write('ERROR: Invalid command   %s \n' % x)


def add(lst):
    iserror = False
    c2 = 0
    c3 = 0
    id_num = lst[0]
    id_address = lst[0][4:]
    if int(id_address) not in objects:
        id_address = Student()
        if len(lst) > 4:
            for c in range(4, len(lst), 2):
                if lst[c] in available_courses:
                    id_address.courses[c2][0] = lst[c]
                else:
                    iserror = True
                c2 += 1
            for l in range(5, len(lst), 2):
                if lst[l] != '':
                    id_address.courses[c3][1] = int(lst[l])
                c3 += 1
        if iserror is False:
            id_address.create(lst[0], lst[2], lst[3])
            objects[int(id_num[4:])] = id_address
            objects[id_address.l_name] = id_address
            f1.write('User added: %s \n' % lst[0])
        else:
            f3.write('ERROR: Invalid course   %s \n' % lst)
    else:
        f3.write('ERROR: User already exists   %s \n' % lst)


def modify(lst):
    c = 0
    c1 = 0
    idnum = int(lst[0][4:])
    if idnum in objects and objects[idnum] != 'DELETED':
        for m in range(5, len(lst), 2):
            if lst[m] != '':
                objects[idnum].courses[c][1] = int(lst[m])
            c += 1
        for n in range(4, len(lst), 2):
            if lst[n] != '':
                objects[idnum].courses[c1][0] = lst[n]
            c1 += 1
        f1.write('User modified: %s \n' % lst[0])
    else:
        f3.write('ERROR: User doesnt exist   %s \n' % lst)


def delete(lst1):
    id = int(lst1[0][4:])
    if id in objects and objects[id] != 'DELETED':
        temp = objects[int(id)].l_name
        objects[temp] = 'DELETED'
        objects[int(id)] = 'DELETED'
        f1.write('User deleted: %s \n' % lst1[0])
    else:
        f3.write('ERROR: User doesnt exist   %s \n' % lst1)


def report():
    f1.close()
    f3.close()
#prints all students to the master file in alpha order with all information---------------------------------------------
    with open('master.txt', 'w') as f2:
        for k in objects:
            if isinstance(k, str) and objects[k] != 'DELETED':
                master.append(objects[k].l_name)
        insertion(master)
        for m in master:
            f2.write(objects[m].generate_report())
        f2.write('\n')
#prints each class in alpha order each with all students sorted by mark-------------------------------------------------
        for c in range(7):
            f2.write('\n')
            f2.write(available_courses[c] + ':' + '\n')
            courses[c].sort()
            for s in courses[c].students:
                f2.write(objects[int(s[0][4:])].name + '   Mark: ' + str(s[1]) + '\n')
            f2.write('Course Average: %s \n' % str(courses[c].getaverage()))
        f2.write('\n')
#Prints out all students failing to master file in alpha order----------------------------------------------------------
        f2.write('\n')
        f2.write('Students Failing: \n')
        for f in master:
            templist = []
            doreport = False
            templist.append(objects[f].name + ' ')
            for course in objects[f].courses:
                if 0 <= course[1] < 50:
                    templist.append(course[0])
                    templist.append(' ')
                    templist.append(str(course[1]))
                    templist.append(' ')
                    doreport = True
            if doreport is True:
                f2.write(''.join(templist))
                f2.write('\n')


courses = [Course() for i in range(7)]
initialize('BATCH1.txt', 'BATCH2.txt', 'BATCH3.txt')
report()
while True:
    search = input('Enter a user search or -1 to exit')
    if search in objects or int(search) in objects:
        if search.isalpha():
            objects[search].display()
        else:
            objects[int(search)].display()
    elif search == -1:
        exit('Program terminated')
    else:
        print('User does not exist')
