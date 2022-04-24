from django.shortcuts import render, redirect
from django.http import HttpResponse
from sqlalchemy import null
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from googleapiclient.discovery import build

#For knowledge graph
from neo4j import GraphDatabase
import logging
from neo4j.exceptions import ServiceUnavailable

#For web scraping using beautiful soup
from bs4 import BeautifulSoup
import requests

def index(request):
    return render(request, 'index.html')

def handleSignup(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # phone = request.POST['phone']

        # Create the user
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = username
        myuser.save()
        student = Student(userid = request.user.id, username=username)
        student.save()
        messages.success(request, " Your EduPath account has been successfully created")
        return redirect('/')
    return render(request,'open.html')

def handleLogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in!")
            return redirect('/')
        else:
            messages.warning(request, "Invalid Credentials, please try again!")
            return HttpResponse("<h3>Invalid Credentials, please try again!</h3><br><a href='/signup'> Click here</a>")
    return render(request,'open.html')

def instruction(request, topic):
    return render(request, 'instruction.html', {"topic":topic})

def test(request, topic, level):
    context = {}
    test = []
    if(topic=="Array"):
        test = Array.objects.filter(level=level)
    elif(topic=="LinkedList"):
        test = LinkedList.objects.all()
    elif(topic=="String"):
        test = String.objects.all()
    elif(topic=="Stack"):
        test = Stack.objects.all()
    elif(topic=="Queue"):
        test = Queue.objects.all()
    elif(topic=="Tree"):
        test = Tree.objects.all()
    elif(topic=="Recursion"):
        test = Recursion.objects.all()
    elif(topic=="Graph"):
        test = Graph.objects.all()
    elif(topic=="DP"):
        test = DP.objects.all()
    elif(topic=="Heap"):
        test = Heap.objects.all()
    i=1
    for ques in test:
        context["ques"+str(i)] = ques.question
        context["ans"+str(i)] = ques.answer
        context["ques"+str(i)+"op1"] = ques.option1
        context["ques"+str(i)+"op2"] = ques.option2
        context["ques"+str(i)+"op3"] = ques.option3
        context["ques"+str(i)+"op4"] = ques.option4
        i += 1
    context["topic"] = topic
    if level == 'Easy':
       context["level"] = 'Beginner'
       context["color"] = 'green'
    elif level == 'Medium':
       context["level"] = 'Intermediate'
       context["color"] = 'yellow'
    else:
       context["level"] = 'Expert'
       context["color"] = 'red'
    
    context['link'] = level
    return render(request, 'test.html', context)

def testScore(request, topic, level):
    score = 0
    if(level=="Easy"):
        answer1 = request.POST.get("choosen1")
        ques1 = Array.objects.get(id = 1)
        print(ques1,answer1)
        correctAns1 = ques1.answer
        if(answer1 == correctAns1):
            score += 1

        answer2 = request.POST.get("choosen_2")
        ques2 = Array.objects.get(id = 2)
        print(ques2,answer2)
        correctAns2 = ques2.answer
        if(answer2 == correctAns2):
            score += 1
        
        answer3 = request.POST.get("choosen_3")
        ques3 = Array.objects.get(id = 3)
        print(ques3,answer3)
        correctAns3 = ques3.answer
        if(answer3 == correctAns3):
            score += 1
        
        answer4 = request.POST.get("choosen_4")
        ques4 = Array.objects.get(id = 4)
        print(ques4,answer4)
        correctAns4 = ques4.answer
        if(answer4 == correctAns4):
            score += 1
        
        answer5 = request.POST.get("choosen_5")
        ques5 = Array.objects.get(id = 5)
        print(ques5,answer5)
        correctAns5 = ques5.answer
        if(answer5 == correctAns5):
            score += 1
    elif(level=="Medium"):
        answer1 = request.POST.get("choosen1")
        ques1 = Array.objects.get(id = 6)
        print(ques1,answer1)
        correctAns1 = ques1.answer
        if(answer1 == correctAns1):
            score += 1

        answer2 = request.POST.get("choosen_2")
        ques2 = Array.objects.get(id = 7)
        print(ques2,answer2)
        correctAns2 = ques2.answer
        if(answer2 == correctAns2):
            score += 1
        
        answer3 = request.POST.get("choosen_3")
        ques3 = Array.objects.get(id = 8)
        print(ques3,answer3)
        correctAns3 = ques3.answer
        if(answer3 == correctAns3):
            score += 1
        
        answer4 = request.POST.get("choosen_4")
        ques4 = Array.objects.get(id = 9)
        print(ques4,answer4)
        correctAns4 = ques4.answer
        if(answer4 == correctAns4):
            score += 1
        
        answer5 = request.POST.get("choosen_5")
        ques5 = Array.objects.get(id = 10)
        print(ques5,answer5)
        correctAns5 = ques5.answer
        if(answer5 == correctAns5):
            score += 1
    elif(level=="Hard"):
        answer1 = request.POST.get("choosen1")
        ques1 = Array.objects.get(id = 11)
        print(ques1,answer1)
        correctAns1 = ques1.answer
        if(answer1 == correctAns1):
            score += 1

        answer2 = request.POST.get("choosen_2")
        ques2 = Array.objects.get(id = 12)
        print(ques2,answer2)
        correctAns2 = ques2.answer
        if(answer2 == correctAns2):
            score += 1
        
        answer3 = request.POST.get("choosen_3")
        ques3 = Array.objects.get(id = 13)
        print(ques3,answer3)
        correctAns3 = ques3.answer
        if(answer3 == correctAns3):
            score += 1
        
        answer4 = request.POST.get("choosen_4")
        ques4 = Array.objects.get(id = 14)
        print(ques4,answer4)
        correctAns4 = ques4.answer
        if(answer4 == correctAns4):
            score += 1
        
        answer5 = request.POST.get("choosen_5")
        ques5 = Array.objects.get(id = 15)
        print(ques5,answer5)
        correctAns5 = ques5.answer
        if(answer5 == correctAns5):
            score += 1

    student = Student.objects.get(username = request.user.username)
    student.curr_topic = topic
    student.save()

    assess_details = AssessDetails.objects.filter(student = student, topic=topic)
    assess_detail = null
    if len(assess_details)==0:
        assess_detail = AssessDetails(student = student, topic=topic)
        if(level=="Easy"):
            assess_detail.scoreBeg = 2*score
        elif(level=="Medium"):
            assess_detail.scoreImd = 2*score
        else:
            assess_detail.scoreExp = 2*score
    else :
        assess_detail = assess_details[0]
        if(level=="Easy"):
            assess_detail.scoreBeg = 2*score
        elif(level=="Medium"):
            assess_detail.scoreImd = 2*score
        else:
            assess_detail.scoreExp = 2*score
        
    assess_detail.save()

    if(level=="Easy"):
        return redirect('/test/'+topic+'/Medium')
    elif(level=="Medium"):
        return redirect('/test/'+topic+'/Hard')
    return redirect('/levelDecider/' + topic)

def levelDecider(request, topic):
    student = Student.objects.get(username = request.user.username)
    assess_detail = AssessDetails.objects.filter(student = student, topic=topic)[0]
    beg = assess_detail.scoreBeg
    imd = assess_detail.scoreImd
    exp = assess_detail.scoreExp

    level = ""
    if(beg>=8 and imd>=6 and exp>=4):
        level = "hard"
    elif(beg>=8 and imd>=6):
        level = "medium"
    elif(beg>=8 and imd<6):
        level = "easy"
    elif(beg>=8 and exp>=4 and imd<6):
        level = "hard"
    elif(beg<8 and imd>=6 and exp<4):
        level = "easy"
    elif(beg<8 and imd<6):
        level = "easy"
    elif(beg<8 and imd>=6 and exp>=4):
        level = "medium"
    
    context = {}
    context["level"] = level
    context["scoreEasy"] = beg
    context["scoreImd"] = imd
    context["scoreExp"] = exp

    assess_detail.level = level
    assess_detail.save()

    return render(request, 'goal.html', context)

def logoutuser(request):
    logout(request)
    return redirect('/')

def cognitiveTest(request):
    cogQuest = Cognitive.objects.all()
    return render(request, 'cogTest.html', { 'cogQuest' : cogQuest})

def cogScore(request):
    q1 = request.POST.get('op1')
    q2 = request.POST.get('op2')
    q3 = request.POST.get('op3')
    q4 = request.POST.get('op4')
    q5 = request.POST.get('op5')
    q6 = request.POST.get('op6')
    q7 = request.POST.get('op7')
    q8 = request.POST.get('op8')
    q9 = request.POST.get('op9')
    q10 = request.POST.get('op10')

    tts=0
    vts=0
    reslist = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    for res in reslist:
        if res=='1':
            tts+=1
        else:
           vts+=1 

    student = Student.objects.get(username = request.user.username)
    student.textual_trait = tts
    student.visual_trait = vts
    student.save()
    # return HttpResponse("Your evaluation is completed, with scores as : text : " + str(tts) + " visual : " + str(vts))
    return render(request, 'cogScore.html', {'tts':tts, 'vts':vts})

def customSearch(request, topic):
    topics = topic.split('*')
    ind = int(topics[len(topics)-1])
    
    #Fetch content from database if available
    student = Student.objects.get(username = request.user.username)
    content = Content.objects.filter(student=student, subtopic=topics[ind])

    if len(content) == 0:
        query_string = topics[ind] + " " + str(student.language)

        # For textual material
        api_key1 = "AIzaSyBHWk5xigAfm3H6uZkcAgZTyGljA-9Ui04"
        resource1 = build('customsearch', 'v1', developerKey=api_key1).cse()
        result1 = resource1.list(q=query_string, cx='abb409adb2e6e494d').execute()
    

        # For visual material
        api_key2 = "AIzaSyDjGy2izljcjoDjKeDB5eaSEGyHno5MKN8"
        resource2 = build('customsearch', 'v1', developerKey=api_key2).cse()
        result2 = resource2.list(q=query_string, cx='a1729a859a285ea44').execute()

        new_content = Content(
            student = student,
            subtopic = topics[ind],

            text1 = result1['items'][0]['link'],
            text2 = result1['items'][1]['link'],
            text3 = result1['items'][2]['link'],
            text4 = result1['items'][3]['link'],

            video1 = result2['items'][0]['link'],
            video2 = result2['items'][1]['link'],
            video3 = result2['items'][2]['link'],
            video4 = result2['items'][3]['link'],
        )
        new_content.save()
    
    #divide contents in the ratio of cognitive traits
    text_links = []
    vis_links = []
    content = Content.objects.filter(student=student, subtopic=topics[ind])[0]
    text = student.textual_trait
    
    if text==0 :
        text_links = []
        vis_links = [content.video1, content.video2, content.video3, content.video4]

    if text==1 or text==2:
        text_links = [content.text1]
        vis_links = [content.video1, content.video2, content.video3, content.video4]

    if text==3 or text==4:
        text_links = [content.text1, content.text2]
        vis_links = [content.video1, content.video2, content.video3, content.video4]
    
    if text==5 :
        text_links = [content.text1, content.text2, content.text3]
        vis_links = [content.video1, content.video2, content.video3]

    if text==6 or text==7:
        text_links = [content.text1, content.text2, content.text3, content.text4]
        vis_links = [content.video1, content.video2]

    if text==8 or text==9:
        text_links = [content.text1, content.text2, content.text3, content.text4]
        vis_links = [content.video1]

    if text==10 :
        text_links = [content.text1, content.text2, content.text3, content.text4]
        vis_links = []

    ind = ind+1
    if ind == len(topics)-1 :
        ind=-1
    topic = topic[:-1]
    topic = topic + str(ind)
    prac_links = ['abcdedfgryjbvhg', 'jsdfhwhfuryofkbej;ghtekbnrkltji', 'bchfhufiehwjb']
    return render(request, 'learnPath.html', {'text_link' : text_links, 'vis_link' : vis_links, 'prac_link' : prac_links, 'topic' : topic, 'ind': ind, 'subtopic':topics[ind-1]})



def graph(request):
    #save preffered language
    student = Student.objects.get(username = request.user.username)
    lang = request.POST.get('lang')
    student.language = lang
    student.save()

    # connection code
    # Aura queries use an encrypted connection using the "neo4j+s" URI scheme
    # Aura queries use an encrypted connection using the "neo4j+s" URI scheme
    uri = "neo4j+s://37f2df4f.databases.neo4j.io"
    user = "neo4j"
    password = "QiUgVlre0zTZABDT2ypCjCwoRb0CrIpgQOx2RSZxjVk"
    app = App(uri, user, password)
    
    
    id = TopicId.objects.get(topic=student.curr_topic)
    assess_detail = AssessDetails.objects.get(student = student, topic=student.curr_topic)

    print(id.id, assess_detail.level)
    topics = app._return_data(id.id, assess_detail.level)
    app.close()

    topicstr = '*'.join(topics)
    topicstr += '*0'
    print(topicstr)
    return redirect('customSearch/' + topicstr)
    


class App:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        # Don't forget to close the driver connection when you are finished with it
        self.driver.close()

    def _return_data(self,nodeid,diff):
        with self.driver.session() as session:
            result = session.read_transaction(self._data,nodeid,diff)
            topics = []
            for row in result:
                topics.append("{row}".format(row=row))

            return topics

    @staticmethod
    def _data(tx,nodeid,diff):
        query = (
            "MATCH (k:KP{parent_id:$nodeid,diff:$diff})"
            "RETURN k.name AS name"
        )
        result = tx.run(query, nodeid=nodeid,diff=diff)
        return [row["name"] for row in result]   


    