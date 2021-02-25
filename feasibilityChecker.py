#HTTP Server template
from http.server import BaseHTTPRequestHandler, HTTPServer

import time
import requests
import json

#usikker på om de to neste linjene er nødvedig!
#HOST_NAME = '127.0.0.1' 
#PORT_NUMBER = 4343 # Maybe set this to 1234

def materialCalculation(numbers):
    #should check the materials needed for production
	#based on product volume
	#not developed for this case but expandable for further development.
    return True #but for now

def retrieveManufaqConstrains():
    print("Vi er inne i retrieveManufaqConstrains")
    URL = "http://127.0.0.1:3030/chair_design/query"
    print("insde retriveManufaqConstraints: ")
    #the new select query added, but not tested
    selectQuery = 'PREFIX kbe:<http://www.kbe.com/chair_design.owl#> '+\
                'SELECT ?backHeightMax ?backHeightMin ?chairColor ?chairMaterial ?legLengthMax ?legLengthMin ?legSideMax ?legSideMin ?seatSideMax ?seatSideMin ?backShape ?shapeMaterial '+\
                'WHERE'+\
                '{'+\
                '?back_1 a kbe:Back.'+\
                '?back_1 kbe:hasBackHeightMax ?backHeightMax.'+\
                '?back_1 kbe:hasBackHeightMin ?backHeightMin.'+\
                '?chair_1 a kbe:Chair.'+\
                '?chair_1 kbe:hasColor ?chairColor.'+\
                '?chair_1 kbe:hasMaterial ?chairMaterial.'+\
                '?leg_1 a kbe:Leg.'+\
                '?leg_1 kbe:hasLegLengthMax ?legLengthMax.'+\
                '?leg_1 kbe:hasLegLengthMin ?legLengthMin.'+\
                '?leg_1 kbe:hasLegSideMax ?legSideMax.'+\
                '?leg_1 kbe:hasLegSideMin ?legSideMin.'+\
                '?shape_1 a kbe:Shape.'+\
                '?shape_1 kbe:hasMaterial ?shapeMaterial.'+\
                '?shape_1 kbe:hasShape ?backShape.'+\
                '?seat_1 a kbe:Seat.'+\
                '?seat_1 kbe:hasSeatSideMax ?seatSideMax.'+\
                '?seat_1 kbe:hasSeatSideMin ?seatSideMin.'+\
                '}'
    
    #testQuery = 'PREFIX kbe:<http://www.kbe.com/chair_design.owl#> SELECT ?data WHERE {?inst kbe:' + 'legLengthMax' + ' ?data.}'

    PARAMS = {'query': selectQuery}
    #PARAMS = {'query': testQuery}

    tull = requests.get(url = URL, params = PARAMS)
    print("ManuFaqConstrains r: ", tull.text)
    data = tull.json()
    #print("JSON: "+ data['results']['bindings'][0]['data']['value'])

    #arrangement of data_pool [backHeightMax,backHeightMin,chairColor,chairMaterial
    # legLengthMax,legLengthMin,legSideMax,legSideMin,shapeMaterial,backShape
    # seatSideMax,seatSideMin]
    """data_pool = [data['results']['bindings'][0]['backHeightMax']['value'],\
                data['results']['bindings'][0]['backHeightMin']['value'],\
                data['results']['bindings'][0]['chairColor']['value'],\
                data['results']['bindings'][0]['chairMaterial']['value'],\
                data['results']['bindings'][0]['legLengthMax']['value'],\
                data['results']['bindings'][0]['legLengthMin']['value'],\
                data['results']['bindings'][0]['legSideMax']['value'],\
                data['results']['bindings'][0]['legSideMin']['value'],\
                data['results']['bindings'][0]['shapeMaterial']['value'],\
                data['results']['bindings'][0]['backShape']['value'],\
                data['results']['bindings'][0]['seatSideMax']['value'],\
                data['results']['bindings'][0]['seatSideMin']['value']]"""
    
    return 0

