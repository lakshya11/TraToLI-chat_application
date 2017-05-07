from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import User
from .models import Message

@login_required
def home(request):
	loged_in_user = request.user
	users = User.objects.filter(~Q(username = loged_in_user))
	print users
	context = {
		'users': users
	}
	return render(request, 'chat_app/home.html',context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'chat_app/signup.html', {'form': form})

def start_chat(request,receiver):
	sender = request.user()
	chat_history = Chat.objects.value_list(message_id__text,flat=True).filter(sender=sender,receiver= receiver)
	return render(request, 'chat_app/chat.html',{'chat_history':chat_history})