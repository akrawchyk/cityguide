from django.utils.translation import ugettext_lazy as _

from feincms.module.page.models import Page
from feincms.contents import RichTextContent
from feincms.module.medialibrary.contents import MediaFileContent


Page.register_extensions(
    'feincms.extensions.changedate',
    'feincms.module.page.extensions.navigation',
    'feincms.module.page.extensions.titles',
)

Page.register_templates({
    'title': _('Standard template'),
    'path': 'cityguide/index.html',
    'regions': (
        ('main', _('Main content area')),
        ('sidebar', _('Sidebar'), 'inherited'),
    ),
})

Page.create_content_type(RichTextContent)
Page.create_content_type(MediaFileContent, TYPE_CHOICES=(
    ('default', _('default')),
))
