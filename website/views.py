import json
from django.shortcuts import render, redirect
import os
import numpy as np
import pandas as pd
from .models import OPALS
from .forms import Page1Form, Page2Form, Page3Form, Page4Form, Page5Form, Page6Form

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
            request.session['age_groups'] = form.cleaned_data['age_groups'] #used throughout the form for confitional rendering
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

            #comes from script in page4.html
            infant_settings = json.loads(request.POST.get('infant_settings_data', '[]'))
            toddler_settings = json.loads(request.POST.get('toddler_settings_data', '[]'))
            preschool_settings = json.loads(request.POST.get('preschool_settings_data', '[]'))
            
            # Log or use the data
            print(f"Infant Settings ({len(infant_settings)}): {infant_settings}")
            print(f"Toddler Settings ({len(toddler_settings)}): {toddler_settings}")
            print(f"Preschool Settings ({len(preschool_settings)}): {preschool_settings}")

            if len(infant_settings) >= 0 and len(infant_settings)<=1:
                question19 = 1
            elif len(infant_settings) >= 2 and len(infant_settings)<=4:
                question19 = 2
            elif len(infant_settings) >= 5 and len(infant_settings)<=7:
                question19 = 3
            elif len(infant_settings) >= 8:
                question19 = 4
            
            if len(toddler_settings) >= 0 and len(toddler_settings)<=3:
                question20 = 1
            elif len(toddler_settings) >= 4 and len(toddler_settings)<=7:
                question20 = 2
            elif len(toddler_settings) >= 8 and len(toddler_settings)<=9:
                question20 = 3
            elif len(toddler_settings) >= 10:
                question20 = 4

            if len(preschool_settings) >= 0 and len(preschool_settings)<=3:
                question21 = 1
            elif len(preschool_settings) >= 4 and len(preschool_settings)<7:
                question21 = 2
            elif len(preschool_settings) >= 8 and len(preschool_settings)<=9:
                question21 = 3
            elif len(preschool_settings) >= 10:
                question21 = 4

            request.session['question19'] = question19
            request.session['question20'] = question20
            request.session['question21'] = question21

            print(request.session['question19'])
            print(request.session['question20'])
            print(request.session['question21'])

            # request.session['question22'] = form.cleaned_data['question22']
            # request.session['question23'] = form.cleaned_data['question23']
            request.session['question24'] = form.cleaned_data['question24']
            request.session['question25'] = form.cleaned_data['question25']

            return redirect('page5')
        else:
            print(form.errors)
    else:
        form = Page4Form()
    age_groups = request.session.get('age_groups', [])
    return render(request, 'page4.html', {'form': form, 'age_groups': age_groups})


