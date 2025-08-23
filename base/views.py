from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import Contact_form

def home(request):
    if request.method == 'POST':
        form = Contact_form(request.POST)
        if form.is_valid():
            # Obtener los datos del formulario
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            
            # Crear el mensaje completo
            full_message = f"""
            Nombre: {name}
            Email: {email}
            Teléfono: {phone}
            
            Mensaje:
            {body}
            """
            
            try:
                # Enviar el correo
                send_mail(
                    subject=f"Contacto desde web: {subject}",
                    message=full_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['sosoftware1@hotmail.com'],
                    fail_silently=False,
                )
                messages.success(request, '¡Mensaje enviado correctamente! Te contactaremos pronto.')
            except Exception as e:
                messages.error(request, 'Hubo un error al enviar el mensaje. Por favor, intenta nuevamente.')
            
            return redirect('home')
    else:
        form = Contact_form()
    
    return render(request, 'base/home.html', {'form': form})
