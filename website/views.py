import json
from django.shortcuts import render, redirect
import os
import numpy as np
import pandas as pd
from .models import OPALS
from .forms import Page1Form, Page2Form, Page3Form, Page4Form

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def page1(request):
    if request.method == 'POST':
        form = Page1Form(request.POST)
        if form.is_valid():
            # Save the form data to the database
            request.session['first_name'] = form.cleaned_data['first_name']
            request.session['last_name'] = form.cleaned_data['last_name']
            request.session['email'] = form.cleaned_data['email']
            request.session['address'] = form.cleaned_data['address']
            request.session['city'] = form.cleaned_data['city']
            request.session['state'] = form.cleaned_data['state']
            request.session['zip_code'] = form.cleaned_data['zip_code']
            request.session['age_groups'] = form.cleaned_data['age_groups']
            print(request.session['age_groups'])
            return redirect('page2')  # Redirect to the next page after saving
        
        else:
            print(form.errors)
    else:
        form = Page1Form()
    return render(request, 'page1.html', {'form': form})

def page2(request):
    if request.method == 'POST':
        form = Page2Form(request.POST)
        if form.is_valid():
            request.session['question1'] = form.cleaned_data['question1']
            request.session['question2'] = form.cleaned_data['question2']
            request.session['question3'] = form.cleaned_data['question3']
            request.session['question4'] = form.cleaned_data['question4']
            request.session['question5'] = form.cleaned_data['question5']
            request.session['question6'] = form.cleaned_data['question6']
            request.session['question7'] = form.cleaned_data['question7']
            request.session['question8'] = form.cleaned_data['question8']
            request.session['question9'] = form.cleaned_data['question9']
            request.session['question10'] = form.cleaned_data['question10']
            request.session['question11'] = form.cleaned_data['question11']
            request.session['question12'] = form.cleaned_data['question12']

            print(request.session['question1'])
            
            return redirect('page3')  # Redirect to the next page after saving
        else:
            print(form.errors)
    else:
        form = Page2Form()
    return render(request, 'page2.html', {'form': form})

def page3(request):
    if request.method == 'POST':
        form = Page3Form(request.POST)
        if form.is_valid():
            # Save form data to session
            request.session['question13'] = form.cleaned_data['question13']
            request.session['question14'] = form.cleaned_data['question14']
            request.session['question15'] = form.cleaned_data['question15']
            request.session['question16'] = form.cleaned_data['question16']
            request.session['question17'] = form.cleaned_data['question17']
            request.session['question18'] = form.cleaned_data['question18']

            return redirect('page4')  # Redirect to a thank you page
        else:
            print(form.errors)  # For debugging
    else:
        form = Page3Form()
    
    return render(request, 'page3.html', {'form': form})

