from flask import Flask, render_template
app =Flask(__name__, template_folder="web2")
@app.route('/')
def home():
    return render_template("C:\web2\loginpage.html")
if __name__=='__main__':
    app.run(debug=True)