def page5(request):
    if request.method == 'POST':
        form = Page5Form(request.POST)
        if form.is_valid():
            # Process general form data
            
            # Process gross motor activities checkboxes for each age group
            if "Infant" in request.session.get('age_groups', []):
                request.session['balancing1'] = form.cleaned_data['balancing1']
                request.session['bouncing1'] = form.cleaned_data['bouncing1']
                request.session['bowling1'] = form.cleaned_data['bowling1']
                request.session['brachiating1'] = form.cleaned_data['brachiating1']
                request.session['climbing1'] = form.cleaned_data['climbing1']
                request.session['crawling1'] = form.cleaned_data['crawling1']
                request.session['dribbling1'] = form.cleaned_data['dribbling1']
                request.session['drumming1'] = form.cleaned_data['drumming1']
                request.session['hula_hopping1'] = form.cleaned_data['hula_hopping1']
                request.session['kicking1'] = form.cleaned_data['kicking1']
                request.session['rocking1'] = form.cleaned_data['rocking1']
                request.session['sliding1'] = form.cleaned_data['sliding1']
                request.session['throwing1'] = form.cleaned_data['throwing1']
                request.session['other4'] = form.cleaned_data['other4']
                
                request.session['question26'] = form.cleaned_data['question26']
                request.session['question29'] = form.cleaned_data['question29']
                
                # Process data from JavaScript arrays
                infant_gross_motor = json.loads(request.POST.get('infant_gross_motor_data', '[]'))
                print(f"Infant Gross Motor Activities ({len(infant_gross_motor)}): {infant_gross_motor}")

            if "Toddler" in request.session.get('age_groups', []):
                request.session['balancing2'] = form.cleaned_data['balancing2']
                request.session['bouncing2'] = form.cleaned_data['bouncing2']
                request.session['bowling2'] = form.cleaned_data['bowling2']
                request.session['brachiating2'] = form.cleaned_data['brachiating2']
                request.session['climbing2'] = form.cleaned_data['climbing2']
                request.session['crawling2'] = form.cleaned_data['crawling2']
                request.session['dancing2'] = form.cleaned_data['dancing2']
                request.session['digging2'] = form.cleaned_data['digging2']
                request.session['dribbling2'] = form.cleaned_data['dribbling2']
                request.session['drumming2'] = form.cleaned_data['drumming2']
                request.session['hula_hopping2'] = form.cleaned_data['hula_hopping2']
                request.session['jumping2'] = form.cleaned_data['jumping2']
                request.session['kicking2'] = form.cleaned_data['kicking2']
                request.session['lifting2'] = form.cleaned_data['lifting2']
                request.session['pull_ups2'] = form.cleaned_data['pull_ups2']
                request.session['pushing2'] = form.cleaned_data['pushing2']
                request.session['raking2'] = form.cleaned_data['raking2']
                request.session['riding2'] = form.cleaned_data['riding2']
                request.session['rocking2'] = form.cleaned_data['rocking2']
                request.session['sliding2'] = form.cleaned_data['sliding2']
                request.session['sweeping2'] = form.cleaned_data['sweeping2']
                request.session['swinging2'] = form.cleaned_data['swinging2']
                request.session['throwing2'] = form.cleaned_data['throwing2']
                request.session['other5'] = form.cleaned_data['other5']
                
                request.session['question27'] = form.cleaned_data['question27']
                request.session['question30'] = form.cleaned_data['question30']
                
                # Process data from JavaScript arrays
                toddler_gross_motor = json.loads(request.POST.get('toddler_gross_motor_data', '[]'))
                print(f"Toddler Gross Motor Activities ({len(toddler_gross_motor)}): {toddler_gross_motor}")

            if "Preschool" in request.session.get('age_groups', []):
                request.session['balancing3'] = form.cleaned_data['balancing3']
                request.session['bouncing3'] = form.cleaned_data['bouncing3']
                request.session['bowling3'] = form.cleaned_data['bowling3']
                request.session['brachiating3'] = form.cleaned_data['brachiating3']
                request.session['climbing3'] = form.cleaned_data['climbing3']
                request.session['crawling3'] = form.cleaned_data['crawling3']
                request.session['dancing3'] = form.cleaned_data['dancing3']
                request.session['digging3'] = form.cleaned_data['digging3']
                request.session['dribbling3'] = form.cleaned_data['dribbling3']
                request.session['drumming3'] = form.cleaned_data['drumming3']
                request.session['hammering3'] = form.cleaned_data['hammering3']
                request.session['hopping3'] = form.cleaned_data['hopping3']
                request.session['hula_hopping3'] = form.cleaned_data['hula_hopping3']
                request.session['jumping3'] = form.cleaned_data['jumping3']
                request.session['kicking3'] = form.cleaned_data['kicking3']
                request.session['lifting3'] = form.cleaned_data['lifting3']
                request.session['pull_ups3'] = form.cleaned_data['pull_ups3']
                request.session['pushing3'] = form.cleaned_data['pushing3']
                request.session['raking3'] = form.cleaned_data['raking3']
                request.session['riding3'] = form.cleaned_data['riding3']
                request.session['rocking3'] = form.cleaned_data['rocking3']
                request.session['sliding3'] = form.cleaned_data['sliding3']
                request.session['sweeping3'] = form.cleaned_data['sweeping3']
                request.session['swinging3'] = form.cleaned_data['swinging3']
                request.session['throwing3'] = form.cleaned_data['throwing3']
                request.session['other6'] = form.cleaned_data['other6']
                
                request.session['question28'] = form.cleaned_data['question28']
                request.session['question31'] = form.cleaned_data['question31']
                
                # Process data from JavaScript arrays
                preschool_gross_motor = json.loads(request.POST.get('preschool_gross_motor_data', '[]'))
                print(f"Preschool Gross Motor Activities ({len(preschool_gross_motor)}): {preschool_gross_motor}")

            # Process literacy materials checkboxes for each age group
            if "Infant" in request.session.get('age_groups', []):
                request.session['audio1'] = form.cleaned_data['audio1']
                request.session['books1'] = form.cleaned_data['books1']
                request.session['display_pictures1'] = form.cleaned_data['display_pictures1']
                request.session['environmental_print1'] = form.cleaned_data['environmental_print1']
                request.session['microphone1'] = form.cleaned_data['microphone1']
                request.session['language_cards1'] = form.cleaned_data['language_cards1']
                request.session['storytelling1'] = form.cleaned_data['storytelling1']
                request.session['other7'] = form.cleaned_data['other7']
                
                request.session['question32'] = form.cleaned_data['question32']
                request.session['question35'] = form.cleaned_data['question35']
                
                infant_literacy = json.loads(request.POST.get('infant_literacy_data', '[]'))
                print(f"Infant Literacy Materials ({len(infant_literacy)}): {infant_literacy}")

            if "Toddler" in request.session.get('age_groups', []):
                request.session['alphabet2'] = form.cleaned_data['alphabet2']
                request.session['audio2'] = form.cleaned_data['audio2']
                request.session['books2'] = form.cleaned_data['books2']
                request.session['display_pictures2'] = form.cleaned_data['display_pictures2']
                request.session['environmental_print2'] = form.cleaned_data['environmental_print2']
                request.session['microphone2'] = form.cleaned_data['microphone2']
                request.session['language_cards2'] = form.cleaned_data['language_cards2']
                request.session['storytelling2'] = form.cleaned_data['storytelling2']
                request.session['language_games2'] = form.cleaned_data['language_games2']
                request.session['other8'] = form.cleaned_data['other8']
                
                request.session['question33'] = form.cleaned_data['question33']
                request.session['question36'] = form.cleaned_data['question36']
                
                toddler_literacy = json.loads(request.POST.get('toddler_literacy_data', '[]'))
                print(f"Toddler Literacy Materials ({len(toddler_literacy)}): {toddler_literacy}")

            if "Preschool" in request.session.get('age_groups', []):
                request.session['journaling3'] = form.cleaned_data['journaling3']
                request.session['alphabet3'] = form.cleaned_data['alphabet3']
                request.session['audio3'] = form.cleaned_data['audio3']
                request.session['books3'] = form.cleaned_data['books3']
                request.session['display_pictures3'] = form.cleaned_data['display_pictures3']
                request.session['environmental_print3'] = form.cleaned_data['environmental_print3']
                request.session['microphone3'] = form.cleaned_data['microphone3']
                request.session['language_cards3'] = form.cleaned_data['language_cards3']
                request.session['storytelling3'] = form.cleaned_data['storytelling3']
                request.session['language_games3'] = form.cleaned_data['language_games3']
                request.session['other9'] = form.cleaned_data['other9']
                
                request.session['question34'] = form.cleaned_data['question34']
                request.session['question37'] = form.cleaned_data['question37']
                
                preschool_literacy = json.loads(request.POST.get('preschool_literacy_data', '[]'))
                print(f"Preschool Literacy Materials ({len(preschool_literacy)}): {preschool_literacy}")

            # Process math/science materials checkboxes for each age group
            if "Infant" in request.session.get('age_groups', []):
                request.session['bird_feeder1'] = form.cleaned_data['bird_feeder1']
                request.session['building_materials1'] = form.cleaned_data['building_materials1']
                request.session['discovery_bottles1'] = form.cleaned_data['discovery_bottles1']
                request.session['fill_dump_station1'] = form.cleaned_data['fill_dump_station1']
                request.session['funnels1'] = form.cleaned_data['funnels1']
                request.session['garden1'] = form.cleaned_data['garden1']
                request.session['grid1'] = form.cleaned_data['grid1']
                request.session['hopscotch1'] = form.cleaned_data['hopscotch1']
                request.session['living_animals1'] = form.cleaned_data['living_animals1']
                request.session['magnifying_glasses1'] = form.cleaned_data['magnifying_glasses1']
                request.session['matching_games1'] = form.cleaned_data['matching_games1']
                request.session['mirrors1'] = form.cleaned_data['mirrors1']
                request.session['numbers1'] = form.cleaned_data['numbers1']
                request.session['prism1'] = form.cleaned_data['prism1']
                request.session['rolling_ramps1'] = form.cleaned_data['rolling_ramps1']
                request.session['slime1'] = form.cleaned_data['slime1']
                request.session['sorting_containers1'] = form.cleaned_data['sorting_containers1']
                request.session['varying_size_containers1'] = form.cleaned_data['varying_size_containers1']
                request.session['visual_patterns1'] = form.cleaned_data['visual_patterns1']
                request.session['wind_chimes1'] = form.cleaned_data['wind_chimes1']
                request.session['other10'] = form.cleaned_data['other10']
                
                request.session['question38'] = form.cleaned_data['question38']
                request.session['question41'] = form.cleaned_data['question41']
                
                infant_math_science = json.loads(request.POST.get('infant_math_science_data', '[]'))
                print(f"Infant Math/Science Materials ({len(infant_math_science)}): {infant_math_science}")

            if "Toddler" in request.session.get('age_groups', []):
                request.session['bird_feeder2'] = form.cleaned_data['bird_feeder2']
                request.session['building_materials2'] = form.cleaned_data['building_materials2']
                request.session['discovery_bottles2'] = form.cleaned_data['discovery_bottles2']
                request.session['fill_dump_station2'] = form.cleaned_data['fill_dump_station2']
                request.session['funnels2'] = form.cleaned_data['funnels2']
                request.session['garden2'] = form.cleaned_data['garden2']
                request.session['hopscotch2'] = form.cleaned_data['hopscotch2']
                request.session['living_animals2'] = form.cleaned_data['living_animals2']
                request.session['magnifying_glasses2'] = form.cleaned_data['magnifying_glasses2']
                request.session['matching_games2'] = form.cleaned_data['matching_games2']
                request.session['mirrors2'] = form.cleaned_data['mirrors2']
                request.session['numbers2'] = form.cleaned_data['numbers2']
                request.session['prism2'] = form.cleaned_data['prism2']
                request.session['recording_temp2'] = form.cleaned_data['recording_temp2']
                request.session['rolling_ramps2'] = form.cleaned_data['rolling_ramps2']
                request.session['scales2'] = form.cleaned_data['scales2']
                request.session['slime2'] = form.cleaned_data['slime2']
                request.session['sorting_containers2'] = form.cleaned_data['sorting_containers2']
                request.session['spinners2'] = form.cleaned_data['spinners2']
                request.session['steps2'] = form.cleaned_data['steps2']
                request.session['varying_size_containers2'] = form.cleaned_data['varying_size_containers2']
                request.session['visual_patterns2'] = form.cleaned_data['visual_patterns2']
                request.session['wind_chimes2'] = form.cleaned_data['wind_chimes2']
                request.session['other11'] = form.cleaned_data['other11']
                
                request.session['question39'] = form.cleaned_data['question39']
                request.session['question42'] = form.cleaned_data['question42']
                
                toddler_math_science = json.loads(request.POST.get('toddler_math_science_data', '[]'))
                print(f"Toddler Math/Science Materials ({len(toddler_math_science)}): {toddler_math_science}")

            if "Preschool" in request.session.get('age_groups', []):
                request.session['bird_feeder3'] = form.cleaned_data['bird_feeder3']
                request.session['building_materials3'] = form.cleaned_data['building_materials3']
                request.session['dice3'] = form.cleaned_data['dice3']
                request.session['discovery_bottles3'] = form.cleaned_data['discovery_bottles3']
                request.session['fill_dump_station3'] = form.cleaned_data['fill_dump_station3']
                request.session['funnels3'] = form.cleaned_data['funnels3']
                request.session['garden3'] = form.cleaned_data['garden3']
                request.session['grid3'] = form.cleaned_data['grid3']
                request.session['hopscotch3'] = form.cleaned_data['hopscotch3']
                request.session['living_animals3'] = form.cleaned_data['living_animals3']
                request.session['magnifying_glasses3'] = form.cleaned_data['magnifying_glasses3']
                request.session['matching_games3'] = form.cleaned_data['matching_games3']
                request.session['mirrors3'] = form.cleaned_data['mirrors3']
                request.session['numbers3'] = form.cleaned_data['numbers3']
                request.session['prism3'] = form.cleaned_data['prism3']
                request.session['pulleys3'] = form.cleaned_data['pulleys3']
                request.session['recording_temp3'] = form.cleaned_data['recording_temp3']
                request.session['rolling_ramps3'] = form.cleaned_data['rolling_ramps3']
                request.session['scales3'] = form.cleaned_data['scales3']
                request.session['slime3'] = form.cleaned_data['slime3']
                request.session['sorting_containers3'] = form.cleaned_data['sorting_containers3']
                request.session['spinners3'] = form.cleaned_data['spinners3']
                request.session['steps3'] = form.cleaned_data['steps3']
                request.session['timers3'] = form.cleaned_data['timers3']
                request.session['varying_size_containers3'] = form.cleaned_data['varying_size_containers3']
                request.session['visual_patterns3'] = form.cleaned_data['visual_patterns3']
                request.session['wind_chimes3'] = form.cleaned_data['wind_chimes3']
                request.session['other12'] = form.cleaned_data['other12']
                
                request.session['question40'] = form.cleaned_data['question40']
                request.session['question43'] = form.cleaned_data['question43']
                
                preschool_math_science = json.loads(request.POST.get('preschool_math_science_data', '[]'))
                print(f"Preschool Math/Science Materials ({len(preschool_math_science)}): {preschool_math_science}")

            # Process dramatic play materials checkboxes for each age group
            if "Infant" in request.session.get('age_groups', []):
                request.session['animal_figures1'] = form.cleaned_data['animal_figures1']
                request.session['crayons1'] = form.cleaned_data['crayons1']
                request.session['child_sized_furniture1'] = form.cleaned_data['child_sized_furniture1']
                request.session['collage_materials1'] = form.cleaned_data['collage_materials1']
                request.session['cooking_eating_equipment1'] = form.cleaned_data['cooking_eating_equipment1']
                request.session['dolls1'] = form.cleaned_data['dolls1']
                request.session['dress_up1'] = form.cleaned_data['dress_up1']
                request.session['easels1'] = form.cleaned_data['easels1']
                request.session['musical_instruments1'] = form.cleaned_data['musical_instruments1']
                request.session['paint_brushes1'] = form.cleaned_data['paint_brushes1']
                request.session['paints1'] = form.cleaned_data['paints1']
                request.session['paper_cardboard1'] = form.cleaned_data['paper_cardboard1']
                request.session['play_dough1'] = form.cleaned_data['play_dough1']
                request.session['soft_animals1'] = form.cleaned_data['soft_animals1']
                request.session['toy_telephones1'] = form.cleaned_data['toy_telephones1']
                
                request.session['question44'] = form.cleaned_data['question44']
                request.session['question47'] = form.cleaned_data['question47']
                
                infant_dramatic_play = json.loads(request.POST.get('infant_dramatic_play_data', '[]'))
                print(f"Infant Dramatic Play Materials ({len(infant_dramatic_play)}): {infant_dramatic_play}")

            if "Toddler" in request.session.get('age_groups', []):
                request.session['animal_figures2'] = form.cleaned_data['animal_figures2']
                request.session['crayons2'] = form.cleaned_data['crayons2']
                request.session['child_sized_furniture2'] = form.cleaned_data['child_sized_furniture2']
                request.session['collage_materials2'] = form.cleaned_data['collage_materials2']
                request.session['cooking_eating_equipment2'] = form.cleaned_data['cooking_eating_equipment2']
                request.session['dolls2'] = form.cleaned_data['dolls2']
                request.session['dress_up2'] = form.cleaned_data['dress_up2']
                request.session['easels2'] = form.cleaned_data['easels2']
                request.session['musical_instruments2'] = form.cleaned_data['musical_instruments2']
                request.session['paint_brushes2'] = form.cleaned_data['paint_brushes2']
                request.session['paints2'] = form.cleaned_data['paints2']
                request.session['paper_cardboard2'] = form.cleaned_data['paper_cardboard2']
                request.session['play_dough2'] = form.cleaned_data['play_dough2']
                request.session['soft_animals2'] = form.cleaned_data['soft_animals2']
                request.session['toy_telephones2'] = form.cleaned_data['toy_telephones2']
                
                request.session['question45'] = form.cleaned_data['question45']
                request.session['question48'] = form.cleaned_data['question48']
                
                toddler_dramatic_play = json.loads(request.POST.get('toddler_dramatic_play_data', '[]'))
                print(f"Toddler Dramatic Play Materials ({len(toddler_dramatic_play)}): {toddler_dramatic_play}")

            if "Preschool" in request.session.get('age_groups', []):
                request.session['animal_figures3'] = form.cleaned_data['animal_figures3']
                request.session['crayons3'] = form.cleaned_data['crayons3']
                request.session['child_sized_furniture3'] = form.cleaned_data['child_sized_furniture3']
                request.session['collage_materials3'] = form.cleaned_data['collage_materials3']
                request.session['cooking_eating_equipment3'] = form.cleaned_data['cooking_eating_equipment3']
                request.session['dolls3'] = form.cleaned_data['dolls3']
                request.session['dress_up3'] = form.cleaned_data['dress_up3']
                request.session['easels3'] = form.cleaned_data['easels3']
                request.session['musical_instruments3'] = form.cleaned_data['musical_instruments3']
                request.session['paint_brushes3'] = form.cleaned_data['paint_brushes3']
                request.session['paints3'] = form.cleaned_data['paints3']
                request.session['paper_cardboard3'] = form.cleaned_data['paper_cardboard3']
                request.session['play_dough3'] = form.cleaned_data['play_dough3']
                request.session['soft_animals3'] = form.cleaned_data['soft_animals3']
                request.session['toy_telephones3'] = form.cleaned_data['toy_telephones3']
                
                request.session['question46'] = form.cleaned_data['question46']
                request.session['question49'] = form.cleaned_data['question49']
                
                preschool_dramatic_play = json.loads(request.POST.get('preschool_dramatic_play_data', '[]'))
                print(f"Preschool Dramatic Play Materials ({len(preschool_dramatic_play)}): {preschool_dramatic_play}")

            # Process the outdoor time plan
            request.session['question50'] = form.cleaned_data['question50']

            # Redirect to the next page
            return redirect('page6')  # Replace with the actual next page URL
        else:
            print(form.errors)
    else:
        form = Page5Form()
    
    # Get age groups from session for conditional rendering
    age_groups = request.session.get('age_groups', [])
    return render(request, 'page5.html', {'form': form, 'age_groups': age_groups})

def page6(request):
    if request.method == 'POST':
        form = Page6Form(request.POST)
        if form.is_valid():
            # Process the form data
            request.session['question51'] = form.cleaned_data['question51']
            request.session['question52'] = form.cleaned_data['question52']
            request.session['question53'] = form.cleaned_data['question53']
            request.session['question54'] = form.cleaned_data['question54']
            request.session['question55'] = form.cleaned_data['question55']
            request.session['question56'] = form.cleaned_data['question56']
            request.session['question57'] = form.cleaned_data['question57']
            request.session['question58'] = form.cleaned_data['question58']
            request.session['question59'] = form.cleaned_data['question59']
            request.session['question60'] = form.cleaned_data['question60']
            
            # Redirect to the next page or thank you page
            return redirect('page6')  # Replace with the actual next page URL
        else:
            print(form.errors)
    else:
        form = Page6Form()
    
    return render(request, 'page6.html', {'form': form})