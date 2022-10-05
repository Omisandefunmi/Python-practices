num_list = []
playing = True
i = 0

while playing:
    num = int(input("Enter an integer or -1 to end: "))
    if num == -1:
        playing = False
    else:
        num_list.append(num)
        i += 1
num_sum = 0
for num in num_list:
    num_sum += num

average = num_sum / i
print("The average of ", num_list, "is ", average)


x = 0
while x <= 5:
    if x == 4:
        break
    print(x)
    x += 1



