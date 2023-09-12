from django import forms
from .models import Person, District, Branch, Materials


class PersonCreationForm(forms.ModelForm):
    name=forms.CharField(label='Name',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Enter Your Name'
    }))

    age=forms.IntegerField(label='Age',widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type': 'text',
    }))

    dob = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'size':'2',
        'type':'date',
    }))
    # gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])

    phone_number=forms.CharField(label="Phone Number",widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type': 'text',
    }))

    mail_id = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'type': 'email',
            'placeholder': 'example@example.com'
        }))

    address=forms.Textarea()

    # account = forms.ChoiceField(choices=[('S', 'Savings_Account'), ('C', 'Current_Account'), ('O', 'Other_Account')])

    materials = forms.ModelMultipleChoiceField(
        queryset=Materials.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={
        }))


    class Meta:
        model = Person
        fields=['name','age','dob','gender','phone_number','mail_id','address',
                'account','materials','district','branches']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branches'].queryset = Branch.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branches'].queryset = Branch.objects.filter(district_id=district_id).all()
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['branches'].queryset = self.instance.district.branches_set.all()
