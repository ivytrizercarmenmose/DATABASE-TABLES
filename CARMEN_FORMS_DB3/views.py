from .forms import members_Reg


def members(request):
    submit_button = request.POST.get("members")
    name = ''
    age = ''
    phone = ''
    city = ''
    country = ''

    reg_members_form = members_Reg(request.POST or None)
    if reg_members_form.is_valid():
        name = reg_members_form.cleaned_data.get("name")
        age = reg_members_form.cleaned_data.get("age")
        phone = reg_members_form.cleaned_data.get("phone")
        city = reg_members_form.cleaned_data.get("city")
        country = reg_members_form.cleaned_data.get("country")

    context = {'reg_members_form': reg_members_form,
               'name': name,
               'age': age,
               'phone': phone,
               'city': city,
               'country': country,
               'submit_button': submit_button}
    return render(request, 'login.html', context)
