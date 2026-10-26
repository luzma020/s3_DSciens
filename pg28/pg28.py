import matplotlib.pyplot as plt
import numpy as np
langluages=['java','python','php','javaScript','dc#','c++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
plt.figure(figsize=(8,5))
plt.bar(langluages,popularity,color='skyblue')
plt.title("popularity of programming languages")
plt.xlabel("languages")
plt.ylabel('popularity(%)')
plt.show()
plt.figure(figsize=(8,5))
plt.bar(langluages,popularity,color='red')
plt.title("popularity of programming languages(horizontal)")
plt.xlabel('popularity(%)')
plt.ylabel('programming languages')
plt.show()
colors = ['red','green','blue','yellow','magenta','cyan']
plt.figure(figsize=(8,5))
plt.bar(langluages,popularity,color=colors)
plt.title("popularity of programming languages (different colors)")
plt.xlabel('programming languages')
plt.ylabel('popularity(%)')
plt.show()
plt.figure(figsize=(8,5))
plt.pie(popularity,labels=langluages,autopct='%1.1f%%',startangle=140)
plt.title('popularity of programming languages(pie chart)')
plt.axis('equal')
plt.show()