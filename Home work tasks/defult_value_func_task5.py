""" Давайте напишем функцию, которая возвращает полное имя пользователя. 
В базе данных в основном хранят имя пользователя first_name, его фамилию last_name и отчество, 
или, как принято в западных странах, второе имя — middle_name. 
Причем middle_name — это необязательная переменная, она может быть, а может 
и не передаваться при вызове функции. 
Наша функция будет возвращать строку 
с полным именем 'first_name middle_name last_name', если же middle_name отсутствует, 
то возвращаемая строка должна быть 'first_name last_name'. """

def get_fullname (first_name, last_name, middle_name = ''):
    print(bool(middle_name))
    if middle_name == '':
        return f"{first_name} {last_name}"
    else:
        return f"{first_name} {middle_name} {last_name}" # Order of words is here

print (get_fullname("Serhii", "Korobchenko", "Olegovich"))
    
        
    
        