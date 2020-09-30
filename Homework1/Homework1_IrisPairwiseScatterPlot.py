# library & dataset
import matplotlib.pyplot as plt
import seaborn as sns


iris = sns.load_dataset('iris')
sns.pairplot(iris, kind="scatter", hue="species", markers=["o", "s", "D"], palette="Set2")
plt.show()
 
