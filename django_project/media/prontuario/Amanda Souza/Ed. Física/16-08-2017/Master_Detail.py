class MasterDetailCrud(Crud):
    is_m2m = False
    link_return_to_parent_field = False

    class BaseMixin(Crud.BaseMixin):

        @property
        def list_url(self):
            obj = self.crud if hasattr(self, 'crud') else self
            if not obj.ListView:
                return ''
            return self.resolve_url(ACTION_LIST, args=(self.kwargs['pk'],))

        @property
        def create_url(self):
            obj = self.crud if hasattr(self, 'crud') else self
            if not obj.CreateView:
                return ''
            return self.resolve_url(ACTION_CREATE, args=(self.kwargs['pk'],))

        @property
        def detail_url(self):
            obj = self.crud if hasattr(self, 'crud') else self
            if not obj.DetailView:
                return ''
            pkk = self.request.GET['pkk'] if 'pkk' in self.request.GET else ''
            return (super().detail_url + (('?pkk=' + pkk) if pkk else ''))

        @property
        def update_url(self):
            obj = self.crud if hasattr(self, 'crud') else self
            if not obj.UpdateView:
                return ''
            pkk = self.request.GET['pkk'] if 'pkk' in self.request.GET else ''
            return (super().update_url + (('?pkk=' + pkk) if pkk else ''))

        @property
        def delete_url(self):
            obj = self.crud if hasattr(self, 'crud') else self
            if not obj.DeleteView:
                return ''
            return super().delete_url

        def get_context_data(self, **kwargs):
            obj = self.crud if hasattr(self, 'crud') else self
            self.object = getattr(self, 'object', None)
            parent_object = None
            if self.object:
                if '__' in obj.parent_field:
                    fields = obj.parent_field.split('__')
                    parent_object = self.object
                    for field in fields:
                        parent_object = getattr(parent_object, field)
                else:
                    parent_object = getattr(self.object, obj.parent_field)

                if not isinstance(parent_object, models.Model):
                    if parent_object.count() > 1:
                        if 'pkk' not in self.request.GET:
                            raise Http404()
                        root_pk = self.request.GET['pkk']
                        parent_object = parent_object.filter(id=root_pk)

                    parent_object = parent_object.first()

                    if not parent_object:
                        raise Http404()

                root_pk = parent_object.pk
            else:
                root_pk = self.kwargs['pk'] if 'pkk' not in self.request.GET\
                    else self.request.GET['pkk']
            kwargs.setdefault('root_pk', root_pk)
            context = super(CrudBaseMixin, self).get_context_data(**kwargs)

            if parent_object:
                context['title'] = '%s <small>(%s)</small>' % (
                    self.object, parent_object)

            return context

    class ListView(Crud.ListView):
        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/%s$' % cls.model._meta.model_name

        def get_context_data(self, **kwargs):
            obj = self.crud if hasattr(self, 'crud') else self
            context = CrudListView.get_context_data(self, **kwargs)

            parent_model = None
            if '__' in obj.parent_field:
                fields = obj.parent_field.split('__')
                parent_model = pm = self.model
                for field in fields:
                    pm = getattr(pm, field)
                    if isinstance(pm.field, ForeignKey):
                        parent_model = getattr(
                            parent_model, field).field.related_model
                    else:
                        parent_model = getattr(
                            parent_model, field).rel.related_model
                    pm = parent_model

            else:
                parent_model = getattr(
                    self.model, obj.parent_field).field.related_model

            params = {'pk': kwargs['root_pk']}

            if self.container_field:
                container = self.container_field.split('__')
                if len(container) > 1:
                    params['__'.join(container[1:])] = self.request.user.pk

            try:
                parent_object = parent_model.objects.get(**params)
            except:
                raise Http404()

            context[
                'title'] = '%s <small>(%s)</small>' % (
                context['title'], parent_object)
            return context

        def get_queryset(self):
            obj = self.crud if hasattr(self, 'crud') else self
            qs = super().get_queryset()

            kwargs = {obj.parent_field: self.kwargs['pk']}

            """if self.container_field:
                kwargs[self.container_field] = self.request.user.pk"""

            return qs.filter(**kwargs)

    class CreateView(Crud.CreateView):

        @classmethod
        def get_url_regex(cls):
            return r'^(?P<pk>\d+)/%s/create$' % cls.model._meta.model_name

        def get_form(self, form_class=None):
            obj = self.crud if hasattr(self, 'crud') else self
            form = super(MasterDetailCrud.CreateView, self).get_form(
                self.form_class)
            parent_field = obj.parent_field.split('__')
            if not obj.is_m2m or len(parent_field) > 1:
                field = self.model._meta.get_field(parent_field[0])
                try:
                    parent = field.related_model.objects.get(
                        pk=self.kwargs['pk'])
                except ObjectDoesNotExist:
                    raise Http404()
                setattr(form.instance, parent_field[0], parent)
            return form

        def get_context_data(self, **kwargs):
            obj = self.crud if hasattr(self, 'crud') else self
            context = Crud.CreateView.get_context_data(
                self, **kwargs)

            params = {'pk': self.kwargs['pk']}

            if self.container_field:
                # FIXME refatorar para parent_field com '__'
                parent_model = getattr(
                    self.model, obj.parent_field).field.related_model

                container = self.container_field.split('__')
                if len(container) > 1:
                    params['__'.join(container[1:])] = self.request.user.pk

                try:
                    parent_object = parent_model.objects.get(**params)
                except Exception:
                    raise Http404()
            else:
                parent_model = self.model
                parent_object = None
                if '__' in obj.parent_field:
                    fields = obj.parent_field.split('__')
                    for field in fields:
                        if parent_model == self.model:
                            parent_model = getattr(
                                parent_model, field).field.related_model
                            parent_object = parent_model.objects.get(**params)
                        else:
                            parent_object = getattr(parent_object, field)

                else:
                    parent_model = getattr(
                        parent_model, obj.parent_field).field.related_model
                    parent_object = parent_model.objects.get(**params)

                context['root_pk'] = parent_object.pk

            if parent_object:
                context['title'] = '%s <small>(%s)</small>' % (
                    context['title'], parent_object)

            return context

        @property
        def cancel_url(self):
            if self.list_url:
                return self.list_url
            obj = self.crud if hasattr(self, 'crud') else self

            params = {'pk': self.kwargs['pk']}

            parent_model = self.model
            parent_object = None
            if '__' in obj.parent_field:
                fields = obj.parent_field.split('__')
                for field in fields:
                    if parent_model == self.model:
                        parent_model = getattr(
                            parent_model, field).field.related_model
                        parent_object = parent_model.objects.get(**params)
                    else:
                        parent_object = getattr(parent_object, field)
                    break

            else:
                parent_model = getattr(
                    parent_model, obj.parent_field).field.related_model
                parent_object = parent_model.objects.get(**params)

            return reverse(
                '%s:%s' % (parent_model._meta.app_config.name,
                           '%s_%s' % (
                               parent_model._meta.model_name,
                               ACTION_DETAIL)),
                kwargs={'pk': parent_object.pk})

    class UpdateView(Crud.UpdateView):

        @classmethod
        def get_url_regex(cls):
            return r'^%s/(?P<pk>\d+)/edit$' % cls.model._meta.model_name

    class DeleteView(Crud.DeleteView):

        @classmethod
        def get_url_regex(cls):
            return r'^%s/(?P<pk>\d+)/delete$' % cls.model._meta.model_name

        def get_success_url(self):
            obj = self.crud if hasattr(self, 'crud') else self
            if '__' in obj.parent_field:
                fields = obj.parent_field.split('__')
                parent_object = self.object
                for field in fields:
                    parent_object = getattr(parent_object, field)
                    break
            else:
                parent_object = getattr(self.object, obj.parent_field)
            if not isinstance(parent_object, models.Model):
                if parent_object.count() > 1:
                    if 'pkk' not in self.request.GET:
                        raise Http404
                    root_pk = self.request.GET['pkk']
                    parent_object = parent_object.filter(id=root_pk)

                parent_object = parent_object.first()

                if not parent_object:
                    raise Http404
            root_pk = parent_object.pk

            pk = root_pk

            if obj.is_m2m:
                namespace = parent_object._meta.app_config.name
                return reverse('%s:%s' % (
                    namespace,
                    '%s_%s' % (parent_object._meta.model_name, ACTION_DETAIL)),
                    args=(pk,))
            else:
                return self.resolve_url(ACTION_LIST, args=(pk,))

    class DetailView(Crud.DetailView):
        template_name = 'crud/detail_detail.html'

        @classmethod
        def get_url_regex(cls):
            return r'^%s/(?P<pk>\d+)$' % cls.model._meta.model_name

        @property
        def detail_list_url(self):
            obj = self.crud if hasattr(self, 'crud') else self

            if not obj.ListView:
                return ''

            if '__' in obj.parent_field:
                fields = obj.parent_field.split('__')
                parent_object = self.object
                for field in fields:
                    parent_object = getattr(parent_object, field)
            else:
                parent_object = getattr(self.object, obj.parent_field)

            if not isinstance(parent_object, models.Model):
                if parent_object.count() > 1:
                    if 'pkk' not in self.request.GET:
                        raise Http404
                    root_pk = self.request.GET['pkk']
                    parent_object = parent_object.filter(id=root_pk)

                parent_object = parent_object.first()

                if not parent_object:
                    raise Http404
            root_pk = parent_object.pk

            pk = root_pk
            return self.resolve_url(ACTION_LIST, args=(pk,))

        @property
        def detail_create_url(self):
            obj = self.crud if hasattr(self, 'crud') else self
            if not obj.CreateView:
                return ''

            if not isinstance(parent_object, models.Model):
                if parent_object.count() > 1:
                    if 'pkk' not in self.request.GET:
                        raise Http404
                    root_pk = self.request.GET['pkk']
                    parent_object = parent_object.filter(id=root_pk)

                parent_object = parent_object.first()

                if not parent_object:
                    raise Http404
            root_pk = parent_object.pk

            url = self.resolve_url(ACTION_CREATE, args=(root_pk,))
            if not obj.is_m2m:
                return url
            else:
                if '__' in obj.parent_field:
                    fields = obj.parent_field.split('__')
                    parent_object = self.object
                    for field in fields:
                        parent_object = getattr(parent_object, field)
                else:
                    parent_object = getattr(self.object, obj.parent_field)

                return url + '?pkk=' + str(parent_object.pk)

        @property
        def detail_set_create_url(self):
            obj = self.crud if hasattr(self, 'crud') else self

            root_pk = self.object.pk
            pk = root_pk

            url = self.resolve_url_set(ACTION_CREATE, args=(pk,))
            if not obj.is_m2m:
                return url
            else:
                if '__' in obj.parent_field:
                    fields = obj.parent_field.split('__')
                    parent_object = self.object
                    for field in fields:
                        parent_object = getattr(parent_object, field)
                else:
                    parent_object = getattr(self.object, obj.parent_field)

                return url + '?pkk=' + str(parent_object.pk)

        @property
        def detail_root_detail_url(self):
            obj = self.crud if hasattr(self, 'crud') else self
            if not obj.link_return_to_parent_field:
                return ''
            if hasattr(obj, 'parent_field'):
                parent_field = obj.parent_field.split('__')
                if not obj.is_m2m or len(parent_field) > 1:
                    # field = self.model._meta.get_field(parent_field[0])

                    if isinstance(getattr(
                            self.object, parent_field[0]), models.Model):
                        parent_object = getattr(self.object, parent_field[0])

                        root_pk = parent_object.pk
                        pk = root_pk

                        namespace = parent_object._meta.app_config.name
                        return reverse('%s:%s' % (
                            namespace,
                            '%s_%s' % (parent_object._meta.model_name,
                                       ACTION_DETAIL)),
                                       args=(pk,))
            return ''

        @property
        def detail_root_detail_verbose_name(self):
            obj = self.crud if hasattr(self, 'crud') else self
            if hasattr(obj, 'parent_field'):
                parent_field = obj.parent_field.split('__')
                if not obj.is_m2m or len(parent_field) > 1:
                    field = self.model._meta.get_field(parent_field[0])

                    return field.verbose_name
            return ''
