def path(class_name):

    templates_map = {
        'CreateUserView' : ['system/user/create/user_create.html'],
        'ListUserView'   : ['system/user/create/user_list.html'],
    }

    return templates_map[class_name]
