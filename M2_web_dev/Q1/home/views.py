from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate, logout
from .forms import CreateUserform,toDo,toDoForm
# Create your views here.

def home(request):
  return render(request,'index.html')

def register(request):
  form=CreateUserform()
  if request.method=='POST':
    form=CreateUserform(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
    
  context={'form':form}
  

  return render(request,'register.html',context)
def login_user(request):
  
  if request.method=='POST':
    username=request.POST['username']
    password1=request.POST['password1']
   
    user=authenticate(request,username=username,password=password1)
    if user is not None:
      login(request,user)
      return redirect('home')
      
    else:
      return redirect('register')
      
    # if form.is_valid():
    #   form.save()
  return render(request,'login.html')

def toDoAdd(request):
    form=toDoForm()
    if request.method=="POST":
        data=toDoForm(request.POST)
        if data.is_valid():
            data.save()

            #print message success
            
            return redirect('home')
        else:
            #print failure message
            return redirect('home')
    context={"form":form}
    return render(request, 'crud/toDoAdd.html', context)
def toDoUpdate(request, id):
    data=toDo.objects.get(id=id)
    update_todo=toDoForm(request.POST or None, instance=data)
    if update_todo.is_valid():
        update_todo.save()

        #print message success
       
        return redirect('home')
    context={"form":update_todo}
    return render(request, 'crud/toDoUpdate.html', context)

def toDoDelete(request, id):
    data=toDo.objects.get(id=id)
    data.delete()
    #print success message
    
    return redirect('dashboard')