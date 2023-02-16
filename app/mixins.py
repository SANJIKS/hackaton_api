import requests
import json

HOST = 'http://3.67.196.232/'

class CreateMixin:
    def create_todo(self, url) -> None:
        data_ = {
            'title': input('Введите название: '),
            'is_done': input('Введите статус(True или False): ')
        }
        response = requests.post(url + 'todo/create', data=json.dumps(data_))
        if response.status_code == 200:
            print(1)
        else:
            print(0)


class ReadMixin:
    def get_all_todos(self, url):
        response = requests.get(url + 'todo/all')
        if response.status_code == 200:
            print(json.loads(response.text))
        else:
            print(Exception('Проблемы на стороне сервера'))

class RetrieveMixin:
    def retrieve_todo(self, url):
        id_ = input('Введите id: ')
        response = requests.get(url + f'todo/{id_}')
        if response.status_code == 200:
            print(json.loads(response.text))
        elif response.status_code == 404:
            print(Exception('Нет такой записи'))
        else:
            print(Exception('Непредвиденная ошибка', response.status_code))


class UpdateMixin:
    def update_todo(self, url):
        id_ = input('Введите id: ')
        data_ = {
            'title': input('Введите название: '),
            'is_done': input('Введите новый статус(True или False): ')
        }
        response = requests.put(url + f'todo/{id_}/update', data=json.dumps(data_))
        if response.status_code == 200:
            print(json.loads(response.text))
        elif response.status_code == 404:
            print(Exception('Нет такой записи'))
        else:
            print(Exception('Непредвиденная ошибка', response.status_code))

class DeleteMixin:
    def delete_todo(self, url):
        id_ = input('Введите id: ')
        response = requests.delete(url + f'todo/{id_}/delete')
        if response.status_code == 200:
            print(json.loads(response.text))
        elif response.status_code == 404:
            print(Exception('Нет такой записи'))
        else:
            print(Exception('Непредвиденная ошибка'))


