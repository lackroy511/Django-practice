from pytils.translit import slugify


class SlugifyMixin:
    
    def form_valid(self, form):

        if form.is_valid():
            new_entry = form.save()
            new_entry.slug = slugify(new_entry.header)
            new_entry = form.save()

        return super().form_valid(form)