import sqlalchemy
from sqlalchemy import create_engine,and_,or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Index, UniqueConstraint, ForeignKey
from sqlalchemy.orm import sessionmaker,relationships

engine = create_engine('mysql+pymysql://root:root123@127.0.0.1:3306/soderberg?charset=utf8', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # books = relationships('book')


class Book(Base):
    __tablename__='Book'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    user_id=Column(String(20),ForeignKey('User.id'))


Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()
# new_user = User(id='5', name='Jack')
# session.add(new_user)
# session.commit()
# session.close()
# user = session.query(User).filter(User.id == '5').one()
# print(type(user))
# print(user.name)
# session.add_all([User(id='7',name='Mike'),User(id='8',name='Alex')])
# session.commit()
# session.query(User).filter(User.id == '5').delete()
# result=session.query(User).all()
# session.query(User).filter(User.id=='8').update({'name':'badboy'})
# session.commit()
# print(result)
for row in session.query(User).filter(or_(User.name=='badboy',User.id=='8')):
    print(row.name)
# session.close()
# print(sqlalchemy.__version__)
