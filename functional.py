import pymysql
import pymysql.cursors
import re
from conf import host, user, password, db_name
from datetime import datetime
def connect_toBD():
    try:
        global connection
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Succesfull")
    except Exception as e:
        print("Error")
        print(e)

    return connection

def close_connection(connection):
    if connection is not None:
        connection.close()
        connection = None

def new_client_(phone_number, name_client, problem, complicacy, model, production_date, guaranteed_period, service_type):

    cursor = connection.cursor()
    try:
        cursor.callproc('new_client', (phone_number, name_client, problem, complicacy, model, production_date, guaranteed_period, service_type))
        connection.commit()
        cursor.close()
        return True
    except Exception as e:
        cursor.close()
        print(e)
        return False



def new_empl(phone_number, name, surname, age, exp, id_dep, id_post, passw):

    cursor = connection.cursor()
    try:
        query = (f"insert into employee(name, surname, age, work_experience, employee_phone_number, id_department, "
                 f"id_post, password_empl) values('{name}', '{surname}', {age}, '{exp}', '{phone_number}', "
                 f" '{id_dep}', '{id_post}', "
                 f" '{passw}')")
        cursor.execute(query)
        connection.commit()
        cursor.close()
        return True
    except Exception as e:
        cursor.close()
        print(e)
        return False
def get_all_applications():

    cursor = connection.cursor()
    try:
        cursor.callproc('all_applications')
        row = cursor.fetchall()
        cursor.close()
        return row
    except Exception as e:
        cursor.close()
        print(e)
        return False

def add_depart(addr_d, id_warehouse):

    cursor = connection.cursor()
    try:
        query = (f"insert into department(address_department, id_warehouse) values('{addr_d}', {id_warehouse})")
        cursor.execute(query)
        connection.commit()
        cursor.close()
        return True
    except Exception as e:
        cursor.close()
        print(e)
        return False

def delete_depart(id_dep):
    cursor = connection.cursor()

    try:
        query = (f"delete from department where id_department = {id_dep}")
        cursor.execute(query)
        connection.commit()
        cursor.close()
        return True
    except Exception as e:
        cursor.close()
        print(e)
        return False

def delete_empl(phone):
    cursor = connection.cursor()

    try:
        query = (f"delete from employee where employee_phone_number = '{phone}'")
        cursor.execute(query)
        connection.commit()
        cursor.close()
        return True
    except Exception as e:
        cursor.close()
        print(e)
        return False
def get_applications_with_param(for_, to_, stat, sor):
    cursor = connection.cursor()
    try:
        if len(for_) == 0 and len(to_) == 0:
            if len(stat) == 0:
                date = ''
            else:
                date = f"where status = '{stat}'"
        else:
            if len(stat) == 0:
                date = f"where date_of_receipt between '{for_}' and '{to_}'"
            else:
                date = f"where (date_of_receipt between '{for_}' and '{to_}') and (status = '{stat}')"

        if len(sor) == 0:
            qsor = ""
        else:
            qsor = f"ORDER BY {sor}"

        query = (
            f"SELECT application.id_application, application.date_of_receipt, application.complicacy, status_of_application.status, "
            f"client.phone_number AS 'Client phone', "
            f"problem.type_problem, vacuum_cleaner.model, "
            f"Concat(employee.name,' ', employee.surname) AS 'Employee', application.ready_date "
            f"FROM application "
            f"JOIN client ON application.id_client = client.id_client "
            f"JOIN vacuum_cleaner ON application.id_vacuum = vacuum_cleaner.id_vacuum "
            f"JOIN problem ON application.id_problem = problem.id_problem "
            f"LEFT JOIN employee ON application.id_employee = employee.id_employee "
            f"JOIN status_of_application ON application.id_status = status_of_application.id_status "
            f"{date} "
            f"{qsor} ;")

        cursor.execute(query)
        row = cursor.fetchall()
        cursor.close()
        return row
    except Exception as e:
        cursor.close()
        print(e)
        return False

def get_empl_with_param(adr, post, sor):
    cursor = connection.cursor()
    try:
        if len(adr) == 0:
            if len(post) == 0:
                date = ''
            else:
                date = f"where tittle = '{post}'"
        else:
            if len(post) == 0:
                date = f"where address_department = '{adr}'"
            else:
                date = f"where (address_department = '{adr}') and (tittle = '{post}')"

        if len(sor) == 0:
            qsor = ""
        else:
            qsor = f"ORDER BY {sor}"

        query = (
            f"select e.id_employee, CONCAT(e.name,' ', e.surname) as employee, e.age, e.employee_phone_number, "
            f"d.address_department, p.tittle, e.password_empl "
            f"from employee e "
            f"join department d on e.id_department = d.id_department "
            f"join post p on e.id_post = p.id_post "
            f"{date} "
            f"{qsor} ;")

        cursor.execute(query)
        row = cursor.fetchall()
        cursor.close()
        return row
    except Exception as e:
        cursor.close()
        print(e)
        return False


