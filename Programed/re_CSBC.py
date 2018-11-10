import re

###################################################################################
###################################################################################
# '''
# sub(repl, string[, count])
# 如果 repl 是字符串，則會使用 repl 去替換字符串每一個匹配的子串，並返回替換後的字符串，另外，repl 還可以使用 \id 的形式來引用分組，但不能使用編號 0；
# 如果 repl 是函數，這個方法應當只接受一個參數（Match 對象），並返回一個字符串用於替換（返回的字符串中不能再引用分組）。
# '''
#
# # txt = "123&%#@!()happy word"
# #
# # # 用234取代掉123,若要刪除他,函數第二個欄位不要給值
# # print(re.sub('123', '234', txt))
#
# '''
# '.'
# 匹配除「\n」之外的任何單個字符
# 例： a.c 匹配 abc1234 => abc
#
# '^'
# 匹配輸入字串的開始位置
# 設定 RegExp 物件的 Multiline 屬性，可匹配「\n」或「\r」之後的位置
# 例： ^ab 匹配 abc1234 => ab
#
# '$'
# 匹配輸入字串的結束位置
# 設定 RegExp 物件的 Multiline 屬性，可匹配「\n」或「\r」之前的位置
# 例： 34$ 匹配 abc1234 => 34
#
# '*'
# 匹配至少零次
# 例： ac* 匹配 abc1234 => a
#
# '+'
# 匹配至少一次
# 例： ab.+ 匹配 abc1234 => abc1234
#
# '?'
# 匹配零次或一次
# 例： ab? 匹配 abc1234 => ab
#
# '*?' '+?' '??'
# 匹配模式是 non-greedy，符合的最少字串，預設為 greedy
# 可用在（*，+，?，{n}，{n,}，{n,m}）後面
# 例： a+? 匹配 aaaaa => a
#
# {m}
# 匹配 m 次
# 例： a{3} 匹配 aaaaa => aaa
#
# {m,n}
# 匹配次數介於 m & n 之間，省略 n 表示無限次
# 例： a{1,3} 匹配 aaaaa => aaa
#
# '\'
# 使用限制字元
# 例： a\+ 匹配 a+aaaa => a+
#
# []
# 匹配字元集合
# - 表示從某字元到某字元，例：[a-z]
# ^ 表示排除字元，例：[^a-z]，需放置最前面，不然當作字元 '^'
# 例： [a\-z]b 匹配 a-baaa => -b
#
# '|'
# 或
# 例： (a|b)aa 匹配 a-baaa => baa
#
# (...)
# 取得匹配的子字串，並放進 group
# 例： (a|b)aa 匹配 a-baaa => baa, \1 = b (match.group(0) = baa, match.group(1) = b)
#
# (?aiLmsux)
# 指定匹配方式
# (?a) 讓 \w, \W, \b, \B, \d, \D, \s and \S 只依 ASCII 匹配
# (?i) 忽略大小寫
# (?L) 讓 \w, \W, \b, \B, \s and \S 依本地字符編碼 (Python 3.6 已被移除)
# (?m) ^ $ 匹配不同行的頭和尾
# (?s) '.' 匹配全部，包括 \n
# (?u) unicode 匹配 (Python 3 已移除，預設已為 unicode 匹配)
# (?x) 忽略空白字符，且可以用 # 當作註解，可多行建立 pattern，利用 """abc string"""
# 例： (?x)t es #測試 匹配 test => tes
# 可同時使用，例：(?imx)^aa 匹配 a-bA\n#AA => None 因 AA 被註解
#
# (?:...)
# 不取得匹配的子字串
# 例： (?:a|b|c)1 匹配 abc1234 => c1
#
# (?P<name>)
#
# 增加別名
# 例： (?P<aa>a|b|c)1 匹配 abc1234 => c1, group('aa') = c
#
# (?P=name)
# 與別名的字串匹配
# 例： (?P<aa>a|b|c)1234(?P=aa) 匹配 abc1234c => c1234c
#
# (?#...)
# 註解
# 例： (?P:a|b|c)(?#comment)1234 匹配 abc1234 => c1234
#
# (?=...)
# 之後的字串需匹配，但不消耗字串且不放進 group
# 例： abc(?=1234)123 匹配 abc1234 => abc123
#
# (?!...)
# 之後的字串需不匹配，但不消耗字串且不放進 group
# 例： ab(?!\d).123 匹配 abc1234 => abc123
#
# (?<=...)
# 之前的字串需匹配，但不消耗字串且不放進 group
# 例： c(?<=abc)123 匹配 abc1234 => c123
#
# (?<!...)
# 之前的字串需不匹配，但不消耗字串且不放進 group
# 例： (?<!\d)c123 匹配 abc1234 => c123
#
# (?(id/name)yes-pattern|no-pattern)
# 若子字串匹配成立，則為 yes-pattern 否則為 no-pattern (可省略)
# 例： (\d)?abc(?(1)\d|) 匹配 1abc1 或 abc 或 1abc 或 abc1
#
# \A
# 匹配輸入字串的開始位置，不受 Multiline 影響
# 例： (?m)\Aabc 匹配 de\nabc => None
#
# \b
# 匹配單詞的開頭或結尾，也就是單詞的分界處
# \b 在字符類裡使用代表退格，故建議使用 r'string' 或 \\
# 例： \\bhi\\b.* 匹配 history, hi a => hi a
#
# \B
# 匹配不是單詞開頭或結束的位置
# 例： \B1234\B. 匹配 1234a1234c => 1234c
#
# \d
# 匹配數字 unicode 包括全部數字，在 (?a) 下同 [0-9]
# unicode 數字
# 例： 1\d 匹配 1234 => 12
#
# \D
# 匹配非數字 unicode 包括全部數字，在 (?a) 下同 [^0-9]
# unicode 數字
# 例： a\D 匹配 abc => ab
#
# \s
# 匹配空白字符 unicode 包括全部空白字符，在 (?a) 下同 [ \t\n\r\f\v]
# unicode 空白字符
# 例： a\s 匹配 a\nbc => a\n
#
# \S
# 匹配非空白字符 unicode 包括全部空白字符，在 (?a) 下同 [^ \t\n\r\f\v]
# unicode 空白字符
# 例： b\S 匹配 a\nbc => bc
#
# \w
# 匹配 word， unicode 包括全部 word，在 (?a) 下同 [a-zA-Z0-9_]
# 例： b\w 匹配 a\nbc => bc
#
# \W
# 匹配非 word， unicode 包括全部 word，在 (?a) 下同 [^a-zA-Z0-9_]
# 例： a\W 匹配 a\nbc => a\n
#
# \Z
# 匹配輸入字串的結尾位置，不受 Multiline 影響
# 例： (?m)de\Z 匹配 de\nabc => None
# '''
#
# # txt = "123&%#@!()happy word"
# #
# # # 刪除所有數字
# # print(re.sub('\d+', '', txt))
# # # 刪除所有符號
# # print(re.sub('\W+', '', txt))
# # # 刪除所有空白
# # print(re.sub('\s+', '', txt))
#
# '''
# 特殊案例
# 如果你要比對的字串,含有re所內建的符號,如(),?,#,[],+會造成找不到或出錯
#
# txt = "123&%#@!()happy word"
#
# # 出錯範例,我要取代掉'('
# print(re.sub('(', '', txt))
#
# 錯誤碼
# print(re.sub(keyword, txt))
# sre_constants.error: missing ), unterminated subpattern at position 0
# 上面是說你的比對字串在第0個位置有問題(從0開始算),以後出現明明應該比對到卻比對不到,或是出錯,可以依照這個去看看你的字串哪個地方出問題
#
# 解決方法如下
# '''
#
# # txt = "123&%#@!()happy word"
# #
# # # 解決辦法,我要取代掉'(',將特殊符號前面加上'\',代表這個符號沒任何含意,就是字串
# # print(re.sub('\(', '', txt))
# # # 特殊案例也可以應用在比對函數search和match上,比對函數說明在下面

