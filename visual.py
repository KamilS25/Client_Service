import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import functional
from functional import *


def launch_widjets():
    global connection
    connection = functional.connect_toBD()
    tk.Button(Launch_frame, text='Старт', command=BackToMenu, font=('Arial', 25)).grid(column=0, row=0, padx=180,
                                                                                       pady=170)


def menu_widgets():
    tk.Button(Menu_frame, text="Для Админа", command=check_admin, font=('Arial', 15)).grid(column=0, row=1, padx=0,
                                                                                           pady=5)
    tk.Button(Menu_frame, text="Для сотрудника", command=go_to_worker, font=('Arial', 15)).grid(column=0, row=2, padx=0,
                                                                                                pady=5)
    tk.Button(Menu_frame, text="Выйти", command=exit_out, font=('Arial', 15)).grid(column=0, row=4, padx=0, pady=5)
    tk.Button(Menu_frame, text='Для клиента', command=check_client, font=('Arial', 15)).grid(column=0, row=3, padx=0,
                                                                                             pady=5)


def admin_widgets():
    name_admin = functional.get_employee_name(id_admin)
    tk.Label(Admin_frame, text=f'Хорошей работы, {name_admin}', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=0, padx=0, pady=15)

    tk.Button(Admin_frame, text='Вывести сотрудников', font=('Arial', 10), command=look_empl).grid(column=0, row=1,
                                                                                                   padx=0, pady=5)
    tk.Button(Admin_frame, text='Добавить сотрудника', font=('Arial', 10), command=add_empl).grid(column=0, row=2,
                                                                                                  padx=0, pady=5)
    tk.Button(Admin_frame, text='Удалить сотрудника', font=('Arial', 10), command=del_empl).grid(column=0, row=3,
                                                                                                 padx=0, pady=5)


    tk.Button(Admin_frame, text='Вывести отделы', font=('Arial', 10), command=look_depart).grid(column=0, row=4,
                                                                                                padx=0, pady=5)
    tk.Button(Admin_frame, text='Добавить отдел', font=('Arial', 10), command=add_depart).grid(column=0, row=5,
                                                                                               padx=0, pady=5)
    tk.Button(Admin_frame, text='Удалить отдел', font=('Arial', 10), command=del_depart).grid(column=0, row=6,
                                                                                              padx=0, pady=5)
    tk.Button(Admin_frame, text='Вернуться в меню', font=('Arial', 10), command=BackToMenu).grid(column=0, row=7,
                                                                                                 padx=0, pady=5)


def worker_widgets():
    tk.Button(Worker_frame, text='Мастер', font=('Arial', 10), command=check_master).grid(column=0, row=2, padx=0,
                                                                                          pady=5)
    tk.Button(Worker_frame, text='Администратор', font=('Arial', 10), command=check_administrator).grid(column=0, row=6,
                                                                                                        padx=0, pady=5)
    tk.Button(Worker_frame, text='Вернуться в меню', font=('Arial', 10), command=BackToMenu).grid(column=0, row=8,
                                                                                                  padx=0, pady=5)


def client_widjets():
    name_c = functional.get_client_name(id_client)

    print(name_c)

    tk.Label(Client_frame, text=f'Здравствуйте, {name_c[1]}', fg='black',
             font=('Arial', 15, 'bold')).grid(column=0, row=0, padx=0, pady=15)
    tk.Button(Client_frame, text='Посмотреть мои заявки', font=('Arial', 10), command=client_application).grid(column=0,
                                                                                                               row=1,
                                                                                                               padx=0,
                                                                                                               pady=5)
    global EnterID
    EnterID = tk.Entry(Client_frame, bg='white', font=10)
    EnterID.grid(column=1, row=2, padx=5, pady=5)

    tk.Label(Client_frame, text='Введите номер заявки', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=2, padx=0, pady=15)
    tk.Button(Client_frame, text='Рассчитать стоимость', font=('Arial', 10), command=calculate_cost).grid(column=0,
                                                                                                          row=3, padx=0,
                                                                                                          pady=5)
    tk.Button(Client_frame, text='Вернуться в меню', font=('Arial', 10), command=BackToMenu).grid(column=0, row=7,
                                                                                                  padx=0, pady=5)


def administrator_widjets():
    name_ad = functional.get_employee_name(id_administrator)
    tk.Label(Administrator_frame, text=f'Хорошей работы, {name_ad}', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=0, padx=0, pady=15)

    tk.Button(Administrator_frame, text='Добавить нового клиента', font=('Arial', 10), command=add_client).grid(
        column=0,
        row=1, padx=0,
        pady=5)

    global EnterPhoneAd
    EnterPhoneAd = tk.Entry(Administrator_frame, bg='white', font=10)
    EnterPhoneAd.grid(column=0, row=3, padx=0, pady=5)

    tk.Label(Administrator_frame, text='Введите номер клиента', font=('Arial', 10)).grid(column=0, row=2, padx=0,
                                                                                         pady=5)
    tk.Button(Administrator_frame, text='Посмотреть заявки клиента', font=('Arial', 10),
              command=look_client_appl_from_ad).grid(column=0, row=4, padx=0,
                                                     pady=5)
    tk.Button(Administrator_frame, text='Добавить услугу к заявке клиента', font=('Arial', 10),
              command=add_service).grid(column=0, row=5, padx=0, pady=5)
    tk.Button(Administrator_frame, text='Просмотр заявок', font=('Arial', 10),
              command=applications_for_ad).grid(column=0, row=6, padx=0, pady=5)
    tk.Button(Administrator_frame, text='Вернуться в меню', font=('Arial', 10), command=BackToMenu).grid(column=0,
                                                                                                         row=7, padx=0,
                                                                                                         pady=5)


def master_widjets():
    name_master = functional.get_employee_name(id_master)
    tk.Label(Master_frame, text=f'Хорошей работы, {name_master}', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=0, padx=0, pady=15)

    tk.Button(Master_frame, text='Мои заявки', font=('Arial', 10), command=master_application).grid(column=0, row=1,
                                                                                                    padx=0,
                                                                                                    pady=5)
    tk.Button(Master_frame, text='Новые заявки', font=('Arial', 10), command=application_status_master).grid(column=0,
                                                                                                             row=2,
                                                                                                             padx=0,
                                                                                                             pady=5)
    tk.Button(Master_frame, text='Взять заявку в работу', font=('Arial', 10), command=take_application_to_work).grid(
        column=0,
        row=3,
        padx=0,
        pady=5)

    tk.Button(Master_frame, text='Отметить выполненную заявку', font=('Arial', 10), command=ready_applic).grid(column=0,
                                                                                                               row=5,
                                                                                                               padx=0,
                                                                                                               pady=5)

    tk.Button(Master_frame, text='Посмотреть услуги к заявке', font=('Arial', 10), command=look_services).grid(column=0,
                                                                                                               row=4,
                                                                                                               padx=0,
                                                                                                               pady=5)

    tk.Button(Master_frame, text='Вернуться в меню', font=('Arial', 10), command=BackToMenu).grid(column=0, row=6,
                                                                                                  padx=0, pady=5)


def del_empl():
    window_for_admin_delE = tk.Toplevel(window)
    window_for_admin_delE.title('')

    admin_frame_delE = tk.Frame(window_for_admin_delE, width=200, height=200)
    admin_frame_delE.grid()

    def confirm_empl_del():
        ph = EnterPhoneE.get()

        if functional.phone_check(ph):

            if functional.delete_empl(ph):
                messagebox.showinfo('', 'Сотрудник удалён!')
                window_for_admin_delE.destroy()
            else:
                messagebox.showerror('Ошибка', 'Что-то пошло не так...')
                window_for_admin_delE.destroy()
        else:
            messagebox.showerror('Ошибка', 'Неправильно введен номер\n'
                                           'Формат: 8xxxxxxxxxx ')

    tk.Label(admin_frame_delE,
             text='Выберите номер телефона сотрудника: ',
             fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=0, padx=0, pady=5)

    global EnterPhoneE
    EnterPhoneE = tk.Entry(admin_frame_delE, bg='white', font=10)
    EnterPhoneE.grid(column=0, row=1, padx=0, pady=5)

    tk.Button(admin_frame_delE, text='Подтвердить', font=('Arial', 10), command=confirm_empl_del).grid(column=0, row=6,
                                                                                                       padx=0, pady=5)


