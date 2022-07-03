#graphs.py
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import pandas as pd

def DrawGraph():
    
    data = pd.read_csv("listings_summary_dec18.csv")
    df = pd.DataFrame(data)

    x = df['minimum_nights']
    y = df['price']

    plt.bar(x, y, color='g')
    plt.title("prices of properties")
    plt.xlabel("price")
    plt.ylabel("Types of property")

    plt.show()
DrawGraph()
