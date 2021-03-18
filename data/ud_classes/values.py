class Values:
    window_height = 720
    window_width = 1280
    window_size = (window_width, window_height)
    window_caption = 'Until die'
    # Room
    room_height = window_height
    room_width = window_width
    room_size = (room_width, room_height)
    # Floor
    floor_height = int(0.2 * room_height)
    floor_length = room_width
    floor_size = (floor_length, floor_height)
    floor_position_x = 0
    floor_position_y = room_height - floor_height
    floor_position = (floor_position_x, floor_position_y)
    # Roof
    roof_height = int(0.2 * room_height)
    roof_width = room_width
    roof_size = (roof_width, roof_height)
    roof_position_x = 0
    roof_position_y = 0
    roof_position = (roof_position_x, roof_position_y)
    # Wall
    wall_height = room_height
    wall_width = int(0.125 * room_width)
    wall_size = (wall_width, wall_height)
    # Left wall
    left_wall_position_x = 0
    left_wall_position_y = 0
    left_wall_position = (left_wall_position_x, left_wall_position_y)
    # Right wall
    right_wall_position_x = room_width - wall_width
    right_wall_position_y = 0
    right_wall_position = (right_wall_position_x, right_wall_position_y)
    # Refrigerator
    refrigerator_x_position = room_width - 2 * wall_width
    refrigerator_y_position = room_height - 5 * floor_height // 2
    refrigerator_position = (refrigerator_x_position, refrigerator_y_position)
    # Choice panel
    choice_panel_width = wall_width // 2
    choice_panel_height = wall_height // 15
    choice_panel_size = (choice_panel_width, choice_panel_height)
    choice_panel_font_size = wall_height // 45
    # Text panel
    text_panel_width = 3 * wall_width // 2
    text_panel_height = wall_height // 10
    text_panel_size = (text_panel_width, text_panel_height)
    text_panel_font_size = wall_height // 45
    # HP panel
    hp_panel_width = room_width // 45
    hp_panel_height = room_height // 45
    hp_panel_size = (hp_panel_width, hp_panel_height)
    # Hand panel
    hand_panel_width = choice_panel_width // 2
    hand_panel_height = choice_panel_width // 2
    hand_panel_size = (hand_panel_width, hand_panel_width)
    # Door
    door_x_pos = 2 * wall_width
    # Range
    response_range = room_width // 20





