from crispy_forms.helper    import FormHelper
from crispy_forms.layout    import Layout, Div, Submit
from django                 import forms

from apps.admin.user_tasks.models import UserTask


class TaskUpdateForm(forms.ModelForm):

    class Meta:
        model = UserTask

        fields = [
            'user',
            'status',
            'description'
        ]

        labels = {
            'user': 'Assigned To',
        }

    @property
    def helper(self):

        helper = FormHelper()
        helper.layout = Layout(
            Div(
                "user",
                css_class="grid grid-cols-1 gap-3",
            ),
            Div(
                "status",
                css_class="grid grid-cols-1 gap-3",
            ),
            Div(
                "description",
                css_class="grid grid-cols-1 gap-3",
            ),
            Submit(
                "create-btn",
                "Update Task",
                css_class="cursor-pointer py-2 bg-blue-500 text-white font-semibold uppercase hover:bg-blue-500/80 duration-200 rounded hover:drop-shadow-xl tracking-tight self-end px-5",
            ),
        )

        return helper
