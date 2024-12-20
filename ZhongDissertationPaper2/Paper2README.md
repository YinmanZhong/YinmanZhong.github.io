This is about paper 2
```python
plt.figure(figsize=(10, 6))
sns.scatterplot(x="document_word_count", y="combined_tfidf", hue="MedicaidState", data=pd.concat([expanded_states_df, non_expanded_states_df]), palette="muted", alpha=0.6, edgecolor='none')
#plt.title('Combined TF-IDF vs Document Word Count (Scatter Plot)', fontsize=16, fontweight='bold')
plt.xlabel('Document Word Count', fontsize=20)
plt.ylabel('Combined TF-IDF Scores', fontsize=20)
plt.legend(title='Medicaid Status Group',  fontsize=12, title_fontsize=14)
plt.xticks(rotation=45, fontsize=16)  # Bold years on the x-axis
plt.yticks(fontsize=16)  # Bold numbers on the y-axis
plt.show()
```
<table border="0"  style='border:none;'  bordercolor="#ffffff"  width=100%  >
<tr style='border:none;'  >   
   <td valign="center" style='border:none;'  > 
        <img  height="300" width = "500" align="center" src="https://github.com/YinmanZhong/YinmanZhong.github.io/blob/main/ZhongDissertationPaper2/Result_Figure_1.png">
   </td>
 </tr>
 </table>
