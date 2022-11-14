import PySimpleGUI as sg
import random
import string


# Add some color to the window
sg.theme('Dark2')	

layout = [
	[sg.Text('Please enter your Info Below:')],
	[sg.Text('Employee ID', size =(15, 1)), sg.InputText()],
	[sg.Text('Full Name', size =(15, 1)), sg.InputText()],
	[sg.Text('Contractor',size=(15, 1), font='Lucida',justification='left')],
    [sg.Combo(['Yes','No'],key='con')],
    [sg.Text('Employee Level',size=(15, 1), font='Lucida',justification='left')],
    [sg.Combo(['Non-Employee','Employee','Supervisor', 'Manager','Executive'],key='lev')],
	[sg.Text('Department',size=(15, 1), font='Lucida',justification='left')],
    [sg.Combo(['Supply','Human Resources','Information Technology', 'Executive'],key='dep')],
	[sg.Text('Remote Job',size=(15, 1), font='Lucida',justification='left')],
    [sg.Combo(['Yes','No'],key='rem')],
    [sg.Text('Transfer, Change of Job, or Promotion',size=(15, 1), font='Lucida',justification='left')],
    [sg.Combo(['Yes','No'],key='tra')],
	[sg.Text('Revoke Access',size=(15, 1), font='Lucida',justification='left')],
    [sg.Combo(['Yes','No'],key='rev')],
	[sg.Submit('Run'), sg.Cancel('Exit')]
]

window = sg.Window('Employee Access Form', layout, no_titlebar=True, grab_anywhere=True)



event, values = window.read()
window.close()


# The input data looks like a simple list
# when automatic numbered

access_var = ""

if values['rev'] == "Yes":
    access_var = "Revoke Access"
elif values['tra'] == "Yes":
    access_var = "Change Access"
else:
    access_var = "Grant Access"

id_number = values[0]
con_var = ""
lev_var = ""
dir_var = ""
rem_var = ""
last_three = values[0][-3::]


#Contractor
if values['con'] == "Yes":
    con_var = "Access Category: Restricted"

elif values['con'] == "No":
    con_var = "Access Category: Normal"

#Employee Level
if values['lev'] == "Non-Employee":
    lev_var = "Physical Access: Escort Required"

elif values['lev'] == "Employee":
    lev_var = "Physical Access: Common Areas"

elif values['lev'] == "Supervisor":
    lev_var = "Physical Access: Common Areas, Supervised Section"

elif values['lev'] == "Manager":
    lev_var = "Physical Access: Common Areas, Department-Wide"

elif values['lev'] == "Executive":
    lev_var = "Physical Access: All"

#File Directory Access
if values['dep'] == "Human Resources":
      
    if values['lev'] == "Employee":
        dir_var = "File Directory Access: /HR/Section A/Employee Data"

    elif values['lev'] == "Supervisor":
        dir_var = "File Directory Access: /HR/Section A"

    elif values['lev'] == "Manager":
        dir_var = "File Directory Access: /HR/"


elif values['dep'] == "Supply":

    if values['lev'] == "Employee":
        dir_var = "File Directory Access: /Supply/Team 1/Invoices"

    elif values['lev'] == "Supervisor":
        dir_var = "File Directory Access: /Supply/Team 1"

    elif values['lev'] == "Manager":
        dir_var = "File Directory Access: /Supply/"

elif values['dep'] == "Information Technology":
      
    if values['lev'] == "Employee":
        dir_var = "File Directory Access: /IT/IT Admin/Help Tickets"

    elif values['lev'] == "Supervisor":
        dir_var = "File Directory Access: /IT/IT Admin"

    elif values['lev'] == "Manager":
        dir_var = "File Directory Access: /IT/"

elif values['dep'] == "Executive":
    dir_var = "File Directory Access: /"

if values['rem'] == "Yes":
    rem_var = "VPN Access Required: Yes"

elif values['rem'] == "No":
    rem_var = "VPN Access Required: No"
    
#Random Password Generator

letters = string.ascii_letters
x = ''.join(random.choice(letters) for i in range(10)) 

if access_var == "Grant Access" or access_var == "Change Access":
    with open("C:/Users/nicho/OneDrive/Documents/Access Ctrl/"+id_number+'.txt', 'w') as f:
        f.write(access_var + '\n' + '--------------------------------------------------------' + '\n' +
            "Employee Summary:" + '\n' + '\n' +
            "Employee ID: " + values[0] + '\n' +
            "Full Name: " + values[1] + '\n' +
            "Contractor: " + values['con'] + '\n' +    
            "Employee Level: " + values['lev'] + '\n' +
            "Department: " + values['dep'] + '\n' +
            "Remote: " + values['rem'] + '\n' +
            "Lateral Transfer, Change of Position, or Promotion: " + values['tra'] + '\n' +
            "Revoke Access: " + values['rev'] + '\n' +'\n' +
            '--------------------------------------------------------' + '\n' +
            "Access Summary:" + '\n' + '\n' +
            con_var + '\n' + 
            lev_var + '\n' +
            dir_var + '\n' +
            rem_var + '\n' +
            '--------------------------------------------------------' + '\n' +
            "Login Credentials:" + '\n' + '\n' +
            'Username: ' + values[1][:1:]+values[0] + '\n' +
            'Temporary Password: ' + x+last_three)
        
elif access_var == "Revoke Access":
    with open("C:/Users/nicho/OneDrive/Documents/Access Ctrl/"+id_number+'.txt', 'w') as f:
        f.write(access_var + '\n' + '--------------------------------------------------------' + '\n' +
            "Employee ID: " + values[0] + '\n' +
            "Full Name: " + values[1] + '\n' +
            "Contractor: " + values['con'] + '\n' +    
            "Employee Level: " + values['lev'] + '\n' +
            "Department: " + values['dep'] + '\n' +
            "Remote: " + values['rem'] + '\n' +
            "Lateral Transfer, Change of Position, or Promotion: " + values['tra'] + '\n' +
            "Revoke Access: " + values['rev'])