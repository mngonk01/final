from flask import Flask, request, render_template
import os
import psycopg2
import  json
import requests
from engine_module import GitData
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker,load_only

from init import getUrl

path = getUrl()
db = create_engine(path)
app = Flask(__name__)



#@app.route("/")
#def hello():
    #return '<h3>Enter user Name and Submit User GitHub repository on Data Base </h3></br><hr><form action="/fetch_api" method="POST"><input name="text"><input type="submit" value="Echo"></form>'
#    return  render_template()
#it have input form section in base.html file
@app.route('/')
def show_form():

    return render_template('base.html')


# Api get parameter form form section
@app.route('/fetch_api', methods=['GET', 'POST'])
def fetch_api():
    #fetch data and store in database
    #name = request.form.to_dict(flat=False)
    #print(name)
    first = request.form["username"]
    print(first)

    url_data = requests.get('https://api.github.com/users/' + first + '/repos')


    Session = sessionmaker(db)
    session = Session()
    data =  url_data.json()
    print(data)
    try:
        name = data[0]['name']
        full_name =data[0]['full_name']
        language =data[0]['language']
        forks_count = data[0]['forks_count']
        description =data[0]['description']


        user = GitData(name=name, full_name=full_name, language=language, forks_count=forks_count, description=description)
        session.add(user)
        session.commit()
    except KeyError as ke:
        pass

    return render_template('submit.html')




#fetch data from database and Display in database

@app.route('/fetch_data_from_database',methods=['GET'])
def renderblog():

  #simply fetch the data from postgresql and display in table formate in browser
    Session = sessionmaker(db)
    session = Session()
    allData = session.query(GitData).all()


    return render_template('result.html', data = allData)








if (__name__ == "__main__"):
    app.run(port=5002,debug=True)
