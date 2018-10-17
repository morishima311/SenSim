import sys
import json

data = sys.stdin.read()
sys.stdin.close()

dict = json.loads(data)

with open('/home/morishima/workspace/simpleFog/fog/testlog.json', 'w') as f:
    f.write(json.dumps(dict))

threshold = 50

if dict["fields"]["value"] >= threshold:
    msg = "forward"
    sys.stdout.write(str(msg))
    #sys.stdout.close()
else:
    msg = "drop"
    sys.stdout.write(str(msg))
    #sys.stdout.close()

sys.stdout.close()
