from django.shortcuts import render,redirect,get_object_or_404
from postapp.models import Blog
from django.core.paginator import Paginator
from django.http import HttpResponse,HttpResponseRedirect

def homepage(request):
    PostData=Blog.objects.all()
    
    if request.method=="GET":
        pt=request.GET.get('search')
        if pt!=None:
            PostData=Blog.objects.filter(title__icontains=pt)
            
                    
    paginator=Paginator(PostData,6)
    page_number=request.GET.get('page')
    PostDatafinal=paginator.get_page(page_number)
    totalpage=PostDatafinal.paginator.num_pages
      
    data={
      
        # 'PostData':PostData,
        'PostData':PostDatafinal,
        'lastpage':totalpage,
        'totalpagelist':[n+1 for n in range (totalpage)],
           
    }
    return render(request,"index.html",data)

def PostDetails(request,id):
    post=get_object_or_404(Blog,pk=id)
    return render(request,"Detailspage.html",{'post':post})

def Add_post(request):
    
    if request.method=="POST":
        Blogs_title=request.POST.get('Blog_Title')        
        Blogs_image=request.POST.get('Blog_image')        
        Blogs_des=request.POST.get('Blog_des')
                
      
        s=Blog()
        s.title=Blogs_title
        s.image=Blogs_image
        s.des=Blogs_des
        
        s.save()
    
        return redirect("/home/")
        
    return render(request,"AddPost.html",{})  
    
    

# Create your views here.
   