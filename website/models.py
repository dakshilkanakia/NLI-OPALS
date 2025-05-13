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
    age_groups = models.CharField(max_length=255, 
                                default='',
                                help_text="Comma-separated age groups (e.g. Infant,Toddler,Preschool)")

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
    
    # waiting for  Robin
    # question22 = models.CharField(max_length=10, blank=True, null=True,
    #                               choices=[
    #                                   ('level221', '0-2 settings'),
    #                                   ('level222', '3-5 settings'),
    #                                   ('level223', '6-8 settings'),
    #                                   ('level224', '9-11 settings'),
    #                               ],
    #                             )
    # question23 = models.CharField(max_length=10, blank=True, null=True,
    #                               choices=[
    #                                   ('level231', '0-2 settings'),
    #                                   ('level232', '3-5 settings'),
    #                                   ('level233', '6-8 settings'),
    #                                   ('level234', '9-11 settings'),
    #                               ],
    #                             )
    question24 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level241', 'There is no multipurpose activity settings/lawn.'),
                                    ('level242', 'Multipurpose activity setting/lawn sufficient for only a few children to use together.'),
                                    ('level243', 'A medium size multipurpose activity setting/lawn large enough for at least half a class of children to use together.'),
                                    ('level244', 'A large multipurpose activity setting/lawn large enough for all children in a class to use together.'),
                                ],
                                )

    question25 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level251', 'There is no covered outdoor classroom/gathering place.'),
                                    ('level252', 'There is a covered outdoor classroom/gathering place large enough for only a small, informal group of children to use together with teacher.'),
                                    ('level253', 'There is a medium size covered outdoor classroom/gathering place large enough for at least half a class to use together with teacher.'),
                                    ('level254', 'There is a large covered outdoor classroom/gathering place large enough for all children in a class to use together with teacher.'),
                                ],
                                )

    # page5 fields
    # Infant gross motor activities
    balancing1 = models.BooleanField(default=False)
    bouncing1 = models.BooleanField(default=False)
    bowling1 = models.BooleanField(default=False)
    brachiating1 = models.BooleanField(default=False)
    climbing1 = models.BooleanField(default=False)
    crawling1 = models.BooleanField(default=False)
    dribbling1 = models.BooleanField(default=False)
    drumming1 = models.BooleanField(default=False)
    hula_hopping1 = models.BooleanField(default=False)
    kicking1 = models.BooleanField(default=False)
    rocking1 = models.BooleanField(default=False)
    sliding1 = models.BooleanField(default=False)
    throwing1 = models.BooleanField(default=False)
    other4 = models.BooleanField(default=False)

    question26 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level261', '0 material(s) accessible to children'),
                                    ('level262', '1-2 material accessible to children'),
                                    ('level263', '3-4 material accessible to children'),
                                    ('level264', '5+ material accessible to children'),
                                ])

    # Toddler gross motor activities
    balancing2 = models.BooleanField(default=False)
    bouncing2 = models.BooleanField(default=False)
    bowling2 = models.BooleanField(default=False)
    brachiating2 = models.BooleanField(default=False)
    climbing2 = models.BooleanField(default=False)
    crawling2 = models.BooleanField(default=False)
    dancing2 = models.BooleanField(default=False)
    digging2 = models.BooleanField(default=False)
    dribbling2 = models.BooleanField(default=False)
    drumming2 = models.BooleanField(default=False)
    hula_hopping2 = models.BooleanField(default=False)
    jumping2 = models.BooleanField(default=False)
    kicking2 = models.BooleanField(default=False)
    lifting2 = models.BooleanField(default=False)
    pull_ups2 = models.BooleanField(default=False)
    pushing2 = models.BooleanField(default=False)
    raking2 = models.BooleanField(default=False)
    riding2 = models.BooleanField(default=False)
    rocking2 = models.BooleanField(default=False)
    sliding2 = models.BooleanField(default=False)
    sweeping2 = models.BooleanField(default=False)
    swinging2 = models.BooleanField(default=False)
    throwing2 = models.BooleanField(default=False)
    other5 = models.BooleanField(default=False)

    question27 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level271', '0-2 material(s) accessible to children'),
                                    ('level272', '3-4 material accessible to children'),
                                    ('level273', '5-6 material accessible to children'),
                                    ('level274', '7+ material accessible to children'),
                                ])

    # Preschool gross motor activities
    balancing3 = models.BooleanField(default=False)
    bouncing3 = models.BooleanField(default=False)
    bowling3 = models.BooleanField(default=False)
    brachiating3 = models.BooleanField(default=False)
    climbing3 = models.BooleanField(default=False)
    crawling3 = models.BooleanField(default=False)
    dancing3 = models.BooleanField(default=False)
    digging3 = models.BooleanField(default=False)
    dribbling3 = models.BooleanField(default=False)
    drumming3 = models.BooleanField(default=False)
    hammering3 = models.BooleanField(default=False)
    hopping3 = models.BooleanField(default=False)
    hula_hopping3 = models.BooleanField(default=False)
    jumping3 = models.BooleanField(default=False)
    kicking3 = models.BooleanField(default=False)
    lifting3 = models.BooleanField(default=False)
    pull_ups3 = models.BooleanField(default=False)
    pushing3 = models.BooleanField(default=False)
    raking3 = models.BooleanField(default=False)
    riding3 = models.BooleanField(default=False)
    rocking3 = models.BooleanField(default=False)
    sliding3 = models.BooleanField(default=False)
    sweeping3 = models.BooleanField(default=False)
    swinging3 = models.BooleanField(default=False)
    throwing3 = models.BooleanField(default=False)
    other6 = models.BooleanField(default=False)

    question28 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level281', '0-2 material(s) accessible to children'),
                                    ('level282', '3-4 material accessible to children'),
                                    ('level283', '5-6 material accessible to children'),
                                    ('level284', '7+ material accessible to children'),
                                ])

    # Infant material condition
    question29 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level291', '0 materials available or not in repair'),
                                    ('level292', 'Half or less materials are in good repair'),
                                    ('level293', 'Most materials are in good repair'),
                                    ('level294', 'Almost all materials are in good repair'),
                                ])

    # Toddler material condition
    question30 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level301', '2 or less materials available or not in repair'),
                                    ('level302', 'Half or less materials are in good repair'),
                                    ('level303', 'Most materials are in good repair'),
                                    ('level304', 'Almost all materials are in good repair'),
                                ])

    # Preschool material condition
    question31 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level311', '2 or less materials available or not in repair'),
                                    ('level312', 'Half or less materials are in good repair'),
                                    ('level313', 'Most materials are in good repair'),
                                    ('level314', 'Almost all materials are in good repair'),
                                ])

    # Infant literacy materials
    audio1 = models.BooleanField(default=False)
    books1 = models.BooleanField(default=False)
    display_pictures1 = models.BooleanField(default=False)
    environmental_print1 = models.BooleanField(default=False)
    microphone1 = models.BooleanField(default=False)
    language_cards1 = models.BooleanField(default=False)
    storytelling1 = models.BooleanField(default=False)
    other7 = models.BooleanField(default=False)

    question32 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level321', '0 material(s) accessible to children'),
                                    ('level322', '1 material accessible to children'),
                                    ('level323', '2 material accessible to children'),
                                    ('level324', '3+ material accessible to children'),
                                ])

    # Toddler literacy materials
    alphabet2 = models.BooleanField(default=False)
    audio2 = models.BooleanField(default=False)
    books2 = models.BooleanField(default=False)
    display_pictures2 = models.BooleanField(default=False)
    environmental_print2 = models.BooleanField(default=False)
    microphone2 = models.BooleanField(default=False)
    language_cards2 = models.BooleanField(default=False)
    storytelling2 = models.BooleanField(default=False)
    language_games2 = models.BooleanField(default=False)
    other8 = models.BooleanField(default=False)

    question33 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level331', '0-2 material(s) accessible to children'),
                                    ('level332', '3-4 material accessible to children'),
                                    ('level333', '5-6 material accessible to children'),
                                    ('level334', '7+ material accessible to children'),
                                ])

    # Preschool literacy materials
    journaling3 = models.BooleanField(default=False)
    alphabet3 = models.BooleanField(default=False)
    audio3 = models.BooleanField(default=False)
    books3 = models.BooleanField(default=False)
    display_pictures3 = models.BooleanField(default=False)
    environmental_print3 = models.BooleanField(default=False)
    microphone3 = models.BooleanField(default=False)
    language_cards3 = models.BooleanField(default=False)
    storytelling3 = models.BooleanField(default=False)
    language_games3 = models.BooleanField(default=False)
    other9 = models.BooleanField(default=False)

    question34 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level341', '0-2 material(s) accessible to children'),
                                    ('level342', '3-4 material accessible to children'),
                                    ('level343', '5-6 material accessible to children'),
                                    ('level344', '7+ material accessible to children'),
                                ])

    # Infant literacy material condition
    question35 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level351', '0 materials available or not in repair'),
                                    ('level352', 'Half or less materials are in good repair'),
                                    ('level353', 'Most materials are in good repair'),
                                    ('level354', 'Almost all materials are in good repair'),
                                ])

    # Toddler literacy material condition
    question36 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level361', '2 or less materials available or not in repair'),
                                    ('level362', 'Half or less materials are in good repair'),
                                    ('level363', 'Most materials are in good repair'),
                                    ('level364', 'Almost all materials are in good repair'),
                                ])

    # Preschool literacy material condition
    question37 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level371', '2 or less materials available or not in repair'),
                                    ('level372', 'Half or less materials are in good repair'),
                                    ('level373', 'Most materials are in good repair'),
                                    ('level374', 'Almost all materials are in good repair'),
                                ])

    # Infant math/science materials
    bird_feeder1 = models.BooleanField(default=False)
    building_materials1 = models.BooleanField(default=False)
    discovery_bottles1 = models.BooleanField(default=False)
    fill_dump_station1 = models.BooleanField(default=False)
    funnels1 = models.BooleanField(default=False)
    garden1 = models.BooleanField(default=False)
    grid1 = models.BooleanField(default=False)
    hopscotch1 = models.BooleanField(default=False)
    living_animals1 = models.BooleanField(default=False)
    magnifying_glasses1 = models.BooleanField(default=False)
    matching_games1 = models.BooleanField(default=False)
    mirrors1 = models.BooleanField(default=False)
    numbers1 = models.BooleanField(default=False)
    prism1 = models.BooleanField(default=False)
    rolling_ramps1 = models.BooleanField(default=False)
    slime1 = models.BooleanField(default=False)
    sorting_containers1 = models.BooleanField(default=False)
    varying_size_containers1 = models.BooleanField(default=False)
    visual_patterns1 = models.BooleanField(default=False)
    wind_chimes1 = models.BooleanField(default=False)
    other10 = models.BooleanField(default=False)

    question38 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level381', '0-2 material(s) accessible to children'),
                                    ('level382', '3-4 material accessible to children'),
                                    ('level383', '5-6 material accessible to children'),
                                    ('level384', '7+ material accessible to children'),
                                ])

    # Toddler math/science materials
    bird_feeder2 = models.BooleanField(default=False)
    building_materials2 = models.BooleanField(default=False)
    discovery_bottles2 = models.BooleanField(default=False)
    fill_dump_station2 = models.BooleanField(default=False)
    funnels2 = models.BooleanField(default=False)
    garden2 = models.BooleanField(default=False)
    hopscotch2 = models.BooleanField(default=False)
    living_animals2 = models.BooleanField(default=False)
    magnifying_glasses2 = models.BooleanField(default=False)
    matching_games2 = models.BooleanField(default=False)
    mirrors2 = models.BooleanField(default=False)
    numbers2 = models.BooleanField(default=False)
    prism2 = models.BooleanField(default=False)
    recording_temp2 = models.BooleanField(default=False)
    rolling_ramps2 = models.BooleanField(default=False)
    scales2 = models.BooleanField(default=False)
    slime2 = models.BooleanField(default=False)
    sorting_containers2 = models.BooleanField(default=False)
    spinners2 = models.BooleanField(default=False)
    steps2 = models.BooleanField(default=False)
    varying_size_containers2 = models.BooleanField(default=False)
    visual_patterns2 = models.BooleanField(default=False)
    wind_chimes2 = models.BooleanField(default=False)
    other11 = models.BooleanField(default=False)

    question39 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level391', '0-2 material(s) accessible to children'),
                                    ('level392', '3-4 material accessible to children'),
                                    ('level393', '5-6 material accessible to children'),
                                    ('level394', '7+ material accessible to children'),
                                ])

    # Preschool math/science materials
    bird_feeder3 = models.BooleanField(default=False)
    building_materials3 = models.BooleanField(default=False)
    dice3 = models.BooleanField(default=False)
    discovery_bottles3 = models.BooleanField(default=False)
    fill_dump_station3 = models.BooleanField(default=False)
    funnels3 = models.BooleanField(default=False)
    garden3 = models.BooleanField(default=False)
    grid3 = models.BooleanField(default=False)
    hopscotch3 = models.BooleanField(default=False)
    living_animals3 = models.BooleanField(default=False)
    magnifying_glasses3 = models.BooleanField(default=False)
    matching_games3 = models.BooleanField(default=False)
    mirrors3 = models.BooleanField(default=False)
    numbers3 = models.BooleanField(default=False)
    prism3 = models.BooleanField(default=False)
    pulleys3 = models.BooleanField(default=False)
    recording_temp3 = models.BooleanField(default=False)
    rolling_ramps3 = models.BooleanField(default=False)
    scales3 = models.BooleanField(default=False)
    slime3 = models.BooleanField(default=False)
    sorting_containers3 = models.BooleanField(default=False)
    spinners3 = models.BooleanField(default=False)
    steps3 = models.BooleanField(default=False)
    timers3 = models.BooleanField(default=False)
    varying_size_containers3 = models.BooleanField(default=False)
    visual_patterns3 = models.BooleanField(default=False)
    wind_chimes3 = models.BooleanField(default=False)
    other12 = models.BooleanField(default=False)

    question40 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level401', '0-2 material(s) accessible to children'),
                                    ('level402', '3-4 material accessible to children'),
                                    ('level403', '5-6 material accessible to children'),
                                    ('level404', '7+ material accessible to children'),
                                ])

    # Infant math/science material condition
    question41 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level411', '2 or less materials available or not in repair'),
                                    ('level412', 'Half or less materials are in good repair'),
                                    ('level413', 'Most materials are in good repair'),
                                    ('level414', 'Almost all materials are in good repair'),
                                ])

    # Toddler math/science material condition
    question42 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level421', '2 or less materials available or not in repair'),
                                    ('level422', 'Half or less materials are in good repair'),
                                    ('level423', 'Most materials are in good repair'),
                                    ('level424', 'Almost all materials are in good repair'),
                                ])

    # Preschool math/science material condition
    question43 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level431', '2 or less materials available or not in repair'),
                                    ('level432', 'Half or less materials are in good repair'),
                                    ('level433', 'Most materials are in good repair'),
                                    ('level434', 'Almost all materials are in good repair'),
                                ])

    # Infant dramatic play materials
    animal_figures1 = models.BooleanField(default=False)
    crayons1 = models.BooleanField(default=False)
    child_sized_furniture1 = models.BooleanField(default=False)
    collage_materials1 = models.BooleanField(default=False)
    cooking_eating_equipment1 = models.BooleanField(default=False)
    dolls1 = models.BooleanField(default=False)
    dress_up1 = models.BooleanField(default=False)
    easels1 = models.BooleanField(default=False)
    musical_instruments1 = models.BooleanField(default=False)
    paint_brushes1 = models.BooleanField(default=False)
    paints1 = models.BooleanField(default=False)
    paper_cardboard1 = models.BooleanField(default=False)
    play_dough1 = models.BooleanField(default=False)
    soft_animals1 = models.BooleanField(default=False)
    toy_telephones1 = models.BooleanField(default=False)

    question44 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level441', '0-2 material(s) accessible to children'),
                                    ('level442', '3-4 material accessible to children'),
                                    ('level443', '5-6 material accessible to children'),
                                    ('level444', '7+ material accessible to children'),
                                ])

    # Toddler dramatic play materials
    animal_figures2 = models.BooleanField(default=False)
    crayons2 = models.BooleanField(default=False)
    child_sized_furniture2 = models.BooleanField(default=False)
    collage_materials2 = models.BooleanField(default=False)
    cooking_eating_equipment2 = models.BooleanField(default=False)
    dolls2 = models.BooleanField(default=False)
    dress_up2 = models.BooleanField(default=False)
    easels2 = models.BooleanField(default=False)
    musical_instruments2 = models.BooleanField(default=False)
    paint_brushes2 = models.BooleanField(default=False)
    paints2 = models.BooleanField(default=False)
    paper_cardboard2 = models.BooleanField(default=False)
    play_dough2 = models.BooleanField(default=False)
    soft_animals2 = models.BooleanField(default=False)
    toy_telephones2 = models.BooleanField(default=False)

    question45 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level451', '0-2 material(s) accessible to children'),
                                    ('level452', '3-4 material accessible to children'),
                                    ('level453', '5-6 material accessible to children'),
                                    ('level454', '7+ material accessible to children'),
                                ])

    # Preschool dramatic play materials
    animal_figures3 = models.BooleanField(default=False)
    crayons3 = models.BooleanField(default=False)
    child_sized_furniture3 = models.BooleanField(default=False)
    collage_materials3 = models.BooleanField(default=False)
    cooking_eating_equipment3 = models.BooleanField(default=False)
    dolls3 = models.BooleanField(default=False)
    dress_up3 = models.BooleanField(default=False)
    easels3 = models.BooleanField(default=False)
    musical_instruments3 = models.BooleanField(default=False)
    paint_brushes3 = models.BooleanField(default=False)
    paints3 = models.BooleanField(default=False)
    paper_cardboard3 = models.BooleanField(default=False)
    play_dough3 = models.BooleanField(default=False)
    soft_animals3 = models.BooleanField(default=False)
    toy_telephones3 = models.BooleanField(default=False)

    question46 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level461', '0-2 material(s) accessible to children'),
                                    ('level462', '3-4 material accessible to children'),
                                    ('level463', '5-6 material accessible to children'),
                                    ('level464', '7+ material accessible to children'),
                                ])

    # Infant dramatic play material condition
    question47 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level471', '2 or less materials available or not in repair'),
                                    ('level472', 'Half or less materials are in good repair'),
                                    ('level473', 'Most materials are in good repair'),
                                    ('level474', 'Almost all materials are in good repair'),
                                ])

    # Toddler dramatic play material condition
    question48 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level481', '2 or less materials available or not in repair'),
                                    ('level482', 'Half or less materials are in good repair'),
                                    ('level483', 'Most materials are in good repair'),
                                    ('level484', 'Almost all materials are in good repair'),
                                ])

    # Preschool dramatic play material condition
    question49 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level491', '2 or less materials available or not in repair'),
                                    ('level492', 'Half or less materials are in good repair'),
                                    ('level493', 'Most materials are in good repair'),
                                    ('level494', 'Almost all materials are in good repair'),
                                ])

    # Outdoor time plan
    question50 = models.CharField(max_length=10, blank=True, null=True,
                                choices=[
                                    ('level501', 'There is no written plan related to outdoor time'),
                                    ('level502', 'There is a plan for outdoor time, but it looks like an outline, with just a few words, and vague definitions of activities children already do. There are no phrases describing what is going to be done.'),
                                    ('level503', 'The plan for outdoor time includes 1 activity related to 1 area of the program on that day. There is enough detail so that someone can implement the activity, and/or understand how the development of the activity will proceed.'),
                                    ('level504', 'The plan for outdoor time includes 2 activities or more related to 2 or more areas of the program on that day. Planning includes a rationale that addresses individual child or classroom needs/goals.'),
                                ])
    

    #page 6

    # Choices for question51
    QUESTION51_CHOICES = [
        ('level511', 'Little language is used, or language used is relevant to teachers perspectives rather than contingent on childrens activities and interests.'),
        ('level512', 'Teachers used some language relevant to childrens interests and activities; teachers language tends to be related to teachers interests, perspectives, or other duties. Verbalizations often restrict use of materials when guiding behaviors.'),
        ('level513', 'Teachers’ language related to childrens interests and activities occurs regularly; language related to teachers interests, perspectives, or other duties occurs for more than a few minutes. Verbalizations may restrict use of materials when guiding behaviors'),
        ('level514', 'Teachers’ language is consistently related to what children are playing with or looking at, what they are focused on or doing. Any restriction verbalization is related to safety/hazard.'),
    ]
    question51 = models.CharField(max_length=20, blank=True, null=True, choices=QUESTION51_CHOICES)

    # Choices for question52
    QUESTION52_CHOICES = [
        ('level521', 'Interactions are primarily for correction or instructions. The quantity of interactions may be very low. The teacher may be intrusive, dismissive or negative toward children. Children’s cues or bids are largely ignored'),
        ('level522', 'Some warm teacher-child interactions with children occur, and some instances of intrusion may occur. Teacher shows a positive response to a child’s bid or cue, but this does not occur often or only to a few select children.'),
        ('level523', 'Warm and positive teacher interactions occur several times and with different children. Most of children’s bids and cues are responded to or teachers occasionally initiate interactions with children who do not show bids/cues. Occasional instances of intrusion can occur.'),
        ('level524', 'Teachers consistently exhibit warm and positive interactions with various children. Children’s bids and cues are almost always responded to or teachers initiate interactions with children who do not show bids/cues. Any instances of intrusion are situationally appropriate.'),
    ]
    question52 = models.CharField(max_length=20, blank=True, null=True, choices=QUESTION52_CHOICES)

    # Choices for question53
    QUESTION53_CHOICES = [
        ('level531', 'Teachers inhibit/prohibit interactions with materials, or interrupt children’s interests or focus. Or teachers do not acknowledge and/or promote children’s persistence and learning.'),
        ('level532', 'Teachers offer or encourage children’s use of a few materials or acknowledge engagement using simple comments/questions.'),
        ('level533', 'Teachers are sensitive to children’s interests and may offer materials that interest children but may not promote extended exploration of materials or areas, or how to use or think about materials in different ways. Teachers ask some open-ended questions, but this is not consistent'),
        ('level534', 'Teachers may offer several materials, or alternative ways of using materials and/or follow children’s lead in exploring concepts and discoveries by asking open-ended questions, challenging their thinking/abilities, and scaffolding their learning.'),
    ]
    question53 = models.CharField(max_length=20, blank=True, null=True, choices=QUESTION53_CHOICES)

    # Choices for question54
    QUESTION54_CHOICES = [
        ('level541', 'Teachers are visually supervising and rarely physically engaged with children/materials.'),
        ('level542', 'Teachers are physically close to children but show limited physical engagement and/or modeling with them.'),
        ('level543', 'Teachers sometimes participate in shared play and reciprocal interactions (e.g., where teachers model inquisitiveness or exploration), but this participation does not last. They may offer or start some activities.'),
        ('level544', 'Teachers offer and start activities and continue to engage in the activities/play with extended interactions. Teachers are at children’s level and physically engaged by sharing activities and encouraging joint attention. Multiple examples of reciprocal/shared interactions (where teachers are modeling inquisitiveness or exploration) are observed between teachers and children.'),
    ]
    question54 = models.CharField(max_length=20, blank=True, null=True, choices=QUESTION54_CHOICES)

    # Choices for question55
    QUESTION55_CHOICES = [
        ('level551', 'Little support is provided for positive peer interactions and challenging situations'),
        ('level552', 'Some support for solving challenging situations. When support is given, it is usually vague (i.e., not giving problem-solving strategies) and/or not appropriate to the developmental level of the children'),
        ('level553', 'Some examples of support for positive peer interactions, but this is not consistent. Support is mostly given to children when there is conflict or challenging situations.'),
        ('level554', 'Teachers consistently support positive peer interaction and challenging situations if it is needed. Support and/or encouragement for positive peer interactions is given to children even if there is no conflict.'),
    ]
    question55 = models.CharField(max_length=20, blank=True, null=True, choices=QUESTION55_CHOICES)

    # Choices for question56
    QUESTION56_CHOICES = [
        ('level561', 'There is no natural environment or children are prohibited from engaging with the natural environment.'),
        ('level562', 'Teachers discourage interactions with the natural environment or do not encourage further exploration.'),
        ('level563', 'Teachers allow children to experience or interact with natural elements/environment. They minimally encourage and/or are passive about children’s engagement with the natural environment.'),
        ('level564', 'Teachers encourage children to be actively engaged with natural elements/environment by using their senses and skills to manipulate and explore it.'),
    ]
    question56 = models.CharField(max_length=20, blank=True, null=True, choices=QUESTION56_CHOICES)

    # Choices for question57
    QUESTION57_CHOICES = [
        ('level571', 'There are no children engaging with natural elements or the natural environment.'),
        ('level572', 'Child(ren) notice natural elements/environment but do not engage/spend time exploring it or are stopped from exploring further'),
        ('level573', 'Child(ren) display curiosity of and exploration with natural elements/environment for a short period of time'),
        ('level574', 'Child(ren) display curiosity of and exploration with the natural elements/environment for a sustained period of time.'),
    ]
    question57 = models.CharField(max_length=20, blank=True, null=True, choices=QUESTION57_CHOICES)

    # Choices for question58
    QUESTION58_CHOICES = [
        ('level581', 'There are no children engaging with the natural environment'),
        ('level582', 'One child engages with the natural environment'),
        ('level583', 'More than one but half or less of the children engage with the natural environment'),
        ('level584', 'More than half of the children engage with the natural environment'),
    ]
    question58 = models.CharField(max_length=20, blank=True, null=True, choices=QUESTION58_CHOICES)

    # Choices for question59
    QUESTION59_CHOICES = [
        ('level591', 'Children spend all their time in required teacher-led whole or small group activities. No or few options for child-directed activities exist'),
        ('level592', 'Children spend most of their time in the required teacher-led small/large group activities. Children have little time to engage in activities of their choice'),
        ('level593', 'Children spend almost half their time in teacher-led small/large group activities. Teacher-led activities do not take up the whole time. Children have half or more of their time to engage in activities of their choice'),
        ('level594', 'Children can choose their activities and direct their own learning. Small or large group activities are optional or short in duration when offered. Group activities may happen spontaneously.'),
    ]
    question59 = models.CharField(max_length=20, blank=True, null=True, choices=QUESTION59_CHOICES)

    # Choices for question60
    QUESTION60_CHOICES = [
        ('level601', 'Climate is characterized by disrespect and harsh interactions, or teachers ignore children. There is no enthusiasm.'),
        ('level602', 'The climate is generally neutral with few instances of enthusiasm, affection, or respect shown between children and adults. There might be instances of sarcasm.'),
        ('level603', 'The climate is generally neutral with some periods of enthusiasm, affection, and respect shown by teachers and children'),
        ('level604', 'A consistently positive climate is demonstrated by sustained affection, enthusiastic, and respectful interactions that are just as likely to occur between any of the children and teachers'),
    ]
    question60 = models.CharField(max_length=20, blank=True, null=True, choices=QUESTION60_CHOICES, )
    