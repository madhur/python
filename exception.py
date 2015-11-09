def fetcher(obj, index):
	return obj[index]

x = 'spam'
fetcher(x, 3)

try:
	fetcher(x, 4)	
except IndexError:
	print ('got exception')


def catcher():
	try:
		fetcher(x, 4)
	except IndexError:
		print('got exception')
	print('continuing')
	
catcher()				