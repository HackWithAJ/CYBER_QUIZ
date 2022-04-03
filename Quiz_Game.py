#Quiz Game in Python

Playing = input("Do you wanna play(yes/no) = ")
if Playing.lower() != "yes":
    quit()

CYAN    = '\033[36m'
WHITE   = '\033[37m'
YELLOW  = '\033[33m'

print(CYAN + "              ______   ______  _____ ____      ___  _   _ ___ _____ ")
print(CYAN + "             / ___\ \ / / __ )| ____|  _ \    / _ \| | | |_ _|__  /  ")
print(CYAN + "            | |    \ V /|  _ \|  _| | |_) |  | | | | | | || |  / /   ")
print(CYAN + "            | |___  | | | |_) | |___|  _ <   | |_| | |_| || | / /_   ")
print(CYAN + "             \____| |_| |____/|_____|_| \_\___\__\_\\___/|___/____|  ")
print(CYAN + "                                         |_____|                                  ")
print(CYAN + "                                                                  By HackWithAJ     ")
print("")                
print(YELLOW + "Okay!! Let's Begin, Goodluck!!")
score = 0
print("")
#1
Answer = input(WHITE + "What is full form of BIOS? ")
if Answer.lower() == "basic input output system":
    print("Correct!")
    score += 1
#2
Answer = input("What is full form of MAC address? ")
if Answer.lower() == "media access controller":
    print("Correct!")
    score += 1
#3
Answer = input("What is full form of RAM? ")
if Answer.lower() == "random access memory":
    print("Correct!")
    score += 1
#4
Answer = input("What is full of GUI? ")
if Answer.lower() == "graphical user interface":
    print("Correct!")
    score += 1
#5
Answer = input("What is full form of CPU? ")
if Answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
#6
Answer = input("SMPS stands for? ")
if Answer.lower() == "switch mode power supply":
    print("Correct!")
    score += 1
#7
Answer = input("LDAP stands for? ")
if Answer.lower() == "lightweight directory access protocol":
    print("Correct!")
    score += 1
#8
Answer = input("ASCII stands for? ")
if Answer.lower() == "american standard code for information interchange":
    print("Correct!")
    score += 1
#9
Answer = input("Full form of API? ")
if Answer.lower() == "application programming interface":
    print("Correct!")
    score += 1
#10
Answer = input("What is full form of APIPA? ")
if Answer.lower() == "automatic private internet protocol address":
    print("Correct!")
    score += 1
#11
Answer = input("NIC stands for? ")
if Answer.lower() == "network interface card":
    print("Correct!")
    score += 1
#12
Answer = input("DNS stands for? ")
if Answer.lower() == "domain name system":
    print("Correct!")
    score += 1
#13
Answer = input("UEFI stands for? ")
if Answer.lower() == "unified extensible firmware interface":
    print("Correct!")
    score += 1
#14
Answer = input("OSI stands for? ")
if Answer.lower() == "open system interconnection":
    print("Correct!")
    score += 1
#15
Answer = input("What is full form of SSL? ")
if Answer.lower() == "secure socket layer":
    print("Correct!")
    score += 1
#16
Answer = input("ICMP stands for? ")
if Answer.lower() == "internet control message protocol":
    print("Correct!")
    score += 1
#17
Answer = input("UDP stands for? ")
if Answer.lower() == "user datagram protocol":
    print("Correct!")
    score += 1
#18
Answer = input("WAP stands for? ")
if Answer.lower() == "wireless access point":
    print("Correct!")
    score += 1
#19
Answer = input("Full form of PING is? ")
if Answer.lower() == "packet internet groper":
    print("Correct!")
    score += 1
#20
Answer = input("XML stands for? ")
if Answer.lower() == "extensible markup language":
    print("Correct!")
    score += 1
#21
Answer = input("VPN stands for? ")
if Answer.lower() == "virtual private network":
    print("Correct!")
    score += 1
#22
Answer = input("URL stands for? ")
if Answer.lower() == "uniform resource locator":
    print("Correct!")
    score += 1
#23
Answer = input("SEO stands for? ")
if Answer.lower() == "search engine optimization":
    print("Correct!")
    score += 1
#24
Answer = input("TELNET stands for? ")
if Answer.lower() == "teletype network protocol":
    print("Correct!")
    score += 1
#25
Answer = input("what is full form of CMOS? ")
if Answer.lower() == "complementary metal oxide semiconductor":
    print("Correct!")
    score += 1
#26
Answer = input("NTP stands for? ")
if Answer.lower() == "network time protocol":
    print("Correct!")
    score += 1
#27
Answer = input("what is full form of TCP? ")
if Answer.lower() == "transmission control protocol":
    print("Correct!")
    score += 1
#28
Answer = input("HTTPS stands for? ")
if Answer.lower() == "hyper text transfer protocol secure":
    print("Correct!")
    score += 1
#29
Answer = input("SMTP stands for? ")
if Answer.lower() == "simple mail transfer protocol":
    print("Correct!")
    score += 1
#30
Answer = input("What is full form of ARP? ")
if Answer.lower() == "address resolution protocol":
    print("Correct!")
    score += 1

print(YELLOW + "You got " + str(score) + " questions correct!")
print("You scored " + str((score / 30) * 100) + " %")

if score >= 28:
    print("You have exellent basics!")
elif score >= 20:
    print("Great! Still you need to learn!")
elif score <= 18:
    print("Not enough! You need more practise!")

Review = input(CYAN +"Have you enjoyed the cyber quiz? ")

if Review.lower() == "yes":
    print(CYAN + "ThankYou!! It means alot!! Have a nice day!! for more queries catch me at instagram - a.j__ftw ")
else:
    print(CYAN + "sorry to disappoint you, for more queries catch me at instagram - a.j__ftw ")
