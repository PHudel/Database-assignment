import pickle
names = []
names2 = []
names3 = []
names4 = []
names5 = []
names6 = []
dict = {}
dict1 = {}
with open('NAMES.txt') as f:
    temp = f.readlines()
for x in temp:
    names.append(x.strip())
    names2.append(x.strip())
    names3.append(x.strip())
    names4.append(x.strip())
    names5.append(x.strip())
    names6.append(x.strip())

for y in range(len(names)):
    dict[y] = names[y]
    dict1[str(y)] = names[y]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new):
        self.data = new

    def set_next(self, new):
        self.next = new


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp_item = Node(item)
        temp_item.set_next(self.head)
        self.head = temp_item

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


def bubble(lst):
    changed = False
    for z in range(1, len(lst)):
        for y in range(len(lst) - z):
            if lst[y] < lst[y + 1]:
                changed = True
                temp_num = lst[y + 1]
                lst[y + 1] = lst[y]
                lst[y] = temp_num
        if changed is False:
            break
    return lst


def selection(lst):
    for x in range(len(lst) - 1, 0, -1):
        counter = 0
        for y in range(1, x + 1):
            if lst[y] > lst[counter]:
                counter = y
        temp_val = lst[x]
        lst[x] = lst[counter]
        lst[counter] = temp_val
    return lst


def insertion(lst):
    for x in range(1, len(lst)):
        current = lst[x]
        pos = x
        while pos > 0 and lst[pos - 1] > current:
            lst[pos] = lst[pos - 1]
            pos -= 1
        lst[pos] = current
    return lst


def merge(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        merge(left)
        merge(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
        #print('Merge Sort:', lst)


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


def binary_search(lst, item):
    if len(lst) == 0:
        return False
    else:
        mid = len(lst) // 2
        if lst[mid] == item:
            return True
        else:
            if item < lst[mid]:
                return binary_search(lst[:mid], item)
            else:
                return binary_search(lst[mid + 1:], item)


my_list = UnorderedList()
for x in names:
    my_list.add(x)
print(my_list.size())
print(my_list.search('PETER'))


merge(names3)
print('Unsorted:', names)
print('Bubble Sort:', bubble(names2))
print('Merge Sort:', names3)
print('Selection Sort:', selection(names4))
print('Insertion Sort:', insertion(names5))
quick(names6)
print(binary_search(names4, 'FRED'))
print(binary_search(names4, 'MEMES'))
print('Integer keys:', dict)
print('String Keys:', dict1)


with open('Pickle.txt', 'wb') as f:
    pickle.dump(dict, f)
