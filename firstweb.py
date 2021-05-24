from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return"<h1>hello world</h1>"

##creating 

#home
#contactus
#products
#services
#about us

 
@app.route('/about')
def about_page():
	return "<b/h1>about us</h1>"

@app.route('/home')
def home_page():
	return "<b> EXCLUSIVE TREAT LAUNDRY AND BOUTIQUE</b>"
@app.route('/contactus')
def contactus():
	return "<p> benjaminharry21@gmail.com, 08109318429</p>"
@app.route('/products')
def products():
	return "<h2> we offer dry claening services and provide male apparels</h2>"

@app.route('/services')
def services():
	return "<h3> we offer both home and office delivery</h3>"


