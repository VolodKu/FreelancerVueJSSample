from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext as __
from core.shared.models import IsEnabledModel, TimestampsModel, OrderedModel, ToDictModel
from filebrowser.fields import FileBrowseField
from solo.models import SingletonModel


class CustomerReview(IsEnabledModel, TimestampsModel, OrderedModel, ToDictModel):
    class Meta:
        verbose_name = _('customer review')
        verbose_name_plural = _('customer reviews')
        ordering = ('order',)

    customer_name = models.CharField(_('name'), max_length=255)
    review_text = models.TextField(_('review text'))
    avatar = FileBrowseField(_('image'), directory='customer_reviews/avatars/', extensions=['.jpg', '.png', '.jpeg'], max_length=500)
    tel = models.CharField(_('tel'), max_length=255, null=True, blank=True)
    email = models.EmailField(_('email'), max_length=255, null=True, blank=True)
    hyperlink = models.URLField(_('hyperlink'), max_length=255, null=True, blank=True)

    def __str__(self):
        return self.customer_name


class PortfolioWork(IsEnabledModel, TimestampsModel, OrderedModel, ToDictModel):
    class Meta:
        verbose_name = _('portfolio work')
        verbose_name_plural = _('portfolio works')
        ordering = ('order',)

    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), null=True, blank=True)
    cover_image = FileBrowseField(_('image'), directory='portfolio/', extensions=['.jpg', '.png', '.jpeg'], max_length=500)

    def __str__(self):
        return self.name


class PortfolioImage(IsEnabledModel, TimestampsModel, OrderedModel, ToDictModel):
    class Meta:
        verbose_name = _('portfolio image')
        verbose_name_plural = _('portfolio images')
        ordering = ('order',)

    portfolio_work = models.ForeignKey(to=PortfolioWork, verbose_name=_('portfolio_work'), related_name='images')
    title = models.CharField(_('title'), max_length=255)
    image = FileBrowseField(_('image'), directory='portfolio/', extensions=['.jpg', '.png', '.jpeg'], max_length=500)

    def __str__(self):
        return self.title


class ServicePackage(IsEnabledModel, TimestampsModel, OrderedModel, ToDictModel):
    class Meta:
        verbose_name = _('service package')
        verbose_name_plural = _('service packages')
        ordering = ('order',)

    name = models.CharField(_('name'), max_length=255)
    note = models.TextField(_('note'), null=True, blank=True)
    
    price_base = models.PositiveIntegerField(_('base price'), null=True, blank=True)
    price_discount = models.PositiveIntegerField(_('discount price'), null=True, blank=True)
    price_currency = models.CharField(_('price currency'), max_length=10)
    price_unit = models.CharField(_('price unit'), max_length=10)

    def __str__(self):
        return self.name


class Service(IsEnabledModel, TimestampsModel, OrderedModel, ToDictModel):
    class Meta:
        verbose_name = _('service')
        verbose_name_plural = _('services')
        ordering = ('order',)

    package = models.ForeignKey(to=ServicePackage, verbose_name=_('package'), related_name='services')
    name = models.CharField(_('name'), max_length=255)

    def __str__(self):
        return self.name


class AdditionalService(IsEnabledModel, TimestampsModel, OrderedModel, ToDictModel):
    class Meta:
        verbose_name = _('additional service')
        verbose_name_plural = _('additional services')
        ordering = ('order',)

    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), null=True, blank=True)
    
    price_base = models.PositiveIntegerField(_('base price'), null=True, blank=True)
    price_discount = models.PositiveIntegerField(_('discount price'), null=True, blank=True)
    price_currency = models.CharField(_('price currency'), max_length=10)
    price_unit = models.CharField(_('price unit'), max_length=10)

    def __str__(self):
        return self.name


class WorkStage(IsEnabledModel, TimestampsModel, OrderedModel, ToDictModel):
    class Meta:
        verbose_name = _('work stage')
        verbose_name_plural = _('work stages')
        ordering = ('order',)

    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), null=True, blank=True)

    def __str__(self):
        return self.name


class ServicesPageTexts(SingletonModel, ToDictModel):
    
    packages_global_note = models.TextField(_('text'), default='And it will be gone too.')

    def __str__(self):
        return __("Services Page Texts")

    class Meta:
        verbose_name = _("services page texts")

        
class Contacts(SingletonModel):
    tel = models.CharField(_('tel'), max_length=255, default='555 55 55')
    email = models.EmailField(_('email'), max_length=255, default='me@example.com')
    vk = models.URLField(_('VK'), max_length=255, default='https://vk.com/id85082')
    facebook = models.URLField(_('Facebook'), max_length=255, default='https://www.facebook.com/grigory.bezyuk')
    instagram = models.URLField(_('Instagram'), max_length=255, default='https://www.instagram.com/gbezyuk/')

    def __str__(self):
        return __("Contacts")

    class Meta:
        verbose_name = _("contacts")

    def to_dict(self):
        opts = self._meta
        data = {}
        for f in opts.concrete_fields:
            if f.name == 'id':
                continue
            data[f.name] = f.value_from_object(self)
        return data


class AboutMe(SingletonModel, ToDictModel):
    title = models.CharField(_('title'), max_length=255, default='Welcome!')
    image = FileBrowseField(_('image'), extensions=['.jpg', '.png', '.jpeg'], max_length=500)
    text = models.TextField(_('text'), default='Lorem ipsum, ladies and gentlemen!')


    def __str__(self):
        return __("About Me")

    class Meta:
        verbose_name = _("about me")