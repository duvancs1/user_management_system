

def check_current_user(self, form, user):

    print('test')
    if not form.cleaned_data:
        return True

    # Have to check if the current user is logged in, so that you don't make yourself inactive by accident
    if not form.cleaned_data.get('is_active'):
        if user.id == self.request.user.id:
            return False

    return True
