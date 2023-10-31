from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from com.application import create_app
from com.model import *

app = create_app(__name__)

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


def add_statement():
	p = Statements(statement='pcs status', description='查询集群状态')
	db.session.add(p)

    db.session.commit()
    print('添加一条数据')


@manager.shell
def myshell():
    return dict(
        app=app,
        db=db,
        Statements=Statements,
		add_statement=add_statement
    )


if __name__ == '__main__':
    manager.run()
