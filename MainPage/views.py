from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from company.models import CompanyBranch, CompanyDescription
from django.core.exceptions import MultipleObjectsReturned



def index(request):
    """Strona główna dla aplikacji ussr."""

    maincompany = get_object_or_404(CompanyBranch, is_main=1)
    shortdescription = get_object_or_404(CompanyDescription, id_company_description = 'Witam')
    context = {'maincompany': maincompany,
                'shortdescription': shortdescription}

    return render(request, 'MainPage/index.html', context)
