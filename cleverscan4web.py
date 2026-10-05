import subprocess

target = input("Enter the target IP or domaine : ")

print("=====================")
print("SCAN LAUNCH WITH NMAP")
print("=====================")

out_rest = subprocess.run(["nmap", "--stats-every=5s", "-sC", "sV", target], capture_output=True, text=True, check=True)

print(out_rest.stdout)

target_domain= input("Enter domain or IP of the Web Site : ")

port = input("Enter the port of the Web Site : ")

wich_protocol = input("Wich protocol ? http or https ? ")

if wich_protocol
# Exemple : feroxbuster -u http://10.129.234.47:3000  -w /usr/share/wordlists/rockyou.txt
feroxbuster -u http:// 