def page4(request):
    if request.method == 'POST':
        form = Page4Form(request.POST)
        if form.is_valid():
            # Save form data to session
            request.session['breast_feeding'] = form.cleaned_data['breast_feeding']
            request.session['indoor_outdoor_transition1'] = form.cleaned_data['indoor_outdoor_transition1']
            request.session['deck1'] = form.cleaned_data['deck1']
            request.session['diaper_changing_station'] = form.cleaned_data['diaper_changing_station']
            request.session['gathering_setting1'] = form.cleaned_data['gathering_setting1']
            request.session['grove_trees1'] = form.cleaned_data['grove_trees1']
            request.session['mound1'] = form.cleaned_data['mound1']
            request.session['manufactured_play1'] = form.cleaned_data['manufactured_play1']
            request.session['multipurpose_lawn1'] = form.cleaned_data['multipurpose_lawn1']
            request.session['multisensory_pathway1'] = form.cleaned_data['multisensory_pathway1']
            request.session['multisensory_setting1'] = form.cleaned_data['multisensory_setting1']
            request.session['music_play1'] = form.cleaned_data['music_play1']
            request.session['playhouse1'] = form.cleaned_data['playhouse1']
            request.session['pollinator_garden1'] = form.cleaned_data['pollinator_garden1']
            request.session['porch_swing1'] = form.cleaned_data['porch_swing1']
            request.session['primary_pathway1'] = form.cleaned_data['primary_pathway1']
            request.session['ramp1'] = form.cleaned_data['ramp1']
            request.session['sand_play1'] = form.cleaned_data['sand_play1']
            request.session['small_bridge'] = form.cleaned_data['small_bridge']
            request.session['steppingstone_pathway1'] = form.cleaned_data['steppingstone_pathway1']
            request.session['tent_structures1'] = form.cleaned_data['tent_structures1']
            request.session['textured_panel'] = form.cleaned_data['textured_panel']
            request.session['water_play_hands_1'] = form.cleaned_data['water_play_hands_1']
            request.session['other1'] = form.cleaned_data['other1']
            
            # Infants total settings radio
            # request.session['question19'] = form.cleaned_data['question19']
            
            # Toddlers settings checkboxes
            request.session['area_pets1'] = form.cleaned_data['area_pets1']
            request.session['indoor_outdoor_transition2'] = form.cleaned_data['indoor_outdoor_transition2']
            request.session['cozy_nook1'] = form.cleaned_data['cozy_nook1']
            request.session['balance_beam1'] = form.cleaned_data['balance_beam1']
            request.session['bridge1'] = form.cleaned_data['bridge1']
            request.session['deck2'] = form.cleaned_data['deck2']
            request.session['earth_play1'] = form.cleaned_data['earth_play1']
            request.session['editable_landscape1'] = form.cleaned_data['editable_landscape1']
            request.session['fruit_garden1'] = form.cleaned_data['fruit_garden1']
            request.session['gathering_setting2'] = form.cleaned_data['gathering_setting2']
            request.session['grove_trees2'] = form.cleaned_data['grove_trees2']
            request.session['hard_surface1'] = form.cleaned_data['hard_surface1']
            request.session['loose_parts1'] = form.cleaned_data['loose_parts1']
            request.session['manufactured_play2'] = form.cleaned_data['manufactured_play2']
            request.session['mound2'] = form.cleaned_data['mound2']
            request.session['multipurpose_lawn2'] = form.cleaned_data['multipurpose_lawn2']
            request.session['multisensory_pathway2'] = form.cleaned_data['multisensory_pathway2']
            request.session['multisensory_setting2'] = form.cleaned_data['multisensory_setting2']
            request.session['music_play2'] = form.cleaned_data['music_play2']
            request.session['outdoor_classroom1'] = form.cleaned_data['outdoor_classroom1']
            request.session['playhouse2'] = form.cleaned_data['playhouse2']
            request.session['pollinator_garden2'] = form.cleaned_data['pollinator_garden2']
            request.session['porch_swing2'] = form.cleaned_data['porch_swing2']
            request.session['primary_pathway2'] = form.cleaned_data['primary_pathway2']
            request.session['project_space'] = form.cleaned_data['project_space']
            request.session['ramp2'] = form.cleaned_data['ramp2']
            request.session['sand_play2'] = form.cleaned_data['sand_play2']
            request.session['steppingstone_pathway2'] = form.cleaned_data['steppingstone_pathway2']
            request.session['swing1'] = form.cleaned_data['swing1']
            request.session['table1'] = form.cleaned_data['table1']
            request.session['tent_structures2'] = form.cleaned_data['tent_structures2']
            request.session['water_play_hands_2'] = form.cleaned_data['water_play_hands_2']
            request.session['water_play_body_1'] = form.cleaned_data['water_play_body_1']
            request.session['other2'] = form.cleaned_data['other2']
            
            # Toddlers total settings radio
            # request.session['question20'] = form.cleaned_data['question20']
            
            # Preschool settings checkboxes
            request.session['area_pets2'] = form.cleaned_data['area_pets2']
            request.session['balance_beam'] = form.cleaned_data['balance_beam']
            request.session['bridge2'] = form.cleaned_data['bridge2']
            request.session['indoor_outdoor_transition3'] = form.cleaned_data['indoor_outdoor_transition3']
            request.session['cozy_nook2'] = form.cleaned_data['cozy_nook2']
            request.session['deck3'] = form.cleaned_data['deck3']
            request.session['dry_creek_bed'] = form.cleaned_data['dry_creek_bed']
            request.session['earth_play2'] = form.cleaned_data['earth_play2']
            request.session['editable_landscape2'] = form.cleaned_data['editable_landscape2']
            request.session['fruit_garden2'] = form.cleaned_data['fruit_garden2']
            request.session['gathering_setting3'] = form.cleaned_data['gathering_setting3']
            request.session['grass_maze'] = form.cleaned_data['grass_maze']
            request.session['grove_trees3'] = form.cleaned_data['grove_trees3']
            request.session['hard_surface2'] = form.cleaned_data['hard_surface2']
            request.session['loose_parts2'] = form.cleaned_data['loose_parts2']
            request.session['manufactured_play3'] = form.cleaned_data['manufactured_play3']
            request.session['mound3'] = form.cleaned_data['mound3']
            request.session['multipurpose_lawn3'] = form.cleaned_data['multipurpose_lawn3']
            request.session['multisensory_pathway3'] = form.cleaned_data['multisensory_pathway3']
            request.session['multisensory_setting3'] = form.cleaned_data['multisensory_setting3']
            request.session['music_play3'] = form.cleaned_data['music_play3']
            request.session['natural_construction_area'] = form.cleaned_data['natural_construction_area']
            request.session['outdoor_classroom2'] = form.cleaned_data['outdoor_classroom2']
            request.session['performance_space'] = form.cleaned_data['performance_space']
            request.session['playhouse3'] = form.cleaned_data['playhouse3']
            request.session['pollinator_garden3'] = form.cleaned_data['pollinator_garden3']
            request.session['primary_pathway3'] = form.cleaned_data['primary_pathway3']
            request.session['project_space2'] = form.cleaned_data['project_space2']
            request.session['ramp3'] = form.cleaned_data['ramp3']
            request.session['sand_play3'] = form.cleaned_data['sand_play3']
            request.session['steppingstone_pathway3'] = form.cleaned_data['steppingstone_pathway3']
            request.session['swing2'] = form.cleaned_data['swing2']
            request.session['table2'] = form.cleaned_data['table2']
            request.session['tent_structures3'] = form.cleaned_data['tent_structures3']
            request.session['water_play_hands_3'] = form.cleaned_data['water_play_hands_3']
            request.session['water_play_body_2'] = form.cleaned_data['water_play_body_2']
            request.session['woodwork_bench'] = form.cleaned_data['woodwork_bench']
            request.session['other3'] = form.cleaned_data['other3']
            
            # Preschool total settings radio
            # request.session['question21'] = form.cleaned_data['question21']

            infant_settings = json.loads(request.POST.get('infant_settings_data', '[]'))
            toddler_settings = json.loads(request.POST.get('toddler_settings_data', '[]'))
            preschool_settings = json.loads(request.POST.get('preschool_settings_data', '[]'))
            
            # Log or use the data
            print(f"Infant Settings ({len(infant_settings)}): {infant_settings}")
            print(f"Toddler Settings ({len(toddler_settings)}): {toddler_settings}")
            print(f"Preschool Settings ({len(preschool_settings)}): {preschool_settings}")

            request.session['infant_settings'] = infant_settings
            request.session['toddler_settings'] = toddler_settings
            request.session['preschool_settings'] = preschool_settings
            

            return redirect('page4')
        else:
            print(form.errors)
    else:
        form = Page4Form()
    return render(request, 'page4.html', {'form': form})