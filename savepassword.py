import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
n = 0
for i in profiles:
    n += 1
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    haslo = ""
    #print( haslo.join(results))
    file = open("haslo"+i+".txt", "w")
    file.write( haslo.join(results) )
    file.close()
input("")


