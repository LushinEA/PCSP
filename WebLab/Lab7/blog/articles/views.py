from .models import Article
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import Http404

# Create your views here.

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
        # обработать данные форны, если метод POST
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
            # в словаре form будет храниться информация, введенная пользователен
            if form["text"] and form["title"]:
                # если поля заполнены без ошибок
                if not Article.objects.filter(title=form['title']).exists():
                    Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                    return redirect('get_article', article_id=Article.objects.count())
                else:
                    form['errors'] = u"Статья с таким названием уже существует"
                    return render(request, 'create_post.html', {'form': form})
        # перейти на страницу поста
            else:
                # если введённые данные некорректны
                form['errors'] = u"Нe все поля запонены"
                return render(request, 'create_post.html', {'form': form})
        else:
        #просто вернуть страницу с формой, если метод GET
            return render(request, 'create_post.html', {})
    else:
        raise Http404

def registred(request):
    if request.method == "POST":
        form = {
            'username': request.POST["username"],
            'email': request.POST["email"],
            'password': request.POST["password"]
        }
        if form["username"] and form['email'] and form['password']:
            try:
                User.objects.get(username=request.POST["username"])
                form['errors'] = u"Пользователь с таким именем уже существует"
                return render(request, 'registrationpage.html', {'form': form})
            except User.DoesNotExist:
                User.objects.create_user(username=request.POST["username"],
                                         email=request.POST["username"],
                                         password=request.POST['password'])
                return redirect('logIn')
        else:
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'registrationpage.html', {'form': form})
    else:
        return render(request, 'registrationpage.html', {})
    
def logIn(request):
    if request.method == "POST":
        form = {
            'username': request.POST["username"],
            'password': request.POST["password"]
        }
        if form["username"] and form['password']:
            user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form['errors'] = u"Введённый пользователь не существует"
                return render(request, 'signInPage.html', {'form': form})
        else:
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'signInPage.html', {'form': form})
    else:
        return render(request, 'signInPage.html', {})

def logOut(request):
    logout(request)
    return redirect('home')
