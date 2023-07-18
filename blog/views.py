from django.shortcuts import render,redirect
# from .models import *
# from .forms import *
from .models import Blog
from .forms import BlogForm


# for authorization 
from django.contrib.auth.decorators import login_required


# before soft delete 
# def home(request):
#     all_blogs=Blog.objects.all()  
#     return render(request,'home.html',{'data':all_blogs})

# we define a functional view home where we create a variable all_blog which contain all theblogs 
# since it is a function it will return something , in this case we render , click on the render  
# here request is the url 

# after soft delete 
def home(request):
#     all_blogs=Blog.objects.filter(is_deleted=False)
#     all_blogs=Blog.all_objects.all()
    all_blogs=Blog.objects.all()
    
    return render(request,'home.html',{'data':all_blogs})




# before applying the authentication
# def form(request):
#     if request.method=="POST":
#         form=BlogForm(request.POST,request.FILES)
#         if form.is_valid:
#             form.save()
#             return redirect('home')
        
#     else:
#         form=BlogForm()
#         return render(request,'form.html',{'data':form})
# # what is the request.POST, request.FILES here what they do    


#  applying the authentication 

# @login_required
# def form(request):
#     if request.method=="POST":
        # form=BlogForm(request.POST,request.FILES)
        # form=BlogForm(request.POST,request.FILES,initial=[{'author':{User.username}}])
#         ValueError at /form_blog/
# dictionary update sequence element #0 has length 1; 2 is required
        
        # form=BlogForm(request.POST,request.FILES,initial=[{'author':request.user,'Title':'power'}])
        # form=BlogForm(request.POST,request.FILES,initial=[{'author':User.username,'Title':'power'}])
        
        # form=BlogForm(request.POST,request.FILES,initial=[{'author':User.get(id),'Title':'power'}])
        # AttributeError at /form_blog/
# type object 'User' has no attribute 'get'
#         form=BlogForm(request.POST,request.FILES,initial=[{'author':User.id,'Title':'power'}])
#         IntegrityError at /form_blog/
# NOT NULL constraint failed: blog_blog.author_id

#         form=BlogForm(request.POST,request.FILES,initial=[{'author':'mk','Title':'power'}])

#         if form.is_valid:
#             form.save()
#             return redirect('home')
        
#     else:
#         # form=BlogForm(initial=[{'author':{request.user},'title':'power'}])
#         # form=BlogForm(initial=[{'author':{request.user},'Title':'power'}])
#         form=BlogForm(initial=[{'author':{request.user},'title':'power'}])
#         return render(request,'form.html',{'data':form})



# from django.forms import formset_factory
# @login_required
# def form(request):
#     if request.method=="POST":
#         blogformset=formset_factory(BlogForm,extra=0)
#         formset=blogformset(initial=[{'author':request.user}])
#         form=BlogForm(request.POST,request.FILES,initial=[{'author':request.user}])
#         if form.is_valid:
#             form.save()
#             return redirect('home')
        
#     else:
#         form=BlogForm()
#         return render(request,'form.html',{'data':form})


# @login_required
# def form(request):
#     if request.method=="POST":
#         initial_dict = {"author":User.username,"title":"title"}
        
#         form=BlogForm(request.POST,request.FILES,initial=[initial_dict])
#         if form.is_valid:
#             form.save()
#             return redirect('home')
        
#     else:
#         form=BlogForm()
        #   return render(request,'form.html',{'data':form})
  
  
# @login_required      
# def form(request):
#     initial_dict = {"author":request.user,"title":"title"} 
#     if request.method=="POST":
#         form=BlogForm(request.POST,request.FILES,initial=initial_dict)
#         if form.is_valid:
#             form.save()
#             return redirect('home')
        
#     else:
        # initial_dict = {"author":User.username,"title":"title"}    
        # initial_dict = {"author":User.username,"title":User.username}    
        # <django.db.models.query_utils.DeferredAttribute object at 0x0000022E57A6D7E0>
        # this error was coming bcz i was passing the User.username , instead of request.user 
        # initial_dict = {"author":User.username,"title":request.user}    
        # initial_dict = {"author":request.user,"title":"title"}    

        # form=BlogForm(initial=initial_dict)
        # return render(request,'form.html',{'data':form})



@login_required      
def form(request):
    if request.method=="POST":
        form=BlogForm(request.POST,request.FILES)
        if form.is_valid:
            blog=form.save(commit=False)
            blog.author=request.user
            blog.save()

            return redirect('home')
        
    else:
        form=BlogForm()
        return render(request,'form.html',{'data':form})









def specific_blog_view(request,pk):
        particular_blog=Blog.objects.get(pk=pk)
        
        return render(request,'view_blog.html',{'data':particular_blog})
  
  
# how this update of blog works eachline explanation   
def specific_blog_update(request,pk):
        if request.method == "POST":
            particularBlog = Blog.objects.get(pk= pk)
            updated_blog = BlogForm(request.POST, request.FILES ,instance = particularBlog)
            if updated_blog.is_valid():
                updated_blog.save()
                return redirect('home')
            
        particularBlog = Blog.objects.get(pk= pk)
        content = BlogForm(instance=particularBlog)
        info = {'data':content}
        return render(request,"update.html",info)
    
    
def specific_blog_del(request,pk):
        particular_blog=Blog.objects.get(pk=pk)
        # particular_blog.delete()
        particular_blog.soft_delete()
        return redirect('home')
        
# what is pk=pk here , is it similar to id=passed parameter 
# also it has a issue that in the django the ids/count is not updated  


from django.http import HttpResponse
def favicon(request):
    return HttpResponse(status=204)