from datetime import datetime
from typing import List, Dict, Tuple

"""
A company tracks daily sales across multiple stores. Write a function that:

Input:
- sales_data: list of (store_id, date, product_category, amount)
  Example: 
  [
    ("S1", "2024-01-15", "Electronics", 1200.50),
    ("S1", "2024-01-15", "Clothing", 850.00),
    ("S2", "2024-01-15", "Electronics", 2100.00),
    ("S1", "2024-01-16", "Electronics", 950.00),
    ("S2", "2024-01-16", "Clothing", 650.00),
    ("S3", "2024-01-15", "Electronics", 300.00),
  ]

Return:
- A dictionary with the following structure:
  {
    "total_revenue": float,  # Sum of all sales
    "store_summary": {
      store_id: {
        "total": float,  # Total revenue for store
        "categories": {category: total_amount}
      }
    },
    "category_summary": {
      category: {
        "total": float,  # Total revenue for category
        "stores": {store_id: total_amount}
      }
    },
    "best_day": {  # Day with highest total revenue
      "date": str,
      "total": float
    }
  }

Rules:
1. All monetary values should be rounded to 2 decimal places
2. If multiple days have same highest revenue, pick the earliest date
3. Return empty dict if input is empty or invalid
4. Handle negative amounts? (Assume all amounts are positive, but validate)
"""

class Sales:
# list of (store_id, date, product_category, amount) 
 def __init__(self, store_id, date,product_category,amount):
    self.store_id = store_id
    self.date =  self.convert_date_str(date)
    self.product_category = product_category
    self.amount = amount
 @staticmethod
 def convert_date_str(date):
  return datetime.strptime(date,'%Y-%m-%d').date()
    
def convert_date_to_str(date) -> datetime:
  if not date:
    return
  return datetime.strftime(date,'%Y-%m-%d')

def roundAllValues(sales_summary):
  # store summary

  store_summary = sales_summary['store_summary']
  
  for storeId, storeData in store_summary.items():
    storeData['total'] = round(storeData['total'],2)
    for category, value in storeData['categories'].items():
      storeData['categories'][category] = round(value,2)

  category_summary = sales_summary['category_summary']

  for value in category_summary.values():
    value['total'] = round(value['total'],2)
    for storeId, amount in value['stores'].items():
      value['stores'][storeId] = round(value['stores'][storeId],2)
    

  
def sales_analyser(sales:List[Tuple[str,str,str,float]]) -> Dict[str,any]:
   if not sales:
    return {}
   

   
   sales_list = []

   for s in sales:
     if len(s) < 4:
       return {}
     (store_id,date,product_category,amount) = s
     sales_list.append(Sales(store_id,date,product_category,amount))

   # sort sales list by date
   sales_list.sort(key=lambda s:s.date)
   

   
   sales_summary = {} #initialize
   total_revenue = 0.0
   store_summary = {}
   category_summary = {}
   best_day_date = None
   best_day_total = 0.0
   daily_totals = {}
   best_day = {'best_day':convert_date_to_str(best_day_date), 'total':best_day_total}



   for sale in sales_list:
      
      if sale.amount < 0:
        return {}

      store_id = sale.store_id
      date =  sale.date
      product_cat = sale.product_category
      amount = sale.amount
      total_revenue += amount


      if not store_id in store_summary:
         store_summary[store_id] = {'total':0, 'categories':{}}
      store_summary[store_id]['total'] +=amount

      if not product_cat in store_summary[store_id]['categories']:
         store_summary[store_id]['categories'][product_cat] = 0.0
      store_summary[store_id]['categories'][product_cat] +=amount

      if not product_cat in category_summary:
        category_summary[product_cat] = {'total':0.0,'stores':{}}
      category_summary[product_cat]['total'] +=amount
      
      if not store_id in category_summary[product_cat]['stores']:
        category_summary[product_cat]['stores'][store_id] = 0.0
      
      category_summary[product_cat]['stores'][store_id] += amount
      date_string = convert_date_to_str(date)
      if not date_string in daily_totals:
          daily_totals[date_string] = 0.0
      daily_totals[date_string] += amount

      if daily_totals[date_string] > best_day_total:
        best_day_total = daily_totals[date_string]
        best_day_date = date
      elif  daily_totals[date_string] == best_day_total:
        # take first
        isFirst = best_day_date > date
        if isFirst:
          best_day_date = date
      


 

   best_day['best_day'] = convert_date_to_str(best_day_date)
   best_day['total'] = round(best_day_total,2) 
   sales_summary['total_revenue'] = round(total_revenue,2)
   sales_summary['store_summary'] = store_summary
   sales_summary['category_summary'] = category_summary
   sales_summary['best_day'] = best_day

   roundAllValues(sales_summary)
   return sales_summary


 
      
    

      
   
   


def main():
    sales =   [
    ("S1", "2024-01-15", "Electronics",1200.5),
    ("S1", "2024-01-15", "Clothing", 850.00),
    ("S2", "2024-01-15", "Electronics", 2100.00),
    ("S1", "2024-01-16", "Electronics", 950.00),
    ("S2", "2024-01-16", "Clothing", 650.00),
    ("S3", "2024-01-15", "Electronics", 300.00),
  ]
    
    print(sales_analyser(sales))
  

main()