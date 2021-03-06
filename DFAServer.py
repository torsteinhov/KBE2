#HTTP Server template

from http.server import BaseHTTPRequestHandler, HTTPServer
from feasibilityChecker import feasibilityCheck
import time
import requests
import json

HOST_NAME = '127.0.0.1' 
PORT_NUMBER = 1234 # Maybe set this to 1234

Torstein = "C:\\Kode\\GitHub\\KBE2\\KBE2\\" #location
Aashild = "C:\\Users\\Hilde\\OneDrive - NTNU\\Fag\\KBE2\\assig1\\KBE2-Chair-Design\\" #location
#yourLocation = "C:\\Users\\Hilde\\OneDrive - NTNU\\Fag\\KBE2\\DFAs" #this must be changed
yourLocation = Aashild #must be changed after whom is using it

#definfing parameters to be changed by the custommer
leg_length1 = "leg length"
leg_side1 = "leg width"
seat_side1 = "seat width"
back_height1 = "back height"
back_shape1 = "back shape"
#back_shape_color1 = "back shape color"
chair_color = "chair color"
back_shape_material1 = "back shape material"
chair_material1 = "chair material"
number_chair1 = "number of chairs"
fname1 = "first name"
lname1 = "last name"
email1 = "e-mail"
pnumber1 = "phone number"

custom_parameters = [leg_length1, leg_side1, seat_side1, back_height1, back_shape1, chair_color, back_shape_material1, chair_material1, number_chair1, fname1, lname1, email1, pnumber1]

resultQuery = False

