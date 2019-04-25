array = [100, 99, 96, 97, 95, 94, 93]
array2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]


class Sort:
    def __init__(self):
        self.lst = []

    def sort(self, lst, s_type):
        self.lst = lst

    def bubble(self):
        changed = False
        for x in range(1, len(self.lst)):
            for y in range(len(self.lst) - x):
                if self.lst[y] < self.lst[y + 1]:
                    changed = True
                    temp = self.lst[y + 1]
                    self.lst[y + 1] = self.lst[y]
                    self.lst[y] = temp
            if changed is False:
                break

    def selection(self):
        for x in range(len(self.lst) - 1, 0, -1):
            counter = 0
            for y in range(1, x + 1):
                if self.lst[y] > self.lst[counter]:
                    counter = y
            temp_val = self.lst[x]
            self.lst[x] = self.lst[counter]
            self.lst[counter] = temp_val

    def insertion(self):
        for x in range(1, len(self.lst)):
            current = self.lst[x]
            pos = x
            while pos > 0 and self.lst[pos - 1] > current:
                self.lst[pos] = self.lst[pos - 1]
                pos -= 1
            self.lst[pos] = current

    def merge(self, tlst=[]):
        if len(self.lst) > 1:
            mid = len(self.lst) // 2
            left = self.lst[:mid]
            right = self.lst[mid:]
            Sort.merge(self, left)
            Sort.merge(self, right)
            i = 0
            j = 0
            k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    self.lst[k] = left[i]
                    i += 1
                else:
                    self.lst[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                self.lst[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                self.lst[k] = right[j]
                j += 1
                k += 1


def bubble(lst):
    changed = False
    for x in range(1, len(lst)):
        for y in range(len(lst)-x):
            if lst[y] < lst[y+1]:
                changed = True
                temp = lst[y+1]
                lst[y+1] = lst[y]
                lst[y] = temp
        if changed is False:
            break
    print('Bubble Sort:', lst)


def selection(lst):
    for x in range(len(lst)-1, 0, -1):
        counter = 0
        for y in range(1, x+1):
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
    print('Insertion Sort:', lst)


def quick(lst):
    quick_helper(lst, 0, len(lst)-1)
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
        mid = len(lst)//2
        if lst[mid] == item:
            return True
        else:
            if item < lst[mid]:
                return binary_search(lst[:mid], item)
            else:
                return binary_search(lst[mid + 1:], item)


def merge(lst):
    if len(lst) > 1:
        mid = len(lst)//2
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
        print('Merge Sort:', lst)


merge(array2)
bubble(array)
selection(array2)
insertion(array)
quick(array2)
print(binary_search(array2, 102))
