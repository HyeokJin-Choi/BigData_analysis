import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\samsung\\Desktop\\BigData_analysis\\dfdata\\prestige.csv")

sns.set_theme(rc={'figure.figsize':(7,7)})
sns.scatterplot(
    data = df,
    x = 'education',
    y = 'income',
    size='women', sizes = (20,4000),
    hue = 'type', alpha = 0.5,
    legend = True
)

for i in range (0,df.shape[0]):
    plt.text(x=df.education[i],y=df.income[i],s=df.job[i])

plt.show()