def del_depart():
    window_for_admin_delD = tk.Toplevel(window)
    window_for_admin_delD.geometry('200x200')
    window_for_admin_delD.title('')

    admin_frame_delD = tk.Frame(window_for_admin_delD, width=200, height=200)
    admin_frame_delD.grid()

    def confirm_depart_del():
        addr = ChooseAdrFordel.get()

        if len(addr) > 0:
            id_dep = functional.get_id_dep(addr)

            if id_dep != False:

                if functional.delete_depart(id_dep):
                    messagebox.showinfo('', 'Отдел удалён!')
                    window_for_admin_delD.destroy()
                else:
                    messagebox.showerror('Ошибка', 'Что-то пошло не так...')
                    window_for_admin_delD.destroy()
            else:
                messagebox.showerror('Ошибка', 'Что-то пошло не так...')
                window_for_admin_delD.destroy()
        else:
            messagebox.showerror('', 'Выберите адрес отдела!')

    tk.Label(admin_frame_delD,
             text='Выберите адрес отдела: ',
             fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=0, padx=0, pady=5)

    adr_d = functional.get_addresses()
    global address_d
    if adr_d != False:
        address_d = [d['address_department'] for d in adr_d]
        address_d.remove('Moscow, Prospect mira 7')
    else:
        messagebox.showerror('', 'Что-то пошло не так...')

    global ChooseAdrForW
    ChooseAdrFordel = ttk.Combobox(admin_frame_delD, values=address_d, state="readonly")
    ChooseAdrFordel.grid(column=0, row=1, padx=0, pady=5)

    tk.Button(admin_frame_delD, text='Подтвердить', font=('Arial', 10), command=confirm_depart_del).grid(column=0,
                                                                                                         row=6,
                                                                                                         padx=0, pady=5)


def add_depart():
    window_for_admin3 = tk.Toplevel(window)
    window_for_admin3.geometry('600x200')
    window_for_admin3.title('')

    admin3_frame = tk.Frame(window_for_admin3, width=600, height=300)
    admin3_frame.grid()

    def confirm_depart():
        addr_d = EnterAddr.get()
        addr_w = ChooseAdrForW.get()

        if functional.check_address(addr_d) and len(addr_w) > 0:
            id_war = functional.get_id_warehouse(addr_w)
            if id_war != False:

                if functional.add_depart(addr_d, id_war):
                    messagebox.showinfo('', 'Отдел добавлен!')
                    window_for_admin3.destroy()
                else:
                    messagebox.showerror('Ошибка', 'Что-то пошло не так...')
                    window_for_admin3.destroy()

            else:
                messagebox.showerror('Ошибка', 'Что-то пошло не так...')
                window_for_admin3.destroy()
        else:
            messagebox.showerror('Ошибка', 'Неправильный ввод адреса')

    tk.Label(Administrator_frame, text='Введите данные отдела', font=('Arial', 10)).grid(column=1, row=0, padx=0,
                                                                                         pady=5)

    global EnterAddr
    tk.Label(admin3_frame, text='Введите адрес отдела(На английском): ', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=1, padx=0, pady=5)
    tk.Label(admin3_frame, text='(Формат: City, street №), Пример: Moscow, Arbat street 5', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=2, padx=0, pady=5)
    EnterAddr = tk.Entry(admin3_frame, bg='white', font=10)
    EnterAddr.grid(column=1, row=3, padx=0, pady=5)

    tk.Label(admin3_frame,
             text='Выберите адрес склада: ',
             fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=4, padx=0, pady=5)

    adr_w = functional.get_addresses_warehouse()
    global address_w
    if adr_w != False:
        address_w = [d['address'] for d in adr_w]
    else:
        messagebox.showerror('', 'Что-то пошло не так...')

    global ChooseAdrForW
    ChooseAdrForW = ttk.Combobox(admin3_frame, values=address_w, state="readonly")
    ChooseAdrForW.grid(column=1, row=4, padx=0, pady=5)

    tk.Button(admin3_frame, text='Подтвердить', font=('Arial', 10), command=confirm_depart).grid(column=0, row=6,
                                                                                                 padx=0, pady=5)


def look_depart():
    window_for_adminD = tk.Toplevel(window)
    window_for_adminD.geometry('600x200')
    window_for_adminD.title('')

    aD_frame = tk.Frame(window_for_adminD, width=600, height=300)
    aD_frame.grid()

    tree = ttk.Treeview(aD_frame, column=('id', 'address_department', 'address'), height=8,
                        show='headings')

    tree.column('id', width=200, anchor=tk.CENTER)
    tree.column('address_department', width=200, anchor=tk.CENTER)
    tree.column('address', width=200, anchor=tk.CENTER)

    tree.heading('id', text='Номер департамента')
    tree.heading('address_department', text='Адрес отдела')
    tree.heading('address', text='Адрес склада')

    tree.pack()

    a = functional.get_depart()

    if a != False:
        id_dep = [d['id_department'] for d in a]
        adr_d = [d['address_department'] for d in a]
        adr_w = [d['address'] for d in a]
        data = [id_dep, adr_d, adr_w]

        first = len(id_dep)
        second = len(data)
        for i in range(0, first):
            temp = []
            for j in range(0, second):
                temp.append(data[j][i])

            tree.insert('', 'end', values=temp)

    else:
        messagebox.showerror('Ошибка', 'Что-то пошло не так')
        window_for_adminD.destroy()


def add_empl():
    global window_for_admin2
    window_for_admin2 = tk.Toplevel(window)
    window_for_admin2.geometry('1000x500')
    window_for_admin2.title('Новый клиент')

    admin_frame2 = tk.Frame(window_for_admin2, width=0, height=15)
    admin_frame2.grid()

    tk.Label(admin_frame2, text='Введите данные', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=0, padx=50, pady=5)

    global EnterPhoneE
    tk.Label(admin_frame2, text='Номер телефона(Формат: 8xxxxxxxxxx): ', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=1, padx=0, pady=5)
    EnterPhoneE = tk.Entry(admin_frame2, bg='white', font=10)
    EnterPhoneE.grid(column=1, row=1, padx=0, pady=5)

    global EnterNameE
    tk.Label(admin_frame2, text='Имя(На английском языке, без пробелов): ', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=2, padx=0, pady=5)
    EnterNameE = tk.Entry(admin_frame2, bg='white', font=10)
    EnterNameE.grid(column=1, row=2, padx=0, pady=5)

    global EnterSurname
    tk.Label(admin_frame2, text='Фамилия(На английском языке, без пробелов): ', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=3, padx=0, pady=5)
    EnterSurname = tk.Entry(admin_frame2, bg='white', font=10)
    EnterSurname.grid(column=1, row=3, padx=0, pady=5)

    global EnterAge
    tk.Label(admin_frame2, text='Возраст, только цифра: ', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=4, padx=0, pady=5)
    EnterAge = tk.Entry(admin_frame2, bg='white', font=10)
    EnterAge.grid(column=1, row=4, padx=0, pady=5)

    global EnterExp
    tk.Label(admin_frame2,
             text='Введите опыт работы(Используйте только цифры без пробелов, если не имеется, писать 0): ',
             fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=5, padx=0, pady=5)
    EnterExp = tk.Entry(admin_frame2, bg='white', font=10)
    EnterExp.grid(column=1, row=5, padx=0, pady=5)

    tk.Label(admin_frame2,
             text='Выберите адрес отдела: ',
             fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=6, padx=0, pady=5)
    adr = functional.get_addresses()
    global address
    if adr != False:
        address = [d['address_department'] for d in adr]
    else:
        messagebox.showerror('', 'Что-то пошло не так...')
    global ChooseAdrForA
    ChooseAdrForA = ttk.Combobox(admin_frame2, values=address, state="readonly")
    ChooseAdrForA.grid(column=1, row=6, padx=0, pady=5)

    tk.Label(admin_frame2,
             text='Выберите должность: ',
             fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=7, padx=0, pady=5)
    global ChoosePost
    p = ['Директор', 'Бухгалтер', 'Администратор', 'Мастер', 'Админ']
    ChoosePost = ttk.Combobox(admin_frame2, values=p, state="readonly")
    ChoosePost.grid(column=1, row=7, padx=0, pady=5)

    global EnterPassw
    tk.Label(admin_frame2, text='Введите пароль(Не более 20 символов): ', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=8, padx=0, pady=5)
    EnterPassw = tk.Entry(admin_frame2, bg='white', font=10)
    EnterPassw.grid(column=1, row=8, padx=0, pady=5)

    tk.Button(admin_frame2, text='Подтверждение', font=('Arial', 10), command=confirm_empl).grid(column=0,
                                                                                                 row=9, padx=0,
                                                                                                 pady=15)


