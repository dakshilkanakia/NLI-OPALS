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

    #used throughout the form
    age_groups = forms.MultipleChoiceField(
        label = "What age groups will you be evaluating for this assessment? Please select all that apply",
        widget=forms.CheckboxSelectMultiple,
        choices=(
            ('Infant', 'Infant'),
            ('Toddler', 'Toddler/Twos'),
            ('Preschool', 'Preschool'),
        )
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
        widget=forms.RadioSelect,required=False,
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
            ('level204', '10 or more settings.  '),
        ],
        widget=forms.RadioSelect,required=False,
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
        widget=forms.RadioSelect,required=False,
        )

    #pathway vale questions waiting for Robin
    #question22 = forms.ChoiceField(
    #    choices = [
    #        ('level221', 'There is no pathway.  '),
    #        ('level222', 'There is a pathway that is not safe for children to use.  '),
    #        ('level223', 'There is a pathway that is safe for children to use.  '),
    #        ('level224', 'There is a pathway that is safe for children to use and is accessible for all children.  '),
    #    ],
    #    widget=forms.RadioSelect,required=True,
    #    )
    #question23 = forms.ChoiceField(
    #    choices = [
    #        ('level231', 'There is no pathway.  '),
    #        ('level232', 'There is a pathway that is not safe for children to use.  '),
    #        ('level233', 'There is a pathway that is safe for children to use.  '),
    #        ('level234', 'There is a pathway that is safe for children to use and is accessible for all children.  '),
    #    ],
    #    widget=forms.RadioSelect,required=True,
    #    )

    question24 = forms.ChoiceField(
        choices = [
            ('level241', 'There is no multipurpose activity settings/lawn.'),
            ('level242', 'Multipurpose activity setting/lawn sufficient for only a few children to use together.'),
            ('level243', 'A medium size multipurpose activity setting/lawn large enough for at least half a class of children to use together.'),
            ('level244', 'A large multipurpose activity setting/lawn large enough for all children in a class to use together.'),
        ],
        widget=forms.RadioSelect,required=True,
        )
    
    question25 = forms.ChoiceField(
        choices = [
            ('level251', 'There is no covered outdoor classroom/gathering place.'),
            ('level252', 'There is a covered outdoor classroom/gathering place large enough for only a small, informal group of children to use together with teacher.'),
            ('level253', 'There is a medium size covered outdoor classroom/gathering place large enough for at least half a class to use together with teacher.'),
            ('level254', 'There is a large covered outdoor classroom/gathering place large enough for all children in a class to use together with teacher.'),
        ],
        widget=forms.RadioSelect,required=True,
        )


