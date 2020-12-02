print('Welcome --------------------------------------------------------------------------')
print('provide comma separated list of numbers to find out two numbers which sum to 2020, I will then return multiplication of those two numbers.')

nums = input('?\n')

list_of_nums = nums.split(',')

for num in list_of_nums:
    for innum in list_of_nums:
        if num != innum:
          if (int(num) + int(innum)) == 2020:
            print(int(num) * int(innum))
            list_of_nums.remove(num)
            list_of_nums.remove(innum)