import os
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.views import generic
from mezzanine.utils.views import render
from django.conf import settings
from django.views import generic
from ..team.models import Team
from mysite.main.models import Pages


class AboutPageView(generic.TemplateView):
    template_name = 'page/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'abou  t')
        return context


class AboutBoardPageView(generic.TemplateView):
    template_name = 'page/about_board.html'

    def get_context_data(self, **kwargs):
        context = super(AboutBoardPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'about_board')
        return context


class AmbassadorsPageView(generic.TemplateView):
    template_name = 'page/ambassadors.html'

    def get_context_data(self, **kwargs):
        context = super(AmbassadorsPageView, self).get_context_data(**kwargs)
        context['ambassadors'] = Pages.objects.all()
        return context


class ApsPageView(generic.TemplateView):
    template_name = 'page/aps.html'

    def get_context_data(self, **kwargs):
        context = super(ApsPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'aps')
        return context


class CommunitiesPageView(generic.TemplateView):
    template_name = 'page/communities.html'

    def get_context_data(self, **kwargs):
        context = super(CommunitiesPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'communities')
        return context


class GetInvolvedPageView(generic.TemplateView):
    template_name = 'page/get_involved.html'

    def get_context_data(self, **kwargs):
        context = super(GetInvolvedPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'get-involved')
        return context


class HomepageView(generic.TemplateView):
    template_name = 'page/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context['images'] = Team.objects.all()
        context['page'] = Pages.objects.filter(slug=u'home')
        return context


class IndexPageView(generic.TemplateView):
    template_name = 'page/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'index')
        return context


class InvolvedParticipatesPageView(generic.TemplateView):
    template_name = 'page/involved_participate.html'

    def get_context_data(self, **kwargs):
        context = super(InvolvedParticipatesPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'involved_participates')
        return context


class JobsPageView(generic.TemplateView):
    template_name = 'page/jobs.html'

    def get_context_data(self, **kwargs):
        context = super(JobsPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'jobs')
        return context


class MissionPageView(generic.TemplateView):
    template_name = 'page/about_mission.html'

    def get_context_data(self, **kwargs):
        context = super(MissionPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'about_mission')
        return context


class NewsPageView(generic.TemplateView):
    template_name = 'page/news.html'

    def get_context_data(self, **kwargs):
        context = super(NewsPageView, self).get_context_data(**kwargs)
        context['news'] = Pages.objects.all()
        return context


class OurPictureView(generic.TemplateView):
    template_name = 'page/COS_team.html'

    def get_context_data(self, **kwargs):
        context = super(OurPictureView, self).get_context_data(**kwargs)
        context['images'] = Team.objects.filter()
        return context


class PartnersPageView(generic.TemplateView):
    template_name = 'page/about_partners.html'

    def get_context_data(self, **kwargs):
        context = super(PartnersPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'about_partners')
        return context


class PrPageView(generic.TemplateView):

    def get(self, request, item):
        return render_to_response(os.path.join('page', 'pr', item) + '.html')


class ServicePageView(generic.TemplateView):
    template_name = 'page/service.html'

    def get_context_data(self, **kwargs):
        context = super(ServicePageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'service')
        return context


class StatsPageView(generic.TemplateView):
    template_name = 'page/stats_consulting.html'

    def get_context_data(self, **kwargs):
        context = super(StatsPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'stats_consulting')
        return context


class SponsorsPageView(generic.TemplateView):
    template_name = 'page/about_sponsors.html'

    def get_context_data(self, **kwargs):
        context = super(SponsorsPageView, self).get_context_data(**kwargs)
        context['page'] = Pages.objects.filter(slug=u'about_sponsors')
        return context
