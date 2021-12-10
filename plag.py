
#
# import requests
#
# response = requests.request(
#     method='POST',
#     url='https://www.prepostseo.com/apis/checkPlag',
#     data = {'key': 'd9ee4480af8c9926d4cc81badb48b588','data':'On the red table, there was a purple curtain. Underneath that was a silver cage.  Inside that cage there was a green teddy bear, with the number 43 written on its chest with a black permanent marker. Its eyes were as green as envy.'},
# )
# print(response.text)
#
# import PyPDF2
#
# pdffile = open('test.pdf','rb')
# reader = PyPDF2.PdfFileReader(pdffile)
#
# # read = reader.getPage(7-1).extractText()
# # print(read)
# print("numpage", reader.numPages)
#
# pageObj = reader.getPage(0)
# print(pageObj.extractText())
#
# pdffile.close()

# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from pdfminer.pdfpage import PDFPage
# from io import StringIO
#
# def convert_pdf_to_txt(path):
#     rsrcmgr = PDFResourceManager()
#     retstr = StringIO()
#     codec = 'utf-8'
#     laparams = LAParams()
#     device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
#     fp = open(path, 'rb')
#     interpreter = PDFPageInterpreter(rsrcmgr, device)
#     password = ""
#     maxpages = 0
#     caching = True
#     pagenos=set()
#
#     for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
#         interpreter.process_page(page)
#
#     text = retstr.getvalue()
#
#     fp.close()
#     device.close()
#     retstr.close()
#     return text
#
# print(convert_pdf_to_txt("test.pdf"))


# COPYLEAKS
# 2d1e3331-ff6d-4ba7-8a67-38df46701de2
# SMALLSEOTOOLS
# 48e2d678e42e2c611d03cb53efb88ea6
#
# ##################### PDF TO TXT #############
# f = open("fromcloudmersive.txt", "r", encoding="utf8")
# totxt = open('totxt.txt', 'w', encoding="utf8")
# file = f.readlines()
#
# for fil in file:
#     if len(fil) > 1:
#         totxt.write(fil.strip() + " ")
#
# # newfile = ""
# # print(len(newfile))
# #
# # for fil in file:
# #     # print(fil.strip("\n"))
# #     totxt.write(fil.strip("\n") + " ")
# #     # print("new")
#
#
# # print(newfile[0])
# f.close()

################################################

#eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNzY2NmMzMDlkOWFlZjgzOWZjOTM2ZTEwYjEzNzg4ODZmYzY5NTA3OWE0ODVmNDQxMzRkZTZjYzc2NTNmNmI0Y2Q1M2FiOTQ0ODEyOWZiMTYiLCJpYXQiOjE2MzUxNjg2NDUuNjEyNjQzLCJuYmYiOjE2MzUxNjg2NDUuNjEyNjQ2LCJleHAiOjQ3OTA4NDIyNDUuNTc3NTU5LCJzdWIiOiI1NDI1MzE1OCIsInNjb3BlcyI6WyJ1c2VyLnJlYWQiLCJ1c2VyLndyaXRlIiwidGFzay5yZWFkIiwidGFzay53cml0ZSIsIndlYmhvb2sucmVhZCIsIndlYmhvb2sud3JpdGUiLCJwcmVzZXQucmVhZCIsInByZXNldC53cml0ZSJdfQ.h-XGlOtFBtqg4czpXlbcDhAiXWGk3AlgUl7CeVJTu0EEjqfzmfUFOOWxjKm2YGJhDYEaIcLk863uI8XIiYt5NmtsO_brrfGFEHDKlknRrAxCPO9BExtgk6Fe5LePOszzByzItp-rXVk8Ty6UN7EjFFcQ9_X2R95_YqztAQcdGEO9x9nq_qFE5yrOG1bAjWmw59C61PG_5rVRZ1nOZamDqwdzU4eFgVJAxV1hXM-x34AUvOJqjyITWtyNlSx2oDoP2rBje4xikiH-dsXtoJXwyV3UN-IAKampbucsthhLUaTjUXJK3zE5fZHjRpfHp4Eo4XmqL2r0zjMzn2kZnYLwWHMc3Pno3f75HGSGNk7bSgghbXuChVrZQKbcGCIzFWk2ZLRboiYzNjTxVAM2K4BRmwjXjOXpmm4lwTMoC37d2h_8vwACxczEABDOEu1m5s7qdayxqsJyJKPgGerIPVhzEAz2FTt3nONXFa6QgF5v_479fv16GYqHmt-Qbjcjjr_PoMRlGKngUEiVXYjtiH39ZV7OvpFYbbs969B_VpH35ZKXVq-e9dCO4zNhpufDqpTmDAh5S9rw-NsVLaPJs-_9LQC02udQNmj3-Uoq2OntUeFJ_oQK58ECNs4sJEBxC0J7anLafnmY4iWjIRTeUycT485_Lf-2I45jt12ohqz-knQ
import json

