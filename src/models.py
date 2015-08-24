# -*- coding:utf-8 -*-
__author__ = 'xxc'

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, ForeignKey, Table, Integer, String, Enum, DateTime, Text
from sqlalchemy.orm import relationship, backref


class Domain(Base):
    __tablename__ = u"domain"
    id = Column(Integer, primary_key=True)
    domain = Column(String())
    configure_id = Column(Integer(), ForeignKey("configure.id"))
    DNSRecords = relationship("DNSRecord")


class DNSRecord(Base):
    __tablename__ = u"dnsrecord"
    id = Column(Integer, primary_key=True)
    domain_id = Column(Integer, ForeignKey("domain.id"))
    ttl = Column(Integer())
    type = Column(Enum("setting", "NS"))
    time = Column(DateTime())
    host = Column(String(255))
    port = Column(Integer())


class Configure(Base):
    __tablename__ = u"configure"
    id = Column(Integer, primary_key=True)
    dns_name = Column(String(20))
    dns_config = Column(Text)
    addr_name = Column(String(20))
    addr_config = Column(Text)
    domains = relationship("Domain")





from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)