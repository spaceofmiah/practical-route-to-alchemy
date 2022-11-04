import datetime
from sqlalchemy import (
	Table, 		Column, 	String, 
	Integer, 	MetaData, 	DateTime,
	ForeignKey,	Boolean,	Sequence
)


table_meta = MetaData()


Item = Table(
	'item',
	table_meta,
	Column(
		'id', 
		Integer, 
		Sequence('item_id'), 
		primary_key=True,
		autoincrement=True,
	),
	Column('category', String(200)),
	Column('name', String(250), nullable=False),
	Column(
		'date_tracked', 
		DateTime, 
		default=datetime.datetime.now
	),
)


CravedItem = Table(
	'craveditem',
	table_meta,
	Column(
		'id', 
		Integer, 
		Sequence('craveditem_id'), 
		primary_key=True,
		autoincrement=True,
	),
	Column('item_id', ForeignKey('item.id')),
	Column('is_satisfied', Boolean(), default=False),
	Column(
		'date_tracked', 
		DateTime, 
		default=datetime.datetime.now
	),
)