# Handler of HTTP requests / responses
class MyHandler(BaseHTTPRequestHandler):


	def do_HEAD(s):
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()


	def do_GET(s):

		global leg_length1, leg_side1, seat_side1, back_height1, back_shape1, back_shape_color1, chair_color, back_shape_material1, chair_material1, number_chair1, fname1, lname1, email1, pnumber1, print_order
		global resultQuery
		"""Respond to a GET request."""
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		
		# Check what is the path
		path = s.path
		
		if path.find("/") != -1 and len(path) == 1:
			s.wfile.write(bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
			s.wfile.write(bytes("<body><p>Current path: " + path + "</p>", "utf-8"))
			s.wfile.write(bytes('</body></html>', "utf-8"))
		elif path.find("/orderChair") != -1:
			s.send_response(200)
			s.send_header("Content-type", "text/html")
			s.end_headers()
			s.wfile.write(bytes("<!DOCTYPE html><html><head>", 'utf-8'))
			s.wfile.write(bytes("<title>Chair Design</title>", 'utf-8'))
			s.wfile.write(bytes("</head><body style="'background-color:#DCFBCC;'">", 'utf-8'))
			s.wfile.write(bytes("<h1>Product details</h1>", 'utf-8'))
			s.wfile.write(bytes("<p>Welcome to our chair company. Here you can customize a chair for your home!</p>", 'utf-8'))
			s.wfile.write(bytes("<p> Write your desired parameters. </p>", 'utf-8'))

			s.wfile.write(bytes("<form action='/yourOrder' method='post'>", 'utf-8'))
			
			#starting with the inputs
			s.wfile.write(bytes("<label for='leg_length'>Length of the legs [cm]:</label><br>", 'utf-8'))
			s.wfile.write(bytes("<input type='text' id='leg_length' name='leg_length' value=" + str(leg_length1) +"><br><br>", 'utf-8'))
			s.wfile.write(bytes("<label for='leg_side'>Width of the legs [cm]: <br>(note that the legs is quadratic)</label><br>", 'utf-8'))
			s.wfile.write(bytes("<input type='text' id='leg_side' name='leg_side' value=" + leg_side1 + "><br><br>", 'utf-8'))
			s.wfile.write(bytes("<label for='seat_side'>Width of the seat [cm]:<br>(note that the seat is quadratic)</label><br>", 'utf-8'))
			s.wfile.write(bytes("<input type='text' id='seat_side' name='seat_side' value=" + seat_side1 + "><br><br>", 'utf-8'))
			s.wfile.write(bytes("<label for='back_height'>Height  of the back [cm]:</label><br>", 'utf-8'))
			s.wfile.write(bytes("<input type='text' id='back_height' name='back_height' value=" + back_height1+ "><br><br>", 'utf-8'))
			
			#starting with the option boxes
			s.wfile.write(bytes("<label for='back_shape'> Choose the shape in the back: </label>", 'utf-8'))
			s.wfile.write(bytes("<select id='back_shape' name='back_shape'>", 'utf-8'))
			s.wfile.write(bytes("<option value='circle'>Circles</option>", 'utf-8'))  
			s.wfile.write(bytes("<option value='square'>Square</option>", 'utf-8'))  
			s.wfile.write(bytes("<option value='cross'>Cross</option>", 'utf-8'))  
			s.wfile.write(bytes("</select> <br><br>", 'utf-8'))  

			""" #not a specific color for the shape in the back
			s.wfile.write(bytes("<label for='back_shape_color'> The color of the shape in the back: </label>", 'utf-8'))  
			s.wfile.write(bytes("<select id='back_shape_color' name='back_shape_color'>", 'utf-8'))  
			s.wfile.write(bytes("<option value='RED'>Red</option>", 'utf-8'))  
			s.wfile.write(bytes("<option value='BLUE'>Blue</option>", 'utf-8'))  
			s.wfile.write(bytes("<option value='YELLOW'>Yellow</option>", 'utf-8'))
			s.wfile.write(bytes("<option value='WHITE'>White</option>", 'utf-8'))
			s.wfile.write(bytes("<option value='BROWN'>Brown</option>", 'utf-8'))
			s.wfile.write(bytes("<option value='BLACK'>Black</option>", 'utf-8'))
			s.wfile.write(bytes("</select><br><br>", 'utf-8'))
			"""

			s.wfile.write(bytes("<label for='chair_color'> The color for the chair: </label>", 'utf-8'))
			s.wfile.write(bytes("<select id='chair_color' name='chair_color'>", 'utf-8')) 
			s.wfile.write(bytes("<option value='RED'>Red</option>", 'utf-8')) 
			s.wfile.write(bytes("<option value='BLUE'>Blue</option>", 'utf-8')) 
			s.wfile.write(bytes("<option value='YELLOW'>Yellow</option>", 'utf-8')) 
			s.wfile.write(bytes("<option value='WHITE'>White</option>", 'utf-8')) 
			s.wfile.write(bytes("<option value='BROWN'>Brown</option>", 'utf-8')) 
			s.wfile.write(bytes("<option value='BLACK'>Black</option>", 'utf-8'))  
			s.wfile.write(bytes("</select><br><br>", 'utf-8'))

			s.wfile.write(bytes("<label for='back_shape_material'> The material for the shape: </label>", 'utf-8'))
			s.wfile.write(bytes("<select id='back_shape_material' name='back_shape_material'>", 'utf-8'))
			s.wfile.write(bytes("<option value='Wood'>Wood</option>", 'utf-8'))
			s.wfile.write(bytes("<option value='Plastic'>Plastic</option>", 'utf-8'))
			s.wfile.write(bytes("<option value='Oak'>Oak</option>", 'utf-8'))
			s.wfile.write(bytes("<option value='Steel'>Steel</option>", 'utf-8'))
			s.wfile.write(bytes("<option value='Aluminum'>Aluminum</option>", 'utf-8'))
			s.wfile.write(bytes("<option value='Gold'>Gold</option>", 'utf-8'))
			s.wfile.write(bytes("</select><br><br>", 'utf-8'))

			s.wfile.write(bytes("<label for='chair_material'> The material for the chair: </label>", 'utf-8'))
			s.wfile.write(bytes("<select id='chair_material' name='chair_material'>", 'utf-8'))
			s.wfile.write(bytes("<option value='Wood'>Wood</option>", 'utf-8'))
			s.wfile.write(bytes("<option value='Plastic'>Plastic</option>", 'utf-8'))
			s.wfile.write(bytes("<option value='Oak'>Oak</option>", 'utf-8'))
			s.wfile.write(bytes("<option value='Steel'>Steel</option>", 'utf-8'))
			s.wfile.write(bytes("<option value='Aluminum'>Aluminum</option>", 'utf-8'))
			s.wfile.write(bytes("<option value='Gold'>Gold</option>", 'utf-8'))
			s.wfile.write(bytes("</select><br><br><br>", 'utf-8'))

			s.wfile.write(bytes("<label for='number_chair'>Number of chairs to order: </label><br>", 'utf-8'))
			s.wfile.write(bytes("<input type='text' id='number_chair' name='number_chair' value=" + number_chair1 + "><br><br>", 'utf-8'))

			s.wfile.write(bytes("<fieldset><legend>Personalia:</legend>", 'utf-8'))
			s.wfile.write(bytes("<label for='fname'>First name:</label><br>", 'utf-8'))
			s.wfile.write(bytes("<input type='text' id='fname' name=fname' value="+fname1+"><br>", 'utf-8'))
			s.wfile.write(bytes("<label for='lname'>Last name:</label><br>", 'utf-8'))
			s.wfile.write(bytes("<input type='text' id='lname' name='lname' value="+lname1+"><br>", 'utf-8'))
			s.wfile.write(bytes("<label for='email'>E-mail:</label><br>", 'utf-8'))
			s.wfile.write(bytes("<input type='text' id='email' name='email' value="+email1+"><br>", 'utf-8'))
			s.wfile.write(bytes("<label for='pnumber'>Phone number:</label><br>", 'utf-8'))
			s.wfile.write(bytes("<input type='text' id='pnumber' name='pnumber' value="+pnumber1+"><br><br>", 'utf-8'))

			s.wfile.write(bytes("</fieldset><br>", 'utf-8'))
			s.wfile.write(bytes("<p>Click 'Submit' to put your chair in the shopping cart:", 'utf-8'))
			s.wfile.write(bytes("<input type='submit' value='Submit'></p>", 'utf-8'))
			s.wfile.write(bytes("<p>Click 'Save' to save your design for later:", 'utf-8'))
			s.wfile.write(bytes("<input type='submit' value='Save'>", 'utf-8'))
			s.wfile.write(bytes("</p>", 'utf-8'))
			s.wfile.write(bytes('</form>', 'utf-8'))
			s.wfile.write(bytes('</body></html>', 'utf-8'))

		elif path.find("/chair_square.png") != -1:
			#Make right headers
			s.send_response(200)
			s.send_header("Content-type", "image/png")
			s.end_headers()
			#Read the file
			#Write file.
			bReader = open(yourLocation +"chair_square.png", "rb")
			theImg = bReader.read()
			#print(theImg)
			s.wfile.write(theImg)
			
		elif path.find("/yourOrder") != -1:
			s.wfile.write(bytes('<html><body style="background-color:#DCFBCC;"><h2>Chair</h2>', 'utf-8'))
			s.wfile.write(bytes('<form action="/yourOrder" method="post">', 'utf-8'))
			s.wfile.write(bytes('<p>The following parameters line has arrived: ' + print_order +'</p>', 'utf-8'))
			s.wfile.write(bytes('<p>We are checking if your chair is possible to make. Please wait.</p>', 'utf-8'))
			s.wfile.write(bytes('</form></body></html>', 'utf-8'))
		
		elif path.find("/info") != -1:
			s.wfile.write(bytes('<html><head><title>Cool interface.</title><meta http-equiv="refresh" content="3"></head>', 'utf-8'))
			s.wfile.write(bytes("<body><p>Info: Hello!.</p>" + str(i), "utf-8"))
			s.wfile.write(bytes('"</body></html>', "utf-8"))
			
	def do_POST(s):
		#allowing us to eddit the custom parameters
		global custom_parameters, resultQuery

		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		
		# Check what is the path
		path = s.path
		if path.find("/yourOrder") != -1:
			content_len = int(s.headers.get('Content-Length'))
			post_body = s.rfile.read(content_len)
			param_line = post_body.decode()

			#making a string to print
			global print_order, yourLocation
			print_order = ""
			#getting the parameter values
			key_val_pair = param_line.split('&')							#splitting the string at "&"
			for i in range(len(custom_parameters)): 						#itterating through the custom_parameter list
				print_order += str(custom_parameters[i]) 					#before changing the parameters, adding the to a string for printing
				print_order +=": "										#for a nice print
				custom_parameters[i] = key_val_pair[i].split('=')[1]		#spliting at "=" to only get the value
				if ' ' in custom_parameters[i]: 							#the last parameter has "HTTP/1.1" and we dont want it
					custom_parameters[i] = custom_parameters[i].split(" ")[0] #spliting to get rid of it ^
				print_order += str(custom_parameters[i])
				print_order += ", "

			resultQuery = s.uploadData(custom_parameters)

			# sjekk om dette går an å produseres mot manufChecker
			url = 'http://127.0.0.1:1234/yourOrder'
			if resultQuery:
		
				s.wfile.write(bytes('<p>Update succeeded.</p>', 'utf-8'))
				
				flagOK = feasibilityCheck()
				if flagOK:
					print("The customers order is OK")
					s.wfile.write(bytes('<p>Your order is possible to make. Congratulation with a new chair! </p>', 'utf-8'))
				else:
					print("The given parameters form the customer is not valid.")
					s.wfile.write(bytes('<p>Your order is not possible to make. Please try again. </p>', 'utf-8'))
				
				'''
				# For futher development
				x = requests.post(url, data = 'Update succeeded',verify=True)
				time.sleep(3) # wait for a few seconds
				x = requests.get(url) #reciving ok/not ok
				data = x.text
				if data.find("NOT OK"):
					print("The given parameters form the customer is not valid.")
					s.wfile.write(bytes('<p>Your order is not possible to make. Please try again. </p>', 'utf-8'))
				else: #if x.text.find("OK"):
					print("The customers order is OK")
					s.wfile.write(bytes('<p>Your order is possible to make. Congratulation with a new chair! </p>', 'utf-8'))
				#wait for 5 sec and set resultQuery to false again
				#print("result of sending the update message: ", x.text)
				'''
				
			fname1 = custom_parameters[9]
			lname1 = custom_parameters[10]
			print("custom_parameters: ", custom_parameters)
			print("back_shape: ", custom_parameters[4])
			#need to find which shape the order has in the back
			if flagOK:
				if custom_parameters[4] == "circle":
					#the shape is a circle
					f = open(yourLocation+"DFAtemplate\\chairdesign_circle_template.dfa", 'r')
					templatefile = f.read()
					oldFileName = "chairdesignCircle_template"
					f.close()
				elif custom_parameters[4] == "cross":
					#the shape is a cross
					f = open(yourLocation+"DFAtemplate\\chairdesign_cross_template.dfa", 'r')
					templatefile = f.read()
					oldFileName = "chairdesignCross_template"
					f.close()
				elif custom_parameters[4] == "square":
					#the shape is a square
					f = open(yourLocation+"DFAtemplate\\chairdesign_rectangle_template.dfa", 'r')
					templatefile = f.read()
					oldFileName = "chairdesignRectangle_template"
					f.close()
				else:
					print("the shape in the back is not recognised.")
			
				param = ["<leg_length>","<leg_side>","<seat_side>","<height_back>","<color_chair>"]

				fileNameFinishedProduct = fname1 + "_" + lname1 + "_finishedProduct"
				tekst = templatefile

				for i in range(len(param)):
					tekst = tekst.replace(param[i],custom_parameters[i])
				tekst = tekst.replace(oldFileName, fileNameFinishedProduct)

				f = open(yourLocation + "\\finished_product\\" + fileNameFinishedProduct + ".dfa", "w")
				f.write(tekst)
				f.close()
				print("Ready to open ", fileNameFinishedProduct)

			s.do_GET() #this is not a optimal solution

		if path.find("/"):
			content_len = int(s.headers.get('Content-Length'))
			post_body = s.rfile.read(content_len)
			param_line = post_body.decode()
			print("Body: ", param_line)
			s.wfile.write(bytes('<p>' + param_line + '</p>', 'utf-8'))
	
	def uploadData(self, custom_parameters):
		# UPLOAD CUSTOMER DATA TO FUSEKI
		
		URL = "http://127.0.0.1:3030/chair_data/update"
  
		# Query that deletes previous values.
		deleteQuery = 'PREFIX kbe:<http://www.kbe.com/chair_data.owl#> '+\
				'DELETE'+\
				'{' +\
				'?back_1 kbe:hasBackHeight ?backHeight.'+\
				'?chair_1 kbe:hasColor ?chairColor.'+\
				'?chair_1 kbe:hasMaterial ?chairMaterial.' +\
				'?leg_1 kbe:hasLegLength ?legLength.'+\
				'?leg_1 kbe:hasLegSide ?legSide.'+\
				'?shape_1 kbe:hasMaterial ?shapeMaterial.'+\
				'?shape_1 kbe:hasShape ?shape.'+\
				'?seat_1 kbe:hasSeatSide ?seatSide.'+\
				'}'+\
				'WHERE'+\
				'{'+\
				'?back_1 kbe:hasBackHeight ?backHeight.'+\
				'?chair_1 kbe:hasColor ?chairColor.'+\
				'?chair_1 kbe:hasMaterial ?chairMaterial.' +\
				'?leg_1 kbe:hasLegLength ?legLength.'+\
				'?leg_1 kbe:hasLegSide ?legSide.'+\
				'?shape_1 kbe:hasMaterial ?shapeMaterial.'+\
				'?shape_1 kbe:hasShape ?shape.'+\
				'?seat_1 kbe:hasSeatSide ?seatSide.'+\
				'}'

		PARAMS = {'update': deleteQuery}
		# sending get request and saving the response as response object 
		r = requests.post(url = URL, data = PARAMS)
		print("Result of DELETE query:", r.text)
		resultDelete = False
		if r.text.find("Update succeeded"):
			resultDelete =  True

		insertQuery = 'PREFIX kbe:<http://www.kbe.com/chair_data.owl#>' +\
				'PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>'+\
				'INSERT'+\
				'{'+\
				'?leg_1 kbe:hasLegLength "'+ str(custom_parameters[0])+'"^^xsd:int.'+\
				'?leg_1 kbe:hasLegSide "'+ str(custom_parameters[1])+'"^^xsd:int.'+\
				'?seat_1 kbe:hasSeatSide "'+ str(custom_parameters[2])+'"^^xsd:int.'+\
				'?back_1 kbe:hasBackHeight "'+ str(custom_parameters[3])+'"^^xsd:int.'+\
				'?shape_1 kbe:hasShape "'+ str(custom_parameters[4])+'"^^xsd:str.'+\
				'?chair_1 kbe:hasColor "'+ str(custom_parameters[5])+'"^^xsd:str.'+\
				'?shape_1 kbe:hasMaterial "'+ str(custom_parameters[6])+'"^^xsd:int.'+\
				'?chair_1 kbe:hasMaterial "'+ str(custom_parameters[7])+'"^^xsd:int.'+\
				'}'+\
				'WHERE'+\
				'{'+\
				'?leg_1 a kbe:Leg.'+\
				'?seat_1 a kbe:Seat.'+\
				'?back_1 a kbe:Back.'+\
				'?chair_1 a kbe:Chair.'+\
				'?shape_1 a kbe:Shape.'+\
				'}'
		# defining a query params 
		PARAMS = {'update': insertQuery} 
		r = requests.post(url = URL, data = PARAMS)
		#Checking the result
		print("Result of INSERT query:", r.text)
		resultInsert = False
		if r.text.find("Update succeeded"):
			resultInsert = True
		
		if (resultInsert and resultDelete):
			return True
		else:
			return False
 
if __name__ == '__main__':
	server_class = HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
	
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()