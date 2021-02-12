#HTTP Server template

from http.server import BaseHTTPRequestHandler, HTTPServer

HOST_NAME = '127.0.0.1' 
PORT_NUMBER = 4321 # Maybe set this to 1234


#definfing parameters upper and lower limits
leg_lengthUp = 2000
leg_lengthLow = 500
leg_sideUp = 50
leg_sideLow = 100
seat_sideUp = 1000
seat_sideLow = 300
back_heightUp = 1500
back_heightLow = 200

chair_color = [RED, GREEN, BROWN, BLACK] # a list with the avaliable colors
back_shape_material = [] #a list with avaliable materials
chair_material = [] #a list with avaliable matrials
# ??  number_chair = # check if there is enough materials for number of chair orders

custom_parameters = [leg_length1, leg_side1, seat_side1, back_height1, chair_color, back_shape_material1, chair_material1, number_chair1]
print_order = "Hei på deg, dette fungerer ikke."

def materialCalculation(numbers):
    #should check the materials needed for production
	#based on product volume
	#not developed for this case but expandable for further development.
    return True #but for now

    
# Handler of HTTP requests / responses
class MyHandler(BaseHTTPRequestHandler):


	def do_HEAD(s):
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()


	def do_GET(s):

		global leg_length1, leg_side1, seat_side1, back_height1, back_shape1, back_shape_color1, chair_color, back_shape_material1, chair_material1, number_chair1, fname1, lname1, email1, pnumber1, print_order
		"""Respond to a GET request."""
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		
		# Check what is the path
		path = s.path
		
		#making it possible to get the global variables
		#s.wfile.write(bytes("<>", 'utf-8'))
		if path.find("/") != -1 and len(path) == 1:
			s.wfile.write(bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
			s.wfile.write(bytes("<body><p>Current path: " + path + "</p>", "utf-8"))
			s.wfile.write(bytes('</body></html>', "utf-8"))
		elif path.find("/setParams") != -1:

			s.wfile.write(bytes("<!DOCTYPE html><html><body>", 'utf-8'))
			s.wfile.write(bytes("<h2>Product details intervals and available</h2>", 'utf-8'))
			s.wfile.write(bytes("<p>Please fill in details about the production below. </p>", 'utf-8'))

			s.wfile.write(bytes("<form action="/action_page.php">", 'utf-8'))

			#intervals for leg length, leg side, seat side, back height
			s.wfile.write(bytes("<p> Write maximum and minimum parameters. </p>", 'utf-8'))

			s.wfile.write(bytes('<label for="leg_lengthUp">Max leg length:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="leg_lengthUp" name="leg_lengthUp" value="John"><br>', 'utf-8'))
			s.wfile.write(bytes('<label for="leg_lengthLow">Min leg length:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="leg_lengthLow" name="leg_lengthLow" value="Doe"><br><br>', 'utf-8'))

			s.wfile.write(bytes('<label for="leg_sideUp">Max leg width:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="leg_sideUp" name="leg_sideUp" value="John"><br>', 'utf-8'))
			s.wfile.write(bytes('<label for="leg_sideLow">Min leg width:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="leg_sideLow" name="leg_sideLow" value="Doe"><br><br>', 'utf-8'))

			s.wfile.write(bytes('<label for="seat_sideUp">Max seat width:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="seat_sideUp" name="seat_sideUp" value="John"><br>', 'utf-8'))
			s.wfile.write(bytes('<label for="seat_sideLow">Min seat width:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="seat_sideLow" name="seat_sideLow" value="Doe"><br><br>', 'utf-8'))

			s.wfile.write(bytes('<label for="back_heightUp">Max back height:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="back_heightUp" name="back_heightUp" value="John"><br>', 'utf-8'))
			s.wfile.write(bytes('<label for="back_heightLow">Min back height:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="back_heightLow" name="back_heightLow" value="Doe"><br><br>', 'utf-8'))

			#chair colors
			s.wfile.write(bytes('<p>Select the available colors for the chair:</p>', 'utf-8'))
			s.wfile.write(bytes('<input type="checkbox" id="chair_color" name="chair_color" value="RED">', 'utf-8'))
			s.wfile.write(bytes('<label for="chair_color"> Red</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="chair_color" name="chair_color" value="BLUE">', 'utf-8'))
			s.wfile.write(bytes('<label for="chair_color"> Blue</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="chair_color" name="chair_color" value="YELLOW">', 'utf-8'))
			s.wfile.write(bytes('<label for="chair_color"> Yellow</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="chair_color" name="chair_color" value="WHITE">', 'utf-8'))
			s.wfile.write(bytes('<label for="chair_color"> White</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="chair_color" name="chair_color" value="BROWN">', 'utf-8'))
			s.wfile.write(bytes('<label for="chair_color"> Brown</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="chair_color" name="chair_color" value="BLACK">', 'utf-8'))
			s.wfile.write(bytes('<label for="chair_color"> Black</label><br><br>', 'utf-8'))

			#back shape material
			s.wfile.write(bytes('<p>Select the available material for the back shape:</p>', 'utf-8'))
			s.wfile.write(bytes('<input type="checkbox" id="back_shape_material" name="back_shape_material" value="Wood">', 'utf-8'))
			s.wfile.write(bytes('<label for="back_shape_material"> Wood</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="back_shape_material" name="back_shape_material" value="Plastic">', 'utf-8'))
			s.wfile.write(bytes('<label for="back_shape_material"> Plastic</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="back_shape_material" name="back_shape_material" value="Oak">', 'utf-8'))
			s.wfile.write(bytes('<label for="back_shape_material"> Oak</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="back_shape_material" name="back_shape_material" value="Steel">', 'utf-8'))
			s.wfile.write(bytes('<label for="back_shape_material"> Steel</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="back_shape_material" name="back_shape_material" value="Aluminum">', 'utf-8'))
			s.wfile.write(bytes('<label for="back_shape_material"> Brown</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="back_shape_material" name="back_shape_material" value="Gold">', 'utf-8'))
			s.wfile.write(bytes('<label for="back_shape_material"> Gold</label><br><br>', 'utf-8'))

			#chair_material
			s.wfile.write(bytes('<p>Select the available material for the chair:</p>', 'utf-8'))
			s.wfile.write(bytes('<input type="checkbox" id="chair_material" name="chair_material" value="Wood">', 'utf-8'))
			s.wfile.write(bytes('<label for="chair_material"> Wood</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="chair_material" name="chair_material" value="Plastic">', 'utf-8'))
			s.wfile.write(bytes('<label for="chair_material"> Plastic</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="chair_material" name="chair_material" value="Oak">', 'utf-8'))
			s.wfile.write(bytes('<label for="chair_material"> Oak</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="chair_material" name="chair_material" value="Steel">', 'utf-8'))
			s.wfile.write(bytes('<label for="chair_material"> Steel</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="chair_material" name="chair_material" value="Aluminum">', 'utf-8'))
			s.wfile.write(bytes('<label for="chair_material"> Brown</label><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="checkbox" id="chair_material" name="chair_material" value="Gold">', 'utf-8'))
			s.wfile.write(bytes('<label for="chair_material"> Gold</label><br><br>', 'utf-8'))

			s.wfile.write(bytes('<input type="submit" value="Submit"></form>', 'utf-8'))
			s.wfile.write(bytes('</body></html>', 'utf-8'))
			s.wfile.write(bytes('', 'utf-8'))

			
	def do_POST(s):
		#allowing us to eddit the custom parameters
		global custom_parameters

		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		
		# Check what is the path
		path = s.path
		print("Path: ", path)
		print("hei på deg!!")
		if path.find("/yourOrder") != -1:
			
			#for debugging
			print("Nå er vi i post-method. ")

			#copied form practise lecture -- is this nessesary?
			content_len = int(s.headers.get('Content-Length'))
			post_body = s.rfile.read(content_len)
			param_line = post_body.decode()
			print("Body: ", param_line)

			#making a string to print
			global print_order, yourLocation
			print_order = ""
			#getting the parameter values
			key_val_pair = param_line.split('&')						#splitting the string at "&"
			for i in range(len(custom_parameters)): 						#itterating through the custom_parameter list
				print_order += str(custom_parameters[i]) 					#before changing the parameters, adding the to a string for printing
				print_order +=": " 											#for a nice print
				custom_parameters[i] = int(key_val_pair[i].split('=')[1])		#spliting at "=" to only get the value
				if ' ' in custom_parameters[i]: 							#the last parameter has "HTTP/1.1" and we dont want it
					custom_parameters[i] = custom_parameters[i].split(" ")[0] #spliting to get rid of it ^
				print_order += str(custom_parameters[i])
				print_order += ", "
			
			#for-loop with list for expandability and KBE-friendly
            custom_parameters = [leg_length1, leg_side1, seat_side1, back_height1, chair_color, back_shape_material1, chair_material1, number_chair1]
			flagOK = False
            if(custom_parameters[0] > leg_lengthLow) and (custom_parameters[0] < leg_lengthUp):
                if (custom_parameters[1] > leg_sideLow) and (custom_parameters[1] < leg_sideUp):
                    if (custom_parameters[2] > seat_sideLow) and (custom_parameters[2] < leg_sideUp):
                        if (custom_parameters[3] > back_heightLow) and (custom_parameters[3]< back_heightUp):
                            if custom_parameters[4] in chair_color:
                                if custom_parameters[5] in back_shape_material:
                                    if custom_parameters[6] in chair_material:
                                        if materialCalculation(custom_parameters[7]):
											s.wfile.write(bytes('OK','utf-8'))
											print("The parameters are accepted")
                                            flagOK = True
            else:
                s.wfile.write(bytes('Not OK', 'utf-8'))
				print("The parameters given is not accepted")

		

	def setConstrain(self, constrain, value):
		URL = "http://127.0.0.1:3030/kbe/update"
  
		# Query that deletes previous values.
		deleteQuery = 'PREFIX kbe:<http://kbe.com/chair_design.owl#> '+\
				'DELETE'+\
				'{' +\
				'kbe:chair a kbe:Chair.'+\
				'kbe:chair ?pred ?obj.'+\
				'kbe:leg a kbe:Leg.' +\
				'kbe:leg ?pred ?obj.'+\
				'kbe:seat a kbe:Seat.'+\
				'kbe:seat ?pred ?obj.'+\
				'kbe:back a kbe:Back.'+\
				'kbe:back ?pred ?obj.'+\
				'kbe:shape a kbe:Shape.'+\
				'kba:shape ?pred ?obj.'+\
				'}'+\
				'WHERE'+\
				'{'+\
				'kbe:chair ?pred ?obj.'+\
				'kbe:leg ?pred ?obj.'+\
				'kbe:seat ?pred ?obj.'+\
				'kbe:back ?pred ?obj.'+\
				'kba:shape ?pred ?obj.'+\
				'}'

		PARAMS = {'update': deleteQuery}
		# sending get request and saving the response as response object 
		r = requests.post(url = URL, data = PARAMS) 

 
if __name__ == '__main__':
	server_class = HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
	
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
