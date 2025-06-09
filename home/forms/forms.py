from django import forms

class UrlForm(forms.Form):
    
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
