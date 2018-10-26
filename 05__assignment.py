'''
Assignment #5
1. Add / modify code ONLY between the marked areas (i.e. "Place code below")
2. Run the associated test harness for a basic check on completeness. A successful run of the test cases does not guarantee accuracy or fulfillment of the requirements. Please do not submit your work if test cases fail.
3. To run unit tests simply use the below command after filling in all of the code:
    python 05_assignment.py
  
4. Unless explicitly stated, please do not import any additional libraries but feel free to use built-in Python packages
5. Submissions must be a Python file and not a notebook file (i.e *.ipynb)
6. Do not use global variables
7. Make sure your work is committed to your master branch
http://flask.pocoo.org/docs/1.0/quickstart/
Using the flask web server, load the HTML form contained in the variable main_page. The form should load at route '/'.
The user should then be able to enter a number and click Calculate at which time the browser will submit
an HTTP POST to the web server. The web server will then capture the post, extract the number entered
and display the number multiplied by 5 on the browser.
Hint: The HTML in main_page needs a modification in the text input
'''

from flask import Flask, request
import re

main_page = '''
<html>
    <head>
    <title></title>
    <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.min.css">
    </head>
<body>
<form class="form-horizontal" method="post" action="/calc">
<fieldset>
<!-- Form Name -->
<legend>Multiplier</legend>
<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="textinput">Number</label>  
  <div class="col-md-4">
  <input id="textinput" type="number" step="0.00001" name='number' placeholder="Enter a number" class="form-control input-md">
  </div>
</div>
<!-- Button -->
<div class="form-group">
  <label class="col-md-4 control-label" for="singlebutton"></label>
  <div class="col-md-4">
    <button id="singlebutton" name="singlebutton" class="btn btn-primary">Calculate</button>
  </div>
</div>
</fieldset>
</form>
<script src="http://netdna.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
</body>
</html>
'''
    # ------ Place code below here \/ \/ \/ ------


from flask import Flask
app = Flask(__name__)

@app.route('/')
#loads html template
def index():
	return main_page

@app.route("/calc", methods = ['POST'])
#performs multiplication
def calc():
	#reads entered number
	num = request.form['number']
	#if entry is not blank return the result
	if num != "":
	   result = float(num)*5
	   return main_page + '''<div class="col-md-4"></div><div class="col-md-4"><h3>5 x ''' + str(num)+ ''' = ''' + str(result) + '''</h3></div><div class="col-md-4"></div>'''
	#if entry is blank return the error message
	else:
	   return main_page + '''<div class="col-md-4"></div><div class="col-md-4"><h4 style="color:red;">Enter a valid number!</h4></div><div class="col-md-4"></div>'''   

 
if __name__ == "__main__":
    app.run()

    # ------ Place code above here /\ /\ /\ ------
