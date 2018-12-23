import json
#make the json pretty
f = open("AMI_Coarse.json", "r")
data = json.load(f)
f.close()
f = open("AMI_Coarse_pretty.json", "w")
json.dump(data, f, sort_keys=True, indent=4)
f.close()