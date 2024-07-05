import pandas as pd


def avg_sales_per_month(df, final_aggregation=False):
  # Create column with year and month
  if not final_aggregation:
    df['year_month'] = df['Order Date'].apply(lambda x: x.strftime('%Y-%m'))

  agg = {
    'Units Sold': 'mean',
    'Total Revenue': 'mean'
  }

  df = df.groupby(['year_month', 'Item Type']).agg(agg).reset_index()

  if final_aggregation:
    rename_cols = {
      'Item Type': 'item_type',
      'Units Sold': 'avg_units_sold',
      'Total Revenue': 'avg_revenue',
    }

    df = df.rename(columns=rename_cols)

  return df


def top_products_sold_by_channel(df, final_aggregation=False):
  agg = {'Units Sold': 'sum'}
  df = df.groupby(['Sales Channel', 'Item Type']).agg(agg).reset_index()

  if final_aggregation:
    df = df.groupby(['Sales Channel', 'Item Type']).agg(agg).reset_index()
    df = df.sort_values(['Sales Channel', 'Units Sold'], ascending=[1, 0])
    df['row_n'] = df.groupby(['Sales Channel']).cumcount() + 1
    df = df.loc[df['row_n'] == 1, ['Sales Channel', 'Item Type', 'Units Sold']]

    rename_cols = {
      'Item Type': 'item_type',
      'Units Sold': 'total_units_sold',
      'Sales Channel': 'channel',
    }

    df = df.rename(columns=rename_cols)
  
  return df


def top_revenue_country_and_region(df, finnal_aggregation=False):
  agg = {'Total Revenue': 'sum'}
  df = df.groupby(['Region', 'Country']).agg(agg).reset_index()
  df = df.sort_values('Total Revenue', ascending=False)
  
  if finnal_aggregation:
    rename_cols = {
      'Region': 'region',
      'Country': 'country',
      'Total Revenue': 'total_revenue',
    }

    df = df.rename(columns=rename_cols).head(5)

  return df


def concat_df(df, df_aux):
  final_df = pd.concat([df, df_aux], ignore_index=True)
  return final_df