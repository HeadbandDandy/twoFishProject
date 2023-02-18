from app.models import User, ToDo
from app.db import Session, Base, engine


# will drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


db = Session()

# insert users
db.add_all([
  User(username='alesmonde0', email='nwestnedge0@cbc.ca', password='password123'),
  User(username='jwilloughway1', email='rmebes1@sogou.com', password='password123'),
  User(username='iboddam2', email='cstoneman2@last.fm', password='password123'),
  User(username='dstanmer3', email='ihellier3@goo.ne.jp', password='password123'),
  User(username='djiri4', email='gmidgley4@weather.com', password='password123')
])

db.commit()

# insert posts
db.add_all([
  ToDo(id = 1, title='Donec posuere metus vitae ipsum', descr='https://buzzfeed.com/in/imperdiet/et/commodo/vulputate.pngjahdjbafjadlbfjaa', user_id=1),
  ToDo(id = 2, title='Morbi non quam nec dui luctus rutrum', descr='https://nasa.gov/donec.jsonjkfdhjkah;dfha;dfjhkd', user_id=1),
  ToDo(id = 3, title='Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue', descr='https://europa.eu/parturient/montes/nascetur/ridiculus/mus/etiam/vel.aspxhj;dfajkdhlfjadhflakhfdaf', user_id=2),
  ToDo(id = 4, title='Nunc purus', descr='http://desdev.cn/enim/blandit/mi.jpgdjhfladfhdjlfhj;dh;fajhkd', user_id=3),
  ToDo(id = 5, title='Pellentesque eget nunc', descr='http://google.ca/nam/nulla/integer.aspxadjhflhdlfhahjfldahfladjhfadjhldf', user_id=4)
])

db.commit()

db.close()

