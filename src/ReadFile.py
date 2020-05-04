

file = open('C:\\Users\\kunning\\Documents\\2.txt', 'r') # r表示是文本文件，rb是二进制文件。（这个mode参数默认值就是r）
# 方法1
line = file.readline()             # 调用文件的 readline()方法
while line:
    print(line, end = '') # 后面跟 ',' 将忽略换行符
    line = file.readline()

# 方法2
file = open(r'C:\Users\kunning\Documents\2.txt', 'r')
for line in file:
    print(line,)

# 方法3
file = open(r'C:\Users\kunning\Documents\2.txt', 'r')
lines = file.readlines()#读取全部内容
for line in lines:
    print(line)
file.close()
