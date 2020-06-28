# Import Matplotlib, Pandas, and Seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Create a count plot with "Spiders" on the x-axis
sns.countplot(x="Spiders", data=df)

# Display the plot
plt.show()
