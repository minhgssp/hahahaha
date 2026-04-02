import traceback
try:
    import pandas as pd
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import seaborn as sns
    import os

    # Set style
    sns.set_theme(style="whitegrid")

    # Load data
    file_path = r"c:\commandcenter\06_Hoctap.tech\Antigravity_Basic\lesson-modules\2.2-analyze-data\Sales_Data.csv"
    df = pd.read_csv(file_path)

    # Convert Date to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # Create a figure with subplots
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Plot 1: Revenue by Region
    sns.barplot(data=df, x='Region', y='Revenue', ax=axes[0], palette='viridis', errorbar=None, estimator='sum')
    axes[0].set_title('Total Revenue by Region', fontsize=14)
    axes[0].set_ylabel('Total Revenue ($)', fontsize=12)

    # Plot 2: Revenue Trend over Time
    sns.lineplot(data=df, x='Date', y='Revenue', hue='Product', ax=axes[1], marker='o', palette='Set2')
    axes[1].set_title('Revenue Trend Over Time by Product', fontsize=14)
    axes[1].set_ylabel('Revenue ($)', fontsize=12)
    axes[1].set_xlabel('Date', fontsize=12)
    axes[1].tick_params(axis='x', rotation=45)

    # Adjust layout
    plt.tight_layout()

    # Save the plot
    output_file = r"c:\commandcenter\06_Hoctap.tech\Antigravity_Basic\lesson-modules\2.2-analyze-data\sales_chart.png"
    plt.savefig(output_file, dpi=300, bbox_inches='tight')

    print(f"Chart successfully generated and saved at: {output_file}")
except Exception as e:
    print(f"ERROR: {e}")
    traceback.print_exc()
