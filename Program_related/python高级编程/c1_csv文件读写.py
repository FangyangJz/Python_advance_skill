import csv

with open('demo.csv','w') as f:
    writer = csv.writer(f, delimiter=' ')
    writer.writerow(['x', 'y', 'z'])
    writer.writerow([1,2,3])
    writer.writerow([4,5,6])

with open('demo.csv') as f:
    reader = csv.reader(f)  # 这里返回的是个可迭代对象
    headers = next(reader)
    print(headers)
