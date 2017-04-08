from django.shortcuts import render

# Create your viewshere.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