def change_status_for_ready(id_application, id_master):
    cursor = connection.cursor()
    try:
        check = (f"select id_employee from application where id_application = {id_application};")
        cursor.execute(check)
        check_id = cursor.fetchall()

        if id_master == check_id[0]['id_employee']:
            cursor.callproc('change_status', (1, id_application))
            connection.commit()
            cursor.close()
            return True
        else:
            cursor.close()
            return False

    except Exception as e:
        cursor.close()
        print(e)
        return False


def get_services_appl(id_application):
    cursor = connection.cursor()

    try:
        query = (f"select st.id_application, s.type " 
                f"from set_of_services st "
                f"join service s on st.id_service = s.id_service "
                f"where id_application = {id_application};")

        cursor.execute(query)
        row = cursor.fetchall()
        cursor.close()
        return row

    except Exception as e:
        cursor.close()
        print(e)
        return False

def get_depart():
    cursor = connection.cursor()

    try:
        query = ("select d.id_department, d.address_department, w.address "
                "from department d "
                "join warehouse w on d.id_warehouse = w.id_warehouse;")
        cursor.execute(query)
        row = cursor.fetchall()
        cursor.close()
        return row

    except Exception as e:
        cursor.close()
        print(e)
        return False

def get_addresses_warehouse():
    cursor = connection.cursor()

    try:
        query = (f"select address from warehouse;")
        cursor.execute(query)
        row = cursor.fetchall()
        cursor.close()
        return row

    except Exception as e:
        cursor.close()
        print(e)
        return False
def get_addresses():
    cursor = connection.cursor()

    try:
        query = (f"select address_department from department;")
        cursor.execute(query)
        row = cursor.fetchall()
        cursor.close()
        return row

    except Exception as e:
        cursor.close()
        print(e)
        return False
def phone_check(phone_number):

    pattern_phone = re.compile(r"^8\d{10}$")
    match = pattern_phone.match(phone_number)

    if match:
        return True
    return False

def check_address(addr):

    if re.match(r'^[A-Za-z]{1,20},\s[A-Za-z]{1,30}(\s[A-Za-z]{1,15})*\s\d{1,3}$', addr):
        return True
    return False
def check_name(name):

    if re.match(r'^[a-zA-Z]+$', name) and ((len(name) <= 20) and (len(name) > 0)):
        return True
    return False

def get_id_dep(addr):
    cursor = connection.cursor()

    try:
        query = (f"select id_department, address_department from department;")
        cursor.execute(query)
        row = cursor.fetchall()

        address = [d['address_department'] for d in row]
        id_dep = [d['id_department'] for d in row]
        cursor.close()

        i = address.index(addr)
        res = id_dep[i]

        return res

    except Exception as e:
        cursor.close()
        print(e)
        return False

def get_id_warehouse(addr):
    cursor = connection.cursor()

    try:
        query = (f"select id_warehouse, address from warehouse;")
        cursor.execute(query)
        row = cursor.fetchall()

        address = [d['address'] for d in row]
        id_war = [d['id_warehouse'] for d in row]
        cursor.close()

        i = address.index(addr)
        res = id_war[i]

        return res

    except Exception as e:
        cursor.close()
        print(e)
        return False

def get_id_post(post):
    cursor = connection.cursor()

    try:
        query = (f"select id_post, tittle from post;")
        cursor.execute(query)
        row = cursor.fetchall()

        pos = [d['tittle'] for d in row]
        id_post = [d['id_post'] for d in row]
        cursor.close()

        i = pos.index(post)
        res = id_post[i]

        return res

    except Exception as e:
        cursor.close()
        print(e)
        return False
def password_check(pas):

    if len(pas) <= 20:
        return True
    return False

def translate_compl(complicacy):

    match complicacy:
        case 'Легко':
            return 'easy'
        case 'Нормально':
            return 'normal'
        case 'Сложно':
            return 'hard'

def translate_stat(status):

    match status:
        case 'Принят':
            return 'Adopted'
        case 'В работе':
            return 'At work'
        case 'Готов':
            return 'Ready'
        case '':
            return ''

def translate_sort(s):

    match s:
        case 'Дате приема':
            return 'date_of_receipt'
        case 'Статусу':
            return 'status'
        case '':
            return ''