def confirm_empl():
    phone = EnterPhoneE.get()
    name = EnterNameE.get()
    surname = EnterSurname.get()
    age = EnterAge.get()
    exp = EnterExp.get()
    dep = ChooseAdrForA.get()
    title = ChoosePost.get()
    passw = EnterPassw.get()

    if functional.phone_check(phone):

        if functional.check_name(name) and functional.check_name(surname):

            if len(age) != 0 and age.isdigit():
                age = age if (int(age) <= 90) and (int(age) >= 16) else 0

                if age != 0:

                    if len(exp) <= 60 and exp.isdigit():

                        exp = exp + ' year' if (int(exp) <= 1) else exp + ' years'
                        if len(dep) > 0:
                            id_depart = functional.get_id_dep(dep)

                            if len(title) > 0:
                                post = functional.translate_post(title)
                                id_post = functional.get_id_post(post)

                                if len(passw) > 0 and len(passw) <= 20:

                                    if functional.new_empl(phone, name, surname, age, exp, id_depart, id_post, passw):
                                        messagebox.showinfo('', 'Новый сотрудник добавлен!')
                                        window_for_admin2.destroy()
                                    else:
                                        messagebox.showerror('Ошибка', 'Что-то пошло не так!')

                                else:
                                    messagebox.showerror('Ошибка',
                                                         'Пароль должен содержать не более 20 символов!\n'
                                                         'Пустым это поле оставлять нельзя!')

                            else:
                                messagebox.showerror('Ошибка',
                                                     'Вы не выбрали должность')
                        else:
                            messagebox.showerror('Ошибка',
                                                 'Вы не выбрали адрес отдела')

                    else:
                        messagebox.showerror('Ошибка',
                                             'Неправильно введен опыт работы.\n'
                                             '0, если опыт отсутствует.\n'
                                             'Если введена очень большая цифра, то вводите правду, не обманывайте!')
                else:
                    messagebox.showerror('Ошибка', 'Человеку либо на пенсию пора, либо слишком молод :)')
            else:
                messagebox.showerror('Ошибка', 'Неправильно введен возраст!')
        else:
            messagebox.showerror('Ошибка', 'Неправильно введено имя или фамилия\n'
                                           'Имя, фамилия не должны превышать более 20 символов')

    else:
        messagebox.showerror('Ошибка', 'Неправильно введен номер телефона!')


def look_empl():
    window_for_admin = tk.Toplevel(window)
    window_for_admin.geometry('800x400')
    window_for_admin.title('Заявки')

    admin_frame = tk.Frame(window_for_admin, width=400, height=400)
    admin_frame.grid()

    tk.Label(admin_frame, text='Задать параметры:', font=('Arial', 10, 'bold')).grid(column=1, row=1, padx=0,
                                                                                     pady=5)
    tk.Label(admin_frame, text='Выберите адрес отдела, можно оставить пустым: ', font=('Arial', 10, 'bold')).grid(
        column=0, row=2,
        padx=0,
        pady=5)

    tk.Label(admin_frame, text='Выберите должность, можно оставить пустым: ', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=3, padx=0, pady=5)

    adr = functional.get_addresses()

    if adr != False:
        global address
        address = [d['address_department'] for d in adr]
    else:
        messagebox.showerror('', 'Что-то пошло не так...')

    global ChooseAdr
    ChooseAdr = ttk.Combobox(admin_frame, values=address, state="readonly")
    ChooseAdr.grid(column=1, row=2, padx=0, pady=5)

    global ChoosePost
    p = ['Директор', 'Бухгалтер', 'Администратор', 'Мастер', 'Админ']
    ChoosePost = ttk.Combobox(admin_frame, values=p, state="readonly")
    ChoosePost.grid(column=1, row=3, padx=0, pady=5)

    global ChooseSortA
    sortA = ['Возрасту', 'Должности']
    ChooseSortA = ttk.Combobox(admin_frame, values=sortA, state="readonly")
    ChooseSortA.grid(column=1, row=4, padx=0, pady=5)

    tk.Label(admin_frame, text='Отсортировать по: (можно не заполнять)', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=4, padx=0, pady=5)

    tk.Button(admin_frame, text='Вывести сотрудников', font=('Arial', 10), command=empl_with_param).grid(column=1,
                                                                                                         row=6, padx=0,
                                                                                                         pady=5)


def empl_with_param():
    window_for_paramE = tk.Toplevel(window)
    window_for_paramE.geometry('1050x600')
    window_for_paramE.title('Заявки')

    ad_frame_paramE = tk.Frame(window_for_paramE, width=1050, height=600)
    ad_frame_paramE.grid()

    tree = ttk.Treeview(ad_frame_paramE, column=('id', 'employee', 'age', 'employee_phone_number', 'address_department',
                                                 'tittle', 'password_empl'), height=30, show='headings')

    tree.column('id', width=150, anchor=tk.CENTER)
    tree.column('employee', width=150, anchor=tk.CENTER)
    tree.column('age', width=150, anchor=tk.CENTER)
    tree.column('employee_phone_number', width=150, anchor=tk.CENTER)
    tree.column('address_department', width=150, anchor=tk.CENTER)
    tree.column('tittle', width=150, anchor=tk.CENTER)
    tree.column('password_empl', width=150, anchor=tk.CENTER)

    tree.heading('id', text='Номер')
    tree.heading('employee', text='ФИО')
    tree.heading('age', text='Возраст')
    tree.heading('employee_phone_number', text='Номер телефона')
    tree.heading('address_department', text='Адрес отдела')
    tree.heading('tittle', text='Должность')
    tree.heading('password_empl', text='Пароль')

    tree.pack()

    adr = ChooseAdr.get()
    post = ChoosePost.get()
    sorEmpl = ChooseSortA.get()

    post_eng = functional.translate_post(post)
    sorEmpl_eng = functional.translate_sorForEmpl(sorEmpl)

    a = functional.get_empl_with_param(adr, post_eng, sorEmpl_eng)

    if a != False:
        id_e = [d['id_employee'] for d in a]
        empl = [d['employee'] for d in a]
        age = [d['age'] for d in a]
        phone = [d['employee_phone_number'] for d in a]
        addr = [d['address_department'] for d in a]
        tit = [d['tittle'] for d in a]
        passw = [d['password_empl'] for d in a]
        data = [id_e, empl, age, phone, addr, tit, passw]

        first = len(id_e)
        second = len(data)
        for i in range(0, first):
            temp = []
            for j in range(0, second):
                temp.append(data[j][i])

            tree.insert('', 'end', values=temp)

    else:
        messagebox.showerror('Ошибка', 'Что-то пошло не так')
        window_for_paramE.destroy()


def look_services():
    window_for_ms = tk.Toplevel(window)
    window_for_ms.geometry('240x200')
    window_for_ms.title('')

    ms_frame = tk.Frame(window_for_ms, width=240, height=300)
    ms_frame.grid()

    tree = ttk.Treeview(ms_frame, column=('id', 'service'), height=5,
                        show='headings')

    tree.column('id', width=120, anchor=tk.CENTER)
    tree.column('service', width=120, anchor=tk.CENTER)

    tree.heading('id', text='Номер заявки')
    tree.heading('service', text='Услуга')

    tk.Label(ms_frame, text='Введите номер заявки: ', font=('Arial', 10, 'bold')).grid(column=0, row=0, padx=0,
                                                                                       pady=5)

    def look_s():
        window_for_ms2 = tk.Toplevel(window)
        window_for_ms2.geometry('240x300')
        window_for_ms2.title('')

        ms_frame2 = tk.Frame(window_for_ms2, width=240, height=300)
        ms_frame2.grid()

        id_applic = EnterIDMs.get()

        tree = ttk.Treeview(ms_frame2, column=('id', 'service'), height=5,
                            show='headings')

        tree.column('id', width=120, anchor=tk.CENTER)
        tree.column('service', width=120, anchor=tk.CENTER)

        tree.heading('id', text='Номер заявки')
        tree.heading('service', text='Услуга')

        tree.pack()

        a = functional.get_services_appl(id_applic)

        if a != False:
            id_ap = [d['id_application'] for d in a]
            tp = [d['type'] for d in a]
            data = [id_ap, tp]

            first = len(id_ap)
            second = len(data)
            for i in range(0, first):
                temp = []
                for j in range(0, second):
                    temp.append(data[j][i])

                tree.insert('', 'end', values=temp)

        else:
            messagebox.showerror('Ошибка', 'Что-то пошло не так')
            window_for_ms2.destroy()

    EnterIDMs = tk.Entry(ms_frame, bg='white', font=10)
    EnterIDMs.grid(column=0, row=1, padx=0, pady=5)

    tk.Button(ms_frame, text='Подтвердить', font=('Arial', 10), command=look_s).grid(column=0, row=2, padx=0, pady=5)


