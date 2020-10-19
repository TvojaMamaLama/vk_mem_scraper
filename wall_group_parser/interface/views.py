from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import TemplateView


from .models import VkGroup
from .group_wall_info import VK_API


class AboutPageView(TemplateView):
    template_name = 'interface/about.html'


class SearchGroupView(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, 'interface/search.html')

    def post(self, request):
        link = request.POST['link'].split('/')[-1]
        group_dict = VK_API.get_group_info(link)
        print(link)
        print(group_dict)
        if not 'error' in group_dict:
            group = VkGroup.objects.filter(screen_name=link)
            print(group)
            if group == None:
                group = VkGroup.objects.create(
                    group_id=group_dict['id'],
                    name=group_dict['name'],
                    screen_name=group_dict['screen_name'],
                    is_closed=group_dict['is_closed'],
                    group_type=group_dict['type'],
                    description=group_dict['description'],
                    status=group_dict['status'],
                    members_count=group_dict['members_count'],
                    wall=group_dict['wall'],
                    )
        else:
            group = group_dict
        print(group)
        return render(request, 'interface/search.html', context= {'group':group})

