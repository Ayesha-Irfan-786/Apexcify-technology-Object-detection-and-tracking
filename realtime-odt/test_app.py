from flask import Flask
app = Flask(_name_)
@app.route("/")
def hi(): return "Hello Flask"
if _name_ == "_main_":p