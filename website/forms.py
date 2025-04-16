from django.contrib.auth.models import User
from django import forms
from django.db import models

class Page1Form(forms.Form):
    first_name = forms.CharField(
        label="Name",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control center-placeholder', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        label="Last Name",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control center-placeholder', 'placeholder': 'Last Name'})
    )
    email = forms.EmailField(
        label="Email",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control center-placeholder', 'placeholder': 'Email'})
    )
    address = forms.CharField(
        label="Address",
        widget=forms.TextInput(attrs={'class': 'form-control center-placeholder', 'placeholder': 'Address'})
        
    )

    city = forms.CharField(
        label="City",
        widget=forms.TextInput(attrs={'class': 'form-control center-placeholder', 'placeholder': 'City'})
    )

    state = forms.ChoiceField(
        label="State",
        widget=forms.Select(attrs={'class': 'form-select text-center ', 'placeholder': 'State'}),
        choices=(
            ('', 'State'),
            ('Alabama', 'Alabama'),
            ('Alaska', 'Alaska'),
            ('Arizona', 'Arizona'), ('Arkansas', 'Arkansas'), ('California', 'California'), 
            ('Colorado', 'Colorado'), ('Connecticut', 'Connecticut'), ('Delaware', 'Delaware'), 
            ('Florida', 'Florida'), ('Georgia', 'Georgia'), ('Hawaii', 'Hawaii'), ('Idaho', 'Idaho'), 
            ('Illinois', 'Illinois'), ('Indiana', 'Indiana'), ('Iowa', 'Iowa'), ('Kansas', 'Kansas'), 
            ('Kentucky', 'Kentucky'), ('Louisiana', 'Louisiana'), ('Maine', 'Maine'), ('Maryland', 'Maryland'), 
            ('Massachusetts', 'Massachusetts'), ('Michigan', 'Michigan'), ('Minnesota', 'Minnesota'), 
            ('Mississippi', 'Mississippi'), ('Missouri', 'Missouri'), ('Montana', 'Montana'), 
            ('Nebraska', 'Nebraska'), ('Nevada', 'Nevada'), ('New Hampshire', 'New Hampshire'), 
            ('New Jersey', 'New Jersey'), ('New Mexico', 'New Mexico'), ('New York', 'New York'), 
            ('North Carolina', 'North Carolina'), ('North Dakota', 'North Dakota'), ('Ohio', 'Ohio'), 
            ('Oklahoma', 'Oklahoma'), ('Oregon', 'Oregon'), ('Pennsylvania', 'Pennsylvania'), 
            ('Rhode Island', 'Rhode Island'), ('South Carolina', 'South Carolina'), 
            ('South Dakota', 'South Dakota'), ('Tennessee', 'Tennessee'), ('Texas', 'Texas'), ('Utah', 'Utah'), 
            ('Vermont', 'Vermont'), ('Virginia', 'Virginia'), ('Washington', 'Washington'), 
            ('West Virginia', 'West Virginia'), ('Wisconsin', 'Wisconsin'), ('Wyoming', 'Wyoming')
            # Add more states here
        )
    )
    
    zip_code = forms.CharField(
        label="Zip",
        widget=forms.TextInput(attrs={'class': 'form-control center-placeholder', 'placeholder': 'Zip'})
    )

class Page2Form(forms.Form):
    CHOICES = [('Yes', 'Yes'), ('No', 'No')]
    
    question1 = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'custom-radio'}),
        required=True
    )
    question2 = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'custom-radio'}),
        required=True
    )
    question3 = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'custom-radio'}),
        required=True
    )
    question4 = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'custom-radio'}),
        required=True
    )
    question5 = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'custom-radio'}),
        required=True
    )
    question6 = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'custom-radio'}),
        required=True
    )
    question7 = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'custom-radio'}),
        required=True
    )
    question8 = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'custom-radio'}),
        required=True
    )
    question9 = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'custom-radio'}),
        required=True
    )
    question10 = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'custom-radio'}),
        required=True
    )
    question11 = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'custom-radio'}),
        required=True
    )
    question12 = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'custom-radio'}),
        required=True
    )

