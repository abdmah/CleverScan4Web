import subprocess

target = input("Enter the target IP or domaine : ")

print("=====================")
print("SCAN LAUNCH WITH NMAP")
print("=====================")

out_rest = subprocess.run(["nmap", "--stats-every=5s", "-sC", "sV", target], capture_output=True, text=True, check=True)

print(out_rest.stdout)

wich_protocol = int(input("Wich protocol ? http(1) or https(2) ? "))

target_domain= input("Enter domain or IP of the Web Site : ")

port = input("Enter the port of the Web Site : ")


# Exemple : feroxbuster -u http://10.129.234.47:3000  -w /usr/share/wordlists/rockyou.txt

if wich_protocol == 1:
    out_ferox= subprocess.run(["feroxbuster", "-u", "http://", target_domain, ":", port], capture_output=True, text=True, check=True)
elif wich_protocol == 2:
    out_ferox= subprocess.run(["feroxbuster", "-u", "https://", target_domain, ":", port], capture_output=True, text=True, check=True)
else:
    print("Please enter 1 or 2")




