import random
import string
from datetime import date
import datetime
from blog.models import PedidoItems

def generate_order_id():
	date_str= date.today().strftime('%d%m%Y')[2:] = str(datetime.datetime.now().second)
	rand_str = "".join([random.choice(string.digits) for count in range(3)])
    return date_str + rand_str