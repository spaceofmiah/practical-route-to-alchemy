"""
Module contains code to interact with item 
database table model with SQLAlchemy
expression language
"""
from typing import List, Dict
from sqlalchemy.sql import select

from db.core.initializer import engine, create_connection
from db.models.items import table_meta, Item, CravedItem


class DDL:
	"""Encapsulates database definition language (DML)"""

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


class DQL:
	"""Encapsulates database query language (DML)"""

	@staticmethod
	def retrieve_all_items():
		statement = select(Item)
		with create_connection() as conn:
			result = conn.execute(statement)
			return result

class DML:
	"""Encapsulates database manipulation language (DML)"""

	@staticmethod
	def add_item(name:str, category:str):
		"""Adds a single item to Item table"""
		statement = Item.insert().values(name=name, category=category)
		with create_connection() as conn:
			result = conn.execute(statement)
			conn.commit()

	@staticmethod
	def add_items(payload:List[Dict[str, str]]):
		"""Inserts multiple items to Item table"""
		with create_connection() as conn:
			conn.execute(Item.insert(), payload)
			conn.commit()


