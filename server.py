from flask import Flask, render_template, request, redirect, flash, session
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^([^0-9]*|[^A-Z]*)$')
app = Flask(__name__)
app.secret_key = 'secret103048580e8w7'

# THE DEFAULT LANDING PAGE
@app.route("/")
def landing():
	return render_template("index.html")

@app.route("/result", methods = ["POST"])
def posting():
	###########################
	#VALIDATING THE FIRST NAME#
	###########################
	if len(request.form['first_name']) < 1:
		flash("First name cannot be empty!") # just pass a string to the flash function
		return redirect("/")
	elif request.form['first_name'].isalpha() != True:
		flash("First name must only contain alphabetic letters.")
		return redirect("/")
	else:
		session['first_name'] = request.form['first_name']

	##########################
	#VALIDATING THE LAST NAME#
	##########################
	if len(request.form['last_name']) < 1:
		flash("Last name cannot be empty!") # just pass a string to the flash function
		return redirect("/")
	elif request.form['last_name'].isalpha() != True:
		flash("Last name must only contain alphabetic letters.")
		return redirect("/")
	else:
		session['last_name'] = request.form['last_name']

	######################
	#VALIDATING THE EMAIL#
	######################
	if len(request.form['email']) < 1:
		flash("Email cannot be blank!")
		return redirect("/")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address!")
		return redirect("/")
	else:
		session['email'] = request.form['email']

	#########################
	#VALIDATING THE PASSWORD#
	#########################
	thepassword = request.form['password_1']

	if len(request.form['password_1']) < 8:
		flash("Password must be at least 8 characters.")
		return redirect("/")
	elif PASSWORD_REGEX.match(request.form['password_1']):
		flash("You must include at least 1 number and 1 uppercase letter in your password.")
		return redirect("/")
	else:
		session['password_1'] = request.form['password_1'] 

	#####################################
	#VALIDATING CONFIRMATION OF PASSWORD#
	#####################################
	if request.form['password_2'] == request.form['password_1']:
		session['password_2'] = request.form['password_2']
	else:
		flash("Passwords do not match.")
		return redirect("/")

	return redirect('/submit')

@app.route("/submit")
def submitted():
	print "Thank you for submitting your information"
	return	render_template("submit.html")


app.run(debug=True)