class Page3Form(forms.Form):
    question13 = forms.ChoiceField(
        choices = [
            ('level131', 'No patch(es) of shade.'),
            ('level132', 'Patch(es) of shade sufficient for a few children.  '),
            ('level133', 'Patch(es) of shade sufficient for most children.  '),
            ('level134', 'Patch(es) of shade sufficient for all children.  '),
        ],
        widget=forms.RadioSelect,required=True,
        )
    question14 = forms.ChoiceField(
        choices = [
            ('level141', 'As calculated  by formula, 0% to 29% sufficient trees.  '),
            ('level142', 'As calculated  by formula, 30% to 64% sufficient trees.  '),
            ('level143', 'As calculated  by formula, 65% to 99% sufficient trees.  '),
            ('level144', 'As calculated  by formula, 100% or more of sufficient trees.  '),
        ],
        widget=forms.RadioSelect,required=True,
        )
    question15 = forms.ChoiceField(
        choices = [
            ('level151', 'As calculated  by formula, 0% to 29% sufficient trees.  '),
            ('level152', 'As calculated  by formula, 30% to 64% sufficient trees.  '),
            ('level153', 'As calculated  by formula, 65% to 99% sufficient trees.  '),
            ('level154', 'As calculated  by formula, 100% or more of sufficient trees.  '),
        ],
        widget=forms.RadioSelect,required=True,
        )
    question16 = forms.ChoiceField(
        choices = [
            ('level161', 'No fruit or vegetables garden.'),
            ('level162', 'There is a vegetable or fruit garden with limited produce to taste or use for snacks/ meals.'),
            ('level163', 'There is a fruit and vegetable garden with enough produce for some of the children to taste or use for snacks/meals.  '),
            ('level164', 'There is a fruit and vegetable garden with abundant produce for all children to taste or use for snacks/meals. '),
            ('level165', 'N/A'),
        ],
        widget=forms.RadioSelect,required=True,
        )
    question17 = forms.ChoiceField(
        choices = [
            ('level171', 'There is no outdoor storage'),
            ('level172', 'There are open storage containers (e.g. crates, open boxes'),
            ('level173', 'There is at least one enclosed closet or chest or sheltered outdoor shelving.'),
            ('level174', 'There is more than one enclosed closet or chest or sheltered outdoor shelving.'),
            ('level175', 'N/A'),
        ],
        widget=forms.RadioSelect,required=True,
        )
    question18 = forms.ChoiceField(
        choices = [
            ('level181', 'There is no outdoor storage'),
            ('level182', 'There is at least one enclosed closet or chest or sheltered outdoor shelving.'),
            ('level183', 'There is at least one enclosed closet or chest or sheltered outdoor shelving and covered wheeled toy storage.'),
            ('level184', 'There is at least one enclosed closet or chest or sheltered outdoor shelving and covered wheeled toy storage, and a secure walk-in storage shed.'),
            ('level185', 'N/A'),
        ],
        widget=forms.RadioSelect,required=True,
        )
    
