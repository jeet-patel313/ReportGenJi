import smtplib
from email.message import EmailMessage


#variables for email sending
EmailAdd = "email@email.com" #enter email here
Pass = "passwordhere" #enter password here

def report():
	print("[+] Welcome to ReportGenerationji\n")
	#title = input("[+] Enter the title of your report: ")
	cvss = input("[+] Enter the cvss score: ")
	#intro = input("[+] Enter introduction for your report: ")
	vuln_name = input("[+] Enter the vulnerability name: ")
	vuln_endpoint = input("[+] Mention the endpoint: ")
	steps = input("[+] Enter the Steps To Reproduce the attack: ")
	impact = input("[+] What is the impact of the vulnerability: ")
	reme = input("[+] What Remediation do you suggest: ")
	
	
	#ref = input("[+] Is there any reference report you want to mention? ") 	

	#print("\n[+] Title: ", title)
	print("\n[+] Cvss score: ", cvss)
	#print(title)
	#print("[+] Introduction: ", intro)
	#print(intro)
	print("[+] Vulnerability Name: ", vuln_name)
	#print(vuln_name)
	print("[+] Vulnerability Endpoint: ", vuln_endpoint)
	#print(vuln_endpoint)
	print("[+] Steps To Reproduce: \n", steps)
	#print(steps)
	print("[+] Impact: ", impact)
	#print(impact)
	print("[+] Remediation: ", reme)
	#print(reme)
	#print("[+] Reference: ", ref)
	#print(ref)
	
	question = input("Do you want to email this report? ")
	if question == ("Y"):
		emailaddress = input("[+] enter email address to send this report: ")
		#from automail mail the report to the concerned authoritymsg = EmailMessage()
		msg = EmailMessage()
		msg["Subject"] = "Bug Report"
		msg["From"] = EmailAdd
		msg["To"] = emailaddress
		msg.set_content("Hello Team \nI have found a vulnerability in you scope whose details are given in this report.\nCvss Score given by reporter:"+cvss+"\nVulnerability Name: "+vuln_name+"\nVulnerability Endpoint"+vuln_endpoint+"\nSteps To Reproduce: "+steps+"\nImpact: "+impact+"\nRemediation: "+reme+"\n\nI hope I was able to explain the security issue. Hope to hear from you soon. \nThank YOU\nJeet Patel")
		with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
			smtp.login(EmailAdd, Pass)
			smtp.send_message(msg)
			smtp.quit()
		print("[+]An email of the report has been sent to the provided email", emailaddress)

	else:
		data = ["\n\n\nCvss Score by reporter: ", cvss, "\nVulnerability Name: ", vuln_name, "\nVulnerability Endpoint: ", vuln_endpoint, "\nSteps To Reproduce: ", steps, "\nImpact: ", impact, "\nRemediation: ", reme, "\n\nI hope I was able to explain the security issue. Hope to hear from you soon. \n Thank YOU\nJeet Patel"]
		file = open("report.txt", "a")
		file.writelines(data)
		file.close()
		print("[+] Your report has been saved to report.txt")

	

report()