def retrieveCustomerData():
    print("Vi er inne i retrieveCustomerData")
    URL = "http://127.0.0.1:3030/chair_data/query"
    selectQuery = 'PREFIX kbe:<http://www.kbe.com/chair_data.owl#>'+\
                'SELECT ?backHeight ?chairColor ?chairMaterial ?legLength ?legSide ?shapeMaterial ?backShape ?seatSide '+\
                'WHERE'+\
                '{'+\
                '?back_1 a kbe:Back.'+\
                '?back_1 kbe:hasBackHeight ?backHeight.'+\
                '?chair_1 a kbe:Chair.'+\
                '?chair_1 kbe:hasColor ?chairColor.'+\
                '?chair_1 kbe:hasMaterial ?chairMaterial.'+\
                '?leg_1 a kbe:Leg.'+\
                '?leg_1 kbe:hasLegLength ?legLength.'+\
                '?leg_1 kbe:hasLegSide ?legSide.'+\
                '?shape_1 a kbe:Shape.'+\
                '?shape_1 kbe:hasMaterial ?shapeMaterial.'+\
                '?shape_1 kbe:hasShape ?backShape.'+\
                '?seat_1 a kbe:Seat.'+\
                '?seat_1 kbe:hasSeatSide ?seatSide.'+\
                '}'
    PARAMS = {'query': selectQuery}
    tull = requests.get(url = URL, params = PARAMS)
    print("CustomerData r: ",tull.text)
    data = tull.json()
    print("JSON: ", data)

    data_pool_customer = [data['results']['bindings'][0]['backHeight']['value'],\
                data['results']['bindings'][0]['chairColor']['value'],\
                data['results']['bindings'][0]['chairMaterial']['value'],\
                data['results']['bindings'][0]['legLength']['value'],\
                data['results']['bindings'][0]['legSide']['value'],\
                data['results']['bindings'][0]['shapeMaterial']['value'],\
                data['results']['bindings'][0]['backShape']['value'],\
                data['results']['bindings'][0]['seatSide']['value']]
    
    return data_pool_customer

def feasibilityCheck():
    #for-loop with list for expandability and KBE-friendly
    
    production_intz_param = retrieveCustomerData()
    manufaqConstrains = retrieveManufaqConstrains()
    
    print("starting on evluating the data.")
    flagOK = False
    #arrangement of data_pool [backHeightMax,backHeightMin,chairColor,chairMaterial
        # legLengthMax,legLengthMin,legSideMax,legSideMin,shapeMaterial,backShape
        # seatSideMax,seatSideMin]

    #The indexes is a mess but its correct.
    if(production_intz_param[0] > manufaqConstrains[1]) and (production_intz_param[0] < manufaqConstrains[0]):
        if (production_intz_param[3] > manufaqConstrains[5]) and (production_intz_param[3] < manufaqConstrains[4]):
            if (production_intz_param[4] > manufaqConstrains[7]) and (production_intz_param[2] < manufaqConstrains[6]):
                if (production_intz_param[7] > manufaqConstrains[11]) and (production_intz_param[3] < manufaqConstrains[10]):
                    if production_intz_param[1] in manufaqConstrains[2]:
                        if production_intz_param[5] in manufaqConstrains[8]:
                            if production_intz_param[2] in manufaqConstrains[3]:
                                if materialCalculation(production_intz_param[7]):
                                    #return s.wfile.write(bytes('OK','utf-8'))
                                    print("The parameters are accepted")
                                    flagOK = True
    else:
        #return s.wfile.write(bytes('Not OK', 'utf-8'))
        print("The parameters given is not accepted")

    return flagOK

"""
print("feasibility checker started. \n")
# This is suppose to get a signal when a new chair is uploaded
# this should be happening in a time interval
URL = 'http://127.0.0.1:1234/yourOrder'
print("url found")			
r = requests.get(url = URL)
print(r.status_code)

print("Have asked about the url to fuseki")
answer = r.text
if answer.find("Update succeeded"):
    print("Succeeded find!")
    if feasibilityCheck():
        x.request.post(url, data = 'OK')
        print("Result of sending OK: ", x.text)
    else:
        x.request.post(url, data = 'NOT OK')
        print("Result of sending NOT OK: ", x.text)

"""    

