from django.db.models.query_utils import RegisterLookupMixin
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import *
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .forms import CommentForm

data = [
  {
    "image_url": "blog/images/nature.jpg",
    "title": "Nature",
    "slug": "nature",
    "excerpt": "Nature is incredible I love walking in the nature and due to all this global warming thing we are actually hurting the nature. Let's vouch to protect our nature for the betterment of Mankind.",
    "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodoconsequat. Duis aute irure dolor in reprehenderit in voluptate velit essecillum do tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodoconsequat. Duis aute irure dolor in reprehenderit in voluptate velit essecillum do tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodoconsequat. Duis aute irure dolor in reprehenderit in voluptate velit essecillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat nonproident, sunt in culpa qui officia deserunt mollit anim id est laborum."  
  },
  {
    "image_url": "blog/images/mountains.jpg",
    "title": "Trekking in the Mountains",
    "slug": "trekking-in-the-mountains",
    "excerpt": "Mountains are the most fascinating phenomenon ever. The mysterious formations of mountains are Flabbergast many people. One of the Beauty of earth is the Mountains.",
    "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodoconsequat. Duis aute irure dolor in reprehenderit in voluptate velit essecillum do tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodoconsequat. Duis aute irure dolor in reprehenderit in voluptate velit essecillum do tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodoconsequat. Duis aute irure dolor in reprehenderit in voluptate velit essecillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat nonproident, sunt in culpa qui officia deserunt mollit anim id est laborum."
  },
  {
    "image_url": "blog/images/technology.jpg",
    "title": "Latest Technology",
    "slug": "latest-technology",
    "excerpt": "Technology is the application of latest knowledge and skills to innovate and create new things. Technology is the manifestation of mankinds intellectual capabilities relative to other animals living on his Planet.",
    "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodoconsequat. Duis aute irure dolor in reprehenderit in voluptate velit essecillum do tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodoconsequat. Duis aute irure dolor in reprehenderit in voluptate velit essecillum do tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodoconsequat. Duis aute irure dolor in reprehenderit in voluptate velit essecillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat nonproident, sunt in culpa qui officia deserunt mollit anim id est laborum."
  },
  {
    "image_url": "blog/images/nature.jpg",
    "title": "Nature",
    "slug": "nature",
    "excerpt": "Nature is incredible I love walking in the nature and due to all this global warming thing we are actually hurting the nature. Let's vouch to protect our nature for the betterment of Mankind.",
    "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodoconsequat. Duis aute irure dolor in reprehenderit in voluptate velit essecillum do tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodoconsequat. Duis aute irure dolor in reprehenderit in voluptate velit essecillum do tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodoconsequat. Duis aute irure dolor in reprehenderit in voluptate velit essecillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat nonproident, sunt in culpa qui officia deserunt mollit anim id est laborum."  
  },
  {
    "image_url": "blog/images/mountains.jpg",
    "title": "Trekking in the Mountains",
    "slug": "trekking-in-the-mountains",
    "excerpt": "Mountains are the most fascinating phenomenon ever. The mysterious formations of mountains are Flabbergast many people. One of the Beauty of earth is the Mountains.",
    "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodoconsequat. Duis aute irure dolor in reprehenderit in voluptate velit essecillum do tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodoconsequat. Duis aute irure dolor in reprehenderit in voluptate velit essecillum do tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodoconsequat. Duis aute irure dolor in reprehenderit in voluptate velit essecillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat nonproident, sunt in culpa qui officia deserunt mollit anim id est laborum."
  }
]

# Create your views here.


# def index(request):
#   return render(request, "blog/index.html", {
#     "data": data[:-4:-1]
#   })

def index(request):
  posts = Post.objects.all().order_by("-date")[:3]
  return render(request, "blog/index.html", {
    "posts": posts
  })


# def posts(request):
#   return render(request, "blog/posts.html", {
#     "Data": data
#   })

def posts(request):
  all_posts = Post.objects.all().order_by("-date")
  return render(request, "blog/posts.html", {
    "posts": all_posts
  })


# def post_detail(request, slug):
#   requested_data = None
#   for i in data:
#     if i['slug'] == slug:
#       requested_data = i
#   return render(request, "blog/post_detail.html", {
#     "data": requested_data
#   })

# def post_detail(request, slug):
#   post = Post.objects.get(slug=slug)
#   return render(request, "blog/post_detail.html", {
#     "post": post,
#     "tags": post.tags.all()
#   })


class PostDetailView(View):

  def get(self, request, slug):
    post = Post.objects.get(slug=slug)
    
    form = CommentForm()
    comments = post.comment_set.all().order_by("-id")

    current_id = str(post.id)
    id_list = request.session.get("readlater_id_list")

    read_later = False
    if id_list != None:
      for i in id_list:
        if i == current_id:
          read_later = True 

    return render(request, "blog/post_detail.html", {
      "post": post,
      "tags": post.tags.all(),
      "read_later": read_later,
      "form": form,
      "comments": comments
    })

  
  
  def post(self, request, slug):
    
    if request.POST.get("add_id") != None:
      post_id = request.POST["add_id"]
      readlater_id_list = request.session.get("readlater_id_list")
      
      if readlater_id_list == None:
        readlater_id_list = [post_id]
      else:
        readlater_id_list.append(post_id)
      
      request.session["readlater_id_list"] = readlater_id_list
    
    else:
      post_id = request.POST["remove_id"]
      readlater_id_list = request.session["readlater_id_list"]
      readlater_id_list.remove(post_id)
      request.session["readlater_id_list"] = readlater_id_list
   
    return HttpResponseRedirect(reverse("post-detail", args=[slug]))


# class ReadlaterView(TemplateView):
#   template_name = "blog/readlater.html"


def read_later(request):

  readlater_ids_list = request.session.get("readlater_id_list")
  posts = []
  if readlater_ids_list != None:
    for id in readlater_ids_list:
      post_id = int(id)
      post = Post.objects.get(id=post_id)
      posts.append(post)

  return render(request, "blog/readlater.html", {
    "posts": posts
  })


class CommentView(View):
  
  def post(self, request):
    form = CommentForm(request.POST)
    slug = request.POST["comment"]

    if form.is_valid():
      comment = form.save(commit=False)
      comment.post = Post.objects.get(slug=slug)
      comment.save()

    return HttpResponseRedirect(reverse("post-detail", args=[slug])) 