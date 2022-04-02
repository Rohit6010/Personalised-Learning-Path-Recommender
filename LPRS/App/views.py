from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


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
    student = Student.objects.get(username = request.user.username);
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