class Page5Form(forms.Form):
    # for infants
    balancing1 = forms.BooleanField(required=False, label="Balancing", widget=forms.CheckboxInput())
    bouncing1 = forms.BooleanField(required=False, label="Bouncing(Body)", widget=forms.CheckboxInput())
    bowling1 = forms.BooleanField(required=False, label="Bowling", widget=forms.CheckboxInput())
    brachiating1 = forms.BooleanField(required=False, label="Brachiating", widget=forms.CheckboxInput())
    climbing1 = forms.BooleanField(required=False, label="Climbing", widget=forms.CheckboxInput())
    crawling1 = forms.BooleanField(required=False, label="Crawling through", widget=forms.CheckboxInput())
    dribbling1 = forms.BooleanField(required=False, label="Dribbling", widget=forms.CheckboxInput())
    drumming1 = forms.BooleanField(required=False, label="Drumming", widget=forms.CheckboxInput())
    hula_hopping1 = forms.BooleanField(required=False, label="Hula Hopping/ hoop rolling", widget=forms.CheckboxInput())
    kicking1 = forms.BooleanField(required=False, label="Kicking", widget=forms.CheckboxInput())
    rocking1 = forms.BooleanField(required=False, label="Rocking", widget=forms.CheckboxInput())
    sliding1 = forms.BooleanField(required=False, label="Sliding", widget=forms.CheckboxInput())
    throwing1 = forms.BooleanField(required=False, label="Throwing/Catcing", widget=forms.CheckboxInput())
    other4 = forms.BooleanField(required=False, label="Other", widget=forms.CheckboxInput())

    question26 = forms.ChoiceField(
        choices = [
            ('level261', '0 material(s) accessible to children'),
            ('level262', '1-2 material accessible to children'),
            ('level263', '3-4 material accessible to children'),
            ('level264', '5+ material accessible to children'),
        ],
        widget=forms.RadioSelect,required=False,
        )

    # for toddlers
    balancing2 = forms.BooleanField(required=False, label="Balancing", widget=forms.CheckboxInput())
    bouncing2 = forms.BooleanField(required=False, label="Bouncing(Body)", widget=forms.CheckboxInput())
    bowling2 = forms.BooleanField(required=False, label="Bowling", widget=forms.CheckboxInput())
    brachiating2 = forms.BooleanField(required=False, label="Brachiating", widget=forms.CheckboxInput())
    climbing2 = forms.BooleanField(required=False, label="Climbing", widget=forms.CheckboxInput())
    crawling2 = forms.BooleanField(required=False, label="Crawling through", widget=forms.CheckboxInput())
    dancing2 = forms.BooleanField(required=False, label="Dancing", widget=forms.CheckboxInput())
    digging2 = forms.BooleanField(required=False, label="Digging/Scooping", widget=forms.CheckboxInput())
    dribbling2 = forms.BooleanField(required=False, label="Dribbling", widget=forms.CheckboxInput())
    drumming2 = forms.BooleanField(required=False, label="Drumming", widget=forms.CheckboxInput())
    hula_hopping2 = forms.BooleanField(required=False, label="Hula Hopping/hoop rolling", widget=forms.CheckboxInput())
    jumping2 = forms.BooleanField(required=False, label="Jumping off/on", widget=forms.CheckboxInput())
    kicking2 = forms.BooleanField(required=False, label="Kicking", widget=forms.CheckboxInput())
    lifting2 = forms.BooleanField(required=False, label="Lifting", widget=forms.CheckboxInput())
    pull_ups2 = forms.BooleanField(required=False, label="Pull Up/Hanging by arms or legs", widget=forms.CheckboxInput())
    pushing2 = forms.BooleanField(required=False, label="Pushing/Pulling", widget=forms.CheckboxInput())
    raking2 = forms.BooleanField(required=False, label="Raking", widget=forms.CheckboxInput())
    riding2 = forms.BooleanField(required=False, label="Riding", widget=forms.CheckboxInput())
    rocking2 = forms.BooleanField(required=False, label="Rocking", widget=forms.CheckboxInput())
    sliding2 = forms.BooleanField(required=False, label="Sliding", widget=forms.CheckboxInput())
    sweeping2 = forms.BooleanField(required=False, label="Sweeping", widget=forms.CheckboxInput())
    swinging2 = forms.BooleanField(required=False, label="Swinging", widget=forms.CheckboxInput())
    throwing2 = forms.BooleanField(required=False, label="Throwing/Catching", widget=forms.CheckboxInput())
    other5 = forms.BooleanField(required=False, label="Other", widget=forms.CheckboxInput())

    question27 = forms.ChoiceField(
        choices = [
            ('level271', '0-2 material(s) accessible to children'),
            ('level272', '3-4 material accessible to children'),
            ('level273', '5-6 material accessible to children'),
            ('level274', '7+ material accessible to children'),
        ],
        widget=forms.RadioSelect,required=False,
        )
    # for preschoolers
    balancing3 = forms.BooleanField(required=False, label="Balancing", widget=forms.CheckboxInput())
    bouncing3 = forms.BooleanField(required=False, label="Bouncing(Body)", widget=forms.CheckboxInput())
    bowling3 = forms.BooleanField(required=False, label="Bowling", widget=forms.CheckboxInput())
    brachiating3 = forms.BooleanField(required=False, label="Brachiating", widget=forms.CheckboxInput())
    climbing3 = forms.BooleanField(required=False, label="Climbing", widget=forms.CheckboxInput())
    crawling3 = forms.BooleanField(required=False, label="Crawling through", widget=forms.CheckboxInput())
    dancing3 = forms.BooleanField(required=False, label="Dancing", widget=forms.CheckboxInput())
    digging3 = forms.BooleanField(required=False, label="Digging/Scooping", widget=forms.CheckboxInput())
    dribbling3 = forms.BooleanField(required=False, label="Dribbling", widget=forms.CheckboxInput())
    drumming3 = forms.BooleanField(required=False, label="Drumming", widget=forms.CheckboxInput())
    hammering3 = forms.BooleanField(required=False, label="Hammering", widget=forms.CheckboxInput())
    hopping3 = forms.BooleanField(required=False, label="Hopping", widget=forms.CheckboxInput())
    hula_hopping3 = forms.BooleanField(required=False, label="Hula Hopping/hoop rolling", widget=forms.CheckboxInput())
    jumping3 = forms.BooleanField(required=False, label="Jumping off/on", widget=forms.CheckboxInput())
    kicking3 = forms.BooleanField(required=False, label="Kicking", widget=forms.CheckboxInput())
    lifting3 = forms.BooleanField(required=False, label="Lifting", widget=forms.CheckboxInput())
    pull_ups3 = forms.BooleanField(required=False, label="Pull Up/Hanging by arms or legs", widget=forms.CheckboxInput())
    pushing3 = forms.BooleanField(required=False, label="Pushing/Pulling", widget=forms.CheckboxInput())
    raking3 = forms.BooleanField(required=False, label="Raking", widget=forms.CheckboxInput())
    riding3 = forms.BooleanField(required=False, label="Riding", widget=forms.CheckboxInput())
    rocking3 = forms.BooleanField(required=False, label="Rocking", widget=forms.CheckboxInput())
    sliding3 = forms.BooleanField(required=False, label="Sliding", widget=forms.CheckboxInput())
    sweeping3 = forms.BooleanField(required=False, label="Sweeping", widget=forms.CheckboxInput())
    swinging3 = forms.BooleanField(required=False, label="Swinging", widget=forms.CheckboxInput())
    throwing3 = forms.BooleanField(required=False, label="Throwing/Catching", widget=forms.CheckboxInput())
    other6 = forms.BooleanField(required=False, label="Other", widget=forms.CheckboxInput())

    question28 = forms.ChoiceField(
        choices = [
            ('level281', '0-2 material(s) accessible to children'),
            ('level282', '3-4 material accessible to children'),
            ('level283', '5-6 material accessible to children'),
            ('level284', '7+ material accessible to children'),
        ],
        widget=forms.RadioSelect,required=False,
        )
    
    # for infant
    question29 = forms.ChoiceField(
        choices = [
            ('level291', '0 materials available or not in repair'),
            ('level292', 'Half or less materials are in good repair'),
            ('level293', 'Most materials are in good repair'),
            ('level294', 'Almost all materials are in good repair'),
        ],
        widget=forms.RadioSelect,required=False,
        )
    
    # for toddler
    question30 = forms.ChoiceField(
        choices = [
            ('level301', '2 or less materials available or not in repair'),
            ('level302', 'Half or less materials are in good repair'),
            ('level303', 'Most materials are in good repair'),
            ('level304', 'Almost all materials are in good repair'),
        ],
        widget=forms.RadioSelect,required=False,
        )
    
    # for preschooler
    question31 = forms.ChoiceField(
        choices = [
            ('level311', '2 or less materials available or not in repair'),
            ('level312', 'Half or less materials are in good repair'),
            ('level313', 'Most materials are in good repair'),
            ('level314', 'Almost all materials are in good repair'),
        ],
        widget=forms.RadioSelect,required=False,
        )
    
    # for infant
    audio1 = forms.BooleanField(required=False, label="Audio books", widget=forms.CheckboxInput())
    books1 = forms.BooleanField(required=False, label="Books", widget=forms.CheckboxInput())
    display_pictures1 = forms.BooleanField(required=False, label="Display Pictures (e.g., photographs, paintings)", widget=forms.CheckboxInput())
    environmental_print1 = forms.BooleanField(required=False, label="Environmental Print (e.g., labels, food boxes, words)", widget=forms.CheckboxInput())
    microphone1 = forms.BooleanField(required=False, label="Microphone/Talk tubes ", widget=forms.CheckboxInput())
    language_cards1 = forms.BooleanField(required=False, label="Picture/Language Cards", widget=forms.CheckboxInput())
    storytelling1 = forms.BooleanField(required=False, label="Story telling materials (e.g., flannel boards, velcro, magnets, story blocks)", widget=forms.CheckboxInput())
    other7 = forms.BooleanField(required=False, label="Other", widget=forms.CheckboxInput())

    question32 = forms.ChoiceField(
        choices = [
            ('level321', '0 material(s) accessible to children'),
            ('level322', '1 material accessible to children'),
            ('level323', '2 material accessible to children'),
            ('level324', '3+ material accessible to children'),
        ],
        widget=forms.RadioSelect,required=False,
        )
    
    # for toddler
    alphabet2 = forms.BooleanField(required=False, label="Alphabet materials", widget=forms.CheckboxInput())
    audio2 = forms.BooleanField(required=False, label="Audio books", widget=forms.CheckboxInput())
    books2 = forms.BooleanField(required=False, label="Books", widget=forms.CheckboxInput())
    display_pictures2 = forms.BooleanField(required=False, label="Display Pictures (e.g., photographs, paintings)", widget=forms.CheckboxInput())
    environmental_print2 = forms.BooleanField(required=False, label="Environmental Print (e.g., labels, food boxes, words)", widget=forms.CheckboxInput())
    microphone2 = forms.BooleanField(required=False, label="Microphone/Talk tubes ", widget=forms.CheckboxInput())
    language_cards2 = forms.BooleanField(required=False, label="Picture/Language Cards", widget=forms.CheckboxInput())
    storytelling2 = forms.BooleanField(required=False, label="Story telling materials (e.g., flannel boards, velcro, magnets, story blocks)", widget=forms.CheckboxInput())
    language_games2 = forms.BooleanField(required=False, label="Word and language games", widget=forms.CheckboxInput())
    other8 = forms.BooleanField(required=False, label="Other", widget=forms.CheckboxInput())

    question33 = forms.ChoiceField(
        choices = [
            ('level331', '0-2 material(s) accessible to children'),
            ('level332', '3-4 material accessible to children'),
            ('level333', '5-6 material accessible to children'),
            ('level334', '7+ material accessible to children'),
        ],
        widget=forms.RadioSelect,required=False,
        )

    # for preschooler
    journaling3 = forms.BooleanField(required=False, label="Additional materials for journaling or recording observations, collecting data", widget=forms.CheckboxInput())
    alphabet3 = forms.BooleanField(required=False, label="Alphabet materials", widget=forms.CheckboxInput())
    audio3 = forms.BooleanField(required=False, label="Audio books", widget=forms.CheckboxInput())
    books3 = forms.BooleanField(required=False, label="Books", widget=forms.CheckboxInput())
    display_pictures3 = forms.BooleanField(required=False, label="Display Pictures (e.g., photographs, paintings)", widget=forms.CheckboxInput())
    environmental_print3 = forms.BooleanField(required=False, label="Environmental Print (e.g., labels, food boxes, words)", widget=forms.CheckboxInput())
    microphone3 = forms.BooleanField(required=False, label="Microphone/Talk tubes ", widget=forms.CheckboxInput())
    language_cards3 = forms.BooleanField(required=False, label="Picture/Language Cards", widget=forms.CheckboxInput())
    storytelling3 = forms.BooleanField(required=False, label="Story telling materials (e.g., flannel boards, velcro, magnets, story blocks)", widget=forms.CheckboxInput())
    language_games3 = forms.BooleanField(required=False, label="Word and language games", widget=forms.CheckboxInput())
    other9 = forms.BooleanField(required=False, label="Other", widget=forms.CheckboxInput())

    question34 = forms.ChoiceField(
        choices = [
            ('level341', '0-2 material(s) accessible to children'),
            ('level342', '3-4 material accessible to children'),
            ('level343', '5-6 material accessible to children'),
            ('level344', '7+ material accessible to children'),
        ],
        widget=forms.RadioSelect,required=False,
        )
    
    # for infant
    question35 = forms.ChoiceField(
        choices = [
            ('level351', '0 materials available or not in repair'),
            ('level352', 'Half or less materials are in good repair'),
            ('level353', 'Most materials are in good repair'),
            ('level354', 'Almost all materials are in good repair'),
        ],
        widget=forms.RadioSelect,required=False,
        )
    
    # for toddler
    question36 = forms.ChoiceField(
        choices = [
            ('level361', '2 or less materials available or not in repair'),
            ('level362', 'Half or less materials are in good repair'),
            ('level363', 'Most materials are in good repair'),
            ('level364', 'Almost all materials are in good repair'),
        ],
        widget=forms.RadioSelect,required=False,
        )
    
    # for preschooler
    question37 = forms.ChoiceField(
        choices = [
            ('level371', '2 or less materials available or not in repair'),
            ('level372', 'Half or less materials are in good repair'),
            ('level373', 'Most materials are in good repair'),
            ('level374', 'Almost all materials are in good repair'),
        ],
        widget=forms.RadioSelect,required=False,
        )
    
    # for infant
    bird_feeder1 = forms.BooleanField(required=False, label="Bird Feeder", widget=forms.CheckboxInput())
    building_materials1 = forms.BooleanField(required=False, label="Building Materials", widget=forms.CheckboxInput())
    discovery_bottles1 = forms.BooleanField(required=False, label="Discovery Bottles/Bins", widget=forms.CheckboxInput())
    fill_dump_station1 = forms.BooleanField(required=False, label="Fill and Dump Station", widget=forms.CheckboxInput())
    funnels1 = forms.BooleanField(required=False, label="Funnels and Tubes", widget=forms.CheckboxInput())
    garden1 = forms.BooleanField(required=False, label="Garden", widget=forms.CheckboxInput())
    grid1 = forms.BooleanField(required=False, label="Grid/100 Chart", widget=forms.CheckboxInput())
    hopscotch1 = forms.BooleanField(required=False, label="Hopscotch", widget=forms.CheckboxInput())
    living_animals1 = forms.BooleanField(required=False, label="Living Animals", widget=forms.CheckboxInput())
    magnifying_glasses1 = forms.BooleanField(required=False, label="Magnifying Glass", widget=forms.CheckboxInput())
    matching_games1 = forms.BooleanField(required=False, label="Matching Games", widget=forms.CheckboxInput())
    mirrors1 = forms.BooleanField(required=False, label="Mirrors", widget=forms.CheckboxInput())
    numbers1 = forms.BooleanField(required=False, label="Numbers", widget=forms.CheckboxInput())
    prism1 = forms.BooleanField(required=False, label="Prism/Color tiles", widget=forms.CheckboxInput())
    rolling_ramps1 = forms.BooleanField(required=False, label="Rolling Ramps", widget=forms.CheckboxInput())
    slime1 = forms.BooleanField(required=False, label="Slime/goop/shaving cream/bubbles", widget=forms.CheckboxInput()) 
    sorting_containers1 = forms.BooleanField(required=False, label="Sorting Containers", widget=forms.CheckboxInput())
    varying_size_containers1 = forms.BooleanField(required=False, label="Varying Size Containers(Atleast 2 sizes)", widget=forms.CheckboxInput())
    visual_patterns1 = forms.BooleanField(required=False, label="Visual Patterns", widget=forms.CheckboxInput())
    wind_chimes1 = forms.BooleanField(required=False, label="Wind Chimes/pinwheel", widget=forms.CheckboxInput())
    other10 = forms.BooleanField(required=False, label="Other", widget=forms.CheckboxInput())

    question38 = forms.ChoiceField(
        choices = [
            ('level381', '0-2 material(s) accessible to children'),
            ('level382', '3-4 material accessible to children'),
            ('level383', '5-6 material accessible to children'),
            ('level384', '7+ material accessible to children'),
        ],
        widget=forms.RadioSelect,required=False,
        )
    
    # for toddler
    bird_feeder2 = forms.BooleanField(required=False, label="Bird Feeder", widget=forms.CheckboxInput())
    building_materials2 = forms.BooleanField(required=False, label="Building Materials", widget=forms.CheckboxInput())
    discovery_bottles2 = forms.BooleanField(required=False, label="Discovery Bottles/Bins", widget=forms.CheckboxInput())
    fill_dump_station2 = forms.BooleanField(required=False, label="Fill and Dump Station", widget=forms.CheckboxInput())
    funnels2 = forms.BooleanField(required=False, label="Funnels and Tubes", widget=forms.CheckboxInput())
    garden2 = forms.BooleanField(required=False, label="Garden", widget=forms.CheckboxInput())
    hopscotch2 = forms.BooleanField(required=False, label="Hopscotch", widget=forms.CheckboxInput())
    living_animals2 = forms.BooleanField(required=False, label="Living Animals", widget=forms.CheckboxInput())
    magnifying_glasses2 = forms.BooleanField(required=False, label="Magnifying Glass", widget=forms.CheckboxInput())
    matching_games2 = forms.BooleanField(required=False, label="Matching Games", widget=forms.CheckboxInput())
    mirrors2 = forms.BooleanField(required=False, label="Mirrors", widget=forms.CheckboxInput())
    numbers2 = forms.BooleanField(required=False, label="Numbers", widget=forms.CheckboxInput())
    prism2 = forms.BooleanField(required=False, label="Prism/Color tiles", widget=forms.CheckboxInput())
    recording_temp2 = forms.BooleanField(required=False, label="Recording temp/rain", widget=forms.CheckboxInput())
    rolling_ramps2 = forms.BooleanField(required=False, label="Rolling Ramps", widget=forms.CheckboxInput())
    scales2 = forms.BooleanField(required=False, label="Scales", widget=forms.CheckboxInput())
    slime2 = forms.BooleanField(required=False, label="Slime/goop/shaving cream/bubbles", widget=forms.CheckboxInput())
    sorting_containers2 = forms.BooleanField(required=False, label="Sorting Containers", widget=forms.CheckboxInput())
    spinners2 = forms.BooleanField(required=False, label="Spinners", widget=forms.CheckboxInput())
    steps2 = forms.BooleanField(required=False, label="Steps/Visual Schedule", widget=forms.CheckboxInput())
    varying_size_containers2 = forms.BooleanField(required=False, label="Varying Size Containers(Atleast 2 sizes)", widget=forms.CheckboxInput())
    visual_patterns2 = forms.BooleanField(required=False, label="Visual Patterns", widget=forms.CheckboxInput())
    wind_chimes2 = forms.BooleanField(required=False, label="Wind Chimes/pinwheel", widget=forms.CheckboxInput())
    other11 = forms.BooleanField(required=False, label="Other", widget=forms.CheckboxInput())

    question39 = forms.ChoiceField(
        choices = [
            ('level391', '0-2 material(s) accessible to children'),
            ('level392', '3-4 material accessible to children'),
            ('level393', '5-6 material accessible to children'),
            ('level394', '7+ material accessible to children'),
        ],
        widget=forms.RadioSelect,required=False,
        )
    
    # for preschooler
    bird_feeder3 = forms.BooleanField(required=False, label="Bird Feeder", widget=forms.CheckboxInput())
    building_materials3 = forms.BooleanField(required=False, label="Building Materials", widget=forms.CheckboxInput())
    dice3 = forms.BooleanField(required=False, label="Dice", widget=forms.CheckboxInput())
    discovery_bottles3 = forms.BooleanField(required=False, label="Discovery Bottles/Bins", widget=forms.CheckboxInput())   
    fill_dump_station3 = forms.BooleanField(required=False, label="Fill and Dump Station", widget=forms.CheckboxInput())
    funnels3 = forms.BooleanField(required=False, label="Funnels and Tubes", widget=forms.CheckboxInput())
    garden3 = forms.BooleanField(required=False, label="Garden", widget=forms.CheckboxInput())
    grid3 = forms.BooleanField(required=False, label="Grid/100 Chart", widget=forms.CheckboxInput())
    hopscotch3 = forms.BooleanField(required=False, label="Hopscotch", widget=forms.CheckboxInput())
    living_animals3 = forms.BooleanField(required=False, label="Living Animals", widget=forms.CheckboxInput())
    magnifying_glasses3 = forms.BooleanField(required=False, label="Magnifying Glass", widget=forms.CheckboxInput())
    matching_games3 = forms.BooleanField(required=False, label="Matching Games", widget=forms.CheckboxInput())
    mirrors3 = forms.BooleanField(required=False, label="Mirrors", widget=forms.CheckboxInput())
    numbers3 = forms.BooleanField(required=False, label="Numbers", widget=forms.CheckboxInput())
    prism3 = forms.BooleanField(required=False, label="Prism/Color tiles", widget=forms.CheckboxInput())
    pulleys3 = forms.BooleanField(required=False, label="Pulleys/Levers", widget=forms.CheckboxInput())
    recording_temp3 = forms.BooleanField(required=False, label="Recording temp/rain", widget=forms.CheckboxInput())
    rolling_ramps3 = forms.BooleanField(required=False, label="Rolling Ramps", widget=forms.CheckboxInput())
    scales3 = forms.BooleanField(required=False, label="Scales", widget=forms.CheckboxInput())
    slime3 = forms.BooleanField(required=False, label="Slime/goop/shaving cream/bubbles", widget=forms.CheckboxInput())
    sorting_containers3 = forms.BooleanField(required=False, label="Sorting Containers", widget=forms.CheckboxInput())
    spinners3 = forms.BooleanField(required=False, label="Spinners", widget=forms.CheckboxInput())
    steps3 = forms.BooleanField(required=False, label="Steps/Visual Schedule", widget=forms.CheckboxInput())
    timers3 = forms.BooleanField(required=False, label="Timer/Stopwatchers", widget=forms.CheckboxInput())
    varying_size_containers3 = forms.BooleanField(required=False, label="Varying Size Containers(Atleast 2 sizes)", widget=forms.CheckboxInput())
    visual_patterns3 = forms.BooleanField(required=False, label="Visual Patterns", widget=forms.CheckboxInput())
    wind_chimes3 = forms.BooleanField(required=False, label="Wind Chimes/pinwheel", widget=forms.CheckboxInput())
    other12 = forms.BooleanField(required=False, label="Other", widget=forms.CheckboxInput())

    question40 = forms.ChoiceField(
        choices = [
            ('level401', '0-2 material(s) accessible to children'),
            ('level402', '3-4 material accessible to children'),
            ('level403', '5-6 material accessible to children'),
            ('level404', '7+ material accessible to children'),
        ],
        widget=forms.RadioSelect,required=False,
        )
    
    # for infant
    question41 = forms.ChoiceField(
        choices = [
            ('level411', '2 or less materials available or not in repair'),
            ('level412', 'Half or less materials are in good repair'),
            ('level413', 'Most materials are in good repair'),
            ('level414', 'Almost all materials are in good repair'),
        ],
        widget=forms.RadioSelect,required=False,
        )
    
    # for toddler
    question42 = forms.ChoiceField(
        choices = [
            ('level421', '2 or less materials available or not in repair'),
            ('level422', 'Half or less materials are in good repair'),
            ('level423', 'Most materials are in good repair'),
            ('level424', 'Almost all materials are in good repair'),
        ],
        widget=forms.RadioSelect,required=False,
        )
    
    # for preschooler
    question43 = forms.ChoiceField(
        choices = [
            ('level431', '2 or less materials available or not in repair'),
            ('level432', 'Half or less materials are in good repair'),
            ('level433', 'Most materials are in good repair'),
            ('level434', 'Almost all materials are in good repair'),
        ],
        widget=forms.RadioSelect,required=False,
        )
    
    # for infant
    animal_figures1 = forms.BooleanField(required=False, label="Animal Figures", widget=forms.CheckboxInput())
    crayons1 = forms.BooleanField(required=False, label="Crayons/Pens/Pencils/Markers", widget=forms.CheckboxInput())
    child_sized_furniture1 = forms.BooleanField(required=False, label="Child-Sized Furniture", widget=forms.CheckboxInput())
    collage_materials1 = forms.BooleanField(required=False, label="Collage Materials with differnt textures", widget=forms.CheckboxInput())
    cooking_eating_equipment1 = forms.BooleanField(required=False, label="Cooking eating equipment (e.g., pots and pans, dishes, spoons)", widget=forms.CheckboxInput())
    dolls1 = forms.BooleanField(required=False, label="Dolls/Puppets", widget=forms.CheckboxInput())
    dress_up1 = forms.BooleanField(required=False, label="Dress Up Clothes", widget=forms.CheckboxInput())
    easels1 = forms.BooleanField(required=False, label="Easels(functional with eg chalk/paint)", widget=forms.CheckboxInput())
    musical_instruments1 = forms.BooleanField(required=False, label="Musical instruments or instruments to make music (e.g., pans, buckets, sticks)", widget=forms.CheckboxInput())
    paint_brushes1 = forms.BooleanField(required=False, label="Paint Brushes", widget=forms.CheckboxInput())
    paints1 = forms.BooleanField(required=False, label="Paints", widget=forms.CheckboxInput())
    paper_cardboard1 = forms.BooleanField(required=False, label="Paper/Cardboard", widget=forms.CheckboxInput())
    play_dough1 = forms.BooleanField(required=False, label="Play Dough", widget=forms.CheckboxInput())
    soft_animals1 = forms.BooleanField(required=False, label="Soft Animals", widget=forms.CheckboxInput())
    toy_telephones1 = forms.BooleanField(required=False, label="Toy Telephones", widget=forms.CheckboxInput())

    question44 = forms.ChoiceField(
        choices = [
            ('level441', '0-2 material(s) accessible to children'),
            ('level442', '3-4 material accessible to children'),
            ('level443', '5-6 material accessible to children'),
            ('level444', '7+ material accessible to children'),
        ],
        widget=forms.RadioSelect,required=False,
        )
    
    # for toddler
    animal_figures2 = forms.BooleanField(required=False, label="Animal Figures", widget=forms.CheckboxInput())
    crayons2 = forms.BooleanField(required=False, label="Crayons/Pens/Pencils/Markers", widget=forms.CheckboxInput())
    child_sized_furniture2 = forms.BooleanField(required=False, label="Child-Sized Furniture", widget=forms.CheckboxInput())
    collage_materials2 = forms.BooleanField(required=False, label="Collage Materials with differnt textures", widget=forms.CheckboxInput())
    cooking_eating_equipment2 = forms.BooleanField(required=False, label="Cooking eating equipment (e.g., pots and pans, dishes, spoons)", widget=forms.CheckboxInput())
    dolls2 = forms.BooleanField(required=False, label="Dolls/Puppets", widget=forms.CheckboxInput())
    dress_up2 = forms.BooleanField(required=False, label="Dress Up Clothes", widget=forms.CheckboxInput())
    easels2 = forms.BooleanField(required=False, label="Easels(functional with eg chalk/paint)", widget=forms.CheckboxInput())
    musical_instruments2 = forms.BooleanField(required=False, label="Musical instruments or instruments to make music (e.g., pans, buckets, sticks)", widget=forms.CheckboxInput())
    paint_brushes2 = forms.BooleanField(required=False, label="Paint Brushes", widget=forms.CheckboxInput())
    paints2 = forms.BooleanField(required=False, label="Paints", widget=forms.CheckboxInput())
    paper_cardboard2 = forms.BooleanField(required=False, label="Paper/Cardboard", widget=forms.CheckboxInput())
    play_dough2 = forms.BooleanField(required=False, label="Play Dough", widget=forms.CheckboxInput())
    soft_animals2 = forms.BooleanField(required=False, label="Soft Animals", widget=forms.CheckboxInput())
    toy_telephones2 = forms.BooleanField(required=False, label="Toy Telephones", widget=forms.CheckboxInput())  
    
    question45 = forms.ChoiceField(
        choices = [
            ('level451', '0-2 material(s) accessible to children'),
            ('level452', '3-4 material accessible to children'),
            ('level453', '5-6 material accessible to children'),
            ('level454', '7+ material accessible to children'),
        ],
        widget=forms.RadioSelect,required=False,
        )
    
    # for preschooler
    animal_figures3 = forms.BooleanField(required=False, label="Animal Figures", widget=forms.CheckboxInput())
    crayons3 = forms.BooleanField(required=False, label="Crayons/Pens/Pencils/Markers", widget=forms.CheckboxInput())
    child_sized_furniture3 = forms.BooleanField(required=False, label="Child-Sized Furniture", widget=forms.CheckboxInput())
    collage_materials3 = forms.BooleanField(required=False, label="Collage Materials with differnt textures", widget=forms.CheckboxInput())
    cooking_eating_equipment3 = forms.BooleanField(required=False, label="Cooking eating equipment (e.g., pots and pans, dishes, spoons)", widget=forms.CheckboxInput())
    dolls3 = forms.BooleanField(required=False, label="Dolls/Puppets", widget=forms.CheckboxInput())
    dress_up3 = forms.BooleanField(required=False, label="Dress Up Clothes", widget=forms.CheckboxInput())
    easels3 = forms.BooleanField(required=False, label="Easels(functional with eg chalk/paint)", widget=forms.CheckboxInput())
    musical_instruments3 = forms.BooleanField(required=False, label="Musical instruments or instruments to make music (e.g., pans, buckets, sticks)", widget=forms.CheckboxInput())
    paint_brushes3 = forms.BooleanField(required=False, label="Paint Brushes", widget=forms.CheckboxInput())
    paints3 = forms.BooleanField(required=False, label="Paints", widget=forms.CheckboxInput())
    paper_cardboard3 = forms.BooleanField(required=False, label="Paper/Cardboard", widget=forms.CheckboxInput())
    play_dough3 = forms.BooleanField(required=False, label="Play Dough", widget=forms.CheckboxInput())
    soft_animals3 = forms.BooleanField(required=False, label="Soft Animals", widget=forms.CheckboxInput())
    toy_telephones3 = forms.BooleanField(required=False, label="Toy Telephones", widget=forms.CheckboxInput())

    question46 = forms.ChoiceField(
        choices = [
            ('level461', '0-2 material(s) accessible to children'),
            ('level462', '3-4 material accessible to children'),
            ('level463', '5-6 material accessible to children'),
            ('level464', '7+ material accessible to children'),
        ],
        widget=forms.RadioSelect,required=False,
        )
    
    # for infant
    question47 = forms.ChoiceField(
        choices = [
            ('level471', '2 or less materials available or not in repair'),
            ('level472', 'Half or less materials are in good repair'),
            ('level473', 'Most materials are in good repair'),
            ('level474', 'Almost all materials are in good repair'),
        ],
        widget=forms.RadioSelect,required=False,
        )
    
    # for toddler
    question48 = forms.ChoiceField(
        choices = [
            ('level481', '2 or less materials available or not in repair'),
            ('level482', 'Half or less materials are in good repair'),
            ('level483', 'Most materials are in good repair'),
            ('level484', 'Almost all materials are in good repair'),
        ],
        widget=forms.RadioSelect,required=False,
        )
    
    # for preschooler
    question49 = forms.ChoiceField(
        choices = [
            ('level491', '2 or less materials available or not in repair'),
            ('level492', 'Half or less materials are in good repair'),
            ('level493', 'Most materials are in good repair'),
            ('level494', 'Almost all materials are in good repair'),
        ],
        widget=forms.RadioSelect,required=False,
        )
    
    question50 = forms.ChoiceField(
        choices = [
            ('level501', 'There is no written plan related to outdoor time'),
            ('level502', 'There is a plan for outdoor time, but it looks like an outline, with just a few words, and vague definitions of activities children already do. There are no phrases describing what is going to be done'),
            ('level503', 'The plan for outdoor time includes 1 activity related to 1 area of the program on that day. There is enough detail so that someone can implement the activity, and/or understand how the development of the activity will proceed.'),
            ('level504', 'The plan for outdoor time includes 2 activities or more related to 2 or more areas of the program on that day. Planning includes a rationale that addresses individual child or classroom needs/goals.'),
        ],  
        widget=forms.RadioSelect,required=True,
        )
    
