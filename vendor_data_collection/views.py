from django.shortcuts import render
from . import forms
from django.http import HttpResponseRedirect, HttpResponse

FORM_DATA={
    'name':'',
    'phone':'',
    'availability':'',
    'vendor_type':'',
    'paytm':'',
    'lat':[],
    'long':[],
    'pin':[],
    'start_hour':[],
    'start_min':[],
    'start_type':[],
    'end_hour':[],
    'end_min':[],
    'end_type':[],
    'hygeine_rating':[],
    'taste_rating':[]
}

# Create your views here.
def add_vendor_p1(request):
    add_vendor_form=forms.add_vendor_form_p1()

    if request.method=='POST':
        add_vendor_form=forms.add_vendor_form_p1(request.POST)
        if add_vendor_form.is_valid():
            FORM_DATA['name']=add_vendor_form.data.__getitem__('name')
            FORM_DATA['phone']=add_vendor_form.data.__getitem__('phone')
            FORM_DATA['availability']=add_vendor_form.data.__getitem__('availability')
            FORM_DATA['vendor_type']=add_vendor_form.data.__getitem__('vendor_type')
            FORM_DATA['paytm']=add_vendor_form.paytm_available = request.POST.get('paytm_available', 'off')
            return HttpResponseRedirect('/vendor_data/add/p2/')

    return render(request,'vendor_data/add.html',{'form':add_vendor_form})

def add_vendor_p2(request):
    add_vendor_locations_form=forms.add_vendor_form_p2()

    if request.method=='POST':
        add_vendor_locations_form=forms.add_vendor_form_p2(request.POST)

        if add_vendor_locations_form.is_valid():
            for i in range(10):
                lat_name='Latitude'+str(i)
                long_name='Longitude'+str(i)
                pin_name='Pin'+str(i)
                start_hour_name='StartHour'+str(i)
                start_minute_name='StartMinute'+str(i)
                start_type_name='StartType'+str(i)
                end_hour_name='EndHour'+str(i)
                end_minute_name='EndMinute'+str(i)
                end_type_name='EndType'+str(i)

                data={}
                data['lat']=add_vendor_locations_form.data.__getitem__(lat_name)
                data['long']=add_vendor_locations_form.data.__getitem__(long_name)
                data['pin']=add_vendor_locations_form.data.__getitem__(pin_name)
                data['start_hour']=add_vendor_locations_form.data.__getitem__(start_hour_name)
                data['start_min']=add_vendor_locations_form.data.__getitem__(start_minute_name)
                data['start_type']=add_vendor_locations_form.data.__getitem__(start_type_name)
                data['end_hour']=add_vendor_locations_form.data.__getitem__(end_hour_name)
                data['end_min']=add_vendor_locations_form.data.__getitem__(end_minute_name)
                data['end_type']=add_vendor_locations_form.data.__getitem__(end_type_name)

                if data['lat']!='' and data['long']!='' and data['pin']!='':
                    FORM_DATA['lat'].append(data['lat'])
                    FORM_DATA['long'].append(data['long'])
                    FORM_DATA['pin'].append(data['pin'])
                    FORM_DATA['start_hour'].append(data['start_hour'])
                    FORM_DATA['start_min'].append(data['start_min'])
                    FORM_DATA['start_type'].append(data['start_type'])
                    FORM_DATA['end_hour'].append(data['end_hour'])
                    FORM_DATA['end_min'].append(data['end_min'])
                    FORM_DATA['end_type'].append(data['end_type'])
            if FORM_DATA['vendor_type']=='street-food' or FORM_DATA['vendor_type']=='drinks':
                return HttpResponseRedirect('/vendor_data/add/p3/')
            else:
                return HttpResponseRedirect('/vendor_data/add/p4')

    return render(request,'vendor_data/add_location.html',{'form':add_vendor_locations_form})

def add_vendor_p3(request):

    add_rating_form=forms.add_vendor_form_p3()

    if request.method=='POST':
        add_rating_form=forms.add_vendor_form_p3(request.POST)
        if(add_rating_form.is_valid()):
            FORM_DATA['hygeine_rating']=add_rating_form.data.__getitem__('hygeine_rating')
            FORM_DATA['taste_rating']=add_rating_form.data.__getitem__('taste_rating')

            return HttpResponseRedirect('/vendor_data/add/p4/')


    return render(request,'vendor_data/add_rating.html',{'form':add_rating_form})


def add_vendor_p4(request):
    return render(request,'vendor_data/add_menu.html')