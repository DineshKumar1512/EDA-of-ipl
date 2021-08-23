import pandas as pd
import streamlit as st
import plotly.express as px

st.title("""

IPL Analysis

""")
   
df=pd.read_csv('matches.csv')
df1=pd.read_csv('deliveries.csv')
merge_df = pd.merge(df1,df, left_on='match_id', right_on ='id')
st.header("""Matches file""")
st.dataframe(df.head(30))
st.header("""Deliveries file""")
st.dataframe(df1.head(30))

st.header("""

From matches.csv

""")

a=df['winner'].value_counts()

b=df['season'].value_counts()

c=df['venue'].value_counts().head(10)

d=df['city'].value_counts().head(10)

e=df['toss_winner'].value_counts()

f=df['result'].value_counts()

g=df['player_of_match'].value_counts().nlargest(20)

h=df['toss_decision'].value_counts().nlargest(20)

i=df['umpire1'].value_counts().nlargest(20)

j=df.groupby('season')['winner'].tail(1).value_counts()

df5=df[df['toss_decision']=='bat']
k=df5['venue'].value_counts().nlargest(10)

df56=df[df['toss_decision']=='field']
l=df56['venue'].value_counts().nlargest(10)

m=df.groupby('venue')['winner'].count().sort_values(ascending=False).head(10)



z = st.selectbox('data type', ['select','Match Winner','Season','Venue','City','Toss Winner','Result','Man of the Match',
                               'Toss Decision','Umpire','IPL Trophies','Batting Venue','Bowling Venue','Winning Venue'],key='asd')
select = st.selectbox('Visualization type', ['select','Bar chart', 'Area chart','Scatter chart','Pie chart'],key='asd')

if z=='Match Winner':
    y=a
elif z=='Season':
    y=b
elif z=='Venue':
    y=c
elif z=='City':
    y=d
elif z=='Toss Winner':
    y=e
elif z=='Result':
    y=f
elif z=='Man of the Match':
    y=g
elif z=='Toss Decision':
    y=h
elif z=='Umpire':
    y=i
elif z=='IPL Trophies':
    y=j
elif z=='Batting Venue':
    y=k
elif z=='Bowling Venue':
    y=l
elif z=='Winning Venue':
    y=m

    
if select == 'Area chart':
    st.area_chart(y)
elif select=='Bar chart':
    fig=px.bar(y,x=y.index,y=y.values,color=y.values,color_continuous_scale=["#003f5c","#bc5090","#ffa600"],height=500)
    st.plotly_chart(fig)
elif select=='Scatter chart':
    fig=px.scatter(y,x=y.index,y=y.values,color=y.values,color_continuous_scale=["#003f5c","#bc5090","#ffa600"],height=500)
    st.plotly_chart(fig)
elif select=="Pie chart":
    fig=px.pie(y,names=y.index,values=y.values,height=500)
    st.plotly_chart(fig)


st.header("""

From deliveries.csv

""")

a1=df1['dismissal_kind'].value_counts()

b1=df1['fielder'].value_counts().nlargest(20)

c1=df1.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).nlargest(10)

d1=df1.groupby('bowler')['player_dismissed'].count().sort_values(ascending = False).nlargest(10)

e1=df1['batsman'].value_counts().head(10)

z=df1.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False)
z1=z[z>1000]
y=df1['batsman'].value_counts()
y1=y[y>1000]
f1=((z1/y1)*100).sort_values(ascending=False).head(10)

z=df1.groupby('bowler')['player_dismissed'].count()
z2=z[z>50]
y=df1['bowler'].value_counts()
y2=y[y>100]
g1=((y2/z2)).sort_values(ascending=True).head(15)

z=df1.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False)
z3=z[z>1000]
y=df1['player_dismissed'].value_counts()
y3=y[y>50]
h1=((z3/y3)).sort_values(ascending=False).head(10)

z=df1.groupby('bowler')['player_dismissed'].count().sort_values(ascending = False)
z4=z[z>50]
y=df1.groupby('bowler')['total_runs'].sum().sort_values(ascending=False)
y4=y[y>1000]
i1=((y4/z4)).sort_values(ascending=True).head(10)


