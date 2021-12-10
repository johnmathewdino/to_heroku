import json
import requests

import time
import cloudmersive_convert_api_client
from cloudmersive_convert_api_client.rest import ApiException
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from requests.structures import CaseInsensitiveDict
from proposalpanelists.models import AdviserAndPanelist


def PDFtoTxt(file):
    print("entered PDFtoText")

    key = "8a8435db-51ef-43f3-a8e6-c9703708a341"

    # Configure API key authorization: Apikey
    configuration = cloudmersive_convert_api_client.Configuration()
    configuration.api_key['Apikey'] = key

    # create an instance of the API class
    api_instance = cloudmersive_convert_api_client.ConvertDocumentApi(
        cloudmersive_convert_api_client.ApiClient(configuration))
    input_file = file  # file | Input file to perform the operation on.
    # str | Optional; specify how whitespace should be handled when converting PDF to text.  Possible values are 'preserveWhitespace' which will attempt to preserve whitespace in the document and relative positioning of text within the document, and 'minimizeWhitespace' which will not insert additional spaces into the document in most cases.  Default is 'preserveWhitespace'. (optional)
    text_formatting_mode = 'minimizeWhitespace'

    try:
        # Convert PDF Document to Text (txt)
        api_response = api_instance.convert_document_pdf_to_txt(
            input_file, text_formatting_mode=text_formatting_mode)
        print("Almost return PDFtoText")

        return TxttoOneline(str(api_response.text_result))
        # return str(api_response.text_result)

    except ApiException as e:
        text = "Exception when calling ConvertDocumentApi->convert_document_pdf_to_txt: %s\n" % e
        error = {'error': text}
        print(text)
        return error


def TxttoOneline(text):
    print("entered TXttoOneline")

    newfile = ""
    TexttoWord = text.split()

    for words in TexttoWord:
        newfile = newfile + " " + words
    # return plagiarism_check(newfile)
    print("almost TXttoOneline")
    return newfile


def plagiarism_check(text):
    url = "https://smallseotools.com/api/checkplag"

    payload = {'key': 'bf8a5eb657fb3b6514b483ff32e3db53',
               'data': text}
    headers = {}

    get_resp = requests.request("POST", url, headers=headers, data=payload)
    resp = get_resp.text
    print('first response', resp)
    print('first response type:', type(resp))
    resp_loads = json.loads(resp)
    print('resp_loads', resp_loads)
    print('resp_loads_type', type(resp_loads))
    print('resp_loads_recall', resp_loads['recall'])
    if resp_loads['recall'] == True:
        while resp_loads['recall'] != False:
            get_resp2 = requests.get('https://smallseotools.com/api/query-footprint/' + str(
                resp_loads['hash']) + '/' + str(resp_loads['key']))
            resp2 = get_resp2.text
            print('second request', resp2)
            print('second request type', type(resp2))
            resp2_loads = json.loads(resp2)
            print('resp2_loads', resp2_loads)
            print('resp2_loads_type', type(resp2_loads))
            print('resp2_loads_recall', resp2_loads['recall'])

            resp_loads = resp2_loads
    print('Final_resp_loads', resp_loads)

    return resp_loads


@login_required
def plagcheckhome(response):
    loaded_data = ""
    query = ""
    data = ""
    if response.method == "POST":
        print("first if")
        if response.POST.get("plagtextarea"):

            text = response.POST.get("plagtextarea")
            query = str(text)

            loaded_data = plagiarism_check(text)

        if response.POST.get("formFile"):
            print("second if")

            file = response.POST.get("formFile")
            # loaded_data = PDFtoTxt(file)
            text = PDFtoTxt(file)
            query = str(text)
            loaded_data = plagiarism_check(text)
            # data = PDFtoTxt(text)

    print(data)

    # TO CHECK FOR QUERIES LEFT
    url = "https://smallseotools.com/api/info"
    payload = {'key': 'bf8a5eb657fb3b6514b483ff32e3db53'}
    headers = {}
    resp = requests.request("POST", url, headers=headers, data=payload)
    print(resp.text)

    #
    # # LOAD DATA FROM A FILE
    # # FOR VIEWING THE DESIGN
    # raw_data = open('text.txt','r')
    # read_raw_data = raw_data.read()
    #
    # jsonloads_raw_data = json.loads(read_raw_data)
    # loaded_data = jsonloads_raw_data
    #
    #
    #

    name = response.user.get_full_name
    userrole = response.user.userprofile.role

    # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
    resuser = response.user
    unseen = 0
    adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)

    return render(response, 'plagcheckhome.html', {
        "name": name,
        "userrole": userrole,
        "loaded_data": loaded_data,
        "query": query,
        "unseen": unseen,
        "resuser": resuser,
        "adviser":adviser,
    })