def translate_post(post):

    match post:
        case 'Директор':
            return 'Head of department'
        case 'Бухгалтер':
            return 'Bookkeeper'
        case 'Администратор':
            return 'Administrator'
        case 'Мастер':
            return 'Master'
        case 'Админ':
            return 'Admin'
        case '':
            return ''


def translate_sorForEmpl(s):

    match s:
        case 'Возрасту':
            return 'age'
        case 'Должности':
            return 'tittle'
        case '':
            return ''
def translate_probl(problem):

    match problem:
        case 'Сломался аккумулятор':
            return 'Broken battery'
        case 'Проблема с фильтром':
            return 'Filter problem'
        case 'Сломался мотор':
            return 'Broken motor'

def translate_serv(service):

    match service:
        case 'Замена аккумулятора':
            return 'Battery replacement'
        case 'Замена фильтра':
            return 'Filter replacement'
        case 'Чистка фильтра':
            return 'Filter cleaning'
        case 'Замена мотора':
            return 'Motor replacement'
        case 'Ремонт мотора':
            return 'Motor repair'

def check_vacuum_model(vacuum):

    if re.match(r'^[A-Za-z0-9 -]*$', vacuum):
        return True
    return False

def check_date(date):

     try:
         datetime.strptime(date, '%Y-%m-%d')
         return True
         #if date <= datetime.now():
          #  return True
         #return False
     except Exception as e:
         return False


def check_entry_master(log, pas):
    cursor = connection.cursor()

    try:
        entry_master = f"select id_employee from employee where employee_phone_number = {log} and password_empl = {pas} and id_post = 4;"
        cursor.execute(entry_master)
        row = cursor.fetchall()
        if row:
            id_m = row[0]['id_employee']
            cursor.close()
            return True, id_m
        else:
            return False
    except Exception as e:
        cursor.close()
        return False


def check_entry_administrator(log, pas):
    cursor = connection.cursor()

    try:
        entry_administrator = f"select id_employee from employee where employee_phone_number = {log} and password_empl = {pas} and id_post = 3;"
        cursor.execute(entry_administrator)
        row = cursor.fetchall()
        if row:
            id_a = row[0]['id_employee']
            cursor.close()
            return True, id_a
        else:
            return False
    except Exception as e:
        cursor.close()
        return False

def check_entry_admin(log, pas):
    cursor = connection.cursor()

    try:
        entry_admin = (f"select id_employee from employee where employee_phone_number = {log} "
                       f"and password_empl = {pas} and id_post = 5;")
        cursor.execute(entry_admin)
        row = cursor.fetchall()
        if row:
            id_ad = row[0]['id_employee']
            cursor.close()
            return True, id_ad
        else:
            return False
    except Exception as e:
        cursor.close()
        return False

def check_entry_client(log):
    cursor = connection.cursor()

    try:
        entry_client = (f"select id_client from client where phone_number = {log}")
        cursor.execute(entry_client)
        row = cursor.fetchall()
        if row:
            id_cl = row[0]['id_client']
            cursor.close()
            return True, id_cl
        else:
            return False
    except Exception as e:
        cursor.close()
        return False


def look_my_applications(id_master):

    cursor = connection.cursor()

    try:
        look_appl = (f"SELECT application.id_application, application.date_of_receipt, application.complicacy, status_of_application.status, "
	    f"client.phone_number AS 'Client phone', "
	    f"problem.type_problem, vacuum_cleaner.model, " 
	    f"Concat(employee.name,' ', employee.surname) AS 'Employee' "
	    f"FROM application "
	    f"JOIN client ON application.id_client = client.id_client "
	    f"JOIN vacuum_cleaner ON application.id_vacuum = vacuum_cleaner.id_vacuum "
	    f"JOIN problem ON application.id_problem = problem.id_problem "
	    f"JOIN employee ON application.id_employee = employee.id_employee "
	    f"JOIN status_of_application ON application.id_status = status_of_application.id_status "
        f"where employee.id_employee = {id_master} and application.id_status = 3 "
        f"ORDER BY date_of_receipt;")

        cursor.execute(look_appl)
        row = cursor.fetchall()
        cursor.close()
        return row

    except Exception as e:
        cursor.close()
        return False