import cloudconvert
# key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNzY2NmMzMDlkOWFlZjgzOWZjOTM2ZTEwYjEzNzg4ODZmYzY5NTA3OWE0ODVmNDQxMzRkZTZjYzc2NTNmNmI0Y2Q1M2FiOTQ0ODEyOWZiMTYiLCJpYXQiOjE2MzUxNjg2NDUuNjEyNjQzLCJuYmYiOjE2MzUxNjg2NDUuNjEyNjQ2LCJleHAiOjQ3OTA4NDIyNDUuNTc3NTU5LCJzdWIiOiI1NDI1MzE1OCIsInNjb3BlcyI6WyJ1c2VyLnJlYWQiLCJ1c2VyLndyaXRlIiwidGFzay5yZWFkIiwidGFzay53cml0ZSIsIndlYmhvb2sucmVhZCIsIndlYmhvb2sud3JpdGUiLCJwcmVzZXQucmVhZCIsInByZXNldC53cml0ZSJdfQ.h-XGlOtFBtqg4czpXlbcDhAiXWGk3AlgUl7CeVJTu0EEjqfzmfUFOOWxjKm2YGJhDYEaIcLk863uI8XIiYt5NmtsO_brrfGFEHDKlknRrAxCPO9BExtgk6Fe5LePOszzByzItp-rXVk8Ty6UN7EjFFcQ9_X2R95_YqztAQcdGEO9x9nq_qFE5yrOG1bAjWmw59C61PG_5rVRZ1nOZamDqwdzU4eFgVJAxV1hXM-x34AUvOJqjyITWtyNlSx2oDoP2rBje4xikiH-dsXtoJXwyV3UN-IAKampbucsthhLUaTjUXJK3zE5fZHjRpfHp4Eo4XmqL2r0zjMzn2kZnYLwWHMc3Pno3f75HGSGNk7bSgghbXuChVrZQKbcGCIzFWk2ZLRboiYzNjTxVAM2K4BRmwjXjOXpmm4lwTMoC37d2h_8vwACxczEABDOEu1m5s7qdayxqsJyJKPgGerIPVhzEAz2FTt3nONXFa6QgF5v_479fv16GYqHmt-Qbjcjjr_PoMRlGKngUEiVXYjtiH39ZV7OvpFYbbs969B_VpH35ZKXVq-e9dCO4zNhpufDqpTmDAh5S9rw-NsVLaPJs-_9LQC02udQNmj3-Uoq2OntUeFJ_oQK58ECNs4sJEBxC0J7anLafnmY4iWjIRTeUycT485_Lf-2I45jt12ohqz-knQ"

#####################Cloudmersive
#8a8435db-51ef-43f3-a8e6-c9703708a341

