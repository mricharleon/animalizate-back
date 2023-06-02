def close_session(view_func):
    """
    This is a decorator function that closes the database session and disposes of the bind after the
    view function is executed.

    :param view_func: view_func is a function that takes a request object as its argument and returns a
    response object. It is the function that will be wrapped by the decorator
    :return: The `close_session` function returns a new function `wrapper` that takes two arguments
    `context` and `request`.
    """
    def wrapper(context, request):
        response = view_func(request)
        request.dbsession.close()
        request.dbsession.get_bind().dispose()
        return response
    return wrapper
