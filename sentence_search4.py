import pandas as pd 
import re
import jieba


from zhon.hanzi import punctuation
df = pd.read_csv('E:/down/01python/study/datasanalys/出任2.txt', sep='\t',header=None,names=['编码','一选','二选','三选']) 
df=pd.DataFrame(df)
#df=df.set_index(df['编码'])#设置编码为索引列
Word=("设置编码为索引列")#如果代中嵌入了单

str = Word
str=re.sub(r"[%s]+" %punctuation, "",Word)#去除所有的标点
Word=str.replace(' ','')





jg=df['编码'][(df['一选']==Word) | (df['二选']==Word)| (df['三选']==Word)]#.to_string(index=False)
seg_list = list(jieba.cut(Word))

list1=[]
list2=[]
for seg in seg_list:
	seg_jg=df['编码'][(df['一选']==seg) | (df['二选']==seg)| (df['三选']==seg)]
 	
	if  seg_jg.array.size>0:
		
		#print('%s通过第一个测试'%seg)
		g=seg_jg.to_string(index=False)
		#print(g)
		if  "\n" in g:	
			
			#print("有换行符")
			g.replace('\n', 'z')
			q=g.replace('\n', 'z')
			w=q.replace(' ', '')
			#print(w)
			result1=re.search(r'\w+(?=z)',w).group()#(?<=\\n),,只能匹配第一行\w.*， ([\s\S]*)换行匹配
			result2=re.search(r'(?<=z).*',w).group()#以z开头并且不包含z,这是零宽断言
			#print(result1,result2)
			ab1=len(result1)
			#print(ab1)
			ab2=len(result2)
			#print(ab2)
			#是为了副值
			g=()
			if ab1> ab2:
				#print('取大值')					
				g=result2
			if ab2> ab1:
				#print('取小值')
				g=result1
				#print(g)
		 				
		else:
			#print('没有换行符')
			pass
		#print('唯一的编码为%s'%g)
		list1.append(g)
		#print(list1)

	if seg_jg.array.size==0:
		#print('%s没有通过测试,开始切分单个词'% seg)
		
		#print(seg)
		for seg1 in seg:
			seg=seg1
			seg_jg=df['编码'][(df['一选']==seg) | (df['二选']==seg)| (df['三选']==seg)]
		
			if seg_jg.array.size>0:
				#print('%s通过了第一个测试'%seg)
				g=seg_jg.to_string(index=False)
				d="%s"% (g)
			
				if  "\n" in g:	

					#print("为空值且有换行符")
					g.replace('\n', 'z')
					q=g.replace('\n', 'z')
					
					result1=re.search(r'\w+(?=z)',q).group()#(?<=\\n),,只能匹配第一行\w.*， ([\s\S]*)换行匹配
					result2=re.search(r'(?<=z)\w+',q).group()#以z开头并且不包含z,这是零宽断言
					ab1=len(result1)
					ab2=len(result2)
					#是为了副值
					g=()
					if ab1> ab2:
						#print('计算大小')					
						g=result2
					if ab2> ab1:
						g=result1
				 				
				else:
					#print('没有换行符')
					pass
				#print(g)
				list1.append(g)
				
list2.append(list1)
a = eval('[%s]'%repr(list2).replace('[', '').replace(']', ''))
jg = "_ ".join(a)#把一个Lis中的各str合并。
print("%s的编码为%s"%(Word,jg))
#print(a)
	#a=seg_jg	
	#print(a.to_string(index=False))