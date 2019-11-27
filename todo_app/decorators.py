from rest_framework.response import Response
import jwt
import traceback

def permission_required():
    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            try:
                public_key = open('jwt-key.pub').read()
                access_token = request.request.META['HTTP_AUTHORIZATION']
                access_token = access_token.replace("Bearer ", "")
            except Exception as e:
                return Response({"status": False, "message": 'Please Login before Accessing'}, status=401)
            try:
                decorator_data = jwt.decode(access_token, public_key, algorithm='RS256')
            except Exception as e:
                print(e)
                traceback.print_exc()
                return Response({"status": False, "message": 'UnAuthorised'}, status=401)
            request.request.META.update({'user_id': decorator_data["user_id"]})
            return view_method(request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper
