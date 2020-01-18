from flask_script import Manager,Server,Shell
from app import create_app,db
from flask_migrate import Migrate, MigrateCommand

app = create_app()

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return {"app":app,"db":db, 'User':user,'Comment':comment}

if __name__ == '__main__':
    manager.run()