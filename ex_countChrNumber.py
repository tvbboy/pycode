instr = input('please input char:')
upper, lower, digit, other = 0, 0, 0, 0
for c in instr:
    if c >= 'A' and c <= 'Z':
        upper = upper+1
    elif c >= 'a' and c <= 'z':
        lower = lower+1
    elif c >= '0' and c <= '9':
        digit = digit+1
    else:
        other = other+1
print('大写字母{}个，小写字母{}个，数字{}个，其他字符{}个'.format(upper, lower, digit, other))