def ready_applic():
    window_for_m = tk.Toplevel(window)
    window_for_m.geometry('200x200')
    window_for_m.title('')

    m_frame2 = tk.Frame(window_for_m, width=200, height=200)
    m_frame2.grid()

    tk.Label(m_frame2, text='Введите номер заявки', font=('Arial', 10)).grid(column=0, row=0, padx=0,
                                                                             pady=5)

    def change_for_ready():
        id_applic = EnterIDM.get()

        if change_status_for_ready(id_applic, id_master):
            messagebox.showinfo('Поздравляем', 'Завяка выполнена, так держать!')
            window_for_m.destroy()
        else:
            messagebox.showerror('Ошибка', 'Что-то пошло не так...\n'
                                           'Проверьте правильность номера заявки.\n'
                                           'Возможно, Вы пытаетесь закрыть чужую заявку')

    EnterIDM = tk.Entry(m_frame2, bg='white', font=10)
    EnterIDM.grid(column=0, row=1, padx=0, pady=5)

    tk.Button(m_frame2, text='Подтвердить', font=('Arial', 10), command=change_for_ready).grid(column=0,
                                                                                               row=2, padx=0,
                                                                                               pady=5)


def applications_for_ad():
    window_for_ad4 = tk.Toplevel(window)
    window_for_ad4.geometry('800x400')
    window_for_ad4.title('Заявки')

    ad_frame4 = tk.Frame(window_for_ad4, width=400, height=400)
    ad_frame4.grid()

    tk.Button(ad_frame4, text='Вывести все заявки', font=('Arial', 10), command=all_applic).grid(column=1,
                                                                                                 row=0, padx=0,
                                                                                                 pady=5)
    tk.Label(ad_frame4, text='Заявки с параметрами:', font=('Arial', 10, 'bold')).grid(column=1, row=1, padx=0,
                                                                                       pady=5)
    tk.Label(ad_frame4, text='Дата получения "от и до" (Формат: year-mm-dd)', font=('Arial', 10, 'bold')).grid(column=0,
                                                                                                               row=2,
                                                                                                               padx=0,
                                                                                                               pady=5)
    global EnterFrom
    EnterFrom = tk.Entry(ad_frame4, bg='white', font=10)
    EnterFrom.grid(column=1, row=3, padx=0, pady=5)
    global EnterTo
    EnterTo = tk.Entry(ad_frame4, bg='white', font=10)
    EnterTo.grid(column=2, row=3, padx=0, pady=5)

    tk.Label(ad_frame4, text='Выберите статус, если не нужно, не заполняйте: ', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=4, padx=0, pady=5)
    stat = ['Принят', 'В работе', 'Готов']
    global ChooseStatus
    ChooseStatus = ttk.Combobox(ad_frame4, values=stat, state="readonly")
    ChooseStatus.grid(column=1, row=4, padx=0, pady=5)

    tk.Label(ad_frame4, text='Отсортировать по: (можно не заполнять)', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=5, padx=0, pady=5)

    global ChooseSort
    sortF = ['Дате приема', 'Статусу']
    ChooseSort = ttk.Combobox(ad_frame4, values=sortF, state="readonly")
    ChooseSort.grid(column=1, row=5, padx=0, pady=5)

    tk.Button(ad_frame4, text='Вывести заявки', font=('Arial', 10), command=applic_with_param).grid(column=1,
                                                                                                    row=6, padx=0,
                                                                                                    pady=5)


def applic_with_param():
    window_for_param = tk.Toplevel(window)
    window_for_param.geometry('1080x600')
    window_for_param.title('Заявки')

    ad_frame_param = tk.Frame(window_for_param, width=1080, height=600)
    ad_frame_param.grid()

    tree = ttk.Treeview(ad_frame_param, column=('id', 'date', 'complicacy', 'status', 'phone',
                                                'problem', 'model', 'employee', 'ready_date',), height=30,
                        show='headings')

    tree.column('id', width=120, anchor=tk.CENTER)
    tree.column('date', width=120, anchor=tk.CENTER)
    tree.column('complicacy', width=120, anchor=tk.CENTER)
    tree.column('status', width=120, anchor=tk.CENTER)
    tree.column('phone', width=120, anchor=tk.CENTER)
    tree.column('problem', width=120, anchor=tk.CENTER)
    tree.column('model', width=120, anchor=tk.CENTER)
    tree.column('employee', width=120, anchor=tk.CENTER)
    tree.column('ready_date', width=120, anchor=tk.CENTER)

    tree.heading('id', text='Номер заявки')
    tree.heading('date', text='Дата получения')
    tree.heading('complicacy', text='Сложность')
    tree.heading('status', text='Статус заказа')
    tree.heading('phone', text='Телефон клиента')
    tree.heading('problem', text='Тип проблемы')
    tree.heading('model', text='Модель')
    tree.heading('employee', text='Сотрудник')
    tree.heading('ready_date', text="Дата готовности")

    tree.pack()

    from_ = EnterFrom.get()
    to_ = EnterTo.get()
    stat = ChooseStatus.get()
    sor = ChooseSort.get()

    stat_eng = functional.translate_stat(stat)
    sor_eng = functional.translate_sort(sor)

    if (functional.check_date(from_) and (functional.check_date(to_))) or ((len(from_) == 0) and (len(to_) == 0)):
        a = functional.get_applications_with_param(from_, to_, stat_eng, sor_eng)

        if a != False:
            id_ap = [d['id_application'] for d in a]
            date_of = [d['date_of_receipt'] for d in a]
            compl = [d['complicacy'] for d in a]
            stat = [d['status'] for d in a]
            client_ph = [d['Client phone'] for d in a]
            probl = [d['type_problem'] for d in a]
            model_ = [d['model'] for d in a]
            empl = [d['Employee'] for d in a]
            rdate = [d['ready_date'] for d in a]
            data = [id_ap, date_of, compl, stat, client_ph, probl, model_, empl, rdate]

            first = len(id_ap)
            second = len(data)
            for i in range(0, first):
                temp = []
                for j in range(0, second):
                    temp.append(data[j][i])

                tree.insert('', 'end', values=temp)

        else:
            messagebox.showerror('Ошибка', 'Что-то пошло не так')
            window_for_param.destroy()
    else:
        messagebox.showerror('Внимание', '1. Проверьте правильность ввода даты(пример: 2023-03-12).\n'
                                         '2. Возможно, в одну ячейки вы ввели данные, а в другую нет, так нельзя!')


