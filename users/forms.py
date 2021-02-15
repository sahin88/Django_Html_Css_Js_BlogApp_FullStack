from django import forms


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# asagidaki  yeni bir form olusturuyoruz bu formda hangi method kullanilcak öncelikle bunu söylüyoru
# User model in icerisinde default olarak 'username',passwd1 vs 	var ancak burada email olmadigi icin emaili ekliyoruz


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

    def get_absolute_url(self):
        # bu kisim  esasinda POst model cagirildiktan sonra geliyor ama
        return reverse('post-detail', kwargs={'pk': self.pk})


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