class Page6Form(forms.Form):
    question51 = forms.ChoiceField(
        choices = [
            ('level511', 'Little language is used, or language used is relevant to teachers perspectives rather than contingent on childrens activities and interests.'),
            ('level512', 'Teachers used some language relevant to childrens interests and activities; teachers language tends to be related to teachers interests, perspectives, or other duties. Verbalizations often restrict use of materials when guiding behaviors.'),
            ('level513', 'Teachers’ language related to childrens interests and activities occurs regularly; language related to teachers interests, perspectives, or other duties occurs for more than a few minutes. Verbalizations may restrict use of materials when guiding behaviors'),
            ('level514', 'Teachers’ language is consistently related to what children are playing with or looking at, what they are focused on or doing. Any restriction verbalization is related to safety/hazard.'),
        ],
        widget=forms.RadioSelect,required=True,
        )
    
    question52 = forms.ChoiceField(
        choices = [
            ('level521', 'Interactions are primarily for correction or instructions. The quantity of interactions may be very low. The teacher may be intrusive, dismissive or negative toward children. Children’s cues or bids are largely ignored'),
            ('level522', 'Some warm teacher-child interactions with children occur, and some instances of intrusion may occur. Teacher shows a positive response to a child’s bid or cue, but this does not occur often or only to a few select children.'),
            ('level523', 'Warm and positive teacher interactions occur several times and with different children. Most of children’s bids and cues are responded to or teachers occasionally initiate interactions with children who do not show bids/cues. Occasional instances of intrusion can occur. '),
            ('level524', 'Teachers consistently exhibit warm and positive interactions with various children.  Children’s bids and cues are almost always responded to or teachers initiate interactions with children who do not show bids/cues. Any instances of intrusion are situationally appropriate.'),
        ],
        widget=forms.RadioSelect,required=True,
        )
    
    question53 = forms.ChoiceField(
        choices = [
            ('level531', 'Teachers inhibit/ prohibit interactions with materials, or interrupt children’s interests or focus. Or teachers do not acknowledge and/or promote children’s persistence and learning.'),
            ('level532', 'Teachers offer or encourage children’s use of a few materials or acknowledge engagement using simple comments/ questions. '),
            ('level533', 'Teachers are sensitive to children’s interests and may offer materials that interest children but may not promote extended exploration of materials or areas, or how to use or think about materials in different ways. Teachers ask some open-ended questions, but this is not consistent '),
            ('level534', 'Teachers may offer several materials, or alternative ways of using materials and/or follow children’s lead in exploring concepts and discoveries by asking open-ended questions, challenging their thinking/abilities, and scaffolding* their learning.'),
        ],
        widget=forms.RadioSelect,required=True,
        )
    
    question54 = forms.ChoiceField(
        choices = [
            ('level541', 'Teachers are visually supervising and rarely physically engaged with children/ materials. '),
            ('level542', 'Teachers are physically close to children but show limited physical engagement and/or modeling with them. '),
            ('level543', 'Teachers sometimes participate in shared play and reciprocal interactions (e.g., where teachers model inquisitiveness or exploration), but this participation does not last. They may offer or start some activities.'),
            ('level544', 'Teachers offer and start activities and continue to engage in the activities/play with extended interactions. Teachers are at children’s level and physically engaged by sharing activities and encouraging joint attention. Multiple examples of reciprocal/shared interactions (where teachers are modeling inquisitiveness or exploration) are observed between teachers and children.'),
        ],
        widget=forms.RadioSelect,required=True,
        )
    
    question55 = forms.ChoiceField(
        choices = [
            ('level551', 'Little support is provided for positive peer interactions and challenging situations'),
            ('level552', 'Some support for solving challenging situations. When support is given, it is usually vague (i.e., not giving problem-solving strategies) and/or not appropriate to the developmental level of the children'),
            ('level553', 'Some examples of support for positive peer interactions, but this is not consistent. Support is mostly given to children when there is conflict or challenging situations. '),
            ('level554', 'Teachers consistently support positive peer interaction and challenging situations if it is needed. Support and/or encouragement for positive peer interactions is given to children even if there is no conflict. '),
        ],
        widget=forms.RadioSelect,required=True,
        )
    
    question56 = forms.ChoiceField(
        choices= [
            ('level561', 'There is no natural environment or children are prohibited from engaging with the natural environment.'),
            ('level562', 'Teachers discourage interactions with the natural environment or do not encourage further exploration.'),
            ('level563', 'Teachers allow children to experience or interact with natural elements/environment. They minimally encourage and/or are passive about children’s engagement with the natural environment.'),
            ('level564', 'Teachers encourage children to be actively engaged with natural elements/environment by using their senses and skills to manipulate and explore it. '),
        ],
        widget=forms.RadioSelect,required=True,
        )
    
    question57 = forms.ChoiceField(
        choices= [
            ('level571', 'There are no children engaging with natural elements or the natural environment.'),
            ('level572', 'Child(ren)* notice natural elements/ environment but do not engage/spend time exploring it or are stopped from exploring further'),
            ('level573', 'Child(ren) display curiosity of and exploration with natural elements/environment for a short period of time'),
            ('level574', 'Child(ren) display curiosity of and exploration with the natural elements/environment for a sustained period of time. '),
        ],
        widget=forms.RadioSelect,required=True,
        )
    
    question58 = forms.ChoiceField(
        choices= [
            ('level581', 'There are no children engaging with the natural environment'),
            ('level582', 'One child engages with the natural environment'),
            ('level583', 'More than one but half or less of the children engage with the natural environment'),
            ('level584', 'More than half of the children engage with the natural environment'),
        ],
        widget=forms.RadioSelect,required=True,
        )
    
    question59 = forms.ChoiceField(
        choices = [
            ('level591', 'Children spend all their time in required teacher-led whole or small group activities.No or few options for child-directed activities exist'),
            ('level592', 'Children spend most of their time in the required teacher-led small/large group activities. Children have little time to engage in activities of their choice'),
            ('level593', 'Children spend almost half their time in teacher-led small/large group activities. Teacher-led activities do not take up the whole time. Children have half or more of their time to engage in activities of their choice'),
            ('level594', 'Children can choose their activities and direct their own learning. Small or large group activities are optional or short in duration when offered. Group activities may happen spontaneously.'),
        ],
        widget=forms.RadioSelect,required=True,
        )
    
    question60 = forms.ChoiceField(
        choices = [
            ('level601', 'Climate is characterized by disrespect and harsh interactions, or teachers ignore children. There is no enthusiasm.'),
            ('level602', 'The climate is generally neutral with few instances of enthusiasm, affection, or respect shown between children and adults. There might be instances of sarcasm.'),
            ('level603', 'The climate is generally neutral with some periods of enthusiasm, affection, and respect shown by teachers and children'),
            ('level604', 'A consistently positive climate is demonstrated by sustained affection, enthusiastic, and respectful interactions that are just as likely to occur between any of the children and teachers'),
        ],
        widget=forms.RadioSelect,required=True,
        )

