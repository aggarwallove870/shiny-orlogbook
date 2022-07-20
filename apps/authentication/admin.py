from django.contrib import admin
from django.utils.translation import gettext as _
from django.contrib.auth.admin import UserAdmin
from apps.authentication.models import *
from django import forms



class UserCreationForm(forms.ModelForm):
    
    class Meta:
        model = NewUser
        fields = ('username',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.set_password(self.cleaned_data["confirm_password"])
        if commit:
            user.save()
        return user

   

class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    add_form = UserCreationForm
    list_display = ("username",)
    ordering = ("email",)

    fieldsets = (
        (None, {'fields': ("username",'email', 'password', 'first_name', 'last_name','institute','supervisor','is_active','is_superuser','is_supervisor', 'profile_photo')}),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email','first_name','last_name','password','confirm_password','institute','supervisor', 'is_active','is_superuser','is_supervisor','profile_photo')}
            ),
        )
    

    filter_horizontal = ()

admin.site.register(NewUser, CustomUserAdmin)