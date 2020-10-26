import json #To convert Python string into json format


# JSON to Ultralight function 
def JSON_to_UL(json_obj):
	# -----------------------------------------------
    # CONVERTING JSON to ULTRALIGHT
    k = ''
    val = ''
    json_object = json.loads(json_obj)
    pairs = json_object.items()
    
    for key, value in pairs:
    	k=key
    	val=value
    	# print "key-",key
    	# print "value-",value

    ul_bat = k + "|" + val
    # -----------------------------
    # print "ultralight battery: ",ul_bat
    return ul_bat


# -------TESTING FUNCTION JSON_to_UL---------------------------------------------
# UNCOMMENT to test function
# bat_obj = {}
# key1 = "key"
# bat_obj[key1] = str(5551)

# js = json.dumps(bat_obj)
# print "JSON = ",js
# ul = JSON_to_UL(js)
# print "checking UL= ",ul
# ------------------------------------------------------------