# commented out the previous code

"""
class feasibilityChecker(BaseHTTPRequestHandler):

    #this need som more work
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

    def do_GET(s):
"""
        #Respond to a GET request.
"""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
		
		# Check what is the path
        path = s.path
        #constraints = s.retrieveManufaqConstrains()
        #s.wfile.write(bytes("<>", 'utf-8'))
        if path.find("/parametersSet") != -1 and len(path) == 1:
            #s.wfile.write(bytes('<html><head><title>Feasibility checker.</title></head>', 'utf-8'))
            #s.wfile.write(bytes("<body><p>Current path: " + path + "</p>", "utf-8"))
            #s.wfile.write(bytes('</body></html>', "utf-8"))
            #s.wfile.write(bytes('<form action="/checking" method="post">', 'utf-8'))
            print("inside get")
            constraints = s.retrieveManufaqConstrains()
    def do_POST(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
		
		# Check what is the path
        path = s.path
        print("Path: ", path)
        print("inside post.")

    def retrieveManufaqConstrains(s):
        URL = "http://127.0.0.1:3030/chair_design/query"
        print("insde retriveManufaqConstraints: ")
        #the new select query added, but not tested
        selectQuery = 'PREFIX kbe:<http://www.kbe.com/chair_design.owl#> '+\
                    'SELECT ?backHeightMax ?backHeightMin ?chairColor ?chairMaterial ?legLengthMax ?legLengthMin ?legSideMax ?legSideMin ?seatSideMax ?seatSideMin ?backShape ?shapeMaterial'+\
                    'WHERE'+\
                    '{'+\
                    'kbe:back_1 a kbe:Back.'+\
                    'kbe:back_1 kbe:hasBackHeightMax ?backHeightMax.'+\
                    'kbe:back_1 kbe:hasBackHeightMin ?backHeightMin.'+\
                    'kbe:chair_1 a kbe:Chair.'+\
                    'kbe:chair_1 kbe:hasColor ?chairColor.'+\
                    'kbe:chair_1 kbe:hasMaterial ?chairMaterial.'+\
                    'kbe:leg_1 a kbe:Leg.'+\
                    'kbe:leg_1 kbe:hasLegLengthMax ?legLengthMax.'+\
                    'kbe:leg_1 kbe:hasLegLengthMin ?legLengthMin.'+\
                    'kbe:leg_1 kbe:hasLegSideMax ?legSideMax.'+\
                    'kbe:leg_1 kbe:hasLegSideMin ?legSideMin.'+\
                    'kbe:shape_1 a kbe:Shape.'+\
                    'kbe:shape_1 kbe:hasMaterial ?shapeMaterial.'+\
                    'kbe:shape_1 kbe:hasShape ?backShape.'+\
                    'kbe:seat_1 a kbe:Seat.'+\
                    'kbe:seat_1 kbe:hasSeatSideMax ?seatSideMax.'+\
                    'kbe:seat_1 kbe:hasSeatSideMin ?seatSideMin.'+\
                    '}'

        PARAMS = {'query':selectQuery}

        r = requests.get(url = URL, params = PARAMS)
        print("r: ",r)
        data = r.json()

        #arrangement of data_pool [backHeightMax,backHeightMin,chairColor,chairMaterial
        # legLengthMax,legLengthMin,legSideMax,legSideMin,shapeMaterial,backShape
        # seatSideMax,seatSideMin]
        data_pool = [data['results']['bindings'][0]['backHeightMax']['value'],\
                    data['results']['bindings'][0]['backHeightMin']['value'],\
                    data['results']['bindings'][0]['chairColor']['value'],\
                    data['results']['bindings'][0]['chairMaterial']['value'],\
                    data['results']['bindings'][0]['legLengthMax']['value'],\
                    data['results']['bindings'][0]['legLengthMin']['value'],\
                    data['results']['bindings'][0]['legSideMax']['value'],\
                    data['results']['bindings'][0]['legSideMin']['value'],\
                    data['results']['bindings'][0]['shapeMaterial']['value'],\
                    data['results']['bindings'][0]['backShape']['value'],\
                    data['results']['bindings'][0]['seatSideMax']['value'],\
                    data['results']['bindings'][0]['seatSideMin']['value']]
        
        return data_pool

    def retrieveCustomerData(self):

        URL = "http://127.0.0.1:3030/chair_data/query"
        selectQuery = 'PREFIX kbe:<http://www.kbe.com/chair_data.owl#>'+\
                    'SELECT ?backHeight ?chairColor ?chairMaterial ?legLength ?legSide ?shapeMaterial ?backShape ?seatSide'+\
                    'WHERE'+\
                    '{'+\
                    'kbe:back_1 a kbe:Back.'+\
                    'kbe:back_1 kbe:hasBackHeight ?backHeight.'+\
                    'kbe:chair_1 a kbe:Chair.'+\
                    'kbe:chair_1 kbe:hasColor ?chairColor.'+\
                    'kbe:chair_1 kbe:hasMaterial ?chairMaterial.'+\
                    'kbe:leg_1 a kbe:Leg.'+\
                    'kbe:leg_1 kbe:hasLegLength ?legLength.'+\
                    'kbe:leg_1 kbe:hasLegSide ?legSide.'+\
                    'kbe:shape_1 a kbe:Shape.'+\
                    'kbe:shape_1 kbe:hasMaterial ?shapeMaterial.'+\
                    'kbe:shape_1 kbe:hasShape ?backShape.'+\
                    'kbe:seat_1 a kbe:Seat.'+\
                    'kbe:seat_1 kbe:hasSeatSide ?seatSide.'+\
                    '}'
        PARAMS = {'query':selectQuery}

        r = requests.get(url = URL, params = PARAMS)
        print("r: ",r)
        data = r.json()

        data_pool_customer = [data['results']['bindings'][0]['backHeight']['value'],\
                    data['results']['bindings'][0]['chairColor']['value'],\
                    data['results']['bindings'][0]['chairMaterial']['value'],\
                    data['results']['bindings'][0]['legLength']['value'],\
                    data['results']['bindings'][0]['legSide']['value'],\
                    data['results']['bindings'][0]['shapeMaterial']['value'],\
                    data['results']['bindings'][0]['backShape']['value'],\
                    data['results']['bindings'][0]['seatSide']['value']]
        
        return data_pool_customer

    def feasibilityCheck(self):
        #for-loop with list for expandability and KBE-friendly

        manufaqConstrains = s.retrieveManufaqConstrains()
        production_intz_param = s.retrieveCustomerData()

        flagOK = False
        #arrangement of data_pool [backHeightMax,backHeightMin,chairColor,chairMaterial
            # legLengthMax,legLengthMin,legSideMax,legSideMin,shapeMaterial,backShape
            # seatSideMax,seatSideMin]

        #The indexes is a mess but its correct.
        if(production_intz_param[0] > manufaqConstrains[1]) and (production_intz_param[0] < manufaqConstrains[0]):
            if (production_intz_param[3] > manufaqConstrains[5]) and (production_intz_param[3] < manufaqConstrains[4]):
                if (production_intz_param[4] > manufaqConstrains[7]) and (production_intz_param[2] < manufaqConstrains[6]):
                    if (production_intz_param[7] > manufaqConstrains[11]) and (production_intz_param[3] < manufaqConstrains[10]):
                        if production_intz_param[1] in manufaqConstrains[2]:
                            if production_intz_param[5] in manufaqConstrains[8]:
                                if production_intz_param[2] in manufaqConstrains[3]:
                                    if materialCalculation(production_intz_param[7]):
                                        return s.wfile.write(bytes('OK','utf-8'))
                                        #print("The parameters are accepted")
                                        flagOK = True
        else:
            return s.wfile.write(bytes('Not OK', 'utf-8'))
            #print("The parameters given is not accepted")

if __name__ == '__main__':
	server_class = HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), feasibilityChecker)
	
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
"""

#retrieveManufaqConstrains()