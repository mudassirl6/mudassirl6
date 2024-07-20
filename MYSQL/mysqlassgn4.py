import mysql.connector
import pandas as pd
# Connect to the MySQL database
def fetch_table(query):
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='MudassirL6',
        database='assignment'
    )
    cursor = con.cursor()
    cursor.execute(query)
    column_names = [i[0] for i in cursor.description]
    result = cursor.fetchall()
    cursor.close()
    con.close()
    return result,column_names

query1 = '''
select a.CustomerID,a.FirstName,a.LastName,a.Address,a.City,o.TypeOfOrder,o.OrderAmount,o.OrderDate,o.DeliveryDate from orders1 o join address1 a on a.CustomerID = o.CustomerID;  
'''

data,column_names= fetch_table(query1)

df = pd.DataFrame(data,columns=column_names)

# 1. Week-wise - Sales based on Customer type

df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['Week'] = df['OrderDate'].dt.strftime('%U')
week_sales = df.groupby(['Week', 'TypeOfOrder']).agg(TotalSales=('OrderAmount', 'sum')).reset_index()
print(week_sales.to_string(index=False))

print()

# 2. Which state/city presents the highest retail market?
retail = df[df['TypeOfOrder'] == 'Retail'].groupby('City').agg(TotalRetailSales=('OrderAmount', 'sum')).reset_index()
highest_retail_value = retail.iloc[retail['TotalRetailSales'].idxmax()]
print(highest_retail_value)

print()
# 3. Which state/city has the lowest wholesale market?

whole_sale = df[df['TypeOfOrder'] == 'Wholesale'].groupby('City').agg(TotalWholeSales=('OrderAmount', 'sum')).reset_index()
lowest_wholesale = whole_sale.iloc[whole_sale['TotalWholeSales'].idxmin()]
print(lowest_wholesale)

print()

#4. The date when we did the highest business?



sales = df.groupby('OrderDate').aggregate(TotalSales=('OrderAmount', 'sum')).reset_index()
highest_business_date = sales[sales['TotalSales'] == sales['TotalSales'].max()]
print(highest_business_date.iloc[[0],[0]].to_string(index=False))

# 5. Unique Customer and Address with Total Order Value


df['FullName'] = df['FirstName']+" "+df['LastName']
customer_list = df.groupby(['CustomerID', 'FullName','Address', 'City']).agg(TotalOrderValue=('OrderAmount', 'sum')).reset_index()
print(customer_list.to_string(index=False))

print()

# 6. Has the business improved week after week?
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['WeekNumber'] = df['OrderDate'].dt.strftime('%U')

weekly_sales = df.groupby('WeekNumber').agg(TotalSales=('OrderAmount', 'sum')).reset_index()
weekly_sales['PercentageChange'] = weekly_sales['TotalSales'].pct_change().fillna(0)*100
print(weekly_sales.to_string(index=False))

print()

# # 7. Percentage change in business between each week

df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['WeekNumber'] = df['OrderDate'].dt.strftime('%U')

weekly_sales = df.groupby('WeekNumber').agg(TotalSales=('OrderAmount', 'sum')).reset_index()
weekly_sales['PercentageChange'] = weekly_sales['TotalSales'].pct_change().fillna(0) * 100
print(weekly_sales[['WeekNumber','TotalSales','PercentageChange']].to_string(index=False))

print()

# 8. Percentage change in retail business between each week
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['WeekNumber'] = df['OrderDate'].dt.strftime('%U')

retail = df[df['TypeOfOrder'] == 'Retail'].groupby(['WeekNumber','TypeOfOrder']).agg(TotalRetailSales=('OrderAmount', 'sum')).reset_index()
retail['PercentageChange'] = retail['TotalRetailSales'].pct_change().fillna(0) * 100
print(retail)

print()

# 9. Percentage change in wholesale business between each week

df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['WeekNumber'] = df['OrderDate'].dt.strftime('%U')

wholesale = df[df['TypeOfOrder'] == 'Wholesale'].groupby(['WeekNumber','TypeOfOrder']).agg(TotalWholeSales=('OrderAmount', 'sum')).reset_index()
wholesale['PercentageChange'] = wholesale['TotalWholeSales'].pct_change().fillna(0) * 100
print(wholesale.to_string(index=False))

print()

# 10. The date when we did the lowest business.

sales = df.groupby('OrderDate').aggregate(TotalSales=('OrderAmount', 'sum')).reset_index()
lowest_business_date = sales[sales['TotalSales'] == sales['TotalSales'].min()]
print(lowest_business_date.iloc[[0],[0]].to_string(index=False))
print()
# 11. Top Buyer in the 6th month of business.

df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['MonthNumber'] = df['OrderDate'].dt.strftime('%m')
df['FullName'] = df['FirstName']+df['LastName']
top_buyer = df[df['MonthNumber'] == '06'].groupby(['CustomerID','FullName']).agg(TotalOrderAmount = ('OrderAmount','sum')).reset_index()
top_buyer = top_buyer[top_buyer['TotalOrderAmount'] == top_buyer['TotalOrderAmount'].max()]
print(top_buyer.to_string(index = False))
print()
# 12. Highest business by type - 6th Month.

df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['MonthNumber'] = df['OrderDate'].dt.strftime('%m')

top_buyer = df[df['MonthNumber'] == '06'].groupby(['TypeOfOrder','MonthNumber']).agg(TotalSales = ('OrderAmount','sum')).reset_index()
top_buyer_by_type = top_buyer[top_buyer['TotalSales'] == top_buyer['TotalSales'].max()]
print(top_buyer_by_type.to_string(index = False))
