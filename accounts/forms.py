from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, UserCreationForm
)
from django.db.transaction import atomic
from django.forms import CharField, Textarea

from accounts.models import Profile


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']

    biography = CharField(
        label='Tell us your story with movies', widget=Textarea,
    )

    # @atomic o sa ne asigure ca nu se intampla schimbari in baza de date
    # doar daca nu sunt erori
    @atomic
    def save(self, commit=True):
        # Salvam obiectul User care vine la pachet cu Django
        result = super().save(commit)

        biography = self.cleaned_data['biography']

        # Cream un obiect Profil in care adaugam datele noastre in plus
        # fata de un utilizator simplu (biography) + user-ul creat inainte
        # si il salvam
        profile = Profile(biography=biography, user=result)
        if commit:
            profile.save()
        return result
