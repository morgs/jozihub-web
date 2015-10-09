from django import forms


# Profile Update Form

class VenueHireForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    contact_email = forms.EmailField()
    affiliated_organisation = forms.CharField(required=False)
    # event_start_time = forms.DateTimeField(widget=forms.DateTimeInput)
    # event_end_time = forms.DateTimeField(widget=forms.SplitDateTimeWidget)
    event_description = forms.CharField(widget=forms.Textarea)
        
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
