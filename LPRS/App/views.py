from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from googleapiclient.discovery import build

#For knowledge graph
from neo4j import GraphDatabase
import logging
from neo4j.exceptions import ServiceUnavailable


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
        student = Student(user = request.user.id, username=username)
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
        test = Array.objects.filter(level=level);
    elif(topic=="LinkedList"):
        test = LinkedList.objects.all();
    elif(topic=="String"):
        test = String.objects.all();
    elif(topic=="Stack"):
        test = Stack.objects.all();
    elif(topic=="Queue"):
        test = Queue.objects.all();
    elif(topic=="Tree"):
        test = Tree.objects.all();
    elif(topic=="Recursion"):
        test = Recursion.objects.all();
    elif(topic=="Graph"):
        test = Graph.objects.all();
    elif(topic=="DP"):
        test = DP.objects.all();
    elif(topic=="Heap"):
        test = Heap.objects.all();
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
    context["level"] = level
    return render(request, 'test.html', context)

def testScore(request, topic, level):
    print("test score chla")
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
    print(student)
    if(level=="Easy"):
        student.scoreBeg = 2*score
    elif(level=="Medium"):
        student.scoreImd = 2*score
    else:
        student.scoreExp = 2*score
    student.save()
    if(level=="Easy"):
        return redirect('/test/'+topic+'/Medium')
    elif(level=="Medium"):
        return redirect('/test/'+topic+'/Hard')
    return redirect('/levelDecider')

def levelDecider(request):
    student = Student.objects.get(username = request.user.username)
    beg = student.scoreBeg
    imd = student.scoreImd
    exp = student.scoreExp

    level = ""
    if(beg>=8 and imd>=6 and exp>=4):
        level = "Hard"
    elif(beg>=8 and imd>=6):
        level = "Medium"
    elif(beg>=8 and imd<6):
        level = "Easy"
    elif(beg>=8 and exp>=4 and imd<6):
        level = "Hard"
    elif(beg<8 and imd>=6 and exp<4):
        level = "Easy"
    elif(beg<8 and imd<6):
        level = "Easy"
    elif(beg<8 and imd>=6 and exp>=4):
        level = "Medium"
    
    context = {}
    context["level"] = level
    context["scoreEasy"] = beg
    context["scoreImd"] = imd
    context["scoreExp"] = exp

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
    return HttpResponse("Your evaluation is completed, with scores as : text : " + str(tts) + " visual : " + str(vts))

def customSearch(request):
  #For textual material
  api_key1 = "AIzaSyBHWk5xigAfm3H6uZkcAgZTyGljA-9Ui04"
  resource1 = build('customsearch', 'v1', developerKey=api_key1).cse()
  result1 = resource1.list(q='asymtotic notation', cx='abb409adb2e6e494d').execute()
  text_links = [result1['items'][0]['link'], result1['items'][1]['link'], result1['items'][2]['link'], result1['items'][3]['link']]
  
  
  #For visual material
  api_key2 = "AIzaSyDjGy2izljcjoDjKeDB5eaSEGyHno5MKN8"
  resource2 = build('customsearch', 'v1', developerKey=api_key2).cse()
  result2 = resource2.list(q='asymtotic notation', cx='a1729a859a285ea44').execute()
  vis_links = [result2['items'][0]['link'], result2['items'][1]['link'], result2['items'][2]['link']]

  #For exercises
  api_key3 = "AIzaSyAubkBVsLRzbrP9onmbrt0fNa8KXUJdBKE"
  resource3 = build('customsearch', 'v1', developerKey=api_key3).cse()
  link_probs = []
  for i in range(1, 50, 10):
    result3 = resource3.list(q='Array Practice Problems', cx='621330a2d0aa2929d', start=i).execute()

    for j in range(10):
        link_probs.append(result3['items'][j]['link'])

  gfg = []
  lc = []
  hack = []
  for links in link_probs:
      if links.find('practice') != -1 and len(gfg) < 2:
         gfg.append(links)

      if links.find('leetcode') != -1 and len(lc) < 2:
         lc.append(links)

      if links.find('hackerrank') != -1 and len(hack) < 2:
         hack.append(links)

  prac_links = [gfg[0], gfg[1], lc[0], lc[1], hack[0], hack[1]]  
  content = [text_links, vis_links, prac_links] 
  return render(request, 'learnPath.html', {'content' : content})

def graph(request):
    # connection code
    # Aura queries use an encrypted connection using the "neo4j+s" URI scheme
    uri = "neo4j+s://37f2df4f.databases.neo4j.io"
    user = "neo4j"
    password = "QiUgVlre0zTZABDT2ypCjCwoRb0CrIpgQOx2RSZxjVk"
    app = App(uri, user, password)
    app.create_friendship("878", "897")
    app.find_person("878")
    app.close()

    return HttpResponse("Connection established")
    

#To establish connection with neo4j 
class App:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        # Don't forget to close the driver connection when you are finished with it
        self.driver.close()

    def create_friendship(self, person1_name, person2_name):
        with self.driver.session() as session:
            # Write transactions allow the driver to handle retries and transient errors
            result = session.write_transaction(
                self._create_and_return_friendship, person1_name, person2_name)
            for row in result:
                  print("Created friendship between: {p1}, {p2}".format(p1=row['p1'], p2=row['p2']))

    @staticmethod
    def _create_and_return_friendship(tx, person1_name, person2_name):
        # To learn more about the Cypher syntax, see https://neo4j.com/docs/cypher-manual/current/
        # The Reference Card is also a good resource for keywords https://neo4j.com/docs/cypher-refcard/current/
        query = (
            "CREATE (p1:Person { name: $person1_name }) "
            "CREATE (p2:Person { name: $person2_name }) "
            "CREATE (p1)-[:KNOWS]->(p2) "
            "RETURN p1, p2"
        )
        result = tx.run(query, person1_name=person1_name, person2_name=person2_name)
        try:
            return [{"p1": row["p1"]["name"], "p2": row["p2"]["name"]}
                    for row in result]
        # Capture any errors along with the query and data for traceability
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
            raise

    def find_person(self, person_name):
        with self.driver.session() as session:
            result = session.read_transaction(self._find_and_return_person, person_name)
            for row in result:
                print("Found person: {row}".format(row=row))

    @staticmethod
    def _find_and_return_person(tx, person_name):
        query = (
            "MATCH (p:Person) "
            "WHERE p.name = $person_name "
            "RETURN p.name AS name"
        )
        result = tx.run(query, person_name=person_name)
        return [row["name"] for row in result]


