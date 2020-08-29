from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationFrom, motorpartform,motorelementform
from django.contrib import messages
from django.views.generic import TemplateView
from .models import motor_element, motor_part, motor_plate, motor_type, fix_history, new_elements
from django.utils import timezone




#functions here
def history_check_plate(plate):
    history_list = fix_history.objects.filter(motor_plate=plate).order_by('-create')
    history_check = []
    history_all = []
    for a in history_list:
        if a.element_name in history_check:
            pass
        else:
            history_all.append(a)
            history_check.append(a.element_name)
    return history_check, history_all
def all_elements_base(type):
    typematch = motor_type.objects.get(type_title=type)
    list = motor_part.objects.filter(motor_type__in=[typematch]).distinct()
    elements_list = motor_element.objects.filter(motor_part__in=list[::1])
    return elements_list

def addnewmotor(platenumber, miles, type, user):
    newone = motor_plate()
    newone.plate = platenumber
    newone.miles = miles
    newone.type = type
    if user == 'AnonymousUser':
        newone.save()
    else:
        newone.user = user
        newone.save()


class page_status():
    def __init__(self, context_status):
        self.context_status = context_status



# Create your views here.
class home(TemplateView):
    template_name = 'base.html'
    ## forms here##
    form = RegistrationFrom()
    context_status = page_status('status')
    ##get action here##
    def get(self, request, *args, **kwargs):
        self.context_status.context_status = {'userform': self.form,
                                              'plate_search': 'none',
                                              }
        return render(request, self.template_name, self.context_status.context_status)

    ##post action##
    def post(self, request, *args, **kwargs):

        if 'add_element' in request.POST:
            plate = request.POST.get('add_element')
            platematch = motor_plate.objects.get(plate=plate)
            element_name = request.POST.get('element_name')
            elements_list = all_elements_base(platematch.type).values_list('element_name', flat=True)
            new_elements_list = new_elements.objects.filter(motor_plate=platematch).values_list('element_name', flat=True)
            if element_name in elements_list or element_name == '' or element_name in new_elements_list:
                print('repeat error')
            else:
                new_element = new_elements(element_name=element_name)
                new_element.save()
                platematch.new_elements.add(new_element)
            sub_data = new_elements.objects.filter(motor_plate=platematch).distinct()
            context = {
                'sub_data': sub_data,
            }
            self.context_status.context_status.update(context)
            return render(request, self.template_name, self.context_status.context_status)


        if 'add_motor' in request.POST:
            type = request.POST.get('type')
            plate = request.POST.get('plate')
            miles = request.POST.get('miles')
            if miles == '':
                miles = 0
            if motor_plate.objects.filter(plate=plate).exists() or plate=='':
                context = {
                    'plate_wrong': 'wrong'
                }
                context.update(self.context_status.context_status)
                return render(request, self.template_name, context)
            else:
                if motor_type.objects.filter(type_title=type).exists():
                    insert_type = motor_type.objects.get(type_title=type)
                else:
                    insert_type = motor_type.objects.get(type_title='None')

                new_plate = motor_plate(plate=plate, type=insert_type, miles=miles)
                new_plate.save()
                return render(request, self.template_name, self.context_status.context_status)


        ##fix history
        if 'fixgistory' in request.POST:
            plate = request.POST.get('fixgistory')
            platematch = motor_plate.objects.get(plate=plate)
            history_list = fix_history.objects.filter(motor_plate=platematch).distinct().order_by('-create', 'element_name')
            timestart = history_list.values_list('create', flat=True)

            context = {
                'search_status': 'all_fix_history',
                'main_data': history_list[::1],
            }

            self.context_status.context_status.update(context)
            return render(request, self.template_name, self.context_status.context_status)

        ##fix history update
        if 'update' in request.POST:
            post_list = []
            for key in request.POST.keys():
                post_list.append(key)
            post_content = request.POST.get(post_list[1])
            plate_N = post_content.split('_')[0]
            elementname = post_content.split('_')[1]
            platematch = motor_plate.objects.get(plate=plate_N)
            if motor_element.objects.filter(element_name=elementname).exists():
                elementitem = motor_element.objects.get(element_name=elementname)
            if new_elements.objects.filter(element_name=elementname).exists():
                elementitem = new_elements.objects.get(element_name=elementname)

            fix = fix_history(plate=platematch.plate, miles=platematch.miles, element_name=elementitem.element_name, element_id=elementitem.element_id)
            fix.save()
            platematch.history.add(fix)
            history_list = history_check_plate(platematch)
            context = {
                'history': history_list[1],
                'hischeck': history_list[0]
            }
            self.context_status.context_status.update(context)
            return render(request, self.template_name, self.context_status.context_status)


        ##part of elements search
        if 'partsearch' in request.POST:
            model = request.POST.get('partsearch')
            part = motor_part.objects.filter(part_title=model)
            elements = motor_element.objects.filter(motor_part__in=part).distinct()
            context = {'search_status': 'part_elements',
                       'main_data': elements,
                       }
            self.context_status.context_status.update(context)
            if model == '自訂':
                context = {'user_setting': 'successful',
                           }
                context.update(self.context_status.context_status)
                return render(request, self.template_name, context)
            context = {}
            context.update(self.context_status.context_status)
            contextadd = {
                'sub_data': '',
            }
            context.update(contextadd)
            return render(request, self.template_name, context)

        ##checkpart successful
        if 'checkpart' in request.POST:
            type = request.POST.get('checkpart')
            typematch = motor_type.objects.get(type_title=type)
            context = { 'search_status': 'parts',
                        'main_data': typematch.type_model.all(),
                        }
            self.context_status.context_status.update(context)
            return render(request, self.template_name, self.context_status.context_status)

        ##platesearch successful
        if 'platesearch' in request.POST:
            ##search from form
            platenumber = request.POST.get('plate')
            miles = request.POST.get('miles')
            ##page change from button
            if platenumber == None:
                platenumber = request.POST.get('platesearch')
                miles = ''
            ##check plate exists or not
            if motor_plate.objects.filter(plate=platenumber).exists():
                platematch = motor_plate.objects.get(plate=platenumber)
                ##update miles
                if len(miles) != 0 and int(miles) >= 0:
                    platematch.miles=int(miles)
                    platematch.save()

                ##get all elements
                elements = all_elements_base(platematch.type)
                history_list = history_check_plate(platematch)
                ##sub_data
                sub_data = new_elements.objects.filter(motor_plate=platematch).distinct()
                self.context_status.context_status = {'userform': self.form,
                                                      'plate_search': 'none',
                                                      }
                context = {
                    'plate_search': 'successful',
                    'search_status': 'all_elements',
                    'plate': platematch,
                    'main_data': elements,
                    'sub_data': sub_data,
                    'history': history_list[1],
                    'hischeck': history_list[0],
                }
                self.context_status.context_status.update(context)
                return render(request, self.template_name, self.context_status.context_status)
            else:
                context = {
                    'no_plate': 'wrong',
                }
                self.context_status.context_status = {'userform': self.form,
                                                      'plate_search': 'none',
                                                      }
                context.update(self.context_status.context_status)
                return render(request, self.template_name, context)

##else

        ##login logout signup
        if 'login_from' in request.POST:

            context = {'btnclick': 'successful',
                       'userform': self.form,
            }
            context.update(self.context_status.context_status)
            return render(request, self.template_name,context)

        if 'logout_post' in request.POST:
            logout(request)
            return HttpResponseRedirect('/')

        if 'login_post' in request.POST:
            login_username = request.POST.get('email')
            login_password = request.POST.get('password')
            user = authenticate(username=login_username, password=login_password)

            try:
                login(request, user)
                return render(request, self.template_name, self.context_status.context_status)
            except:
                context = {
                    'login_wrong': 'wrong'
                }
                context.update(self.context_status.context_status)
                return render(request, self.template_name, context)

        if 'signup_post' in request.POST:
            if self.form.is_valid():
                self.form.save()
                username = self.form.cleaned_data['username']
                password = self.form.cleaned_data['password1']
                messages.success(request, 'Account was created for' + username)
                user = authenticate(username=username, password=password)
                login(request, user)
            else:
                context = {
                    'signup_wrong': 'wrong'
                }
                context.update(self.context_status.context_status)
                return render(request, self.template_name, context)
        return render(request, self.template_name, self.context_status.context_status)






