# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/01_data.cluster.ipynb.

# %% auto 0
__all__ = ['calculate_wcss', 'plot_elbow_method']

# %% ../../nbs/01_data.cluster.ipynb 4
from sklearn.cluster import KMeans
import pandas as pd

# %% ../../nbs/01_data.cluster.ipynb 5
def calculate_wcss(data: pd.DataFrame, # the input dataframe
                   max_k: int # the number of clusters
                  ) -> float:
    "compute the WCSS metric"
    wcss = []
    for k in range(1, max_k + 1):
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(data)
        wcss.append(kmeans.inertia_)
    return wcss

# %% ../../nbs/01_data.cluster.ipynb 6
def plot_elbow_method(wcss, max_k):
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, max_k + 1), wcss, marker='o')
    plt.title('Elbow Method for Optimal k')
    plt.xlabel('Number of clusters (k)')
    plt.ylabel('WCSS')
    plt.grid(True)
    plt.show()
