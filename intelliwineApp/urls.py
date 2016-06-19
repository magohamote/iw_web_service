from django.conf.urls import url
from intelliwineApp import views, bottle_views, vector_views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^bottles_dna_list/$', bottle_views.bottle_dna_list),
    url(r'bottle_dna_detail/(?P<pk>[0-9]+)', bottle_views.bottle_dna_detail),
    url(r'bottle_charac_vector_list/$', vector_views.bottle_charac_vector_list),
    url(r'bottle_vector_detail/(?P<pk>[0-9]+)', vector_views.bottle_vector_detail),
    url(r'compute_similarity/', vector_views.compute_similarity),
    url(r'post_bottle/', vector_views.post_bottle),
]

urlpatterns = format_suffix_patterns(urlpatterns)
