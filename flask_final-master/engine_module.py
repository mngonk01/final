
from sqlalchemy import create_engine

from sqlalchemy import Column, String, Integer, Float

from sqlalchemy.ext.declarative import declarative_base



path = "postgres://ufnwicclfkyezi:dff1c5a9cd380acb719c6c600a99a2dc11b860c6a942198143b170809fa3e7c0@ec2-184-72-238-22.compute-1.amazonaws.com:5432/d2i90vhh1mmhk"
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
	
	
	

