import random
import string

acc_num = ''.join([random.choice(string.digits) for n in range(10)])

print(acc_num)