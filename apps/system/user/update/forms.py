from crispy_forms.helper    import FormHelper
from crispy_forms.layout    import Layout, Div, Submit
from django                 import forms
from django.forms import HiddenInput

from apps.admin.user.models import User


class UserUpdateForm(forms.ModelForm):

    first_name = forms.CharField(required=True)
    last_name  = forms.CharField(required=True)
    salary     = forms.CharField(required=False)

    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'email',
            'salary',
            'contact_number',
            'is_active',
            'position',
            'employee_number',
            'reporting_line_manager',
            'birth_date',
            'description',
            'is_admin'
        ]

        labels = {
            'is_active' : 'Active',
            'is_admin'  : 'Admin'
        }

    @property
    def helper(self):

        helper = FormHelper()
        helper.layout = Layout(
            Div(
                "is_active",
                "is_admin",
                css_class="grid grid-cols-2 gap-3",
            ),
            Div(
                "email",
                css_class="grid grid-cols-1 gap-3",
            ),
            Div(
                "salary",
                "employee_number",
                css_class="grid grid-cols-2 gap-3",
            ),
            Div(
                "contact_number",
                "birth_date",
                css_class="grid grid-cols-2 gap-3",
            ),
            Div(
                "first_name",
                "last_name",
                css_class="grid grid-cols-2 gap-3",
            ),
            Div(
                "position",
                "reporting_line_manager",
                css_class="grid grid-cols-2 gap-3",
            ),
            Div(
                "description",
                css_class="grid grid-cols-1 gap-3",
            ),
            Submit(
                "update-btn",
                "Update",
                css_class="cursor-pointer py-2 bg-blue-500 text-white font-semibold uppercase hover:bg-blue-500/80 duration-200 rounded hover:drop-shadow-xl tracking-tight self-end px-5",
            ),
        )

        if not self.instance.is_admin:
            # Hide the field if the user is not an admin
            self.fields["is_admin"].widget = HiddenInput()

        return helper

    def clean_contact_number(self):

        contact_number = self.cleaned_data['contact_number']

        if contact_number:
            if not contact_number.isdigit():
                raise forms.ValidationError('Please only include digits')

        return contact_number

