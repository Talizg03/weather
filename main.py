import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
st.markdown(""" 
# Title 
## subtitle
-bul1
- bul2

""")
st.radio("which desert is best?",["cake","ice cream","fruits"])
df=sns.load_dataset("penguins")
fig,ax=plt.subplot()
sns.scatterplot(data=df,x="flipper_length_mm",y="bill_length_mm",hue="species",ax=
ax)
st.pyplot(fig)