# -*- coding:utf-8 -*-
__author__ = 'xxc'
from .models import Session, DNSRecord, Configure, Domain
from dnslib import DNSRecord
from dnslib.dns import RR, NS, DNSLabelError
import sqlite3




q = DNSRecord.question("x007007007.gvip.net", qtype="NS")
a = DNSRecord.question("x007007007.gvip.net", qtype="A")

r = DNSRecord.parse(q.send('8.8.4.4'))
for next in r.rr:
    rdata = next.rdata
    assert isinstance(next, RR)
    assert isinstance(rdata, NS)
    ns = str(rdata.label).strip(".")
    print next.ttl, ns
    r = DNSRecord.parse(a.send(ns))
    print r.rr[0].ttl