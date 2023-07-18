from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm

# for authorization 
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method=='POST':
        user_form=UserRegisterForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            # these two lines are doing nothing the 
            
            return redirect('home')
        else:
            # return "Error"
            # You can not pass directly str as a django response . You must use
            # return HttpResponse(resp)
            # if you want to render string data as django view response. have a look django.http.HttpResponse

            return HttpResponse("error")
    else:
        form = UserRegisterForm()
        return render(request, 'register.html', {'data': form})
    
    
# The view users.views.register didn't return an HttpResponse object. It returned None instead.
# this error was happening when i tried to register the user with incorrect password and that to withou writing the else statement in the post method 

@login_required
def profile(request):
    return render(request,'profile.html')