from django.shortcuts import render
from django.contrib.auth.models import User, auth
from EQuiz.models import Organisation,AdminUser
from datetime import datetime
from django.db import connection
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        AUsername = request.POST['AUsername']
        AMobile = request.POST['AMobile']
        AEmail = request.POST['AEmail']
        AAddress = request.POST['AAddress']
        APassword = request.POST['APassword']
        AOrganisation = request.POST['AOrganisation']
        new_admin = AdminUser()
        new_admin.name = AUsername
        new_admin.password = APassword
        new_admin.address = AAddress
        new_admin.organisationid = Organisation.objects.get(pk=AOrganisation)
        new_admin.country = "India"
        new_admin.createdon = datetime.now()
        new_admin.creationmode = "Website"
        new_admin.email = AEmail
        new_admin.mobile = AMobile
        new_admin.save()
        print(AUsername, " created ")
        return render(request, 'Users/successful_register.html', {'Account': AUsername,})
    else:
        Organisation_list = Organisation.objects.all().order_by('name')
        return render(request, 'Users/register.html', {'OrgList': Organisation_list, })

def organisation_register(request):
    if request.method == 'POST':
        new_org = Organisation()
        new_org.name = request.POST['OrgName']
        new_org.address = request.POST['OrgAddress']
        new_org.representative = request.POST['OrgRepresentative']
        new_org.mobile = request.POST['OrgMobile']
        new_org.email = request.POST['OrgEmail']
        new_org.type = request.POST['OrgType']
        new_org.creationmode = 'Website'
        new_org.createdon = datetime.now()
        new_org.save()    
        return render(request, 'Users/successful_register.html', {'Account': new_org.name, })
    else:
        return render(request, 'Users/organisation_register.html', {})

def admin_sigin(request):
    if request.method == 'POST':
        try:
            with connection.cursor() as cursor:
                cursor.execute("select EQuizDB.ValidateAdmin(%s, %s);", [
                            request.POST['UName'], request.POST['UPassword']])
                row = cursor.fetchone()
                if row[0] == 1:
                    request.session['name'] = request.POST['UName']
                    request.session['password'] = request.POST['UPassword']
                    print('Successful Login for ', request.POST['UName'])
                    return redirect('login_success')
                else:
                    print('Login Unsuccesssful')
                    return render(request, 'Users/admin_sign_in.html', {'Name': request.POST['UName'], 'Error': '<strong><i class=\'fas fa-exclamation-triangle\'></i> &nbsp;Password doesn\'t match</strong><br> Please check the Admin name and Password '})
        except Exception as e:
            return render(request, 'Users/admin_sign_in.html', {'Name': request.POST['UName'], 'Error': 'Oops, Unexpected Error Occured, Try Agian...', 'Exception': e, })
    else:
        return render(request, 'Users/admin_sign_in.html', {})

def login_success(request):
    return render(request, 'Users/successful_login.html', {'name': request.session['name'],})

def logout(request):
    request.session['name'] = None
    request.session['password'] = None
    return redirect('/EQuiz/')
