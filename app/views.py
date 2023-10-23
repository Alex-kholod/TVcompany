from django.shortcuts import render
import MySQLdb


# Create your views here.
def models_tv(request):
    connect = MySQLdb.connect('localhost', 'root', 'admin', 'test3')
    cursor = connect.cursor()
    cursor.execute("SELECT tv_id, tv_model, price FROM tv;")
    data_list = []
    keys_list = []
    for row in cursor.fetchall():
        data_dict = {
            "ID": row[0],
            "Model": row[1],
            "Price": row[2]
        }
        data_list.append(data_dict)
        keys_list = data_dict.keys()
    data = {
        "data_list": data_list,
        "keys_list": keys_list
    }
    connect.close()
    return render(request=request, template_name="app/models_tv.html", context=data)


def index(request):
    return render(request=request, template_name="app/index.html")


def shipments(request):
    return render(request=request, template_name="app/shipments.html")


def supply(request):
    return render(request=request, template_name="app/supply.html")


def stocks(request):
    connect = MySQLdb.connect('localhost', 'root', 'admin', 'test3')
    cursor = connect.cursor()
    cursor.execute("""
        select  tv.tv_model, storehouse.storehouse_name, stocks.stock_count
        from stocks
        inner join tv on stocks.tv_id = tv.tv_id
        inner join storehouse using (storehouse_id)
        ORDER by stock_count ASC;
    """)
    data_list = []
    keys_list = []
    for row in cursor.fetchall():
        data_dict = {
            "Model": row[0],
            "Store": row[1],
            "Stock": row[2]
        }
        data_list.append(data_dict)
        keys_list = data_dict.keys()
    data = {
        "data_list": data_list,
        "keys_list": keys_list
    }
    connect.close()
    return render(request=request, template_name="app/stocks.html", context=data)