def all_applic():
    window_for_all = tk.Toplevel(window)
    window_for_all.geometry('1080x600')
    window_for_all.title('Заявки')

    ad_frame_all = tk.Frame(window_for_all, width=1080, height=600)
    ad_frame_all.grid()

    tree = ttk.Treeview(ad_frame_all, column=('id', 'date', 'complicacy', 'status', 'phone',
                                              'problem', 'model', 'employee', 'ready_date',), height=30,
                        show='headings')

    tree.column('id', width=120, anchor=tk.CENTER)
    tree.column('date', width=120, anchor=tk.CENTER)
    tree.column('complicacy', width=120, anchor=tk.CENTER)
    tree.column('status', width=120, anchor=tk.CENTER)
    tree.column('phone', width=120, anchor=tk.CENTER)
    tree.column('problem', width=120, anchor=tk.CENTER)
    tree.column('model', width=120, anchor=tk.CENTER)
    tree.column('employee', width=120, anchor=tk.CENTER)
    tree.column('ready_date', width=120, anchor=tk.CENTER)

    tree.heading('id', text='Номер заявки')
    tree.heading('date', text='Дата получения')
    tree.heading('complicacy', text='Сложность')
    tree.heading('status', text='Статус заказа')
    tree.heading('phone', text='Телефон клиента')
    tree.heading('problem', text='Тип проблемы')
    tree.heading('model', text='Модель')
    tree.heading('employee', text='Сотрудник')
    tree.heading('ready_date', text="Дата готовности")

    tree.pack()

    a = functional.get_all_applications()

    if a != False:
        id_ap = [d['id_application'] for d in a]
        date_of = [d['date_of_receipt'] for d in a]
        compl = [d['complicacy'] for d in a]
        stat = [d['status'] for d in a]
        client_ph = [d['Client phone'] for d in a]
        probl = [d['type_problem'] for d in a]
        model_ = [d['model'] for d in a]
        empl = [d['Employee'] for d in a]
        rdate = [d['ready_date'] for d in a]
        data = [id_ap, date_of, compl, stat, client_ph, probl, model_, empl, rdate]

        first = len(id_ap)
        second = len(data)
        for i in range(0, first):
            temp = []
            for j in range(0, second):
                temp.append(data[j][i])

            tree.insert('', 'end', values=temp)

    else:
        messagebox.showerror('Ошибка', 'Что-то пошло не так')
        window_for_all.destroy()


def add_service():
    window_for_ad3 = tk.Toplevel(window)
    window_for_ad3.geometry('400x400')
    window_for_ad3.title('Заявки')

    ad_frame3 = tk.Frame(window_for_ad3, width=400, height=200)
    ad_frame3.grid()

    tk.Label(ad_frame3, text='Введите номер заявки', font=('Arial', 10, 'bold')).grid(column=0, row=0, padx=0,
                                                                                      pady=5)
    EnterIDApl = tk.Entry(ad_frame3, bg='white', font=10)
    EnterIDApl.grid(column=1, row=0, padx=0, pady=5)

    tk.Label(ad_frame3, text='Выберите услугу: ', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=1, padx=0, pady=5)
    serv = ['Замена аккумулятора', 'Замена фильтра', 'Чистка фильтра', 'Замена мотора', 'Ремонт мотора']
    AddServ = ttk.Combobox(ad_frame3, values=serv, state="readonly")
    AddServ.grid(column=1, row=1, padx=0, pady=5)

    def confirm_serv():

        id = EnterIDApl.get()
        serv = AddServ.get()

        if len(serv) > 0:
            serv_eng = functional.translate_serv(serv)
            if functional.add_service_client(id, serv_eng):
                messagebox.showinfo('', 'Услуга добавлена')
                window_for_ad3.destroy()
            else:
                messagebox.showerror('Ошибка', 'Проверьте правильность номера заявки')
        else:
            messagebox.showerror('Ошибка', 'Вы не выбрали услугу')

    tk.Button(ad_frame3, text='Подтвердить', font=('Arial', 10), command=confirm_serv).grid(column=1, row=2,
                                                                                            padx=0,
                                                                                            pady=5)


def look_client_appl_from_ad():
    window_for_ad2 = tk.Toplevel(window)
    window_for_ad2.geometry('900x320')
    window_for_ad2.title('Заявки')

    ad_frame2 = tk.Frame(window_for_ad2, width=900, height=320)
    ad_frame2.grid()

    tree = ttk.Treeview(ad_frame2, column=('id', 'date', 'complicacy', 'status', 'phone',
                                           'problem', 'model', 'employee', 'ready_date',), height=15, show='headings')

    tree.column('id', width=100, anchor=tk.CENTER)
    tree.column('date', width=100, anchor=tk.CENTER)
    tree.column('complicacy', width=100, anchor=tk.CENTER)
    tree.column('status', width=100, anchor=tk.CENTER)
    tree.column('phone', width=100, anchor=tk.CENTER)
    tree.column('problem', width=100, anchor=tk.CENTER)
    tree.column('model', width=100, anchor=tk.CENTER)
    tree.column('employee', width=100, anchor=tk.CENTER)
    tree.column('ready_date', width=100, anchor=tk.CENTER)

    tree.heading('id', text='Номер заявки')
    tree.heading('date', text='Дата получения')
    tree.heading('complicacy', text='Сложность')
    tree.heading('status', text='Статус заказа')
    tree.heading('phone', text='Телефон клиента')
    tree.heading('problem', text='Тип проблемы')
    tree.heading('model', text='Модель')
    tree.heading('employee', text='Сотрудник')
    tree.heading('ready_date', text="Дата готовности")

    tree.pack()

    phone = EnterPhoneAd.get()
    if functional.phone_check(phone):
        id_client_to_ad = functional.get_client_id(phone)

        a = functional.client_applications(id_client_to_ad[1])
        if a != False:
            id_ap = [d['id_application'] for d in a]
            date_of = [d['date_of_receipt'] for d in a]
            compl = [d['complicacy'] for d in a]
            stat = [d['status'] for d in a]
            client_ph = [d['Client phone'] for d in a]
            probl = [d['type_problem'] for d in a]
            model_ = [d['model'] for d in a]
            empl = [d['Employee'] for d in a]
            rdate = [d['ready_date'] for d in a]
            data = [id_ap, date_of, compl, stat, client_ph, probl, model_, empl, rdate]

            first = len(id_ap)
            second = len(data)
            for i in range(0, first):
                temp = []
                for j in range(0, second):
                    temp.append(data[j][i])

                tree.insert('', 'end', values=temp)

        else:
            messagebox.showerror('Ошибка', 'Проверьте правильность номера клиента')
            window_for_ad2.destroy()
            go_to_administrator()
    else:
        messagebox.showerror('', 'Неправильно введен номер\n'
                                 'Формат: 8xxxxxxxxxx')


def add_client():
    global window_for_ad
    window_for_ad = tk.Toplevel(window)
    window_for_ad.geometry('1000x500')
    window_for_ad.title('Новый клиент')

    ad_frame = tk.Frame(window_for_ad, width=0, height=15)
    ad_frame.grid()

    tk.Label(ad_frame, text='Введите данные', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=0, padx=50, pady=5)

    global EnterPhone
    tk.Label(ad_frame, text='Номер телефона(Формат: 8xxxxxxxxxx): ', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=1, padx=0, pady=5)
    EnterPhone = tk.Entry(ad_frame, bg='white', font=10)
    EnterPhone.grid(column=1, row=1, padx=0, pady=5)

    global EnterName
    tk.Label(ad_frame, text='Имя(На английском языке, без пробелов): ', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=2, padx=0, pady=5)
    EnterName = tk.Entry(ad_frame, bg='white', font=10)
    EnterName.grid(column=1, row=2, padx=0, pady=5)

    global ChooseCompl
    tk.Label(ad_frame, text='Выберите сложность заявки: ', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=3, padx=0, pady=5)
    compl = ['Легко', 'Нормально', 'Сложно']
    ChooseCompl = ttk.Combobox(ad_frame, values=compl, state="readonly")
    ChooseCompl.grid(column=1, row=3, padx=0, pady=5)

    global EnterVacuum
    tk.Label(ad_frame, text='Введите модель робота-пылесоса(На английском): ', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=4, padx=0, pady=5)
    EnterVacuum = tk.Entry(ad_frame, bg='white', font=10)
    EnterVacuum.grid(column=1, row=4, padx=0, pady=5)

    global EnterDate
    tk.Label(ad_frame, text='Введите дату производства(Формат: year-mm-dd, если не имеется, оставить поле пустым): ',
             fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=5, padx=0, pady=5)
    EnterDate = tk.Entry(ad_frame, bg='white', font=10)
    EnterDate.grid(column=1, row=5, padx=0, pady=5)

    global EnterGuar
    tk.Label(ad_frame,
             text='Введите гарантийный период(Используйте только цифры без пробелов, если не имеется, оставить поле пустым): ',
             fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=6, padx=0, pady=5)
    EnterGuar = tk.Entry(ad_frame, bg='white', font=10)
    EnterGuar.grid(column=1, row=6, padx=0, pady=5)

    global ChooseProbl
    tk.Label(ad_frame, text='Выберите проблему: ', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=7, padx=0, pady=5)
    probl = ['Сломался аккумулятор', 'Проблема с фильтром', 'Сломался мотор']
    ChooseProbl = ttk.Combobox(ad_frame, values=probl, state="readonly")
    ChooseProbl.grid(column=1, row=7, padx=0, pady=5)

    global ChooseServ
    tk.Label(ad_frame, text='Выберите услугу: ', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=8, padx=0, pady=5)
    serv = ['Замена аккумулятора', 'Замена фильтра', 'Чистка фильтра', 'Замена мотора', 'Ремонт мотора']
    ChooseServ = ttk.Combobox(ad_frame, values=serv, state="readonly")
    ChooseServ.grid(column=1, row=8, padx=0, pady=5)

    tk.Button(ad_frame, text='Подтверждение', font=('Arial', 10), command=confirm_client).grid(column=0,
                                                                                               row=9, padx=0,
                                                                                               pady=15)
    tk.Button(ad_frame, text='Возврат в меню', font=('Arial', 10), command=BackToMenu).grid(column=0,
                                                                                            row=10, padx=0,
                                                                                            pady=15)


