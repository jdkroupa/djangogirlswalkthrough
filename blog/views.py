from django.shortcuts import render


def post_list(request):
    return render(request=request, template_name="blog/post_list.html", context={})