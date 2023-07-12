from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SignupForm, LoginForm, WritingForm, SectionForm
from .models import Users, Page, Section

def dynamic_form(request):
    form = SectionForm()
    return render(request,"Writing/dynamic_form.html",{"form":form})
# for writing mode in the app
def write_mode(request, section, page):
    if request.method == "POST":
        form = WritingForm(request.POST)
        if form.is_valid():
            pg = Page.objects.get(id=page)
            pg.text=form.cleaned_data['text']
            pg.title=form.cleaned_data['title']
            pg.save()
            id = Section.objects.get(id=section).user.id
            return HttpResponseRedirect(f'/{id}/index')
    context = {
        'title':Page.objects.get(pk=page).title,
        'text':Page.objects.get(pk=page).text
    }
    form = WritingForm(initial=context)
    return render(
        request, "Writing/writing.html", {'form':form}
    )


# for login
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            if Users.objects.filter(user_name=form.cleaned_data["user_name"]).exists():
                if Users.objects.filter(
                    user_name=form.cleaned_data["user_name"],
                    password=form.cleaned_data["password"],
                ).exists():
                    user = Users.objects.get(user_name=form.cleaned_data["user_name"])
                    id = user.id
                    return HttpResponseRedirect(f"{id}/index")
                else:
                    return render(
                        request, "Writing/login.html", {"form": form, "flag2": True}
                    )
            else:
                return render(
                    request,
                    "Writing/login.html",
                    {"form": form, "flag1": True, "flag2": False},
                )
    form = LoginForm()
    return render(
        request, "Writing/login.html", {"form":form,"flag1": False, "flag2": False}
    )


# for signup
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            if (
                Users.objects.filter(user_name=form.cleaned_data["user_name"]).exists()
                is False
            ):
                form.save()
                return HttpResponseRedirect("/index")
            else:
                return render(
                    request, "Writing/signup.html", {"form": form, "flag": True}
                )
    form = SignupForm()
    return render(request, "Writing/signup.html", {"form": form, "flag": False})


# for indexing the documents inside the application
def index(request, id):
    if request.method == "POST":
        if request.POST["flag"] == "0": # for creation of the form
            user = Users.objects.get(id=id)
            name = request.POST['name']
            crSection = Section(name=name, user=user)
            crSection.save()
        if request.POST["flag"] == "-0":
            section = Section.objects.get(pk=request.POST["section_id"])
            page = Page.objects.filter(section=section)
            page.delete()
            section.delete()
        if request.POST["flag"] == "1": # for creation of new pages
            section_id = request.POST["section_id"]
            section = Section.objects.get(id=section_id)
            page = Page(title="New Page", text=" ", section=section)
            page.save()
        if request.POST["flag"] == "-1":
            page = Page.objects.get(pk=request.POST['page_id'])
            page.delete()
    user = Users.objects.get(pk=id)
    sections = Section.objects.filter(user=user)
    pageList = []
    pgList = dict()
    for x in range(len(sections)):
        pgList[sections[x]]=Page.objects.filter(section=sections[x])
        pageList.clear()
    return render(
        request, "Writing/index.html", {"sections": sections, 
                                        'pageList':pgList}
    )


# for home_page
def home(request):
    return render(request, "Writing/home.html")