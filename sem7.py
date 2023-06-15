# 1).

text=input().lower().split()
lowers='аоуыэеёиюяи'
res=set()

for word in text:
    count=0
    for i in word:
        if i in lowers:
            count+=1
    res.add(count)
    print(res)
        
if len(res)==1:
    print('Парам пам пам')
else:
    print('Парам пам')

# 2).

def print_operation_table(operation, num_rows=6, num_columns=6):
    print('       '.join([str(i) for i in range(1, num_columns + 1)]))
    for i in range(2, num_rows + 1):
        print(i, end=' \t')
        for c in range(2, num_columns + 1):
            print(operation(i, c), end=' \t')
        print()

print_operation_table(lambda x, y: x * y)