z=df1.groupby('bowler')['total_runs'].sum().sort_values(ascending=False)
z6=z[z>1000]
y=df1['bowler'].value_counts()
y6=(y[y>500])
n1=((z6/y6)*6).sort_values(ascending=True).head(10)

k=df1[df1['batsman_runs']==6]
o1=k['batsman'].value_counts().head(10)

k2=df1[df1['batsman_runs']==4]
p1=k2['batsman'].value_counts().head(10)

k3=df1[df1['batsman_runs']==1]
q1=k3['batsman'].value_counts().head(10)

k4=df1[df1['batsman_runs']==0]
r1=k4['batsman'].value_counts().head(10)

z1 = st.selectbox('DATA TYPE', ['select','Dismissal Type','Catch taken by','Most Runs','Most Wickets','Balls Faced','Batsman SR','Bowling SR','Batting Average',
                               'Bowling Average','Bowling Economy','Most Sixes','Most Fours','Most Ones','Most Dots'])
select1 = st.selectbox('VISUALIZATION TYPE', ['select','Bar chart', 'Area chart','Scatter chart','Pie chart'])

if z1=='Dismissal Type':
    y1=a1
elif z1=='Catch taken by':
    y1=b1
elif z1=='Most Runs':
    y1=c1
elif z1=='Most Wickets':
    y1=d1
elif z1=='Balls Faced':
    y1=e1
elif z1=='Batsman SR':
    y1=f1
elif z1=='Bowling SR':
    y1=g1
elif z1=='Batting Average':
    y1=h1
elif z1=='Bowling Average':
    y1=i1
elif z1=='Bowling Economy':
    y1=n1
elif z1=='Most Sixes':
    y1=o1
elif z1=='Most Fours':
    y1=p1
elif z1=='Most Ones':
    y1=q1
elif z1=='Most Dots':
    y1=r1

if select1 == 'Area chart':
    st.area_chart(y1)
elif select1=='Bar chart':
    fig=px.bar(y1,x=y1.index,y=y1.values,color=y1.values,color_continuous_scale=["red","yellow"],height=500)
    st.plotly_chart(fig)
elif select1=='Scatter chart':
    fig=px.scatter(y1,x=y1.index,y=y1.values,height=500,color=y1.values,color_continuous_scale=["red","yellow"])
    st.plotly_chart(fig)
elif select1=="Pie chart":
    fig=px.pie(y1,names=y1.index,values=y1.values,height=500)
    st.plotly_chart(fig)

st.header("""

From merge_df

""")

a2=merge_df.groupby('winner')['total_runs'].sum().sort_values(ascending=False).head(10)

b2=merge_df.groupby('winner')['player_dismissed'].count().sort_values(ascending=False).head(10)

c2=merge_df.groupby('season')['batsman_runs'].sum().sort_values(ascending=False)


d2=merge_df.groupby('season')['player_dismissed'].count()

e2=merge_df.groupby('venue')['batsman_runs'].sum().sort_values(ascending=False).head(10)

f2=merge_df.groupby('venue')['player_dismissed'].count().sort_values(ascending=False).head(10)



z2 = st.selectbox('data type', ['select','Winning Team Runs','Winning Team Wickets','Runs per season','Wickets per season','Batting stadiums','Bowling stadiums'],key='asdf')                               
select2 = st.selectbox('Visualization type', ['select','Bar chart', 'Area chart','Scatter chart','Pie chart'],key='asdf')

if z2=='Winning Team Runs':
    y2=a2
elif z2=='Winning Team Wickets':
    y2=b2
elif z2=='Runs per season':
    y2=c2
elif z2=='Wickets per season':
    y2=d2
elif z2=='Batting stadiums':
    y2=e2
elif z2=='Bowling stadiums':
    y2=f2


if select2 == 'Area chart':
    st.area_chart(y2)
elif select2=='Bar chart':
    fig=px.bar(y2,x=y2.index,y=y2.values,color=y2.values,color_continuous_scale=["#004c6d","#00a1c1","#00ffff"],height=500)
    st.plotly_chart(fig)
