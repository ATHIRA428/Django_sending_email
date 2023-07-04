from django.shortcuts import render,redirect
from . forms import AddPost,Profile,AddCommentForm
from model_setup . models import Post,Profile,Comment,Like
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
# Create your views here.



def addpost(request):
    form = AddPost()
    if request.method == 'POST':
        form = AddPost(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  
    
    context = {
        'form': form
    }
    
    return render(request, 'addpost.html', context)

# def create_profile(request):
#     form = Profile()
#     if request.method == 'POST':
#         form = Profile(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/')  
    
#     context = {
#         'form': form
#     }
    
#     return render(request, 'create_profile.html', context)


def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = AddPost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPost(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, 'update_post.html', context)    

def posts(request):
    posts = Post.objects.all()
    for post in posts:
        return render(request, 'post.html', {'post': posts})


# def posts(request):
#     post=Post.objects.all()
#     context={
#         'post':post
#     }
#     return render(request,'post.html',context)

def profile(request):
    profiles=Profile.objects.all()
    context={
        'profiles':profiles
    }
    return render(request,'profile.html',context)

def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('/')

    context = {
        'post': post,
    }

    return render(request, 'delete_post.html', context)

def add_comment(request, post_id):
    try:
        post = get_object_or_404(Post, pk=post_id)
        user = request.user

        if request.method == 'POST':
            form = AddCommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.user = request.user  
                comment.save()
                return redirect('/')
        else:
            form = AddCommentForm()

        context = {
            'form': form,
            'post': post,
        }

        return render(request, 'add_comment.html', context)
    except Exception as e:
        return redirect('/')  
# def add_comment(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     user=request.user
#     if request.method == 'POST':
#         form = AddCommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.user = request.user  
#             comment.save()
#             return redirect('/')
#     else:
#         form = AddCommentForm()
    
#     context = {
#         'form': form,
#         'post': post,
#     }
    
#     return render(request, 'add_comment.html', context)


# def toggle_like(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     user = request.user

#     if request.method == 'POST':
#         liked = Like.toggle_like(user, post)
#         if liked:
#             pass
#         else:
#             pass

#     return redirect('post_detail', post_id=post_id)


# def toggle_like(request, post_id):
#     if request.method == 'POST' and request.user.is_authenticated:
#         post = Post.objects.get(pk=post_id)
#         liked = Like.toggle_like(request.user, post)
#         like_count = post.likes.count()
#         return JsonResponse({'liked': liked, 'like_count': like_count})
#     else:
#         return JsonResponse({'error': 'Invalid request'}, status=400)



# def add_comment(request, post_id):
#     post = get_object_or_404(Post, post_id=post_id)

#     if not request.user.is_authenticated:
#         return redirect('login')  

#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.user = request.user
#             comment.post = post
#             comment.save()
#             return redirect('posts', post_id=post_id)
#     else:
#         form = CommentForm()

#     context = {
#         'form': form,
#         'post': post
#     }

#     return render(request, 'add_comment.html', context)

# @login_required
# def add_comment(request, post_id):
#     post = get_object_or_404(Post, post_id=post_id)

#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.user = request.user
#             comment.post = post
#             comment.save()
#             return redirect('posts', post_id=post_id)
#     else:
#         form = CommentForm()

#     context = {
#         'form': form,
#         'post': post
#     }

#     return render(request, 'add_comment.html', context)