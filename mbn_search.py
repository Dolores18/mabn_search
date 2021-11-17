import pandas as pd 

df = pd.read_table('E:/down/打字练习/蓝宝石/匠心雨码表/蓝宝石形码(匠士雨词库V1.6正式版)20210607.txt',sep=' ',header=None,names=['编码','一选','二选','三选']) 
df=pd.DataFrame(df)
df.replace(['/','^[.?]$'],'',regex=True,inplace=True)
a=df['编码'][df['一选'] == '真的']
b=df['编码'][df['二选'] == '真的']
c=df['编码'][df['三选'] == '真的']
#df[df['三选'] == '真的']['编码']
Word=input('请输入内容:')
jg=df['编码'][(df['一选']==Word) | (df['二选']==Word)| (df['三选']==Word)]
#不同的条件用()包裹起来,并或非分别使用&,|,~而非and,or,not，
df1=df[df['三选'] == '真的']['编码']
index=None
print("%s的编码为:%s" % (Word, jg.to_string(index = False)))

#" {!s} and my number is{:d}".format("Agnel Vishal",100)
#print("So Am %s and am %d years old" %(name,age))