from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import Post
from .forms import PostCreateForm

@login_required
def feed(request):
    """Strona główna z feedem postów wszystkich użytkowników."""
    # Pobierz query wyszukiwania
    search_query = request.GET.get('q', '').strip()
    
    # Bazowe zapytanie
    posts = Post.objects.select_related('author', 'author__profile')
    
    # Jeśli jest zapytanie wyszukiwania, filtruj posty
    if search_query:
        posts = posts.filter(body__icontains=search_query)
    
    # Sortuj po dacie
    posts = posts.order_by('-created')

    return render(
        request,
        'posts/feed.html',
        {
            'posts': posts,
            'search_query': search_query
        }
    )


@login_required
def post_create(request):
    """Tworzenie nowego posta."""
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post został dodany!')
            return redirect('feed')
    else:
        form = PostCreateForm()

    return render(
        request,
        'posts/post_create.html',
        {'form': form}
    )


@login_required
def post_edit(request, post_id):
    """Edycja istniejącego posta."""
    post = get_object_or_404(Post, id=post_id)
    
    # Sprawdź czy użytkownik jest autorem posta
    if post.author != request.user:
        messages.error(request, 'Nie możesz edytować tego posta!')
        return redirect('feed')
    
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post został zaktualizowany!')
            return redirect('feed')
    else:
        form = PostCreateForm(instance=post)
    
    return render(
        request,
        'posts/post_edit.html',
        {'form': form, 'post': post}
    )


@login_required
def post_delete(request, post_id):
    """Usunięcie posta."""
    post = get_object_or_404(Post, id=post_id)
    
    # Sprawdź czy użytkownik jest autorem posta
    if post.author != request.user:
        messages.error(request, 'Nie możesz usunąć tego posta!')
        return redirect('feed')
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post został usunięty!')
        return redirect('feed')
    
    return render(
        request,
        'posts/post_delete.html',
        {'post': post}
    )


@login_required
def post_like(request, post_id):
    """Polubienie lub usunięcie polubienia posta."""
    post = get_object_or_404(Post, id=post_id)
    
    if post.likes.filter(id=request.user.id).exists():
        # Użytkownik już polubił - usuń polubienie
        post.likes.remove(request.user)
        liked = False
    else:
        # Dodaj polubienie
        post.likes.add(request.user)
        liked = True
    
    # Zwróć JSON dla AJAX lub przekieruj
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'liked': liked,
            'total_likes': post.total_likes()
        })
    
    return redirect('feed')