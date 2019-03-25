class NewImageleForm(forms.ModelForm):
    class Meta:
        model =Image
        exclude = ['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }