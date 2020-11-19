from rest_framework.response import Response
from rest_framework.views import APIView

from .services import save_group_info
from .models import Group


class MemeRequestView(APIView):

    def post(self, request):
        token = '66320aec66320aec66320aec2566468bc56663266320aec39bcc3108c904fe8a5860896'
        status, data = save_group_info(request, token)
        return Response(status=status, data=data)

