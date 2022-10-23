import datetime
from sqlalchemy import (
	Table, 		Column, 	String, 
	Integer, 	MetaData, 	DateTime,
	ForeignKey,	Boolean,
)
from db.core.initializer import engine



table_meta = MetaData()


Item = Table(
	'item',
	table_meta,
	Column('category', String(200)),
	Column('id', Integer, primary_key=True),
	Column('name', String(250), nullable=False),
	Column(
		'date_tracked', DateTime, 
		default=datetime.datetime.now
	),
)


CravedItem = Table(
	'craveditem',
	table_meta,
	Column('item_id', ForeignKey('item.id')),
	Column('is_satisfied', Boolean(), default=False),
	Column(
		'date_tracked', DateTime, 
		default=datetime.datetime.now
	),
)



def create_all_tables():
	table_meta.create_all(engine)

def drop_all_tables():
	table_meta.drop_all(engine)