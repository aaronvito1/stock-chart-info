# import requests 
# # from django.shortcuts import render


# def index(request):
# 	# content_html = open("djangoapp/templates/portfolio.html").read()
# 	print('Currency Exchange page being visited')
# 	response = requests.get('https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2020-06-01/2020-06-17?apiKey=fURCL4yNKe4CuMX2Fk5yMA70pUTDAHAe')
# 	data = response.json()
# 	context = {
# 		# "content": content_html,
# 		'ticker_data': data, 
# 	}
# 	return render(request, "index.html", context)

	# print('Currency Exchange page being visited')
# response = requests.get('https://api.polygon.io/v1/meta/symbols/GME/company?&apiKey=fURCL4yNKe4CuMX2Fk5yMA70pUTDAHAe')
# data = response.json()
# print(data)
