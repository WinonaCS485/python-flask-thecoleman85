import pymysql.cursors
from flask import Flask, render_template
# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='an8520td',
                             password='Toby2020!',
                             db='an8520td_university',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


try:
    with connection.cursor() as cursor:
        # Select all Students
        sql = ("SELECT * from Students")
        # execute the SQL command
        cursor.execute(sql)
        
        output = cursor.fetchall()

finally:
    connection.close()




app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',output=output)

@app.route('/cakes')
def cakes():
    return 'yummy cakes'



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port='8520')


