from django import forms

class Contact_form(forms.Form):
    subject = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Nombre'
        self.fields['phone'].widget.attrs['placeholder'] = 'Número de teléfono'
        self.fields['email'].widget.attrs['placeholder'] = 'Correo electrónico'
        self.fields['subject'].widget.attrs['placeholder'] = 'Asunto'
        self.fields['body'].widget.attrs['placeholder'] = 'Escribe tu mensaje aquí'
        
        
        
        