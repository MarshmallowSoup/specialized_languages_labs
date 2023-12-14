import pandas as pd
import matplotlib.pyplot as plt

class Drawer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_data(self):
        self.data = pd.read_csv(self.file_path)

    def plot_time_series(self, region_column):
        if self.data is not None:
            region_data = self.data.groupby(region_column).sum().transpose()
            region_data.plot(figsize=(14, 8), title='Time Series Analysis by Region')
            plt.xlabel('Date')
            plt.ylabel('Total Value')  # You may adjust this based on your data
            plt.legend(title=region_column, bbox_to_anchor=(1.05, 1), loc='upper left')
            plt.tight_layout()
            plt.show()
            return plt

    def plot_pie_chart(self, region_column):
        if self.data is not None:
            region_count = self.data[region_column].value_counts()
            plt.figure(figsize=(12, 12))
            region_count.plot(kind='pie', autopct='%1.1f%%')
            plt.title('Pie Chart: Distribution of Regions')
            plt.ylabel('')
            plt.axis('equal')
            plt.tight_layout()
            plt.show()

    def plot_bar_chart(self, region_column, value_column):
        if self.data is not None:
            plt.figure(figsize=(10, 6))
            avg_value_by_region = self.data.groupby(region_column)[value_column].sum()
            avg_value_by_region.plot(kind='bar', color='skyblue')
            plt.title('Bar Chart: Total Value by Region')
            plt.xlabel('Region')
            plt.ylabel('Total Value')
            plt.xticks(rotation=45)
            plt.grid(axis='y')
            plt.tight_layout()
            plt.show()


    def save(self, plot: plt):
        plot.savefig("./DIAG.png")
        plot.savefig("./DIAG.svg")
        plot.savefig("./DIAG.pdf")


