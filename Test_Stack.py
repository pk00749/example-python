from pythonds.basic.stack import Stack

def operator_priority(formula):
    result_set = []
    operator_list = Stack()
    operator = {'+': 2, '-': 2, '*': 3, '/': 3, '(':1,')':1}

    for element in formula:
        if element in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or element in ('1234567890'):
            result_set.append(element)  # 操作数放入列表
        elif element == '(':
            operator_list.push(element)
        elif element == ')':
            top_of_list = operator_list.pop()
            while top_of_list != '(':
                result_set.append(top_of_list)
                top_of_list = operator_list.pop()
        else:
            while (not operator_list.isEmpty()) and (operator[operator_list.peek()] >= operator[element]):
                print(operator_list.peek())
                print(operator[element])
                result_set.append(operator_list.pop())
            operator_list.push(element)

    while not operator_list.isEmpty():
        result_set.append(operator_list.pop())

    return result_set

print(operator_priority('A+B'))
