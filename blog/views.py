from django.shortcuts import get_object_or_404, render
from django.views import generic

from .forms import CommentForm
from .models import Blog


class BlogListView(generic.ListView):
    queryset = Blog.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/blog-list.html"
    context_object_name = 'blogs'


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    comments = blog.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current blog to the comment
            new_comment.post = blog
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/blog-detail.html',
                  {"blog": blog, "comments": comments,
                   "new_comment": new_comment, "comment_form": comment_form, },
                  )