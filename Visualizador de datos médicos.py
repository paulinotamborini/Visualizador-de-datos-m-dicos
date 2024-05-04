# 1
import pandas as pd
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2).apply(lambda x: 1 if x > 25 else 0)

# 3
df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x > 1 else 0)
df['gluc'] = df['gluc'].apply(lambda x: 1 if x > 1 else 0)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    # 7
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar').fig
    
    # 8
    return fig

# 9
def draw_heat_map():
    # 10
    df_heat = df[(df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]
    
    # 11
    corr = df_heat.corr()
    
    # 12
    mask = np.triu(corr)
    
    # 13
    fig, ax = plt.subplots(figsize=(11, 9))
    
    # 14
    sns.heatmap(corr, annot=True, fmt='.1f', linewidths=.5, mask=mask, vmax=.3, center=0.1, square=True, cbar_kws={'shrink': 0.5})
    
    # 15
    return fig
