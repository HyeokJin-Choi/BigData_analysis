from dateutil.parser import parse
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


df = pd.read_csv('dfdata/time_series2.csv',parse_dates=['date'],
                 index_col='date')
df.reset_index(inplace=True)

df['year']=[d.year for d in df.date]
df['month']=[d.strftime('%b') for d in df.date]
df.info()

years=df['year'].unique()
m=['Jan','Feb','Mar','Apr','May','Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#df['month']= # m리스트 순서대로 카테고리 만들기 pd.
df['month'] = pd.Categorical(df['month'], categories=m, ordered=True)

np.random.seed(100)
mycolors=np.random.choice(list(mpl.colors.XKCD_COLORS.keys()),len(years),
                          replace=False)






#%% 년도별 시계열 그리기
plt.figure(figsize=(16,12),dpi=80)
for i, y in enumerate(years):
    if i>0:
        plt.plot('month','value',data=df.loc[df.year==y,:],
                 color=mycolors[i], label=y)
        plt.text(df.loc[df.year==y,:].shape[0]-0.9,
                 df.loc[df.year==y,'value'][-1:].values[0],
                 y, fontsize=12, color=mycolors[i])
        
plt.gca().set(xlim=(-0.3,11),ylim=(2,30),ylabel='$Drug Sales$',xlabel='$Month$') # 달러기호는 이탤릭채의 처리를 의미
plt.yticks(fontsize=12,alpha=.7)
plt.title("Time series data",fontsize=20)
plt.show()

#%% subplot boxplot 만들기
fig,axes = plt.subplots(1,2,figsize=(20,7),dpi=80)
df.boxplot(column='value',by='year',ax=axes[0],grid=False) # boxplot를 연도에 다른 박스의 설정을 하기 위해서 by를 사용해서 그룹핑함.
df.boxplot(column= 'value',by= 'month',ax=axes[1],grid=False)

plt.show()


#%%  색 다르게 설정하기
grouped = df.groupby('month')['value']

# Generate random colors from XKCD colors
mycolors = np.random.choice(list(mpl.colors.XKCD_COLORS.keys()), len(grouped), replace=False)

# Create the boxplot
box = plt.boxplot(
    [grouped.get_group(g) for g in grouped.groups],
    patch_artist=True,
    labels=grouped.groups.keys()
)

# Set different colors for each box
for patch, color in zip(box['boxes'], mycolors): # 같은 index끼리 묶는 역할을 하는것이 zip의 역할
    patch.set_facecolor(color)

# Display the plot
#plt.show()


#%% seaborn  사용하여 그리기
# Create a 1x2 subplot
fig, axes = plt.subplots(1, 2, figsize=(20, 7), dpi=80)

# First boxplot: Year-wise box plot
sns.boxplot(x='year', y='value', data=df, ax=axes[0], palette='deep') # 색상을 구별하는 방법은 palette와 hue의 방법 이렇게 두개가 있음.

# Second boxplot: Month-wise box plot excluding certain years (1991, 2008)
sns.boxplot(x='month', y='value', 
            data=df.loc[~df.year.isin([1991, 2008]), :])#, 
            #ax=axes[1], hue='month') # hue는 구별할 컬럼을 넣음.

# Set titles for each subplot
axes[0].set_title('Year-wise Box Plot\n(The Trend)', fontsize=18)
axes[1].set_title('Year-wise Box Plot\n(The Seasonality)', fontsize=18)

# Display the plots
plt.show()
# seaborn  사용하여 그리기
# fig,axes = plt.subplots(1,2,figsize=(20,7),dpi=80)
# #palette는 색정보 넣어주고 hue는 뭐 가지고 색 구분할건지 넣어줘야함
# sns.boxplot(x='year', y ='value' ,data = df,ax=axes[0],palette='deep')
# sns.boxplot(x='month',y='value',
#             data=df.loc[~df.year.isin([1991,2008]),:],ax=axes[1],hue='month')

# axes[0].set_title('year-wise Box Plot\n(The Trend',fontsize=18)
# axes[1].set_title('year-wise Box Plot\n(The The Seasonality)',fontsize=18)
# plt.show()
#pallete : 'deep',"muted","bright","pastel","dark","colorblind" # palette의 색상 처리방법들
