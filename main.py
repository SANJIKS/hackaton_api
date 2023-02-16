import requests
import json

from app.mixins import CreateMixin, ReadMixin, RetrieveMixin, UpdateMixin, DeleteMixin


HOST = 'http://3.67.196.232/'

class InterFace(CreateMixin, ReadMixin, RetrieveMixin, UpdateMixin, DeleteMixin):
    pass

interface = InterFace()

while True:
    print('\nДля добавления todo: add\nДля просмотра всех todo: read\nДля просмотра определенного todo: retrieve\nЧтобы обновить todo: update\nДля удаления todo: delete\nДля выхода из программы: quit')
    choice = input('print command: ')
    if choice == 'add':
        interface.create_todo(HOST)
    elif choice == 'read':
        interface.get_all_todos(HOST)
    elif choice == 'retrieve':
        interface.retrieve_todo(HOST)
    elif choice == 'update':
        interface.update_todo(HOST)
    elif choice == 'delete':
        interface.delete_todo(HOST)
    elif choice == 'quit':
        break
    else:
        print('\nNAPISHITE COMANDU IZ SPISKA\n')



# interface.create_todo(HOST)
# interface.get_all_todos(HOST)
# interface.retrieve_todo(HOST)
# interface.update_todo(HOST)
# interface.delete_todo(HOST)