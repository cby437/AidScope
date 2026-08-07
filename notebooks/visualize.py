import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd


def main():
    # column = input("Column: ")
    demand("Bubble View of All Demand Points")
    organization("View of All Aid Organizations")

def demand(graphtitle, column='vulnerable'):
    base_dir = Path(__file__).resolve().parent.parent
    data_path = base_dir / "data" / "demand_params.csv"
    df_d = pd.read_csv(data_path)
    df_d = df_d.rename(columns={"demand point": "demand_point","j": "index","Pj": "population", "rj": "poverty_rate", 
                       "Vj": "vulnerable", "j.1": "congestion"})
    if "Bar" in graphtitle:
        df_d.plot.bar(x=column, title=graphtitle)
    elif "Bubble" in graphtitle:
        size = ((df_d['population'] / df_d['population'].max()) * 2000)
        df_d.plot.scatter(x='population', y=column, s=size, c='C0')
    plt.show()
    return df_d

def organization(graphtitle, column='cash'):
    base_dir = Path(__file__).resolve().parent.parent
    data_path = base_dir / "data" / "organization_params.csv"
    df_org = pd.read_csv(data_path)
    df_org = df_org.rename(columns={"Aid Organization": "aid_organization","i": "index","wi": "legitimacy", "betai": "soft_power", 
                       "hi": "shipping", "Cash Distributed (si) in millions USD ($)": "cash"})
    df_org = df_org.set_index('aid_organization')
    ax = df_org.plot.bar(y=column, title=graphtitle, use_index=True)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    plt.show()
    return df_org

if __name__ == "__main__":
    main()