def client_applications(id_client):

    cursor = connection.cursor()

    try:
        look_appl = (f"SELECT application.id_application, application.date_of_receipt, application.complicacy, status_of_application.status, "
	    f"client.phone_number AS 'Client phone', "
	    f"problem.type_problem, vacuum_cleaner.model, " 
	    f"Concat(employee.name,' ', employee.surname) AS 'Employee', application.ready_date "
	    f"FROM application "
	    f"JOIN client ON application.id_client = client.id_client "
	    f"JOIN vacuum_cleaner ON application.id_vacuum = vacuum_cleaner.id_vacuum "
	    f"JOIN problem ON application.id_problem = problem.id_problem "
	    f"LEFT JOIN employee ON application.id_employee = employee.id_employee "
	    f"JOIN status_of_application ON application.id_status = status_of_application.id_status "
        f"where client.id_client = {id_client} "
        f"ORDER BY date_of_receipt;")

        cursor.execute(look_appl)
        row = cursor.fetchall()
        cursor.close()
        return row

    except Exception as e:
        cursor.close()
        return False

def calculate_cost_appl(id_client, id_application):

    cursor = connection.cursor()
    try:
        ph = (f"select phone_number from client where id_client = {id_client}")
        cursor.execute(ph)
        row = cursor.fetchall()
        if row:
            phone = row[0]['phone_number']
            try:
                func = (f"select cost({phone}, {id_application}) as cost")
                cursor.execute(func)
                res = cursor.fetchall()
                cursor.close()
                return res[0]['cost']
            except Exception as e:
                cursor.close()
                print(e)
                return False

        else:
            cursor.close()
            return False

    except Exception as e:
        cursor.close()
        print(e)
        return e


def get_client_id(phone):
    cursor = connection.cursor()

    try:
        id_client = (f"select id_client from client where phone_number = {phone}")
        cursor.execute(id_client)
        row = cursor.fetchall()
        if row:
            id = row[0]['id_client']
            cursor.close()
            return True, id
        else:
            return False
    except Exception as e:
        cursor.close()
        print(e)
        return False

def add_service_client(id_application, service_type):
    cursor = connection.cursor()

    try:
        q = (f"select id_service from service where type = '{service_type}';")
        cursor.execute(q)
        id_s = cursor.fetchall()
        add_ = (f"insert into set_of_services(id_application, id_service) values({id_application}, {id_s[0]['id_service']});")
        cursor.execute(add_)
        connection.commit()
        cursor.close()
        return True
    except Exception as e:
        cursor.close()
        print(e)
        return False

def get_client_name(id_client):
    cursor = connection.cursor()

    try:
        name_client = (f"select name from client where id_client = {id_client}")
        cursor.execute(name_client)
        row = cursor.fetchall()
        if row:
            name = row[0]['name']
            cursor.close()
            return True, name
        else:
            return False
    except Exception as e:
        cursor.close()
        return False

def get_employee_name(id_employee):
    cursor = connection.cursor()

    try:
        name_empl = (f"select name from employee where id_employee = {id_employee}")
        cursor.execute(name_empl)
        row = cursor.fetchall()
        if row:
            name = row[0]['name']
            cursor.close()
            return name
        else:
            return False
    except Exception as e:
        cursor.close()
        return False


def take_work_m(id_application, id_employee):
    cursor = connection.cursor()

    try:
        check = (f"select id_employee from application "
                 f"where id_application = {id_application};")

        cursor.execute(check)
        row = cursor.fetchall()

        if row[0]['id_employee'] == None:

            try:
                cursor.callproc('take_work', (id_application, id_employee))
                connection.commit()
                cursor.close()
                return 'ok'

            except Exception as e:
                cursor.close()
                return 'error'
        else:
            cursor.close()
            return 'occupied'

    except Exception as e:
        cursor.close()
        return False



def look_application_with_status(status):
    cursor = connection.cursor()

    try:
        appl = (f"SELECT application.id_application, application.date_of_receipt, application.complicacy, "
	    f"status_of_application.status, client.phone_number AS 'Client phone', "
	    f"problem.type_problem, vacuum_cleaner.model "
	    f"FROM application "
	    f"JOIN client ON application.id_client = client.id_client "
	    f"JOIN vacuum_cleaner ON application.id_vacuum = vacuum_cleaner.id_vacuum "
	    f"JOIN problem ON application.id_problem = problem.id_problem "
	    f"JOIN status_of_application ON application.id_status = status_of_application.id_status "
        f"where status_of_application.status = '{status}' "
        f" order by date_of_receipt;")
        cursor.execute(appl)
        row = cursor.fetchall()
        cursor.close()
        return row

    except Exception as e:
        cursor.close()
        return False

if __name__ == '__main__':
    connection = connect_toBD()

    cursor = connection.cursor()
    query = (f"select id_post, tittle from post;")
    cursor.execute(query)
    row = cursor.fetchall()

    pos = [d['tittle'] for d in row]
    id_post = [d['id_post'] for d in row]
    cursor.close()

    i = pos.index('Master')
    res = id_post[i]
    print(res)

    close_connection(connection)





