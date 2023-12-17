from django.shortcuts import render
from django.http import HttpResponse
import requests
### TO PRETTY PRINT JSON
import json
from django.http import JsonResponse
from pprint import pprint

import logging




# Create your views here.

### Represents the HTTP request that the user made to access our web server
def hello_old01(request):
    return HttpResponse('Hello, world!')

from django.shortcuts import render

def hello_old2(request):
    ### Send a GET request to the specified URL with parameters
    ### this prints to console
    response = requests.get('https://randomuser.me/api/')
    print(response.json())
    ### context is a variable that stores information that we would
    context = {'name': 'John'}
    ### return render(request, '../templates/hello.html', context)
    return render(request, 'hello.html', context)

def hello_old3(request):
    ### SEND A GET REQUEST TO THE SPECIFIED URL WITH PARAMETERS
    ### this prints to console
    response = requests.get('https://app.ticketmaster.com/discovery/v2/events.json?apikey=OFYGvXGLUFanaijTT1jpItQsJ5Ayf3c8')
    print(response.json())
    ### to pretty print a string
    ### pprint(json.loads(json_string))
    ### to pretty print a json dictionary
    ### print(json.dumps(data, indent=4))
    print(json.dumps(response.json(), indent=4))
    ### context is a variable that stores information that we would
    ### context = {'name': 'John'}
    ### return render(request, '../templates/hello.html', context)
    ### return render(request, 'hello.html', context)
    return render(request, 'hello.html')

### NOT FIGURED THIS OUT YET!
### to open this in separate window
def view_in_separate_window(request):
  ###response = HttpResponse(render_template) 
  # response = HttpResponse(render_template) 
  # response['Content-Disposition'] = 'attachment; filename="page.html"'
  ###rendered = render(request, 'template.html') 
  rendered = render(request, 'hello.html') 
  response = HttpResponse(rendered.content)
  response['Content-Disposition'] = 'attachment; filename="page.html"' 
  return response


def hello_old4(request):
    ### SEND A GET REQUEST TO THE SPECIFIED URL WITH PARAMETERS
    response = requests.get('https://app.ticketmaster.com/discovery/v2/events.json?apikey=OFYGvXGLUFanaijTT1jpItQsJ5Ayf3c8')
    # ### PRINTS TO CONSOLE ###
    print(response.status_code) ### [15/Dec/2023 23:48:22] "GET / HTTP/1.1" 200 527966 ### 200 means success! WAS IN THE EXAM!!
    # print(json.dumps(response.json(), indent=1))
    # print(response.json())
    # print(response.text)
    # print(response.headers) ### result:

    ### PRETTY PRINT A JSON DICTIONARY:
    # pretty_printed_response=json.dumps(response.json(), indent=1, depth=1) ### wrong 
    # pretty_printed_response=json.dumps(truncate(response.json(), depth=2)) ### wrong!
    pretty_printed_response=json.dumps(response.json(), indent=1)
    ### context = {'name': 'John'}
    ### context = {'name':  '<pre>'+pretty_printed_response+'</pre>'  }
    context = {'pre_un_reformatted_text':  pretty_printed_response}
    return render(request, 'hello.html', context)
    ### return render(request, 'hello.html')





########################### KEEP! WORKED LIKE A CHARM ###################################
def hello_old5(request):
    ### SEND A GET REQUEST TO THE SPECIFIED URL WITH PARAMETERS
    response = requests.get('https://app.ticketmaster.com/discovery/v2/events.json?apikey=OFYGvXGLUFanaijTT1jpItQsJ5Ayf3c8')
    ######################
    print(response.status_code) ### [15/Dec/2023 23:48:22] "GET / HTTP/1.1" 200 527966 ### 200 means success! WAS IN THE EXAM!!
    pretty_printed_response=json.dumps(response.json(), indent=1)
    context = {'pre_un_reformatted_text':  pretty_printed_response}
    ################# return render(request, 'hello.html', context)
    return JsonResponse(response.json(), safe=False)




    ################ NOW WE NEED TO MAKE A GIANT DICTIONARY FROM ALL OF THE NECESSARY KEY-VALUE PAIRS AND PASS THEM ON TO THE HTML ###
