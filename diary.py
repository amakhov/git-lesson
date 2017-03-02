import os
from datetime import datetime
now = datetime.strftime(datetime.now(), "%Y.%m.%d")

def punkt2():
    z1=input("Введите новую задачу ")
    z1=str(z1)
    
def menu():
    print ('Ежедневник. Выбирете действие:')
    print ()
    print ('1. Вывести список задач')
    print ('2. Добавить задачу')
    print ('3. Отредактировать задачу')
    print ('4. Завершить задачу')
    print ('5. Начать задачу сначала')
    print ('6. Выход')
    print ()
    a=input('Введите число ')
    a=int(a)
    if a==1:
        print('Список задач на сегодня ', now)  
    elif a==2:
         punkt2()
    elif a==3:
        print('Отредактируйте задачу')
    elif a==4:
        print('Выполнено')
    elif a==5:
        print('Не выполнено')
    elif a==6:
        exit(6)       
    else:
        print('Вы ошиблись с числом!')
                   
menu()
#os.system("cls")

