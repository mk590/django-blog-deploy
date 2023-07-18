from django.forms import ModelForm
from .models import Blog

# class BlogForm(ModelForm):
#     class Meta:
#      model=Blog
#      fields='__all__'
     
     
# ModelForm has no model class specified.
# beacuse of the typo in the blogform that is not writing the class meta and keeping the m small and large in the model 

# trying to bind the author and the username

class BlogForm(ModelForm):
    class Meta:
     model=Blog
     fields=['title','tags','description','content','image_attached']
    #  fields=['title','tags','description','content','image_attached','author']


from django.contrib.auth.models import User

# class BlogForm(ModelForm):
#     class Meta:
#      model=Blog
#      fields=['title','tags','description','content','image_attached']

#      def save(self, commit=True):
#         Blog.title=self.cleaned_data['title']
#         Blog.tags=self.cleaned_data['tags']
#         Blog.description=self.cleaned_data['description']
#         Blog.content=self.cleaned_data['content']
#         # Blog.author=self.cleaned_data[User.username]
#         # Blog.author=User.username
#         # if User.is_authenticated:
#         #  Blog.author=User.username
           
#         # Blog.author=self.cleaned_data['user']
#         Blog.author=User.objects.get(pk=id)
        
#         if Blog.image_attached:
#           Blog.image_attached=self.cleaned_data['image_attached']
        
#         Blog.save()
#         return Blog
      
      
      
      
      # NOT NULL constraint failed: blog_blog.author_id