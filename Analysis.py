import sys,csv

def sanityCheck(row,clicks,conversions,conversionRatio,cost,cpc,revenue,rpc,profit,ad_type):
  error_msg = ""

  if conversions > 0 and clicks >0:
    if abs( (conversions/clicks) - (conversionRatio/100.0)) > 0.01:
      error_msg = "Error: cr: %.2f, %.2f"%(conversions/clicks,conversionRatio/100.0)

  if conversions < 0:
    error_msg = 'Error: conversion cannot be negative!'
  
  if clicks < 0:
    error_msg = 'Error: clicks cannot be negative!'

  if clicks > 0 and abs( (revenue/clicks) - rpc) > 0.1:
    error_msg = "Error: rpc=%.2f, %.2f"%(revenue/clicks,rpc)

  if ad_type != 'CPM' and conversions > clicks:
    error_msg = "Error:  conversions must be less than clicks!"

  if error_msg:
    print error_msg, row
    sys.exit()

if __name__=='__main__':

  ff = csv.reader(open('report.csv','rU'))
  ff.next()
  ff.next()

  i = 3
  for row in ff:
    print i,row
    date = row[0]
    time = row[1]
    advertiser = row[2]
    offer = row[3]
    offer_url = row[4]
    affiliate_source = row[5]
    affiliate_sub_id_1 = row[6]
    affiliate_sub_id_2 = row[7]
    affiliate_sub_id_3 = row[8]
    affiliate_sub_id_4 = row[9]
    affiliate_sub_id_5 = row[10]
    clicks = float(row[11])
    conversions = float(row[12])
    conversionRatio = float(row[13])
    cost = float(row[14])
    cpc = float(row[15])
    revenue = float(row[16])
    rpc = float(row[17])
    profit = float(row[18])
    
    ad_type = 'CPM' # <--------- must get from dewey
    sanityCheck(row,clicks,conversions,conversionRatio,cost,cpc,revenue,rpc,profit,ad_type)
    i += 1
