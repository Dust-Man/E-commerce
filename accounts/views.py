from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm

def signup(request):
    # Vista para registro de usuarios: procesa formulario, crea cuenta y maneja perfil
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Guardar datos adicionales en el perfil del usuario
            if form.cleaned_data.get('phone'):
                user.userprofile.phone = form.cleaned_data.get('phone')
                user.userprofile.save()
            
            email = form.cleaned_data.get('email')
            messages.success(request, f'¡Cuenta creada exitosamente para {email}! Ya puedes iniciar sesión.')
            return redirect('login')
    else:
        # Si no es POST, crear un formulario vacío
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

    # Vista protegida para mostrar y actualizar el perfil del usuario
@login_required
def profile(request):
    if request.method == 'POST':
        # Crear formularios con los datos enviados y la instancia actual del usuario
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.userprofile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, '¡Tu perfil ha sido actualizado correctamente!')
            return redirect('profile')
    else:
        # Si no es POST, mostrar formularios con los datos actuales
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'accounts/profile.html', context)

    # Vista personalizada para la página de inicio de sesión
def custom_login(request):
    return render(request, 'accounts/login.html')