def hello___for_now_derailed(request):
    ###response = requests.get('https://app.ticketmaster.com/discovery/v2/events.json?apikey=OFYGvXGLUFanaijTT1jpItQsJ5Ayf3c8')
    
    url_and_key='https://app.ticketmaster.com/discovery/v2/events.json?apikey=OFYGvXGLUFanaijTT1jpItQsJ5Ayf3c8'
    response = requests.get(url_and_key)

    ### ONLY THESE TWO PARAMETERS ARE TO BE GIVEN BY THE USER ###
    ### ONLY THESE TWO PARAMETERS ARE TO BE GIVEN BY THE USER ###
    ### ONLY THESE TWO PARAMETERS ARE TO BE GIVEN BY THE USER ###
    ### ONLY THESE TWO PARAMETERS ARE TO BE GIVEN BY THE USER ###
    ###response = requests.get(url_and_key, {'city':'Hartford' , 'classificationName' : 'dance'})
    city = 'Hartford'
    classificationName = 'dance'
    twoCriteria = {'city': city , 'classificationName' : classificationName}
    response = requests.get(url_and_key, {'city': city , 'classificationName' : classificationName})
    response = requests.get(url_and_key, twoCriteria)
    


    
    # pretty_printed_response=json.dumps(response.json(), indent=1)
    # pretty_printed_response=json.dumps(response.json()['_embedded']['events'], indent=1) ### all events
    # pretty_printed_response=json.dumps(response.json()['_embedded']['events'][0], indent=1) ### only the zeroth event
    # pretty_printed_response=json.dumps(response.json()['_embedded']['events'][0]['name'], indent=1) ### only the zeroth event
    
    # name_list = []    ### list of all 20 names
    # for event in events:
    #     name_list.append(event['name'])
    # total_number_of_events = len( response.json()['_embedded']['events'] )
    # tnoe = total_number_of_events
    
    context = {'response_json_object':  response.json()} ### THIS WRITES ONE GIANT LONG JSON LINE!
    return render(request, 'hello.html', context)







#def hello_old6(request):
def hello(request):
    response = requests.get('https://app.ticketmaster.com/discovery/v2/events.json?apikey=OFYGvXGLUFanaijTT1jpItQsJ5Ayf3c8')
    # ### PRINTS TO CONSOLE ###
    # print(response.status_code) ### [15/Dec/2023 23:48:22] "GET / HTTP/1.1" 200 527966 ### 200 means success! WAS IN THE EXAM!!
    # print(json.dumps(response.json(), indent=1))
    # print(response.json())
    # print(response.text)
    # print(response.headers) ### result:

    ### KEEP!!!! ###
    # ### PRETTY PRINT A JSON DICTIONARY ###
    pretty_printed_response=json.dumps(response.json()['_embedded']['events'][0]['name'], indent=1) ### only the zeroth event
    pretty_printed_response=json.dumps(response.json()['_embedded']['events'][0], indent=1) ### only the zeroth event
    pretty_printed_response=json.dumps(response.json()['_embedded']['events'], indent=1) ### all events
    ##pretty_printed_response=json.dumps(response.json()['_embedded'][0], indent=1) ### all events
    pretty_printed_response=json.dumps(response.json(), indent=1)

    ### TO GET A LIST OF ALL 20 NAMES ############
    # name_list = []
    # for event in events:
    #     name_list.append(event['name'])
    ###
    total_number_of_events = len( response.json()['_embedded']['events'] )
    tnoe = total_number_of_events
    ### pretty_printed_response=json.dumps(response.json().events[0], indent=1) #### wrong!!
    ### context = {'name': 'John'}
    ### context = {'name':  '<pre>'+pretty_printed_response+'</pre>'  }
    context = {'pre_un_reformatted_text':  tnoe} #### THIS WORKS! it shows the number of events
    context = {'pre_un_reformatted_text':  pretty_printed_response} ### pretty formatted
    ###context = {'pre_un_reformatted_text':  response} ### this just writes     Response <200>
    ###context = {'pre_un_reformatted_text':  response.json()} ### THIS WRITES ONE GIANT LONG JSON LINE!
    ###context = {'response_json_object':  response.json()} ### THIS WRITES ONE GIANT LONG JSON LINE!

    ### LET'S SIFT OUT THE 'events' part:
    ### embedded = response.json()['_embedded']
    ### print(embedded)


    ### !!!!
    ### IT IS VERY IMPORTANT HERE TO GET RID OF '_embedded here, BECAUSE:
    ### in django tamplate language
    ### Variable attributes that begin with an underscore may NOT be accessed as they’re generally considered private!!!!!!!
    ### CANNOT BE ACCESSED in the template!!!    
    events = response.json()['_embedded']['events']
    print (events)
    print (len(events) , ' <======== this is via:    print (len (events))    inside views.py ...') ### this returns 20

    ### let's make a dictionary out of that:
    context = {'events':  events}
    
    return render(request, 'hello.html', context)
    ### return render(request, 'hello.html')