def confirm_client():
    phone = EnterPhone.get()
    name = EnterName.get()
    complicacy = ChooseCompl.get()
    vacuum = EnterVacuum.get()
    date_ = EnterDate.get()
    guar = EnterGuar.get()
    problem = ChooseProbl.get()
    service = ChooseServ.get()

    def guar_write(guar):
        if len(guar) == 0:
            return None
        else:
            t = guar if (int(guar) <= 5) and (int(guar) > 0) else 0
            if t == 0:
                messagebox.showerror('Ошибка', 'Не бывает такого большого гарантийного периода, не обманывай :)')
                return None
            else:
                return t

    if functional.phone_check(phone):

        if functional.check_name(name) and (len(name) > 0 and len(name) <= 20):

            if len(complicacy) > 0:
                complicacy_eng = functional.translate_compl(complicacy)
                if check_vacuum_model(vacuum) and (len(vacuum) > 0):

                    if check_date(date_) or (len(date_) == 0):
                        date_ = None if len(date_) == 0 else date_

                        if (guar.isdigit()) or (len(guar) == 0):
                            guar = guar_write(guar)
                            if len(problem) > 0:
                                problem_eng = functional.translate_probl(problem)

                                if len(service) > 0:
                                    service_eng = functional.translate_serv(service)

                                    if functional.new_client_(phone, name, problem_eng, complicacy_eng, vacuum, date_,
                                                              guar, service_eng):
                                        messagebox.showinfo('Сообщение', 'Клиент добавлен')
                                        window_for_ad.destroy()
                                    else:
                                        messagebox.showerror('Ошибка', 'Что-то пошло не так')
                                else:
                                    messagebox.showerror('Ошибка',
                                                         'Вы не выбрали услугу')

                            else:
                                messagebox.showerror('Ошибка',
                                                     'Вы не выбрали проблему')

                        else:
                            messagebox.showerror('Ошибка', 'Неправильный ввод гарантийного периода!\n'
                                                           'Вводятся только цифры, т.е количество лет'
                                                           'Оставьте поле пустым, если дата производства неизвестна')

                    else:
                        messagebox.showerror('Ошибка', 'Неправильный ввод даты!\n'
                                                       'Пример ввода: 2023-02-12\n'
                                                       'Оставьте поле пустым, если дата производства неизвестна.\n'
                                                       'Дату из будущего вводить нельзя.')

                else:
                    messagebox.showerror('Ошибка', 'Неправильна введена модель роота-пылесоса\n'
                                                   '1. Английский алфавит\n'
                                                   '2. Допустимы цифры и знак "-""!\n'
                                                   '3. Допустимы пробелы')
            else:
                messagebox.showerror('Ошибка', 'Вы не выбрали сложность заявки!')
        else:
            messagebox.showerror('Ошибка', 'Неправильно введено имя!\n'
                                           'Имя не должно превышать больше 20 символов')

    else:
        messagebox.showerror('Ошибка', 'Неправильно введен номер телефона!')


def take_application_to_work():
    window_for_master3 = tk.Toplevel(window)
    window_for_master3.geometry('240x150')
    window_for_master3.title('')

    m_frame3 = tk.Frame(window_for_master3, width=100, height=100)
    m_frame3.grid()

    tk.Label(m_frame3, text='Введите номер заявки', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=0, padx=0, pady=15)

    ID_for_work = tk.Entry(m_frame3, bg='white', font=10)
    ID_for_work.grid(column=0, row=1, padx=5, pady=5)

    def take():
        id_ap = ID_for_work.get()
        res = functional.take_work_m(id_ap, id_master)

        if res == 'ok':
            messagebox.showinfo('Сообщение', 'Заявка закреплена в работе за Вами!\n'
                                             'Вперед к работе!')
            window_for_master3.destroy()

        elif res == 'error':
            messagebox.showerror('Внимание!', 'Проверьте правильность введенного номера заявки!')
            window_for_master3.destroy()

        else:
            messagebox.showerror('Внимание!', 'Эта заявка уже в работе!\n'
                                              'Проверьте правильного введенного номера заявки')

    tk.Button(m_frame3, text='Взять заявку в работу', font=('Arial', 10), command=take).grid(column=0, row=2, pady=5)


def application_status_master():
    window_for_master2 = tk.Toplevel(window)
    window_for_master2.geometry('700x320')
    window_for_master2.title('Мои заявки')

    m_frame2 = tk.Frame(window_for_master2, width=700, height=320)
    m_frame2.grid()

    tree = ttk.Treeview(m_frame2, column=('id', 'date', 'complicacy', 'status', 'phone',
                                          'problem', 'model'), height=15, show='headings')

    tree.column('id', width=100, anchor=tk.CENTER)
    tree.column('date', width=100, anchor=tk.CENTER)
    tree.column('complicacy', width=100, anchor=tk.CENTER)
    tree.column('status', width=100, anchor=tk.CENTER)
    tree.column('phone', width=100, anchor=tk.CENTER)
    tree.column('problem', width=100, anchor=tk.CENTER)
    tree.column('model', width=100, anchor=tk.CENTER)

    tree.heading('id', text='Номер заявки')
    tree.heading('date', text='Дата получения')
    tree.heading('complicacy', text='Сложность')
    tree.heading('status', text='Статус заказа')
    tree.heading('phone', text='Телефон клиента')
    tree.heading('problem', text='Тип проблемы')
    tree.heading('model', text='Модель')

    tree.pack()

    a = functional.look_application_with_status('Adopted')
    if a != False:
        id_ap = [d['id_application'] for d in a]
        date_of = [d['date_of_receipt'] for d in a]
        compl = [d['complicacy'] for d in a]
        stat = [d['status'] for d in a]
        client_ph = [d['Client phone'] for d in a]
        probl = [d['type_problem'] for d in a]
        model_ = [d['model'] for d in a]
        data = [id_ap, date_of, compl, stat, client_ph, probl, model_]

        first = len(id_ap)
        second = len(data)
        for i in range(0, first):
            temp = []
            for j in range(0, second):
                temp.append(data[j][i])

            tree.insert('', 'end', values=temp)

    else:
        messagebox.showinfo('Сообщение', 'Новых заявок нет')
        window_for_master2.destroy()
        go_to_master()


def master_application():
    window_for_master = tk.Toplevel(window)
    window_for_master.geometry('800x320')
    window_for_master.title('Мои заявки')

    m_frame = tk.Frame(window_for_master, width=800, height=320)
    m_frame.grid()

    tree = ttk.Treeview(m_frame, column=('id', 'date', 'complicacy', 'status', 'phone',
                                         'problem', 'model', 'employee'), height=15, show='headings')

    tree.column('id', width=100, anchor=tk.CENTER)
    tree.column('date', width=100, anchor=tk.CENTER)
    tree.column('complicacy', width=100, anchor=tk.CENTER)
    tree.column('status', width=100, anchor=tk.CENTER)
    tree.column('phone', width=100, anchor=tk.CENTER)
    tree.column('problem', width=100, anchor=tk.CENTER)
    tree.column('model', width=100, anchor=tk.CENTER)
    tree.column('employee', width=100, anchor=tk.CENTER)

    tree.heading('id', text='Номер заявки')
    tree.heading('date', text='Дата получения')
    tree.heading('complicacy', text='Сложность')
    tree.heading('status', text='Статус заказа')
    tree.heading('phone', text='Телефон клиента')
    tree.heading('problem', text='Тип проблемы')
    tree.heading('model', text='Модель')
    tree.heading('employee', text='Сотрудник')

    tree.pack()

    a = functional.look_my_applications(id_master)
    if a != False:
        id_ap = [d['id_application'] for d in a]
        date_of = [d['date_of_receipt'] for d in a]
        compl = [d['complicacy'] for d in a]
        stat = [d['status'] for d in a]
        client_ph = [d['Client phone'] for d in a]
        probl = [d['type_problem'] for d in a]
        model_ = [d['model'] for d in a]
        empl = [d['Employee'] for d in a]
        data = [id_ap, date_of, compl, stat, client_ph, probl, model_, empl]

        first = len(id_ap)
        second = len(data)
        for i in range(0, first):
            temp = []
            for j in range(0, second):
                temp.append(data[j][i])

            tree.insert('', 'end', values=temp)

    else:
        messagebox.showinfo('Поздравляем!', 'У вас нет заказов в работе\n'
                                            'Возьмите новые заказы!')
        window_for_master.destroy()
        go_to_master()


