import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Index, UniqueConstraint, ForeignKey
from sqlalchemy.orm import sessionmaker, relationships

engine = create_engine('mysql+pymysql://root:root123@127.0.0.1:3306/soderberg?charset=utf8', echo=True)
Base = declarative_base()


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), unique=True, nullable=False)


class Server(Base):
    __tablename__ = 'server'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(60), unique=True, nullable=False)
    port = Column(Integer, default=22)


class ServerGroups(Base):
    __tablename__ = 'servergroups'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    server_id = Column(Integer, ForeignKey('server.id'))
    group_id = Column(Integer, ForeignKey('group.id'))
Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)