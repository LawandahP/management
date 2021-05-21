from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from rest_framework.generics import get_object_or_404
from unit.models import Unit
from users.forms import CustomUserRegisterForm, CustomUserUpdateForm, UserUpdateForm, ProfileUpdateForm
from .decorators import unauthenticated_user, allowed_users
from .models import CustomUser
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from PyPDF2 import PdfFileWriter, PdfFileReader


@unauthenticated_user
def registerPage(request):
    form = CustomUserRegisterForm()
    if request.method == 'POST':
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, you have been added to the system. You can now Login.')
            return redirect('login')
    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required(login_url='login')
@allowed_users
def addTenant(request):
    form = CustomUserRegisterForm()
    if request.method == 'POST':
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Tenant successfully registered.')
            return redirect('add-tenant')
    context = {'form': form}
    return render(request, 'users/add_user.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'You have logged in successfully')
            return redirect('dashboard')
        else:
            messages.info(request, f'INCORRECT username and or Password')
    context = {}
    return render(request, 'users/login.html', context)


@login_required(login_url='login')
def profile(request):
    units = request.user.takenTenants.all()
    bills = request.user.my_bills.all()
    context = {'units': units, 'bills': bills}
    return render(request, 'users/profile.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users
def list_users(request):
    context = {
        'users': CustomUser.objects.all().order_by('-date_joined')
    }
    return render(request, 'users/user_list.html', context)


@login_required(login_url='login')
@allowed_users
def user_detail_view(request, pk):
    tenant = get_object_or_404(CustomUser, pk=pk)
    # bills = tenant.my_bills.all()
    units = tenant.takenTenants.all()
    context = {'tenant': tenant, 'units': units}
    return render(request, 'users/user_detail.html', context)

    # landlord = get_object_or_404(Landlord, pk=pk)
    # apartments = landlord.owner.all()
    # apartments_count = apartments.count()
    # context = {'landlord': landlord, 'apartments': apartments,
    #            'apartments_count': apartments_count}
    # return render(request, 'landlord/landlord_detail.html', context)


@login_required(login_url='login')
@allowed_users
def user_update_view(request, pk):
    obj = get_object_or_404(CustomUser, pk=pk)
    form = CustomUserUpdateForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, f'Tenant {obj.First_Name} {obj.Middle_Name}\'s info has been UPDATED Successfully')
        return redirect('list-user')
    else:
        return render(request, 'users/user_update.html', {'form': form})


@login_required(login_url='login')
@allowed_users
def user_delete_view(request, pk):
    object = get_object_or_404(CustomUser, pk=pk)
    context = {'object': object}
    if request.method == "POST":
        object.delete()
        messages.success(request, f'Tenant Deleted Successfully')
        return redirect("list-user")
    return render(request, "users/user_delete.html", context)


@login_required(login_url='login')
def update_Profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has UPDATED successfully.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
    return render(request, 'users/profile_update.html', context)


# def generate_lease(request, pk):
#     tenant = get_object_or_404(CustomUser, pk=pk)
#     units = tenant.takenTenants.all()
#     context = {'tenant': tenant, 'units': units}
#     return render(request, 'users/lease_agreement.html', context)
#
#
# @login_required(login_url='login')
# @allowed_users
# def generate_lease_pdf(template_src, context_dict={}):
#     template = get_template(template_src)
#     html = template.render(context_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     return None
#
#
# @login_required(login_url='login')
# @allowed_users
# def generate_pdf(request, pk, *args, **kwargs):
#     template = get_template('users/lease_agreement.html')
#     tenant = get_object_or_404(CustomUser, pk=pk)
#     units = tenant.takenTenants.all()
#     context = {
#         'tenant': tenant,
#         'units': units
#     }
#     html = template.render(request, context)
#     return HttpResponse(html)
#
#
# @login_required(login_url='login')
# @allowed_users
# class DownloadLeasePDF(View):
#     def get(self, request, *args, **kwargs):
#         pdf = generate_lease_pdf('users/lease_agreement.html', data)
#         response = HttpResponse(pdf, content_type='lease/pdf')
#         filename = "lease.pdf" % ("54634")
#         content = "attachment; filename='%s'" % (filename)
#         response['Content-Disposition'] = content
#         return response

def generate_lease_pdf(request, pk):
    tenant = get_object_or_404(CustomUser, pk=pk)
    units = tenant.takenTenants.all()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; attachment; filename={tenant} Lease.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    context = {
        'tenant': tenant,
        'units': units
    }
    html_string = render_to_string('users/lease_agreement.html', context)
    html = HTML(string=html_string)
    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()

        output = open(output.name, 'rb')
        response.write(output.read())
    return response


def create_watermark(input_pdf, output, watermark):
    watermark_obj = PdfFileReader(watermark)
    watermark_page = watermark_obj.getPage(0)

    pdf_reader = PdfFileReader(input_pdf)
    pdf_writer = PdfFileWriter()

    for page in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)
        with open(output, 'wb') as out:
            pdf_writer.write(out)

    if __name__ == '__main__':
        create_watermark(
            input_pdf='Jupyter_Notebook_An_Introduction.pdf',
            output='watermarked_notebook.pdf',
            watermark='watermark.pdf')
