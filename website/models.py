from django.db import models

# Create your models here.

class OPALS(models.Model):
    # page1 fields
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(
        max_length=100,
        choices=[
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
        ]
    )
    zip_code = models.CharField(max_length=10)

    # page2 fields - Yes/No questions
    YES_NO_CHOICES = [('Yes', 'Yes'), ('No', 'No')]
    
    question1 = models.CharField(max_length=100, blank=True, null=True, choices=YES_NO_CHOICES)
    question2 = models.CharField(max_length=100, blank=True, null=True, choices=YES_NO_CHOICES)
    question3 = models.CharField(max_length=100, blank=True, null=True, choices=YES_NO_CHOICES)
    question4 = models.CharField(max_length=100, blank=True, null=True, choices=YES_NO_CHOICES)
    question5 = models.CharField(max_length=100, blank=True, null=True, choices=YES_NO_CHOICES)
    question6 = models.CharField(max_length=100, blank=True, null=True, choices=YES_NO_CHOICES)
    question7 = models.CharField(max_length=100, blank=True, null=True, choices=YES_NO_CHOICES)
    question8 = models.CharField(max_length=100, blank=True, null=True, choices=YES_NO_CHOICES)
    question9 = models.CharField(max_length=100, blank=True, null=True, choices=YES_NO_CHOICES)
    question10 = models.CharField(max_length=100, blank=True, null=True, choices=YES_NO_CHOICES)
    question11 = models.CharField(max_length=100, blank=True, null=True, choices=YES_NO_CHOICES)
    question12 = models.CharField(max_length=100, blank=True, null=True, choices=YES_NO_CHOICES)
    
    # page3 fields - multi-level questions
    QUESTION13_CHOICES = [
        ('level131', 'No patch(es) of shade.'),
        ('level132', 'Patch(es) of shade sufficient for a few children.'),
        ('level133', 'Patch(es) of shade sufficient for most children.'),
        ('level134', 'Patch(es) of shade sufficient for all children.')
    ]
    
    QUESTION14_15_CHOICES = [
        ('level141', 'As calculated by formula, 0% to 29% sufficient trees.'),
        ('level142', 'As calculated by formula, 30% to 64% sufficient trees.'),
        ('level143', 'As calculated by formula, 65% to 99% sufficient trees.'),
        ('level144', 'As calculated by formula, 100% or more of sufficient trees.')
    ]
    
    QUESTION16_CHOICES = [
        ('level161', 'No fruit or vegetables garden.'),
        ('level162', 'There is a vegetable or fruit garden with limited produce to taste or use for snacks/ meals.'),
        ('level163', 'There is a fruit and vegetable garden with enough produce for some of the children to taste or use for snacks/meals.'),
        ('level164', 'There is a fruit and vegetable garden with abundant produce for all children to taste or use for snacks/meals.'),
        ('level165', 'N/A')
    ]
    
    QUESTION17_CHOICES = [
        ('level171', 'There is no outdoor storage'),
        ('level172', 'There are open storage containers (e.g. crates, open boxes'),
        ('level173', 'There is at least one enclosed closet or chest or sheltered outdoor shelving.'),
        ('level174', 'There is more than one enclosed closet or chest or sheltered outdoor shelving.'),
        ('level175', 'N/A')
    ]

    QUESTION18_CHOICES = [
        ('level181', 'There is no outdoor storage'),
        ('level182', 'There is at least one enclosed closet or chest or sheltered outdoor shelving.'),
        ('level183', 'There is at least one enclosed closet or chest or sheltered outdoor shelving and covered wheeled toy storage.'),
        ('level184', 'There is at least one enclosed closet or chest or sheltered outdoor shelving and covered wheeled toy storage, and a secure walk-in storage shed.'),
        ('level185', 'N/A'),
    ]
    
    question13 = models.CharField(max_length=100, blank=True, null=True, choices=QUESTION13_CHOICES)
    question14 = models.CharField(max_length=100, blank=True, null=True, choices=QUESTION14_15_CHOICES)
    question15 = models.CharField(max_length=100, blank=True, null=True, choices=QUESTION14_15_CHOICES)
    question16 = models.CharField(max_length=100, blank=True, null=True, choices=QUESTION16_CHOICES)
    question17 = models.CharField(max_length=100, blank=True, null=True, choices=QUESTION17_CHOICES)
    question18 = models.CharField(max_length=100, blank=True, null=True, choices=QUESTION18_CHOICES)

    breast_feeding = models.BooleanField(default=False)
    indoor_outdoor_transition1 = models.BooleanField(default=False)
    deck1 = models.BooleanField(default=False)
    diaper_changing_station = models.BooleanField(default=False)
    gathering_setting1 = models.BooleanField(default=False)
    grove_trees1 = models.BooleanField(default=False)
    mound1 = models.BooleanField(default=False)
    manufactured_play1 = models.BooleanField(default=False)
    multipurpose_lawn1 = models.BooleanField(default=False)
    multisensory_pathway1 = models.BooleanField(default=False)
    multisensory_setting1 = models.BooleanField(default=False)
    music_play1 = models.BooleanField(default=False)
    playhouse1 = models.BooleanField(default=False)
    pollinator_garden1 = models.BooleanField(default=False)
    porch_swing1 = models.BooleanField(default=False)
    primary_pathway1 = models.BooleanField(default=False)
    ramp1 = models.BooleanField(default=False)
    sand_play1 = models.BooleanField(default=False)
    small_bridge = models.BooleanField(default=False)
    steppingstone_pathway1 = models.BooleanField(default=False)
    tent_structures1 = models.BooleanField(default=False)
    textured_panel = models.BooleanField(default=False)
    water_play_hands_1 = models.BooleanField(default=False)
    other1 = models.BooleanField(default=False)
    
    # Infant total settings radio button
    question19 = models.CharField(max_length=10, blank=True, null=True,
                                  choices=[
                                      ('level191', '0-2 settings'),
                                        ('level192', '3-5 settings'),
                                        ('level193', '6-8 settings'),
                                        ('level194', '9-11 settings'),
                                  ],
                                )

    
    # Toddler settings checkboxes
    area_pets1 = models.BooleanField(default=False)
    indoor_outdoor_transition2 = models.BooleanField(default=False)
    cozy_nook1 = models.BooleanField(default=False)
    balance_beam1 = models.BooleanField(default=False)
    bridge1 = models.BooleanField(default=False)
    deck2 = models.BooleanField(default=False)
    earth_play1 = models.BooleanField(default=False)
    editable_landscape1 = models.BooleanField(default=False)
    fruit_garden1 = models.BooleanField(default=False)
    gathering_setting2 = models.BooleanField(default=False)
    grove_trees2 = models.BooleanField(default=False)
    hard_surface1 = models.BooleanField(default=False)
    loose_parts1 = models.BooleanField(default=False)
    manufactured_play2 = models.BooleanField(default=False)
    mound2 = models.BooleanField(default=False)
    multipurpose_lawn2 = models.BooleanField(default=False)
    multisensory_pathway2 = models.BooleanField(default=False)
    multisensory_setting2 = models.BooleanField(default=False)
    music_play2 = models.BooleanField(default=False)
    outdoor_classroom1 = models.BooleanField(default=False)
    playhouse2 = models.BooleanField(default=False)
    pollinator_garden2 = models.BooleanField(default=False)
    porch_swing2 = models.BooleanField(default=False)
    primary_pathway2 = models.BooleanField(default=False)
    project_space = models.BooleanField(default=False)
    ramp2 = models.BooleanField(default=False)
    sand_play2 = models.BooleanField(default=False)
    steppingstone_pathway2 = models.BooleanField(default=False)
    swing1 = models.BooleanField(default=False)
    table1 = models.BooleanField(default=False)
    tent_structures2 = models.BooleanField(default=False)
    water_play_hands_2 = models.BooleanField(default=False)
    water_play_body_1 = models.BooleanField(default=False)
    other2 = models.BooleanField(default=False)
    
    # Toddler total settings radio button
    question20 = models.CharField(max_length=10, blank=True, null=True,
                                  choices=[
                                      ('level201', '0-2 settings'),
                                      ('level202', '3-5 settings'),
                                      ('level203', '6-8 settings'),
                                      ('level204', '9-11 settings'),
                                      ],
                                    )

    
    # Preschool settings checkboxes
    area_pets2 = models.BooleanField(default=False)
    balance_beam = models.BooleanField(default=False)
    bridge2 = models.BooleanField(default=False)
    indoor_outdoor_transition3 = models.BooleanField(default=False)
    cozy_nook2 = models.BooleanField(default=False)
    deck3 = models.BooleanField(default=False)
    dry_creek_bed = models.BooleanField(default=False)
    earth_play2 = models.BooleanField(default=False)
    editable_landscape2 = models.BooleanField(default=False)
    fruit_garden2 = models.BooleanField(default=False)
    gathering_setting3 = models.BooleanField(default=False)
    grass_maze = models.BooleanField(default=False)
    grove_trees3 = models.BooleanField(default=False)
    hard_surface2 = models.BooleanField(default=False)
    loose_parts2 = models.BooleanField(default=False)
    manufactured_play3 = models.BooleanField(default=False)
    mound3 = models.BooleanField(default=False)
    multipurpose_lawn3 = models.BooleanField(default=False)
    multisensory_pathway3 = models.BooleanField(default=False)
    multisensory_setting3 = models.BooleanField(default=False)
    music_play3 = models.BooleanField(default=False)
    natural_construction_area = models.BooleanField(default=False)
    outdoor_classroom2 = models.BooleanField(default=False)
    performance_space = models.BooleanField(default=False)
    playhouse3 = models.BooleanField(default=False)
    pollinator_garden3 = models.BooleanField(default=False)
    primary_pathway3 = models.BooleanField(default=False)
    project_space2 = models.BooleanField(default=False)
    ramp3 = models.BooleanField(default=False)
    sand_play3 = models.BooleanField(default=False)
    steppingstone_pathway3 = models.BooleanField(default=False)
    swing2 = models.BooleanField(default=False)
    table2 = models.BooleanField(default=False)
    tent_structures3 = models.BooleanField(default=False)
    water_play_hands_3 = models.BooleanField(default=False)
    water_play_body_2 = models.BooleanField(default=False)
    woodwork_bench = models.BooleanField(default=False)
    other3 = models.BooleanField(default=False)
    
    # Preschool total settings radio button
    question21 = models.CharField(max_length=10, blank=True, null=True,
                                  choices=[
                                      ('level211', '0-2 settings'),
                                      ('level212', '3-5 settings'),
                                      ('level213', '6-8 settings'),
                                      ('level214', '9-11 settings'),
                                  ],
                                )
