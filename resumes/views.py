from django.shortcuts import render, redirect, get_object_or_404
from .models import Resume


def index(request):
    if request.POST:
        resume = Resume()
        resume.title = request.POST["title"]
        resume.skill = request.POST["skill"]
        resume.content = request.POST["content"]
        resume.save()
        return redirect("resumes:index")
    resumes = Resume.objects.all()
    return render(
        request,
        "resumes/index.html",
        {"resumes": resumes},
    )


def new(request):
    return render(
        request,
        "resumes/new.html",
    )


def show(request, id):
    resume = get_object_or_404(Resume, id=id)
    if request.POST:

        resume.title = request.POST.get("title")
        resume.skill = request.POST.get("skill")
        resume.content = request.POST.get("content")
        resume.save()
        return redirect("resumes:index")

    return render(
        request,
        "resumes/show.html",
        {"resume": resume},
    )


def edit(request, id):
    resume = get_object_or_404(Resume, id=id)

    return render(
        request,
        "resumes/edit.html",
        {"resume": resume},
    )


def delete(request, id):
    resume = get_object_or_404(Resume, id=id)
    if request.POST:
        resume.delete()
        return redirect("resumes:index")
    return render(
        request,
        "resumes/delete.html",
        {"resume": resume},
    )
