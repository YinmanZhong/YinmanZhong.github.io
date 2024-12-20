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
        <img  height="700" width = "1000" align="center" src="https://github.com/YinmanZhong/YinmanZhong.github.io/blob/main/ZhongDissertationPaper2/Result_Figure_1.png">
   </td>
 </tr>
 </table>

```python
# Bar Chart: Average Combined_tfidf by MedicaidState and TAXYEAR
plt.figure(figsize=(12, 8))
avg_combined_tfidf = pd.concat([expanded_states_df, non_expanded_states_df]).groupby(['MedicaidState', 'TAXYEAR'])['combined_tfidf'].mean().reset_index()
sns.barplot(x="TAXYEAR", y="combined_tfidf", hue="MedicaidState", data=avg_combined_tfidf, palette="muted")
#plt.title('Average Combined TF-IDF by Medicaid Status and Tax Year', fontsize=16, fontweight='bold')
# Adjust the y-axis limit to give more space on top so the legend can fit in
plt.ylim(0, 0.18)
plt.xlabel('Tax Year', fontsize=20)
plt.ylabel('Average Combined TF-IDF Scores', fontsize=20)
plt.legend(title='Medicaid Status Group', fontsize=12, title_fontsize=14)
plt.xticks(rotation=45, fontsize=16)  # Bold years on the x-axis
plt.yticks(fontsize=16)  # Bold numbers on the y-axis
plt.show()
```
<table border="0"  style='border:none;'  bordercolor="#ffffff"  width=100%  >
<tr style='border:none;'  >   
   <td valign="center" style='border:none;'  > 
        <img  height="700" width = "1000" align="center" src="https://github.com/YinmanZhong/YinmanZhong.github.io/blob/main/ZhongDissertationPaper2/Result_Figure_2.png">
   </td>
 </tr>
 </table>

 ```python
# Plotting the trend of combined_tfidf over time for Both Expanded and Non-Expanded States
plt.figure(figsize=(12, 6))
# Plotting the trend for Expanded States with a 95% confidence interval
sns.lineplot(x="TAXYEAR", y="combined_tfidf", data=expanded_states_df,
             marker='o', label="Expanded States", color='blue', linewidth=2.5)
# Plotting the trend for Non-Expanded States with a 95% confidence interval
sns.lineplot(x="TAXYEAR", y="combined_tfidf", data=non_expanded_states_df,
             marker='o', label="Non-Expanded States", color='red', linewidth=2.5)
# Add title, labels, and legend
#plt.title('Trend of Combined TF-IDF over Time (Expanded vs Non-Expanded States)', fontsize=16, fontweight='bold')
plt.xlabel('Tax Year', fontsize=20)  # Bold and larger font size for x-axis title
plt.ylabel('Combined TF-IDF Scores', fontsize=20)  # Bold and larger font size for y-axis title
plt.xticks(rotation=45, fontsize=16)  # Bold years on the x-axis
plt.yticks(fontsize=16)  # Bold numbers on the y-axis
plt.legend(title="Medicaid Status Group", fontsize=12, title_fontsize=14)
# Remove grid lines
plt.grid(False)
# Remove top and right spines for a cleaner look
sns.despine()
# Show the plot
plt.show()
```
<table border="0"  style='border:none;'  bordercolor="#ffffff"  width=100%  >
<tr style='border:none;'  >   
   <td valign="center" style='border:none;'  > 
        <img  height="700" width = "1000" align="center" src="https://github.com/YinmanZhong/YinmanZhong.github.io/blob/main/ZhongDissertationPaper2/Result_Figure_3.png">
   </td>
 </tr>
 </table>
