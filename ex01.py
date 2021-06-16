year = input("请输入年份")
month = input("请输入月份")
day = input("请输入日期")
if int(year) % 4 == 0:
    feb = 29
else:
    feb = 28
days_list = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = 0

for i in range(int(month) - 1):
    days += days_list[i]
days += int(day)
print(days)
