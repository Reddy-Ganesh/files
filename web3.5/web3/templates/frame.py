from flask import *
app=Flask(__name__)
@app.route('/home' ,methods=['GET'])
def home():
    return render_template("sam.html")
if __name__=='__main__':
    app.run(debug=True)