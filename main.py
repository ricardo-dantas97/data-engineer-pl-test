import time
import pandas as pd
from utils import avg_sales_per_month, top_products_sold_by_channel, top_revenue_country_and_region, concat_df

# Path
input_path = 'data/vendas.csv'
output_path = 'results'


def main():
  # Select only columns that will be used
  cols = ['Region', 'Country', 'Item Type', 'Sales Channel', 'Order Date', 'Units Sold', 'Total Revenue']
  
  # Auxiliary dataframes
  df_avg_sales_per_month = pd.DataFrame()
  df_top_product_sold_by_channel = pd.DataFrame()
  df_top_revenue_country_and_region = pd.DataFrame()

  for df in pd.read_csv(input_path, usecols=cols, chunksize=50_000, parse_dates=['Order Date']):
    # Create df about sales per month
    df_avg_sales_per_month_aux = avg_sales_per_month(df)
    df_avg_sales_per_month = concat_df(df_avg_sales_per_month, df_avg_sales_per_month_aux)

    # Create df about most sold product by channel
    df_top_product_sold_by_channel_aux = top_products_sold_by_channel(df)
    df_top_product_sold_by_channel = concat_df(df_top_product_sold_by_channel, df_top_product_sold_by_channel_aux)

    # Create df about country and region with the highest revenue
    df_top_revenue_country_and_region_aux = top_revenue_country_and_region(df)
    df_top_revenue_country_and_region = concat_df(df_top_revenue_country_and_region, df_top_revenue_country_and_region_aux)
    
  # Perform final aggregations
  df_avg_sales_per_month = avg_sales_per_month(df=df_avg_sales_per_month, final_aggregation=True)
  print('Average sales per month data sample:')
  print(df_avg_sales_per_month.head())
  print()

  df_top_product_sold_by_channel = top_products_sold_by_channel(df=df_top_product_sold_by_channel, final_aggregation= True)
  print('Top products sold by channel:')
  print(df_top_product_sold_by_channel)
  print()

  df_top_revenue_country_and_region = top_revenue_country_and_region(df=df_top_revenue_country_and_region, finnal_aggregation=True)
  print('Highest revenue by region and country:')
  print(df_top_revenue_country_and_region)
  print()

  # Create CSV file with the results
  df_avg_sales_per_month.to_csv(f'{output_path}/sales_per_month.csv', index=False)
  df_top_product_sold_by_channel.to_csv(f'{output_path}/top_products_by_channel.csv', index=False)
  df_top_revenue_country_and_region.to_csv(f'{output_path}/top_revenue_by_region_country.csv', index=False)


if __name__ == '__main__':
  start_time = time.time()
  main()
  end_time = time.time()
  total_time = end_time - start_time
  print(f'Execution time in seconds: {total_time}')
