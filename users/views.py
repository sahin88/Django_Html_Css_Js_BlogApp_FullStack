from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.


##User creation form return  user 
##request.POST  is kind of dictionary
#Eger post ile ilgili birsey var ise yani icersine yazi yazilip gönderilmisse bu durumda icerik is valid ile kontrol edilir
# yoksa form adi altinda labelslar ve inputlar anasayfaya gönderilir 


def register(request):
	if request.method == "POST":
		form =UserRegistrationForm(request.POST)
		if  form.is_valid():
			ak=form.save()
			#ak return user name 
			username=form.cleaned_data.get('username')
			messages.success(request, f" Your account has been {username} sucesfully created please register")
			return redirect('login')

	else:
		form=UserRegistrationForm()

	return render(request, 'users/register.html', {"form":form})

#request.Post is dictionry
@login_required
def profile(request):
	if request.method=='POST':
		u_form=UserUpdateForm(request.POST,instance=request.user)
		p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
		
		if  u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			#username=form.cleaned_data.get('username')
			messages.success(request, f" Your account has been sucesfully updated")
			return redirect('profile')
	else:
		u_form=UserUpdateForm(instance=request.user)
		p_form=ProfileUpdateForm(instance=request.user.profile)
		

	context={
	'u_form':u_form,
	'p_form':p_form
	}
	return render (request, 'users/profile.html', context)

