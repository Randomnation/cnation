from django.shortcuts import render_to_response, render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext, loader
from .forms import RegisterForm, ProfileForm
from .models import UserProfile


def main_page(request):
    css1 = 'active'
    return render_to_response('main/index.html', locals(), context_instance=RequestContext(request))


def contact_page(request):
    css4 = 'active'
    return render_to_response('main/contact.html', locals(), context_instance=RequestContext(request))


@login_required
def user_profile(request):
    user = request.user
    return render(request, 'main/profile.html', {'user': user})


@login_required
def profile_update(request, pk):
    update = get_object_or_404(UserProfile, pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=update)
        if form.is_valid():
            update = form.save(commit=False)
            update.save()
            return redirect('main:user_profile', pk=update.pk)
    else:
        form = ProfileForm()
    return render(request, 'main/profile.html', {'form': form})


def register_user(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render_to_response('main/regSuccess.html')

    template = loader.get_template('main/register.html')
    context = RequestContext(request, {'form': form,
                                       })
    return HttpResponse(template.render(context))
