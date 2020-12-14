import requests
import json
import xlsxwriter

def get_pages_endpoint(pages):
    return json.loads(pages.content)["link"][1]["url"].split("=")[1].split("&")[0]
    
total = int(input("Type the number of elements to collect: "))
print("Manifolding...")

headers = {"Accept-Charset": 'utf-8',
    "Accept": 'application/fhir+xml;q=1.0, application/fhir+json;q=1.0, application/xml+fhir;q=0.9, application/json+fhir;q=0.9',
    "User-Agent":'HAPI-FHIR/5.2.0-SNAPSHOT (FHIR Client; FHIR 4.0.1/R4; apache)',
    "Accept-Encoding": 'gzip'}

# MEDICATION PART
URL = "http://hapi.fhir.org/baseR4/Medication?_pretty=true"
get_pages = requests.get(URL, headers=headers)
endpoint = get_pages_endpoint(get_pages)
dicc = {}

for t in range(0,total, 20):
    URL2 = "http://hapi.fhir.org/baseR4?_getpages=" + endpoint + "&_getpagesoffset=" + str(t) + "&_count=20&_pretty=true&_bundletype=searchset"
    page = requests.get(URL2, headers=headers)
    loaded_json = json.loads(page.content)
    lista = loaded_json["entry"]

    for l in lista:
        if "resource" in l:
            resource = l["resource"]
            
            if "code" in resource:
                code = resource["code"]
                
                if "coding" in code:
                    coding = code["coding"]
                    info_coding = coding[0]
                    if "display" in info_coding:
                        display = info_coding["display"]
                        
                    elif "text" in code:
                        text = code["text"]
                        display = text
                        
                    else:
                        display = "ERROR"
                        
                else:
                    text = code["text"]
                    display = text
            else:
                display = "ERROR"  
        
        if display != "ERROR":
            if display in dicc:
                dicc[display] = dicc[display] + 1
            else:
                dicc[display] = 1

#SORTING 
sorted_M = sorted(dicc.items(), key=lambda x: x[1], reverse=True)
sorted_dicc = {}
x_values = []
y_values = []

for s in sorted_M:
    sorted_dicc[s[0]] = s[1]
    x_values.append(s[0])
    y_values.append(s[1])

#Excel part
workbook = xlsxwriter.Workbook('FHIR_Global_Results.xlsx')
worksheet = workbook.add_worksheet("Medication")

row = 4
for sd in sorted_dicc:
    worksheet.write(row, 1, sd)
    worksheet.write(row, 2, sorted_dicc[sd])
    row = row + 1

dicc_len = len(sorted_dicc)
final_pos = dicc_len + 4

#Drawing the chart
chart = workbook.add_chart({'type': 'pie'})
chart.add_series({
    'categories': '=Medication!B5:B' + str(final_pos),
    'values':     '=Medication!C5:C'+ str(final_pos),})

worksheet.insert_chart('H9', chart)


# OBSERVATION PART
URL = "http://hapi.fhir.org/baseR4/Observation?_pretty=true"
get_pages = requests.get(URL, headers=headers)
dicc = {}
endpoint = get_pages_endpoint(get_pages)

for t in range(0,total, 20):
    URL2 = "http://hapi.fhir.org/baseR4?_getpages=" + endpoint + "&_getpagesoffset=" + str(t) + "&_count=20&_pretty=true&_bundletype=searchset"
    page = requests.get(URL2, headers=headers)
    loaded_json = json.loads(page.content)
    lista = loaded_json["entry"]
    for l in lista:
        display = "ERROR"
        if "resource" in l:
            resource = l["resource"]
            if "code" in resource:
                code = resource["code"]

                if "text" in code:
                    text = code["text"]
                    display = text
                elif "coding" in code:
                    coding = code["coding"]
                    if "display" in coding[0]:
                        display = coding[0]["display"]
        
        if display != "ERROR":
            if display in dicc:
                dicc[display] = dicc[display] + 1
            else:
                dicc[display] = 1

#SORTING 
sorted_M = sorted(dicc.items(), key=lambda x: x[1], reverse=True)
sorted_dicc = {}
x_values = []
y_values = []

for s in sorted_M:
    sorted_dicc[s[0]] = s[1]
    x_values.append(s[0])
    y_values.append(s[1])

#Excel part
worksheet = workbook.add_worksheet("Observation")

row = 4
for sd in sorted_dicc:
    worksheet.write(row, 1, sd)
    worksheet.write(row, 2, sorted_dicc[sd])
    row = row + 1

dicc_len = len(sorted_dicc)
final_pos = dicc_len + 4

#Drawing the chart
chart = workbook.add_chart({'type': 'pie'})
chart.add_series({
    'categories': '=Observation!B5:B' + str(final_pos),
    'values':     '=Observation!C5:C'+ str(final_pos),})

worksheet.insert_chart('H9', chart)

#DIAGNOSTIC REPORTS PART
URL = "http://hapi.fhir.org/baseR4/DiagnosticReport?_pretty=true"
get_pages = requests.get(URL, headers=headers)
endpoint = get_pages_endpoint(get_pages)
dicc = {}

for t in range(0,total, 20):
    URL2 = "http://hapi.fhir.org/baseR4?_getpages=" + endpoint + "&_getpagesoffset=" + str(t) + "&_count=20&_pretty=true&_bundletype=searchset"
    page = requests.get(URL2, headers=headers)
    loaded_json = json.loads(page.content)
    lista = loaded_json["entry"]

    for l in lista:
        if "resource" in l:
            resource = l["resource"]
            
            if "code" in resource:
                code = resource["code"]
                
                if "coding" in code:
                    coding = code["coding"]
                    info_coding = coding[0]
                    if "display" in info_coding:
                        display = info_coding["display"]
                        
                    elif "text" in code:
                        text = code["text"]
                        display = text
                        
                    else:
                        display = "ERROR"
                        
                else:
                    text = code["text"]
                    display = text
            else:
                display = "ERROR"  
        
        if display != "ERROR":
            if display in dicc:
                dicc[display] = dicc[display] + 1
            else:
                dicc[display] = 1

#SORTING 
sorted_M = sorted(dicc.items(), key=lambda x: x[1], reverse=True)
sorted_dicc = {}
x_values = []
y_values = []

for s in sorted_M:
    sorted_dicc[s[0]] = s[1]
    x_values.append(s[0])
    y_values.append(s[1])

#Excel part
worksheet = workbook.add_worksheet("DiagnosticReports")

row = 4
for sd in sorted_dicc:
    worksheet.write(row, 1, sd)
    worksheet.write(row, 2, sorted_dicc[sd])
    row = row + 1

dicc_len = len(sorted_dicc)
final_pos = dicc_len + 4

#Drawing the chart
chart = workbook.add_chart({'type': 'pie'})
chart.add_series({
    'categories': '=DiagnosticReports!B5:B' + str(final_pos),
    'values':     '=DiagnosticReports!C5:C'+ str(final_pos),})

worksheet.insert_chart('H9', chart)

workbook.close()
print("Done!")