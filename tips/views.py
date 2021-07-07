from django.shortcuts import render
from django.core.paginator import Paginator
from datetime import datetime
from .models import PythonTip

# Create your views here.
def home(request):
    context = {
        "tips": []
    }
    tips_obj = PythonTip.objects.all().order_by("-id")
    paginator = Paginator(tips_obj, 20)
    tips = paginator.page(1)
    if "page" in request.GET:
        page = request.GET.get("page")
        try:
            tips = paginator.page(page)
        except PageNotAnInteger:
            tips = paginator.page(1)
        except EmptyPage:
            tips = paginator.page(paginator.num_pages)
    context["has_other_pages"] = tips.has_other_pages()
    context["has_previous"] = tips.has_previous()
    context["has_next"] = tips.has_next()
    context["number"] = tips.number
    context["count"] = tips.paginator.num_pages
    context["next_page_number"] = False
    context["previous_page_number"] = False
    if tips.has_next():
        context["next_page_number"] = tips.next_page_number()
    if tips.has_previous():
        context["previous_page_number"] = tips.previous_page_number()

    for tip in tips:
        current_tip = {}
        current_tip["tip"] = tip.tip.replace(">>>", ">")
        current_tip["poster"] = tip.poster
        current_tip["poster_email"] = tip.poster_email
        current_tip["is_published"] = tip.is_published
        post_date, post_time = tip.timestamp.split(" ")
        d = datetime.strptime(post_time, "%H:%M:%S")
        current_tip["post_date"] = post_date
        current_tip["post_time"] = d.strftime("%I:%M %p")
        context["tips"].append(current_tip)
    return render(request, 'index.html', context)
