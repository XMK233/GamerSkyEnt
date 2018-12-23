import json
#see the head of the whole json file
f = open("AMI_Coarse.json", "r")
data = json.load(f)
f.close()
f = open("AMI_Coarse_head.json", "w")
json.dump(data[0], f, sort_keys=True, indent=4)
f.close()

print(data[0])