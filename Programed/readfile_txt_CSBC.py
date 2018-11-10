import os
import re
import csv
import pandas as pd

def strB2Q(ustring):
    """把字符串半角转全角"""
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code<0x0020 or inside_code>0x7e:      #不是半角字符就返回原来的字符
            rstring += uchar
        if inside_code==0x0020: #除了空格其他的全角半角的公式为:半角=全角-0xfee0
            inside_code=0x3000
        else:
            inside_code+=0xfee0
        rstring += chr(inside_code)
    return rstring


def strQ2B(ustring):

    rstring = ""

    for uchar in ustring:
        inside_code = ord(uchar)

        if inside_code == 12288:
            inside_code = 32

        elif (inside_code >= 65281 and inside_code <= 65374):
            inside_code -= 65248

        rstring += chr(inside_code)

    return rstring

'''
open函數
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
'''

data = open('C:/Users/ASIA-I627-A/Desktop/Data.csv', 'w')

csvwriter = csv.writer(data)

# 將我們要的表頭先寫出來
csvwriter.writerow(["Article_ID", "NE_Type", "Position","Length","Text"])


root =('C:Users/ASIA-I627-A/Desktop/demo_txt')

# 讀出所有txt檔並在前面加上路徑，放入list
file_ob_list = []  #放入完整的txt檔路徑,讀取用
film_name_list = [] #只有txt檔的檔名,顯示答案時只要檔名

# 读取文件夹下txt的文件名
file_names = os.listdir(root)
for i in file_names:

    # 循环读取路径下的文件并筛选输出

    if os.path.splitext(i)[1] == ".txt":

    # 在路徑後加上檔名
        fileob = root + '/' + i

        # append函數是將檔名放進list的函數
        file_ob_list.append(fileob)
        film_name_list.append(i)

# #
#
character_lower_list = []
#放原文
character_list = []

# 將txt檔讀出後，分別將小寫及原文各放入list
for a in file_ob_list:
    total = open(a).read()

    character_lower_list.append(strB2Q(str.lower(total))) # 小寫

    character_list.append(strB2Q(total)) #原文

data_mathon={'text_id':film_name_list,'mathon_lower':character_lower_list,'mathon':character_list}

txt_frame = pd.DataFrame(data_mathon)
