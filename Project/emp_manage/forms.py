from django import forms
class feedbackForm(forms.Form):
    name =  forms.CharField(label='Your Name' ,max_length=52)
    email = forms.EmailField(label = "Your Email")
    feedback = forms.CharField(label="give you genuine feedback", widget=forms.Textarea)
    
def __init__(self, *args, **kwargs):
    super(feedbackForm, self).__init__(*args, **kwargs)
    for visible in self.visible_fields():
        visible.field.widget.attrs['class'] = 'form-control' 