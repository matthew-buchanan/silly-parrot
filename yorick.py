import re
from collections import Counter
text = open("hamlet.txt").read()
ham_count = Counter(re.findall(r"H[Aa][Mm]\w+", open("hamlet.txt").read()))

yam_one = re.sub(r"HAM", r"YAM", text)
yam_two = re.sub(r"Ham", r"Yam", yam_one)
open('yamlet.txt', 'w').write(yam_two)
yam_count = Counter(re.findall(r"Y[Aa][Mm]\w+", open("yamlet.txt").read()))
print("\nHamlet:{}\nYamlet:{}".format(ham_count, yam_count))