def client_application():
    window_for_client = tk.Toplevel(window)
    window_for_client.geometry('900x320')
    window_for_client.title('Мои заявки')

    c_frame = tk.Frame(window_for_client, width=900, height=320)
    c_frame.grid()

    tree = ttk.Treeview(c_frame, column=('id', 'date', 'complicacy', 'status', 'phone',
                                         'problem', 'model', 'employee', 'ready_date'), height=15, show='headings')

    tree.column('id', width=100, anchor=tk.CENTER)
    tree.column('date', width=100, anchor=tk.CENTER)
    tree.column('complicacy', width=100, anchor=tk.CENTER)
    tree.column('status', width=100, anchor=tk.CENTER)
    tree.column('phone', width=100, anchor=tk.CENTER)
    tree.column('problem', width=100, anchor=tk.CENTER)
    tree.column('model', width=100, anchor=tk.CENTER)
    tree.column('employee', width=100, anchor=tk.CENTER)
    tree.column('ready_date', width=100, anchor=tk.CENTER)

    tree.heading('id', text='Номер заявки')
    tree.heading('date', text='Дата получения')
    tree.heading('complicacy', text='Сложность')
    tree.heading('status', text='Статус заказа')
    tree.heading('phone', text='Телефон клиента')
    tree.heading('problem', text='Тип проблемы')
    tree.heading('model', text='Модель')
    tree.heading('employee', text='Сотрудник')
    tree.heading('ready_date', text="Дата готовности")

    tree.pack()

    a = functional.client_applications(id_client)
    if a != False:
        id_ap = [d['id_application'] for d in a]
        date_of = [d['date_of_receipt'] for d in a]
        compl = [d['complicacy'] for d in a]
        stat = [d['status'] for d in a]
        client_ph = [d['Client phone'] for d in a]
        probl = [d['type_problem'] for d in a]
        model_ = [d['model'] for d in a]
        empl = [d['Employee'] for d in a]
        rdate = [d['ready_date'] for d in a]
        data = [id_ap, date_of, compl, stat, client_ph, probl, model_, empl, rdate]

        first = len(id_ap)
        second = len(data)
        for i in range(0, first):
            temp = []
            for j in range(0, second):
                temp.append(data[j][i])

            tree.insert('', 'end', values=temp)

    else:
        messagebox.showerror('Ошибка', 'Что-то пошло не так')
        window_for_client.destroy()
        go_to_client()


def check_administrator():
    global window_check
    window_check = tk.Toplevel(window)
    window_check.geometry('550x320')
    window.title('Вход')

    global check_frame
    check_frame = tk.Frame(window_check, width=400, height=200)
    check_frame.grid(column=0, row=0, padx=0, pady=0)

    tk.Label(check_frame, text='Введите номер телефона и пароль', fg='black', font=('Arial', 10, 'bold')).grid(column=2,
                                                                                                               row=0,
                                                                                                               padx=0,
                                                                                                               pady=15)
    tk.Label(check_frame, text='Номер телефона:', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=1, padx=0, pady=5)
    tk.Label(check_frame, text='Формат: 8xxxxxxxxxx', fg='black',
             font=('Arial', 10, 'bold')).grid(column=3, row=1, padx=5, pady=5)

    global EnterLogin
    EnterLogin = tk.Entry(check_frame, bg='white', font=10)
    EnterLogin.grid(column=2, row=1, padx=5, pady=5)

    tk.Label(check_frame, text='Пароль:', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=3, padx=0, pady=5)

    tk.Label(check_frame, text='Не больше 20 символов', fg='black',
             font=('Arial', 10, 'bold')).grid(column=3, row=3, padx=5, pady=5)

    global EnterPassword
    EnterPassword = tk.Entry(check_frame, bg='white', font=10)
    EnterPassword.grid(column=2, row=3, padx=5, pady=5)

    tk.Button(check_frame, text='Подтвердить номер телефона и пароль', font=('Arial', 10),
              command=get_entry_to_administrator).grid(column=2, row=4, padx=0,
                                                       pady=5)

    tk.Button(check_frame, text='Вернуться в меню', font=('Arial', 10), command=BackToMenuFromCheck).grid(column=2,
                                                                                                          row=6, padx=0,
                                                                                                          pady=15)


def calculate_cost():
    id_app = EnterID.get()
    cost_ap = functional.calculate_cost_appl(id_client, id_app)
    if cost_ap:
        messagebox.showinfo('Стоимость', f'Стоимость завяки составляет {cost_ap} руб.')
    else:
        messagebox.showerror('Ошибка', 'Проверьте корректность номера зaявки')


def check_master():
    global window_check
    window_check = tk.Toplevel(window)
    window_check.geometry('550x320')
    window.title('Вход')

    global check_frame
    check_frame = tk.Frame(window_check, width=400, height=200)
    check_frame.grid(column=0, row=0, padx=0, pady=0)

    tk.Label(check_frame, text='Введите номер телефона и пароль', fg='black', font=('Arial', 10, 'bold')).grid(column=2,
                                                                                                               row=0,
                                                                                                               padx=0,
                                                                                                               pady=15)
    tk.Label(check_frame, text='Номер телефона:', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=1, padx=0, pady=5)
    tk.Label(check_frame, text='Формат: 8xxxxxxxxxx', fg='black',
             font=('Arial', 10, 'bold')).grid(column=3, row=1, padx=5, pady=5)

    global EnterLogin
    EnterLogin = tk.Entry(check_frame, bg='white', font=10)
    EnterLogin.grid(column=2, row=1, padx=5, pady=5)

    tk.Label(check_frame, text='Пароль:', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=3, padx=0, pady=5)

    tk.Label(check_frame, text='Не больше 20 символов', fg='black',
             font=('Arial', 10, 'bold')).grid(column=3, row=3, padx=5, pady=5)

    global EnterPassword
    EnterPassword = tk.Entry(check_frame, bg='white', font=10)
    EnterPassword.grid(column=2, row=3, padx=5, pady=5)

    tk.Button(check_frame, text='Подтвердить номер телефона и пароль', font=('Arial', 10),
              command=get_entry_to_master).grid(column=2, row=4, padx=0,
                                                pady=5)

    tk.Button(check_frame, text='Вернуться в меню', font=('Arial', 10), command=BackToMenuFromCheck).grid(column=2,
                                                                                                          row=6, padx=0,
                                                                                                          pady=15)


def check_admin():
    global window_check
    window_check = tk.Toplevel(window)
    window_check.geometry('550x320')
    window.title('Login')

    global check_frame
    check_frame = tk.Frame(window_check, width=400, height=200)
    check_frame.grid(column=0, row=0, padx=0, pady=0)

    tk.Label(check_frame, text='Введите номер телефона и пароль', fg='black', font=('Arial', 10, 'bold')).grid(column=2,
                                                                                                               row=0,
                                                                                                               padx=0,
                                                                                                               pady=15)
    tk.Label(check_frame, text='Номер телефона:', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=1, padx=0, pady=5)
    tk.Label(check_frame, text='Формат: 8xxxxxxxxxx', fg='black',
             font=('Arial', 10, 'bold')).grid(column=3, row=1, padx=5, pady=5)

    global EnterLogin
    EnterLogin = tk.Entry(check_frame, bg='white', font=10)
    EnterLogin.grid(column=2, row=1, padx=5, pady=5)

    tk.Label(check_frame, text='Пароль:', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=3, padx=0, pady=5)

    tk.Label(check_frame, text='Не больше 20 символов', fg='black',
             font=('Arial', 10, 'bold')).grid(column=3, row=3, padx=5, pady=5)

    global EnterPassword
    EnterPassword = tk.Entry(check_frame, bg='white', font=10)
    EnterPassword.grid(column=2, row=3, padx=5, pady=5)

    tk.Button(check_frame, text='Подтвердить номер телефона и пароль', font=('Arial', 10),
              command=get_entry_to_admin).grid(column=2, row=4, padx=0,
                                               pady=5)

    tk.Button(check_frame, text='Вернуться в меню', font=('Arial', 10), command=BackToMenuFromCheck).grid(column=2,
                                                                                                          row=6, padx=0,
                                                                                                          pady=15)


