import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_risk_distribution(df):
    sns.set_style(style='darkgrid')
    plot = sns.countplot(df['Risk'], edgecolor='black', palette=['#00C851', '#ff4444'])

    bars = plot.patches
    for i, bar in enumerate(bars):
        plot.annotate(bar.get_height(), (i, bar.get_height()/2), ha='center', fontsize=15, color='black')

    plt.title("Risk Distribution")
    plt.show()

    percentage_diff = round(100 * (bars[0].get_height() - bars[1].get_height()) / 
                            ((bars[0].get_height() + bars[1].get_height()) / 2), 1)
    print(f'Percentage difference = {percentage_diff}%')

def correlation_plot(df):
    corr = abs(df.corr())
    lower_triangle = np.tril(corr, k=-1)
    mask = lower_triangle == 0

    plt.figure(figsize=(15, 10))
    sns.set_style(style='white')
    sns.heatmap(lower_triangle, center=0.5, cmap='Blues',
                xticklabels=corr.index, yticklabels=corr.columns,
                cbar=False, annot=True, linewidths=1, mask=mask)
    plt.title("Correlation Plot")
    plt.show()