###################################################################################
###################################################################################
# # 基因
# gene = 'vitamin D receptor, granzyme B, neurotrophin 3, insulin'
#
# # 文本
# txt = "VDR/vitamin D receptor regulates autophagic activity through ATG16L1. The Paneth cell is a unique intestinal epithelial cell that can sense the gut microbiome and secrete anti-microbial peptides, thereby playing critical roles in the maintenance of homeostasis at the intestinal-microbial interface. These roles in regulating innate immunity and intestinal microbial ecology are dependent on a functional autophagy pathway through ATG16L1. ATG16L1 is a regulator for autophagy and a risk gene for inflammatory bowel disease (IBD). We demonstrated that a low VDR/vitamin D receptor level in the intestine is associated with abnormal Paneth cells, impaired autophagy function, and imbalanced bacterial profile (dysbiosis), accompanied by a reduction of ATG16L1. We determined that VDR transcriptionally regulates ATG16L1 as a VDR target gene. Administration of the bacterial product butyrate increases intestinal VDR expression and suppresses inflammation in a colitis model. Thus, our study indicates that VDR may be a determinant of IBD risk through its actions on ATG16L1. These insights can be leveraged to define therapeutic targets for restoring Paneth cells and autophagy through VDR in chronic inflammation. It may also have applicability for infectious diseases and autoimmune diseases associated with skin or lung, where the host is in contact with bacteria."
#
# '''
# re.split(pattern, string, maxsplit=0, flags=0)
#
# pattern compile 生成的正則表達式對象，或者自定義也可
# string 要匹配的字符串
# maxsplit 指定最大分割次數，不指定將全部分割
# '''
# gene_list = re.split(', ', gene)
#
# for i in gene_list:
#
#     '''
#     re.search(pattern, string[, flags])
#
#     若string中包含pattern子串，則返回Match對象，否則返回None，注意，如果string中存在多個pattern子串，只返回第一個。
#     '''
#
#     search = re.search(i, txt)
#
#     if search:
#
#         # 返回search對象
#         print('search找到', search)
#         # 返回search字串
#         print('search找到', search.group())
#         # 返回search字串的(開始位置,結束位置),型態為tuple
#         print('search找到', search.span())
#         # 返回search字串的開始位置
#         print('search找到', search.start())
#         # 返回search字串的結束位置
#         print('search找到', search.end())
#
#         # 返回文本內所有符合條件的字串(開始位置,結束位置),型態為list
#         print('search找到', [m.span() for m in re.finditer(i, txt)])
#         # 返回文本內所有符合條件的字串的開始位置,型態為list
#         print('search找到', [m.start() for m in re.finditer(i, txt)])
#         # 返回文本內所有符合條件的字串的結束位置,型態為list
#         print('search找到', [m.end() for m in re.finditer(i, txt)])
###################################################################################
###################################################################################
# # 基因
# gene = 'vitamin D receptor'
#
# # 文本
# txt = "VDR/vitamin D receptor regulates autophagic activity through ATG16L1. The Paneth cell is a unique intestinal epithelial cell that can sense the gut microbiome and secrete anti-microbial peptides, thereby playing critical roles in the maintenance of homeostasis at the intestinal-microbial interface. These roles in regulating innate immunity and intestinal microbial ecology are dependent on a functional autophagy pathway through ATG16L1. ATG16L1 is a regulator for autophagy and a risk gene for inflammatory bowel disease (IBD). We demonstrated that a low VDR/vitamin D receptor level in the intestine is associated with abnormal Paneth cells, impaired autophagy function, and imbalanced bacterial profile (dysbiosis), accompanied by a reduction of ATG16L1. We determined that VDR transcriptionally regulates ATG16L1 as a VDR target gene. Administration of the bacterial product butyrate increases intestinal VDR expression and suppresses inflammation in a colitis model. Thus, our study indicates that VDR may be a determinant of IBD risk through its actions on ATG16L1. These insights can be leveraged to define therapeutic targets for restoring Paneth cells and autophagy through VDR in chronic inflammation. It may also have applicability for infectious diseases and autoimmune diseases associated with skin or lung, where the host is in contact with bacteria."
#
# # 在這次比賽不建議使用
# '''
# re.match(pattern, string[, flags])
#
# 從首字母開始開始匹配，string如果包含pattern子串，則匹配成功，返回Match對象，失敗則返回None，若要完全匹配，pattern要以$結尾。
# '''
#
# match = re.match(gene, txt)
# # 因為不是出現在首字母,故值為None
# print(match)
#
# match = re.match('VDR', txt)
# # 因為出現在首字母,故有匹配到,返回match對象
# print(re.match('VDR', txt))
# # 返回Match字串
# print('match找到', match.group())
# # 返回Match字串的(開始位置,結束位置),型態為tuple
# print('match找到', match.span())
# # 返回Match字串的開始位置
# print('match找到', match.start())
# # 返回Match字串的結束位置
# print('match找到', match.end())
###################################################################################
###################################################################################
# '''
# 這邊說明下面範例文本裡的superman和我們所要比對的基因su明顯不一樣,但su卻包含在superman裡面,
# 所以這會造成superman比對成功,這邊要教學如何匹配整個英文單字,而不是連包含在一起的都匹配到了
# '''
# # 基因
# gene = 'su'
#
# # 文本
# txt = 'you want to be a superman ? if you have a gene su you will become the superman.'
#
# # 錯誤比對,以上例子應該比對到基因su,卻比對到了superman的su,比對位置為span=(17, 19)是superman的su
# print(re.search(gene, txt))
#
# # 解決辦法,\b在re的意思是匹配單詞的開頭或結尾,也就是單詞的分界處,所以可以將單詞乾淨的分開,這樣上面的例子就會比對到基因su而不是superman
# print(re.search(r'\b'+gene+r'\b', txt))
# # 然後r''的意思代表,忽略所有的轉譯字符,\b原本是轉譯字符,意思代表退格,以下示範可以看到退格符刪除了'y'字,所以要讓\b不要代表退格而是要代表匹配單
# # 詞的開頭或結尾,就要使用r''函數知道,我不是要使用轉譯字符,而是要使用正規表示式
# print('happy')
# print('happy\b')
###################################################################################
###################################################################################