def check_client():
    global window_check
    window_check = tk.Toplevel(window)
    window_check.geometry('550x320')
    window.title('Вход')

    global check_frame
    check_frame = tk.Frame(window_check, width=400, height=200)
    check_frame.grid(column=0, row=0, padx=0, pady=0)

    tk.Label(check_frame, text='Введите номер телефона', fg='black', font=('Arial', 10, 'bold')).grid(column=2, row=0,
                                                                                                      padx=0, pady=15)
    tk.Label(check_frame, text='Номер телефона:', fg='black',
             font=('Arial', 10, 'bold')).grid(column=0, row=1, padx=0, pady=5)
    tk.Label(check_frame, text='Формат: 8xxxxxxxxxx', fg='black',
             font=('Arial', 10, 'bold')).grid(column=3, row=1, padx=5, pady=5)

    global EnterLogin
    EnterLogin = tk.Entry(check_frame, bg='white', font=10)
    EnterLogin.grid(column=2, row=1, padx=5, pady=5)

    tk.Button(check_frame, text='Подтвердите номер телефона ', font=('Arial', 10), command=get_entry_to_client).grid(
        column=2, row=4, padx=0,
        pady=5)
    tk.Button(check_frame, text='Вернуться в меню', font=('Arial', 10), command=BackToMenuFromCheck).grid(column=2,
                                                                                                          row=6, padx=0,
                                                                                                          pady=15)


def get_entry_to_master():
    log = EnterLogin.get()
    pas = EnterPassword.get()

    if functional.phone_check(log) and functional.password_check(pas):
        global id_master
        a = functional.check_entry_master(log, pas)
        if a != False:
            id_master = int(a[1])
            master_widjets()
            tk.Button(check_frame, text='Войти', font=('Arial', 10), command=go_to_master).grid(column=2, row=5, padx=0,
                                                                                                pady=5)
        else:
            messagebox.showerror('Неправильный ввод логина или пароля!',
                                 'Такого пользователя нет!')
    else:
        messagebox.showerror('Неправильный ввод логина или пароля!',
                             'Формат номера: 8xxxxxxxxxx\n'
                             'Пароль не должен превышать 20 символов!')


def get_entry_to_administrator():
    log = EnterLogin.get()
    pas = EnterPassword.get()

    if functional.phone_check(log) and functional.password_check(pas):
        global id_administrator
        a = functional.check_entry_administrator(log, pas)
        if a != False:
            id_administrator = int(a[1])
            administrator_widjets()
            tk.Button(check_frame, text='Войти', font=('Arial', 10), command=go_to_administrator).grid(column=2, row=5,
                                                                                                       padx=0,
                                                                                                       pady=5)
        else:
            messagebox.showerror('Неправильный ввод логина или пароля!',
                                 'Такого пользователя нет!')
    else:
        messagebox.showerror('Неправильный ввод логина или пароля!',
                             'Формат номера: 8xxxxxxxxxx\n'
                             'Пароль не должен превышать 20 символов!')


def get_entry_to_admin():
    log = EnterLogin.get()
    pas = EnterPassword.get()

    if functional.phone_check(log) and functional.password_check(pas):
        global id_admin
        a = functional.check_entry_admin(log, pas)
        if a != False:
            id_admin = int(a[1])
            admin_widgets()
            tk.Button(check_frame, text='Войти', font=('Arial', 10), command=go_to_admin).grid(column=2, row=5,
                                                                                               padx=0,
                                                                                               pady=5)
        else:
            messagebox.showerror('Неправильный ввод логина или пароля!',
                                 'Такого пользователя нет!')
    else:
        messagebox.showerror('Неправильный ввод логина или пароля!',
                             'Формат номера: 8xxxxxxxxxx\n'
                             'Пароль не должен превышать 20 символов!')


def get_entry_to_client():
    log = EnterLogin.get()

    if functional.phone_check(log):
        global id_client
        a = functional.check_entry_client(log)
        if a != False:
            id_client = int(a[1])
            client_widjets()
            tk.Button(check_frame, text='Войти', font=('Arial', 10), command=go_to_client).grid(column=2, row=5,
                                                                                                padx=0,
                                                                                                pady=5)
        else:
            messagebox.showerror('Неправильный ввод номера!',
                                 'Такого пользователя нет!')
    else:
        messagebox.showerror('Неправильный ввод телефона!',
                             'Формат номера: 8xxxxxxxxxx')


def exit_out():
    functional.close_connection(connection)

    window.destroy()


def go_to_admin():
    window_check.destroy()

    Launch_frame.grid_forget()
    Menu_frame.grid_forget()
    Client_frame.grid_forget()
    Master_frame.grid_forget()
    Administrator_frame.grid_forget()

    Admin_frame.grid(column=0, row=0, padx=170, pady=100)


def go_to_worker():
    Launch_frame.grid_forget()
    Menu_frame.grid_forget()
    Admin_frame.grid_forget()
    Client_frame.grid_forget()
    Master_frame.grid_forget()
    Administrator_frame.grid_forget()

    Worker_frame.grid(column=0, row=0, padx=200, pady=140)


def BackToMenu():
    Launch_frame.grid_forget()
    Admin_frame.grid_forget()
    Worker_frame.grid_forget()
    Client_frame.grid_forget()
    Master_frame.grid_forget()
    Administrator_frame.grid_forget()

    Menu_frame.grid(column=0, row=0, padx=170, pady=140)


def BackToMenuFromCheck():
    window_check.destroy()

    Launch_frame.grid_forget()
    Admin_frame.grid_forget()
    Worker_frame.grid_forget()
    Client_frame.grid_forget()
    Master_frame.grid_forget()
    Administrator_frame.grid_forget()

    Menu_frame.grid(column=0, row=0, padx=150, pady=120)


def go_to_client():
    window_check.destroy()

    Launch_frame.grid_forget()
    Menu_frame.grid_forget()
    Admin_frame.grid_forget()
    Worker_frame.grid_forget()
    Master_frame.grid_forget()
    Administrator_frame.grid_forget()

    Client_frame.grid(column=0, row=0, padx=120, pady=100)


def go_to_administrator():
    window_check.destroy()

    Launch_frame.grid_forget()
    Menu_frame.grid_forget()
    Admin_frame.grid_forget()
    Worker_frame.grid_forget()
    Master_frame.grid_forget()
    Client_frame.grid_forget()

    Administrator_frame.grid(column=0, row=0, padx=170, pady=100)


def go_to_master():
    window_check.destroy()

    Launch_frame.grid_forget()
    Menu_frame.grid_forget()
    Admin_frame.grid_forget()
    Worker_frame.grid_forget()
    Client_frame.grid_forget()
    Administrator_frame.grid_forget()

    Master_frame.grid(column=0, row=0, padx=150, pady=100)


window = tk.Tk()
window.geometry('500x500')
window.title('Приложение')

Launch_frame = tk.Frame(window, width=500, height=500)
Launch_frame.grid()

Menu_frame = tk.Frame(window, width=500, height=500)
Menu_frame.grid()

Admin_frame = tk.Frame(window, width=500, height=500)
Admin_frame.grid()

Worker_frame = tk.Frame(window, width=500, height=500)
Worker_frame.grid()

Client_frame = tk.Frame(window, width=500, height=500)
Client_frame.grid()

Master_frame = tk.Frame(window, width=500, height=500)
Master_frame.grid()

Administrator_frame = tk.Frame(window, width=500, height=500)
Administrator_frame.grid()

launch_widjets()
menu_widgets()
worker_widgets()

Menu_frame.grid_forget()
Admin_frame.grid_forget()
Worker_frame.grid_forget()
Client_frame.grid_forget()
Master_frame.grid_forget()
Administrator_frame.grid_forget()

tk.mainloop()
