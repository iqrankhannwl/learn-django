from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse, Http404, HttpResponseRedirect
# Create your views here.

from .models import Question, Choice
from django.template import loader
from django.urls import reverse

# def root(request):
#     context = {"status":"ok"}
#     return JsonResponse(context)



# def root(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     output = [q.question_text for q in latest_question_list]
#     context = {"Questions":output}
#     return JsonResponse(context)

# def root(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("index.html")
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))


def root(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "index.html", context)

def details(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        return Http404("Question does not found")
    return render(request, "details.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "details.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("results", args=(question.id,)))