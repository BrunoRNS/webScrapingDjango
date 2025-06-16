from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

class UrlForm(forms.Form):
    """
    Url Form:
    The form for the user to input the URL of the site.
    """
    
    input_url = forms.URLField(
        
        max_length=255, 
        min_length=5, 
        required=True,
    
        widget = forms.TextInput(
        
            attrs = {
                'placeholder': 'URL of the SPA website',
            }
        
        )
        
    )
    
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={
        'id': 'g-recaptcha'
    }))
