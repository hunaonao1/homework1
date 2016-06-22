from flask_script import Manager
from c2_02 import app

manager=Manager(app)

@manager.option('-n','--name',dest='name',default='songying')

@manager.command
def hello(name):
    print 'hello',name

@manager.command
def initialize_database():
    'initialize_database'
    print 'database...'

if __name__== '__main__':
    manager.run()