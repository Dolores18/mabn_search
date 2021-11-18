import pandas as pd 
import jieba
import re
import string
from zhon.hanzi import punctuation
df = pd.read_csv('E:/down/01python/study/datasanalys/出任2.txt', sep='\t',header=None,names=['编码','一选','二选','三选']) 

df=pd.DataFrame(df)
data = input("请输入文字：")  # 默认是精确模式
from zhon.hanzi import punctuation

str = data.
punctuation_str = punctuation

for i in punctuation:
    str = str.replace(i, '')
#data=str.replace(' ','')
#print(data)

Rs2=[] #


seg_list = jieba.cut(data)
for w in seg_list :#读取每一行分词
	Rs2.append(w)
Rs3=[]

Rs4=[]
for X in Rs2:
	
	Rs3=[]
	Word=X
	jg=df['编码'][(df['一选']==Word) | (df['二选']==Word)| (df['三选']==Word)]

	strs=jg.drop_duplicates().to_string(index=False)
	d="%s"% (strs,)
	if  "\n" in d:
		#print("有换行符")
		e=d.replace('\n', 'z')

		result1=re.search(r'\w+(?=z)',e).group()#(?<=\\n),,只能匹配第一行\w.*， ([\s\S]*)换行匹配
		result2=re.search(r'(?<=z)\w+',e).group()#以z开头并且不包含z,这是零宽断言
		ab1=len(result1)
		ab2=len(result2)
		d=()#是为了副值
		if ab1> ab2:
			d=result2
		else:
			d=result1
	else:
		pass
	
	Rs3.append(d)
	Rs4.append(Rs3)
a = eval('[%s]'%repr(Rs4).replace('[', '').replace(']', ''))
jg = "_ ".join(a)
print("%s的编码为%s"%(data,jg))


	









	