elif select2=='Scatter chart':
    fig=px.scatter(y2,x=y2.index,y=y2.values,color=y2.values,color_continuous_scale=["#004c6d","#00a1c1","#00ffff"],height=500)
    st.plotly_chart(fig)
elif select2=="Pie chart":
    fig=px.pie(y2,names=y2.index,values=y2.values,height=500)
    st.plotly_chart(fig)

st.header("""

From merge_df

""")

x4=st.slider("Pick Year:",2008,2019)
st.write(x4)
z3 = st.selectbox('data type', ['select','Runs','Wickets','Batting SR season','Bowling SR season','Batting average season','Bowling average season','Bowling economy season'],key='asdfgh')                               
select3 = st.selectbox('Visualization type', ['select','Bar chart', 'Area chart','Scatter chart','Pie chart'],key='asdfgh')

dfs=merge_df[merge_df['season']==x4]
a13=dfs.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)

dfs=merge_df[merge_df['season']==x4]
a23=dfs.groupby('bowler')['player_dismissed'].count().sort_values(ascending=False).head(10)

dfs=merge_df[merge_df['season']==x4]
z11=dfs.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False)
z12=z11[z11>80]
y11=dfs['batsman'].value_counts()
y12=y11[y11>50]
a3=((z12/y12)*100).sort_values(ascending=False).head(10)

dfs=merge_df[merge_df['season']==x4]
z11=dfs.groupby('bowler')['player_dismissed'].count()
z12=z11[z11>10]
y11=dfs['bowler'].value_counts()
y12=y11[y11>50]
b3=((y12/z12)).sort_values(ascending=True).head(10)

dfs=merge_df[merge_df['season']==x4]
z11=dfs.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False)
z12=z11[z11>50]
y11=dfs['player_dismissed'].value_counts()
y12=y11[y11>10]
c3=((z12/y12)).sort_values(ascending=False).head(10)

dfs=merge_df[merge_df['season']==x4]
z11=dfs.groupby('bowler')['player_dismissed'].count().sort_values(ascending=False)
z12=z11[z11>15]
y11=dfs.groupby('bowler')['total_runs'].sum().sort_values(ascending=False)
y12=y11[y11>50]
d3=((y12/z12)).sort_values(ascending=True).head(10)

dfs=merge_df[merge_df['season']==x4]
z11=dfs.groupby('bowler')['total_runs'].sum().sort_values(ascending=False)
z12=z11[z11>50]
y11=dfs['bowler'].value_counts()
y12=y11[y11>30]
e3=((z12/y12)*6).sort_values(ascending=True).head(10)

if z3=='Batting SR season':
    y3=a3
elif z3=='Bowling SR season':
    y3=b3
elif z3=='Batting average season':
    y3=c3
elif z3=='Bowling average season':
    y3=d3
elif z3=='Bowling economy season':
    y3=e3
elif z3=='Runs':
    y3=a13
elif z3=='Wickets':
    y3=a23

    
if select3 == 'Area chart':
    st.area_chart(y3)
elif select3=='Bar chart':
    fig=px.bar(y3,x=y3.index,y=y3.values,color=y3.values,color_continuous_scale=["#FFC300","#FF5733","#C70039","#900C3F"],height=500)
    st.plotly_chart(fig)
elif select3=='Scatter chart':
    fig=px.scatter(y3,x=y3.index,y=y3.values,color=y3.values,color_continuous_scale=["#FFC300","#FF5733","#C70039","#900C3F"],height=500)
    st.plotly_chart(fig)
elif select3=="Pie chart":
    fig=px.pie(y3,names=y3.index,values=y3.values,height=500)
    st.plotly_chart(fig)



with st.beta_expander("Conclusion"):
    x="""
**Mumbai**,**Chennai**,**Kolkata** always have **high chances** of winning IPL and
have **huge fanbase** all over India

**Kohli**,**Dhoni**,**De villiers**,**Narine**,**Warner** are famous both on and off the pitch

**Bumrah**,**H Pandya**,**Pant**,**Ngidi** are rising stars
    """
    st.markdown(x)
