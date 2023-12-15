from ..classes.csv_parse import Drawer

def main():
    # Example usage:
    drawer = Drawer("./Metro_MedianValuePerSqft_AllHomes.csv")
    drawer.read_data()
    plot = drawer.plot_time_series("RegionName")
    drawer.plot_pie_chart("RegionName")
    drawer.plot_bar_chart("RegionName", "SizeRank")
    
    # drawer.plot_time_series("RegionName")

    drawer.save(plot)

if __name__ == "__main__":
    main()