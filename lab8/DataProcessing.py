import pandas as pd
import matplotlib.pyplot as plt

class Drawer:
    def init(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_data(self):
        self.data = pd.read_csv(self.file_path)

    def plot_pie_chart(self, country_column):
        if self.data is not None:
            country_count = self.data[country_column].value_counts()
            plt.figure(figsize=(12, 12))
            country_count.plot(kind='pie', autopct='%1.1f%%')
            plt.title('Кругова діаграма кількості користувачів з кожного країни')
            plt.ylabel('')
            plt.axis('equal')
            plt.tight_layout()
            plt.show()

            return plt

    def plot_bar_chart(self, country_column, age_column):
        if self.data is not None:
            plt.figure(figsize=(10, 6))
            avg_age_by_country = self.data.groupby(country_column)[age_column].size()
            avg_age_by_country.plot(kind='bar', color='skyblue')
            plt.title('Середній вік користувачів з кожної країни')
            plt.xlabel('Країна')
            plt.ylabel('Середній вік')
            plt.xticks(rotation=45)
            plt.grid(axis='y')
            plt.tight_layout()
            plt.show()

            # Додано піддіаграму
            plt.subplot(1, 3, 3)
            self.plot_subscription_date_distribution()

    def plot_subscription_date_distribution(self):
        if self.data is not None:
            subscription_date_count = self.data['Subscription Date'].value_counts()
            subscription_date_count.plot(kind='line', marker='o', color='red')
            plt.title('Розподіл кількості користувачів за датою підписки')
            plt.xlabel('Дата підписки')
            plt.ylabel('Кількість користувачів')
            plt.grid(True)


    def plot_unique_countries_count(self, country_column):
        if self.data is not None:
            plt.subplot(1, 3, 3)
            unique_countries_count = self.data[country_column].nunique()
            plt.bar('Кількість унікальних країн', unique_countries_count, color='green')
            plt.title('Кількість унікальних компаній у даних')
            plt.xlabel('Показник')
            plt.ylabel('Кількість країн')
            plt.grid(axis='y')
            plt.tight_layout()

            plt.show()

    def save(self, plot: plt):
        pass