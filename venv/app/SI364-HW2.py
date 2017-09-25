## HW 2 
## SI 364 F17
## Due: September 24, 2017
## 500 points

#####

## [PROBLEM 1]

## Edit the following Flask application code so that if you run the application locally and got to the URL http://localhost:5000/question, you see a form that asks you to enter your favorite number. Once you enter a number and submit it to the form, you should then see a web page that says "Double your favorite number is <number>". For example, if you enter 2 into the form, you should then see a page that says "Double your favorite number is 4". Careful about types in your Python code!
## You can assume a user will always enter a number only.

#export FLASK_APP=SI364-HW2.py
#python -m flask run

from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True

@app.route('/question', methods=['GET', 'POST'])
def hello_to_you():
	x = """<!DOCTYPE html>
<html>
<body>
<form action="http://localhost:5000/result" method="GET">
<div>
<label>Favorite number:
<input type="text" name="number" value="">
</label>
<div>
<input type="submit" value="Submit">
</div>
</form>
</body>
</html>"""
	return x

@app.route('/result', methods=['GET', 'POST'])
def question():
	if request.method == "GET":
		num = request.args['number']
		# num *= 2
		x = int(num)
		# print (type(num))
		return "Double your favorite number is " + str(x*2)

@app.route('/question2', methods=['GET', 'POST'])
def hello_to_you2():
	x = """<!DOCTYPE html>
<html>
<body>
<form action="http://localhost:5000/result2" method="GET">
<div>
<label>Enter your name:
<input type="text" name="name" value="">
</label>
<label>Enter your age:
<input type="number" name="age" value="">
</label>
<label>Enter your search term:
<input type="text" name="searchterm" value="">
</label>
<div>
</label>
<input type="radio" name="store" value="Target"> Target<br>
<input type="radio" name="store" value="Walmart"> Walmart<br>
<input type="radio" name="store" value="Kohls"> Kohls
</label>
<div>
<input type="submit" value="Submit">
</div>
</form>
</body>
</html>"""
	return x

@app.route('/result2', methods=['GET', 'POST'])
def question2():
	if request.method == "GET":
		name = request.args['name']
		age = request.args['age']
		searchterm = request.args['searchterm']
		store = request.args['store']
		if int(age) > 13:
			url = ""
			if str(store) == "Target":
				url = 'https://www.target.com/s?searchTerm=' + str(searchterm)
			elif str(store) == "Walmart":
				url = 'https://www.walmart.com/search/?query=' + str(searchterm)
			else:
				url = 'https://www.kohls.com/search.jsp?submit-search=web-regular&search=' + str(searchterm)
			return "<html><body><p>Hi" + " " + str(name) + " " + "here is your <a href='" + str(url) + "' target='_blank'>customized URL</a> based off the search term " + str(searchterm) + " at " + str(store) + ".</p></body></html>"
		else:
			return "Hi " + str(name) + " " + "since you are below the age of 13 you cannot proceed."


if __name__ == '__main__':
    app.run()

#Explanation: The user will input their name, age, a search term of their choosing and will select from the radio buttons which store they would like to shop for that item from. If the user is below the age of 13 they will not be able to proceed. If they are over the age of 13, after they submit the form new data will appear. This new data will include a link to the website of the store they selected with the search results for whatever they entered as their search term. 

## [PROBLEM 2]

## Come up with your own interactive data exchange that you want to see happen dynamically in the Flask application, and build it into the above code for a Flask application. It should:
# - not be an exact repeat of something you did in class, but it can be similar
# - should include an HTML form (of any kind: text entry, radio button, checkbox... feel free to try out whatever you want)
# - should, on submission of data to the HTML form, show new data that depends upon the data entered into the submission form (text entered, radio button selected, etc). So if a user has to enter a number, it should do an operation on that number. If a user has to select a radio button representing a song name, it should do a search for that song in an API.
# You should feel free to be creative and do something fun for you -- 
# And use this opportunity to make sure you understand these steps: if you think going slowly and carefully writing out steps for a simpler data transaction, like Problem 1, will help build your understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you expect in your form; you do not need to handle errors or user confusion. (e.g. if your form asks for a name, you can assume a user will type a reasonable name; if your form asks for a number, you can assume a user will type a reasonable number; if your form asks the user to select a checkbox, you can assume they will do that.)