class Page4Form(forms.Form):

    breast_feeding = forms.BooleanField(required=False, label="Breastfeeding/Bottle-Feeding Nook", widget=forms.CheckboxInput())
    indoor_outdoor_transition1 = forms.BooleanField(required=False, label="Covered Usable Indoor-Outdoor Transition Space", widget=forms.CheckboxInput())
    deck1 = forms.BooleanField(required=False, label="Deck", widget=forms.CheckboxInput())
    diaper_changing_station = forms.BooleanField(required=False, label="Diaper Changing Station", widget=forms.CheckboxInput())
    gathering_setting1 = forms.BooleanField(required=False, label="Gathering Setting", widget=forms.CheckboxInput())
    grove_trees1 = forms.BooleanField(required=False, label="Grove of Small Trees/Large Shrubs", widget=forms.CheckboxInput())
    mound1 = forms.BooleanField(required=False, label="Mound/Slope", widget=forms.CheckboxInput())
    manufactured_play1 = forms.BooleanField(required=False, label="Manufactured Play Equipment", widget=forms.CheckboxInput())
    multipurpose_lawn1 = forms.BooleanField(required=False, label="Multipurpose Activity Setting/Lawn", widget=forms.CheckboxInput())
    multisensory_pathway1 = forms.BooleanField(required=False, label="Multisensory Pathway", widget=forms.CheckboxInput())
    multisensory_setting1 = forms.BooleanField(required=False, label="Multisensory Setting", widget=forms.CheckboxInput())
    music_play1 = forms.BooleanField(required=False, label="Music Play Area", widget=forms.CheckboxInput())
    playhouse1 = forms.BooleanField(required=False, label="Playhouse", widget=forms.CheckboxInput())
    pollinator_garden1 = forms.BooleanField(required=False, label="Pollinator/Flower Garden", widget=forms.CheckboxInput())
    porch_swing1 = forms.BooleanField(required=False, label="Porch Swing", widget=forms.CheckboxInput())
    primary_pathway1 = forms.BooleanField(required=False, label="Primary Pathway(Push/Pull Wheeled Toys)", widget=forms.CheckboxInput())
    ramp1 = forms.BooleanField(required=False, label="Ramp(if used to play)", widget=forms.CheckboxInput())
    sand_play1 = forms.BooleanField(required=False, label="Sand Play Setting", widget=forms.CheckboxInput())
    small_bridge = forms.BooleanField(required=False, label="Small Bridge", widget=forms.CheckboxInput())
    steppingstone_pathway1 = forms.BooleanField(required=False, label="Steppingstone Pathway(In Lawn", widget=forms.CheckboxInput())
    tent_structures1 = forms.BooleanField(required=False, label="Tent-Like Play Structures", widget=forms.CheckboxInput())
    textured_panel = forms.BooleanField(required=False, label="Textured Panel Wall", widget=forms.CheckboxInput())
    water_play_hands_1 = forms.BooleanField(required=False, label="Water Play(Hands-In)", widget=forms.CheckboxInput())
    other1 = forms.BooleanField(required=False, label="Other", widget=forms.CheckboxInput())

    question19 = forms.ChoiceField(
        choices = [
            ('level191', '0-1 settings.  '),
            ('level192', '2-4 settings.  '),
            ('level193', '5-7 settings.  '),
            ('level194', '8 or more settings.  '),
        ],
        widget=forms.RadioSelect,required=True,
        )

    area_pets1 = forms.BooleanField(required=False, label="Area for Pets(Chickens and Rabbits)", widget=forms.CheckboxInput())
    indoor_outdoor_transition2 = forms.BooleanField(required=False, label="Covered Useable Indoor-Outdoor Transition Space", widget=forms.CheckboxInput())
    cozy_nook1 = forms.BooleanField(required=False, label="Cozy Nook", widget=forms.CheckboxInput())
    balance_beam1 = forms.BooleanField(required=False, label="Balance Beam", widget=forms.CheckboxInput())
    bridge1 = forms.BooleanField(required=False, label="Bridge", widget=forms.CheckboxInput())
    deck2 = forms.BooleanField(required=False, label="Deck", widget=forms.CheckboxInput())
    earth_play1 = forms.BooleanField(required=False, label="Earth Play(Dirt or Mud)", widget=forms.CheckboxInput())
    editable_landscape1 = forms.BooleanField(required=False, label="Editable Landscape", widget=forms.CheckboxInput())
    fruit_garden1 = forms.BooleanField(required=False, label="Fruit and/or Vegetable Garden", widget=forms.CheckboxInput())
    gathering_setting2 = forms.BooleanField(required=False, label="Gathering Setting", widget=forms.CheckboxInput())
    grove_trees2 = forms.BooleanField(required=False, label="Grove of Small Trees/Large Shrubs", widget=forms.CheckboxInput())
    hard_surface1 = forms.BooleanField(required=False, label="Hard Surface for Wheeled toys", widget=forms.CheckboxInput())
    loose_parts1 = forms.BooleanField(required=False, label="Loose Parts Play Area", widget=forms.CheckboxInput())
    manufactured_play2 = forms.BooleanField(required=False, label="Manufactured Play Equipment", widget=forms.CheckboxInput())
    mound2 = forms.BooleanField(required=False, label="Mound/Slope", widget=forms.CheckboxInput())
    multipurpose_lawn2 = forms.BooleanField(required=False, label="Multipurpose Activity Setting/Lawn", widget=forms.CheckboxInput())
    multisensory_pathway2 = forms.BooleanField(required=False, label="Multisensory Pathway", widget=forms.CheckboxInput())
    multisensory_setting2 = forms.BooleanField(required=False, label="Multisensory Setting", widget=forms.CheckboxInput())
    music_play2 = forms.BooleanField(required=False, label="Music Play Area", widget=forms.CheckboxInput())
    outdoor_classroom1 = forms.BooleanField(required=False, label="Outdoor Classroom", widget=forms.CheckboxInput())
    playhouse2 = forms.BooleanField(required=False, label="Playhouse", widget=forms.CheckboxInput())
    pollinator_garden2 = forms.BooleanField(required=False, label="Pollinator/Flower Garden", widget=forms.CheckboxInput())
    porch_swing2 = forms.BooleanField(required=False, label="Porch Swing", widget=forms.CheckboxInput())
    primary_pathway2 = forms.BooleanField(required=False, label="Primary Pathway(Push/Pull Wheeled Toys)", widget=forms.CheckboxInput())
    project_space = forms.BooleanField(required=False, label="Project Space", widget=forms.CheckboxInput())
    ramp2 = forms.BooleanField(required=False, label="Ramp(if used to play)", widget=forms.CheckboxInput())
    sand_play2 = forms.BooleanField(required=False, label="Sand Play Setting", widget=forms.CheckboxInput())
    steppingstone_pathway2 = forms.BooleanField(required=False, label="Steppingstone Pathway(In Lawn)", widget=forms.CheckboxInput())
    swing1 = forms.BooleanField(required=False, label="Swing", widget=forms.CheckboxInput())
    table1 = forms.BooleanField(required=False, label="Table", widget=forms.CheckboxInput())
    tent_structures2 = forms.BooleanField(required=False, label="Tent-Like Play Structures", widget=forms.CheckboxInput())
    water_play_hands_2 = forms.BooleanField(required=False, label="Water Play(Hands-In)", widget=forms.CheckboxInput())
    water_play_body_1 = forms.BooleanField(required=False, label="Water Play(Full Body)", widget=forms.CheckboxInput())
    other2 = forms.BooleanField(required=False, label="Other", widget=forms.CheckboxInput())

    question20 = forms.ChoiceField(
        choices = [
            ('level201', '0-3 settings.  '),
            ('level202', '4-7 settings.  '),
            ('level203', '8-9 settings.  '),
            ('leve204', '10 or more settings.  '),
        ],
        widget=forms.RadioSelect,required=True,
        )

    area_pets2 = forms.BooleanField(required=False, label="Area for Pets(Chickens and Rabbits)", widget=forms.CheckboxInput())
    balance_beam = forms.BooleanField(required=False, label="Balance Beam", widget=forms.CheckboxInput())
    bridge2 = forms.BooleanField(required=False, label="Bridge", widget=forms.CheckboxInput())
    indoor_outdoor_transition3 = forms.BooleanField(required=False, label="Covered Usable Indoor-Outdoor Transition Space", widget=forms.CheckboxInput())
    cozy_nook2 = forms.BooleanField(required=False, label="Cozy Nook", widget=forms.CheckboxInput())
    deck3 = forms.BooleanField(required=False, label="Deck", widget=forms.CheckboxInput())
    dry_creek_bed = forms.BooleanField(required=False, label="Dry Creek Bed", widget=forms.CheckboxInput())
    earth_play2 = forms.BooleanField(required=False, label="Earth Play(Dirt or Mud)", widget=forms.CheckboxInput())
    editable_landscape2 = forms.BooleanField(required=False, label="Editable Landscape", widget=forms.CheckboxInput())
    fruit_garden2 = forms.BooleanField(required=False, label="Fruit and/or Vegetable Garden", widget=forms.CheckboxInput())
    gathering_setting3 = forms.BooleanField(required=False, label="Gathering Setting", widget=forms.CheckboxInput())
    grass_maze = forms.BooleanField(required=False, label="Grass Maze", widget=forms.CheckboxInput())
    grove_trees3 = forms.BooleanField(required=False, label="Grove of Small Trees/Large Shrubs", widget=forms.CheckboxInput())
    hard_surface2 = forms.BooleanField(required=False, label="Hard Surface for Wheeled toys", widget=forms.CheckboxInput())
    loose_parts2 = forms.BooleanField(required=False, label="Loose Parts Play Area", widget=forms.CheckboxInput())
    manufactured_play3 = forms.BooleanField(required=False, label="Manufactured Play Equipment", widget=forms.CheckboxInput())
    mound3 = forms.BooleanField(required=False, label="Mound/Slope", widget=forms.CheckboxInput())
    multipurpose_lawn3 = forms.BooleanField(required=False, label="Multipurpose Activity Setting/Lawn", widget=forms.CheckboxInput())
    multisensory_pathway3 = forms.BooleanField(required=False, label="Multisensory Pathway", widget=forms.CheckboxInput())
    multisensory_setting3 = forms.BooleanField(required=False, label="Multisensory Setting", widget=forms.CheckboxInput())
    music_play3 = forms.BooleanField(required=False, label="Music Play Area", widget=forms.CheckboxInput())
    natural_construction_area = forms.BooleanField(required=False, label="Natural Construction Area", widget=forms.CheckboxInput())
    outdoor_classroom2 = forms.BooleanField(required=False, label="Outdoor Classroom", widget=forms.CheckboxInput())
    performance_space = forms.BooleanField(required=False, label="Performance Space", widget=forms.CheckboxInput())
    playhouse3 = forms.BooleanField(required=False, label="Playhouse", widget=forms.CheckboxInput())
    pollinator_garden3 = forms.BooleanField(required=False, label="Pollinator/Flower Garden", widget=forms.CheckboxInput())
    primary_pathway3 = forms.BooleanField(required=False, label="Primary Pathway(Push/Pull Wheeled Toys)", widget=forms.CheckboxInput())
    project_space2 = forms.BooleanField(required=False, label="Project Space", widget=forms.CheckboxInput())
    ramp3 = forms.BooleanField(required=False, label="Ramp(if used to play)", widget=forms.CheckboxInput())
    sand_play3 = forms.BooleanField(required=False, label="Sand Play Setting", widget=forms.CheckboxInput())
    steppingstone_pathway3 = forms.BooleanField(required=False, label="Steppingstone Pathway(In Lawn)", widget=forms.CheckboxInput())
    swing2 = forms.BooleanField(required=False, label="Swing", widget=forms.CheckboxInput())
    table2 = forms.BooleanField(required=False, label="Table", widget=forms.CheckboxInput())
    tent_structures3 = forms.BooleanField(required=False, label="Tent-Like Play Structures", widget=forms.CheckboxInput())
    water_play_hands_3 = forms.BooleanField(required=False, label="Water Play(Hands-In)", widget=forms.CheckboxInput())
    water_play_body_2 = forms.BooleanField(required=False, label="Water Play(Full Body)", widget=forms.CheckboxInput())
    woodwork_bench = forms.BooleanField(required=False, label="Woodwork Bench", widget=forms.CheckboxInput())
    other3 = forms.BooleanField(required=False, label="Other", widget=forms.CheckboxInput())

    question21 = forms.ChoiceField(
        choices = [
            ('level211', '0-3 settings.  '),
            ('level212', '4-7 settings.  '),
            ('level213', '8-9 settings.  '),
            ('level214', '10 or more settings.  '),
        ],
        widget=forms.RadioSelect,required=True,
        )





