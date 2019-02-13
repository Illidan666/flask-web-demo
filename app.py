from flask import Flask
import datetime
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/h1')
def hello_world2():
    return '<h1>Hello World!<h1>'


@app.route('/class')
def hello_class():
    json.encoder(Person('121', '1231231'))
    return json.encoder(Person('121', '1231231'))



class ResponseDemo:
    __id = 1
    __num = '1231'


class Person(object):
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        self._birthday = birthday

    @property
    def age(self):
        return datetime.date.today() - self.birthday

    def __str__(self):
        return '%s,%s(%s)' % (self.name, self.birthday, self.age)


if __name__ == '__main__':
    app.run()
