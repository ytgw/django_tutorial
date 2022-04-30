from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world. You'are at the polls index.")

def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse("You're looking at question %s." % question_id)

def results(request: HttpRequest, question_id: int) -> HttpResponse:
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse("You're voting on question %s." % question_id)
