from django.shortcuts import render , HttpResponse
import joblib


model =joblib.load('static/random_forest_regressor')
def index(request):
    return render(request, 'index.htm')


def about(request):
    #return HttpResponse("hello about")
    return render(request, 'about.htm')

def contact(request):
    return render(request , 'contact.htm')

def login(request):
    return render(request,'login.htm')

def register(request):
    return render(request,'register.htm')
def prediction(request):
    if request.method =="POST":
        print("enter into post prediction")
        age = int(request.POST.get('age'))
        sex = int(request.POST.get('sex'))
        bmi = int(request.POST.get('bmi'))
        children = int(request.POST.get('children'))
        smoker = int(request.POST.get('smoker'))
        region = int(request.POST.get('region'))

        print(age,bmi,sex,children,smoker,region)

        pred = round(model.predict([[age,sex,bmi,children,smoker,region]])[0])

        print(pred)

        output ={
            "output":pred
        }
        return render(request ,'prediction.htm',output)
    else:
        return render(request , 'prediction.htm')