#
# #
# key = "8a8435db-51ef-43f3-a8e6-c9703708a341"
#
# import time
# import cloudmersive_convert_api_client
# from cloudmersive_convert_api_client.rest import ApiException
#
# # Configure API key authorization: Apikey
# configuration = cloudmersive_convert_api_client.Configuration()
# configuration.api_key['Apikey'] = key
#
#
#
# # create an instance of the API class
# api_instance = cloudmersive_convert_api_client.ConvertDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
# input_file = 'test.pdf' # file | Input file to perform the operation on.
# text_formatting_mode = 'minimizeWhitespace' # str | Optional; specify how whitespace should be handled when converting PDF to text.  Possible values are 'preserveWhitespace' which will attempt to preserve whitespace in the document and relative positioning of text within the document, and 'minimizeWhitespace' which will not insert additional spaces into the document in most cases.  Default is 'preserveWhitespace'. (optional)
#
# file = open("fromcloudmersive2.txt", 'w', encoding="utf8")
# try:
#     # Convert PDF Document to Text (txt)
#     api_response = api_instance.convert_document_pdf_to_txt(input_file, text_formatting_mode=text_formatting_mode)
#     print(str(api_response.text_result))
#     file.write(str(api_response.text_result))
# except ApiException as e:
#     print("Exception when calling ConvertDocumentApi->convert_document_pdf_to_txt: %s\n" % e)
# import json
# import requests
#
# import time
# import cloudmersive_convert_api_client
# from cloudmersive_convert_api_client.rest import ApiException
#
#
# def PDFtoTxt(file):
#     key = "8a8435db-51ef-43f3-a8e6-c9703708a341"
#
#     # Configure API key authorization: Apikey
#     configuration = cloudmersive_convert_api_client.Configuration()
#     configuration.api_key['Apikey'] = key
#
#     # create an instance of the API class
#     api_instance = cloudmersive_convert_api_client.ConvertDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
#     input_file = file # file | Input file to perform the operation on.
#     text_formatting_mode = 'minimizeWhitespace' # str | Optional; specify how whitespace should be handled when converting PDF to text.  Possible values are 'preserveWhitespace' which will attempt to preserve whitespace in the document and relative positioning of text within the document, and 'minimizeWhitespace' which will not insert additional spaces into the document in most cases.  Default is 'preserveWhitespace'. (optional)
#
#     try:
#         # Convert PDF Document to Text (txt)
#         api_response = api_instance.convert_document_pdf_to_txt(input_file, text_formatting_mode=text_formatting_mode)
#         return TxttoOneline(str(api_response.text_result))
#     except ApiException as e:
#         text = "Exception when calling ConvertDocumentApi->convert_document_pdf_to_txt: %s\n" % e
#         print(text)
#         return text
#
#
# def TxttoOneline(text):
#     newfile = ""
#     TexttoWord = text.split()
#
#     for words in TexttoWord:
#         newfile = newfile + " " + words
#     return plagiarism_check(newfile)
#
#
# def plagiarism_check(text):
#     receive = requests.request(
#         method='POST',
#         url='https://www.prepostseo.com/apis/checkPlag',
#         data = {'key': 'd9ee4480af8c9926d4cc81badb48b588','data':text},
#     )
#
#     return receive.text
#
# print(PDFtoTxt('test.pdf'))
# print(TxttoOneline(text))









#
#
#
#
#
#
#
# # SMALLSEOTOOLS
# import requests
# key = '48e2d678e42e2c611d03cb53efb88ea6'
#
# response = requests.request(
#     method='POST',
#     url='https://smallseotools.com/api/info',
#     data = {'key': key},
# )
# print(response.text)
# # print("entered plag")
#
#
#
#
# response = requests.request(
#     method='POST',
#     url='https://smallseotools.com/api/checkplag',
#     data = {'key':key,'data':'This page allows you to generate random text strings using true randomness, which for many purposes is better than the pseudo-random number algorithms'},
# )
#
# # {"user_name":"John Mathew Di\u00f1o","queries_limit":"20","queries_used":"0","account_status":"Active"}
# # {"recall":true,"totalQueries":1,"key":1,"hash":"78aeda2f09faab8845dcf6a345ac3dca"}
#
# resp = json.loads(response.text)
# print("resp1")
# print(resp)
#
# x = 0
# y = 1
#
# while x != y:
#
#     response2 = requests.get('https://smallseotools.com/api/query-footprint/'+ str(resp['hash']) + '/' + str(resp['key']))
#     resp2 = json.loads(response2.text)
#     print("resp2")
#     print(resp2)
#     if resp2['recall'] == 'False':
#         break
#
# print(resp2)
import cloudmersive_convert_api_client



def PDFtoTxt(file):
    print("entered PDFtoText")

    key = "8a8435db-51ef-43f3-a8e6-c9703708a341"

    # Configure API key authorization: Apikey
    configuration = cloudmersive_convert_api_client.Configuration()
    configuration.api_key['Apikey'] = key

    # create an instance of the API class
    api_instance = cloudmersive_convert_api_client.ConvertDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))
    input_file = file # file | Input file to perform the operation on.
    text_formatting_mode = 'minimizeWhitespace' # str | Optional; specify how whitespace should be handled when converting PDF to text.  Possible values are 'preserveWhitespace' which will attempt to preserve whitespace in the document and relative positioning of text within the document, and 'minimizeWhitespace' which will not insert additional spaces into the document in most cases.  Default is 'preserveWhitespace'. (optional)


    # Convert PDF Document to Text (txt)
    api_response = api_instance.convert_document_pdf_to_txt(input_file, text_formatting_mode=text_formatting_mode)
    print("Almost return PDFtoText")

    return str(api_response.text_result)
    # return str(api_response.text_result)

print(PDFtoTxt('test.pdf'))










