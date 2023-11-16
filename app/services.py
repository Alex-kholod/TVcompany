import MySQLdb

#Функции получения данных и передачи в представления
def get_models_tv():
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
    return data


def get_supplies():
    connect = MySQLdb.connect('localhost', 'root', 'admin', 'test3')
    cursor = connect.cursor()
    cursor.execute("""
                select date_format(supply.supply_date, "%d %M %Y") as date_create, tv.tv_model, supply.supply_count, 
                supplier.supplier_name, staff_storage.staff_full_name
                from tv
                inner join order_supply using (tv_id)
                inner join supply using (supply_id)
                inner join supplier using (supplier_id)
                inner join staff_storage using (staff_id)
                order by date_create DESC;
            """)
    data_list = []
    keys_list = []
    for row in cursor.fetchall():
        data_dict = {
            "Дата приемки": row[0],
            "Модель телевизора": row[1],
            "Количество": row[2],
            "Поставщик": row[3],
            "Сотрудник": row[4]
        }
        data_list.append(data_dict)
        keys_list = data_dict.keys()
    data = {
        "data_list": data_list,
        "keys_list": keys_list,
        "button_name": "создать приемку"
    }
    connect.close()
    return data


def get_stocks():
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
            "Модель телевизора": row[0],
            "Склад": row[1],
            "Остаток": row[2]
        }
        data_list.append(data_dict)
        keys_list = data_dict.keys()
    data = {
        "data_list": data_list,
        "keys_list": keys_list
    }
    connect.close()
    return data

def get_shipments():
    connect = MySQLdb.connect('localhost', 'root', 'admin', 'test3')
    cursor = connect.cursor()
    cursor.execute("""
                SELECT * FROM shipmentsview;
            """)
    data_list = []
    keys_list = []
    for row in cursor.fetchall():
        data_dict = {
            "Дата создания": row[0],
            "Модель телевизора": row[1],
            "Количество": row[2],
            "Дистрибутор": row[3],
            "Сотрудник": row[4],
            "Машина": row[5]
        }
        data_list.append(data_dict)
        keys_list = data_dict.keys()
    data = {
        "data_list": data_list,
        "keys_list": keys_list,
        "button_name": "создать отгрузку"
    }
    connect.close()
    return data


#Функции добавления данных в базу данных

def add_supply():
    pass