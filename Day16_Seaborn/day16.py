import seaborn as sns
import matplotlib.pyplot as plt

# Built-in dataset
tips = sns.load_dataset("tips")

print(tips.head())
# Count Plot
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.countplot(x="day", data=tips)

plt.title("Customers by Day")

plt.show()
#Histogram
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.histplot(tips["total_bill"])

plt.title("Total Bill Distribution")

plt.show()
#Box Plot
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.boxplot(x="day", y="total_bill", data=tips)

plt.show()
# Heatmap
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

corr = tips.corr(numeric_only=True)

sns.heatmap(corr, annot=True)

plt.show()