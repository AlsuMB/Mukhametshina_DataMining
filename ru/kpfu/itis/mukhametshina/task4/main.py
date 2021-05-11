import hashlib

from ru.kpfu.itis.mukhametshina.task4.db import CBFs

cbf_class = CBFs(10, 3, 100, false_positiveP=0.1)
#
cbf_class.add("qwerty123")
cbf_class.add("1")
cbf_class.add("2")
cbf_class.add("3")
cbf_class.add("4")
cbf_class.add("5")
cbf_class.add("6")
cbf_class.add("7")
cbf_class.add("8")
cbf_class.add("9")

library = ['qwerty123', '1', '0', '-1', '-1', '2', '3', '-3', 'qwerty', '123']
for i in library:
    print(f'Is exist {i} in CBF? {cbf_class.is_exist(i)}')
