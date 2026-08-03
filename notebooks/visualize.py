import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd


def main():
    base_dir = Path(__file__).resolve().parent.parent
    data_path = base_dir / "data" / "demand_params.csv"
    df = pd.read_csv(data_path)
    df = df.rename(columns={"demand point": "demand_point","j": "index","Pj": "population", "rj": "poverty_rate", 
                       "Vj": "vulnerable", "j.1": "congestion"})
    df.head()
    df.plot.bar()
    plt.show()

if __name__ == "__main__":
    main()