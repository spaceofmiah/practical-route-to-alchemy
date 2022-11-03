"""
Module contains code to interact with item 
database table model with SQLAlchemy
expression language
"""
from db.core.initializer import engine
from db.models.items import table_meta, Item, CravedItem


class DDL:

	def __init__(self):
		pass

	@staticmethod
	def create_all_tables():
		"""Creates all tables"""
		table_meta.create_all(engine)

	@staticmethod
	def create_item_table_with_core():
		"""Creates item table"""
		Item.create(engine, checkfirst=True)

	@staticmethod
	def create_craveditem_table_with_core():
		"""Creates craved item table"""
		CravedItem.create(engine, checkfirst=True)

	@staticmethod
	def drop_all_tables():
		"""Drop all tables"""
		table_meta.drop_all(engine)

	@staticmethod
	def drop_item():
		"""Drops Item table"""
		Item.drop(engine)

	@staticmethod
	def drop_craveditem():
		"""Drops CravedItem table"""
		CravedItem.drop(engine)


