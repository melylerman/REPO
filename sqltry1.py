import os
import stat
import pathlib
import pandas as pd
import numpy as np
import re
import openpyxl
import nltk
import sys
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.types import  Integer, Text, String, DateTime, Date, Time
from sqlalchemy.ext.declarative import declarative_base
from . import COBsettingsGlobal as GT



# import COBsettingsGlobal as GT
# from . import COBsettingsGlobal as GT
engineName = 'sqlite:///db.sqlite3'
engine = create_engine(engineName, echo=True)
Base = declarative_base()


# ########################################### #
#               Work Key Process              #
# For Each Process there will be a Key number #
# ########################################### #

table_name = 'COBGeneral'

class WorkNumber(Base):
    __tablename__ = table_name
    COBGeneralKey = Column(String(8), primary_key=True )
    COBNumber = Column(Integer)
    COBText = Column(Text)
     
DBSession = sessionmaker(bind=engine)

session = DBSession()

onlyRow=session.query(WorkNumber).filter(WorkNumber.COBGeneralKey =="Numerato").first()
GT.workNumberKey = onlyRow.COBNumber 
print ("SQLRead **** DworkNumberKey = ",GT.workNumberKey)
session.commit()


table_name = 'PROC'

class ReadPROC(Base):
    __tablename__ = table_name
    COBProjId = Column(Integer, primary_key=True )
    ROWIndex = 	Column(Integer)
    TEXT = 	Column(Text)
    OriginalROW = 	Column(Integer)
    IF = 	Column(Text)
    FLOWSHAPE = 	Column(Text)
    SectionNAME = 	Column(Text)
    SectionClass = 	Column(Text)
    Command = 	Column(Text)
    ShortTEXT = 	Column(Text)
    LINK = 	Column(Text)
    LINKRow = 	Column(Integer)
    CommandKeyword = 	Column(Text)
    PROCX = 	Column(Integer)
    PROCY = 	Column(Integer)
    LENGTH = 	Column(Integer)

        
DBSession = sessionmaker(bind=engine)

session = DBSession()


GT.PROC = pd.DataFrame(session.query(ReadPROC.ROWIndex, ReadPROC.TEXT, ReadPROC.OriginalROW, ReadPROC.IF, ReadPROC.FLOWSHAPE, ReadPROC.SectionNAME, ReadPROC.SectionClass, ReadPROC.Command, ReadPROC.ShortTEXT, ReadPROC.LINK, ReadPROC.LINKRow, ReadPROC.CommandKeyword, ReadPROC.PROCX, ReadPROC.PROCY, ReadPROC.LENGTH).filter(ReadPROC.COBProjId == GT.workNumberKey).with_labels().all())
# print (result.COBProjId, result.ROWIndex)

# for row in result:
#    print (row.ShortTEXT)

# GT.PROC = pd.read_sql_table(
#     table_name,
#     con=engine
# ).where(GT.PROC.COBProjId == 40)
print (GT.PROC)
print ("I AM HERE 5 ")

table_name = 'EDGE'


class ReadEDGE(Base):
    __tablename__ = table_name
    COBProjId = Column(Integer, primary_key=True )
    OriginalROW	=    Column(Integer)
    iFROM	=    Column(Integer)
    iTO	=    Column(Integer)
    IF	=    Column(Text)
    FLOWSHAPETO	=    Column(Text)
    POSX	=    Column(Integer)
    nadaCount	=    Column(Integer)
    iELSE	=    Column(Integer)
    newROW	=    Column(Integer)


DBSession = sessionmaker(bind=engine)

session = DBSession()


GT.EDGE = pd.DataFrame(session.query(ReadEDGE.OriginalROW, ReadEDGE.iFROM, ReadEDGE.iTO, ReadEDGE.IF, ReadEDGE.FLOWSHAPETO, ReadEDGE.POSX, ReadEDGE.nadaCount, ReadEDGE.iELSE, ReadEDGE.newROW).filter(ReadEDGE.COBProjId == GT.workNumberKey).with_labels().all())
# print (result.COBProjId, result.ROWIndex)

# for row in result:
#    print (row.ShortTEXT)

# GT.PROC = pd.read_sql_table(
#     table_name,
#     con=engine
# ).where(GT.PROC.COBProjId == 40)
print (GT.EDGE)
print ("I AM HERE 7 ")



       
# DBSession = sessionmaker(bind=engine)

# session = DBSession()





# GT.EDGE = pd.read_sql_table(
#     table_name,
#     con=engine
# ).where(COBProjId == 40)


print (GT.EDGE)
print ("I AM HERE 6 ")

print(STAM)

session.commit()


