from django.conf.urls import url
from intelliwineApp import views, vector_views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^bottles_dna_list/$', views.bottle_dna_list),
    url(r'bottle_dna_detail/(?P<pk>[0-9]+)', views.bottle_dna_detail),
    url(r'bottles_vector_list/$', vector_views.bottle_vector_list),
    url(r'bottle_vector_detail/(?P<pk>[0-9]+)', vector_views.bottle_vector_detail),
    url(r'compute_similarity/', vector_views.compute_similarity)
]

urlpatterns = format_suffix_patterns(urlpatterns)
