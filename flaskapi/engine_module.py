
from sqlalchemy import create_engine

from sqlalchemy import Column, String, Integer, Float

from sqlalchemy.ext.declarative import declarative_base



path = "postgresql://postgres:root@localhost/postgres"
db = create_engine(path)
base = declarative_base()


class GitData(base):
	#create a table name region and store the data 
	__tablename__ = 'gihubdata'
	id = Column(Integer, primary_key = True)
	name = Column(String)
	full_name = Column(String)
	language = Column(String)
	forks_count = Column(Integer)
	description = Column(String)
	
	 
	def __init__(self, name, full_name, language, forks_count, description):
		self.name = name
		self.full_name = full_name
		self.language = language
		self.forks_count = forks_count
		self.description = description
		
if __name__ == "__main__":
	base.metadata.create_all(db)
	
	
	

