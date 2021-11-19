import pandas as pd 
import jieba
df = pd.read_csv('E:/down/01python/study/datasanalys/出任2.txt', sep='\t',header=None,names=['编码','一选','二选','三选']) 

df=pd.DataFrame(df)
df.replace(['/','^[.?]$'],'',regex=True,inplace=True)
a=df['编码'][df['一选'] == '真的']
b=df['编码'][df['二选'] == '真的']
c=df['编码'][df['三选'] == '真的']
#df[df['三选'] == '真的']['编码']
Word=('他来到了网易杭研大厦')
name=Word
data = ("他来到了网易杭研大厦")  # 默认是精确模式
Rs2=[] #
seg_list = jieba.cut(data)
for w in seg_list :#读取每一行分词
	Rs2.append(w)
Rs3=[]

Rs4=[]
count =0 #计算for循环的次数
for X in Rs2:
	
	Rs3=[]
	
	#print(X)
	Word=X
	jg=df['编码'][(df['一选']==Word) | (df['二选']==Word)| (df['三选']==Word)]

	strs=jg.drop_duplicates().to_string(index=False)
	d="%s"% (strs,)
	print(d)
	Rs3.append(d)

	Rs4.append(Rs3)
	
print(Rs3)
a = eval('[%s]'%repr(Rs4).replace('[', '').replace(']', ''))#把嵌套的list合并成一个
jg = "_ ".join(a)
print("%s的编码为%s"%(data,jg))
	#count += 1#计算for循环的次数



#fprint(Rs3)or num in range(1,count+1):
 #   print(num,end=" ")

	#不同的条件用()包裹起来,并或非分别使用&,|,~而非and,or,not，
	#df1=df[df['三选'] == '真的']['编码']
	#index=None
	#print("%s的编码为:%s" % (Word, jg.to_string(index = False)))

	#" {!s} and my number is{:d}".format("Agnel Vishal",100)
	#print("So Am %s and am %d years old" %(name,age))