djangocms-simple
################

Simplified APIs for django CMS plugins, apps, menus and toolbar modifiers.

djangocms-simple aims at solving 80% of the use cases with drastically
simplified APIs to extend django CMS at the cost of some features. For
extensions that need the full feature set provided by django CMS, simple
use the default APIs.


Usage
=====

All examples are the equivalents to the examples found at http://docs.django-cms.org/en/2.4.0/extending_cms/extending_examples.html#extending-the-cms-examples and http://docs.django-cms.org/en/develop/extending_cms/toolbar.html.

The Poll Plugin::

    from django.utils.translation import ugettext_lazy as _

    from djangocms_simple import register

    from polls.models import PollPlugin

    @register.plugin(_('Poll Plugin'), render_template='polls/plugin.html', model=PollPlugin)
    def get_context(context, instance, placeholder):
        context['instance'] = instance
        return context

The Poll Apphook::

    from django.utils.translation import ugettext_lazy as _

    from djangocms_simple import register

    register.app(_("Poll App"), "polls.urls")
    

The Poll Menu::
    
    from django.utils.translation import ugettext_lazy as _

    from djangocms_simple import register
    from djangocms_simple.menu import Node

    @register.menu(_('Polls Menu'))
    def get_nodes(request):
        root = Node('Polls', reverse('polls.views.index'))
        for poll in Poll.objects.all():
            root.add_child(poll.question, reverse('polls.views.detail', args=(poll.pk,)))
        return root

The Poll Toolbar::

    from djangocms_simple import register

    @register.toolbar
    def populate(toolbar, request, is_app, app_path):
        menu = toolbar.get_or_create_menu('poll-app', _('Polls'))
        url = reverse('admin:polls_poll_changelist')
        menu.add_sideframe_item(_('Poll overview'), url=url)
    
