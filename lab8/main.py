import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class CSVDataVisualizer:
    def __init__(self, csv_file_path):
        self.data = pd.read_csv(csv_file_path)
        self.column_names = self.data.columns

    def explore_data(self):
        # Task 3: Explore Data
        data_summary = self.data.describe().round(2)
        print("Data Summary:\n", data_summary)

    def choose_visualization_types(self):
        # Task 4: Choose Visualization Types
        # Determine visualization types based on data characteristics.
        pass

    def prepare_data(self):
        # Task 5: Prepare Data
        # Implement data preprocessing if necessary for visualization.
        pass

    def basic_visualization(self, column_name):
        # Task 6: Basic Visualization
        # Create a basic visualization for the specified column.
        plt.figure(figsize=(10, 6))
        plt.plot(self.data[column_name])
        plt.title(f"Basic Visualization for {column_name}")
        plt.xlabel("Index")
        plt.ylabel(column_name)
        plt.show()

    def advanced_visualization_heatmap(self):
        # Task 7: Advanced Visualizations - Heatmap
        # Visualize trends in the dataset over time using a heatmap.
        plt.figure(figsize=(15, 10))
        data_subset = self.data.drop(["RegionName", "State", "SizeRank"], axis=1)
        sns.heatmap(data_subset.T, cmap="YlGnBu", xticklabels=10, yticklabels=False)
        plt.title("Heatmap of Housing Data Over Time")
        plt.xlabel("Time (Monthly Columns)")
        plt.ylabel("Metro Areas")
        plt.show()

    def multiple_subplots(self):
        # Task 8: Multiple Subplots
        # Learn to create multiple subplots within a single figure for better comparison.
        pass

    def export_and_share(self, export_format):
        # Task 9: Export and Share
        # Implement functionality to export visualizations in the specified format (PNG, SVG, HTML).
        pass
# Example Usage:
csv_file_path = "Metro_MedianValuePerSqft_AllHomes.csv"
visualizer = CSVDataVisualizer(csv_file_path)
visualizer.explore_data()

# Example usage of basic_visualization for a specific column (e.g., "1996-04")
visualizer.advanced_visualization_heatmap()