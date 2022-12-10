import pandas as pd 
df = pd.read_csv('export_our_test_value_FINAL.csv')

]for val1 in ["1", "2", "3", "4"]:
    for val in ["point_id",	"team",	"skill","skill_type","start_zone","end_zone","end_subzone",	"skill_subtype",	"num_players",	"num_players_numeric",	"home_team_score",	"visiting_team_score",	"home_setter_position",	"visiting_setter_position", "start_coordinate"	"mid_coordinate",	"end_coordinate",	"start_coordinate_x",	"start_coordinate_y",	"mid_coordinate_x",	"mid_coordinate_y",	"end_coordinate_x",	"end_coordinate_y",	"set_number",	"team_touch_id",	"home_team",	"visiting_team",	"point_won_by",	"winning_attack",	"serving_team",	"phase"	,"after_set_change",	"after_timeout",	"possession_id",	"after_serve_possession",	"total_data",	"home_touch"	,"away_touch"]:
        df[val+val1] = ""

counter = 0
for i, row in df.iterrows():
    if (i >0):
        point_id0 = df._get_value(i-1, 'match_id', takeable=False)
        point_idCurr = df._get_value(i, 'match_id', takeable=False)
        if (point_id0 == point_idCurr):
            for val in ["point_id",	"team",	"skill","skill_type","start_zone","end_zone","end_subzone",	"skill_subtype",	"num_players",	"num_players_numeric",	"home_team_score",	"visiting_team_score",	"home_setter_position",	"visiting_setter_position", "start_coordinate",	"mid_coordinate",	"end_coordinate",	"start_coordinate_x",	"start_coordinate_y",	"mid_coordinate_x",	"mid_coordinate_y",	"end_coordinate_x",	"end_coordinate_y",	"set_number",	"team_touch_id",	"home_team",	"visiting_team",	"point_won_by",	"winning_attack",	"serving_team",	"phase"	,"after_set_change",	"after_timeout",	"possession_id",	"after_serve_possession",	"total_data",	"home_touch"	,"away_touch"]:
                val1 = df._get_value(i-1,  val, takeable=False)
                df._set_value(i, val + "1", val1)
    if (i > 1):
        point_id0 = df._get_value(i-2, 'match_id', takeable=False)
        point_idCurr = df._get_value(i, 'match_id', takeable=False)
        if (point_id0 == point_idCurr):
            for val in ["point_id",	"team",	"skill","skill_type","start_zone","end_zone","end_subzone",	"skill_subtype",	"num_players",	"num_players_numeric",	"home_team_score",	"visiting_team_score",	"home_setter_position",	"visiting_setter_position", "start_coordinate",	"mid_coordinate",	"end_coordinate",	"start_coordinate_x",	"start_coordinate_y",	"mid_coordinate_x",	"mid_coordinate_y",	"end_coordinate_x",	"end_coordinate_y",	"set_number",	"team_touch_id",	"home_team",	"visiting_team",	"point_won_by",	"winning_attack",	"serving_team",	"phase"	,"after_set_change",	"after_timeout",	"possession_id",	"after_serve_possession",	"total_data",	"home_touch"	,"away_touch"]:
                val1 = df._get_value(i-2,  val, takeable=False)
                df._set_value(i, val + "2", val1)
    if (i>2):
        point_id0 = df._get_value(i-3, 'match_id', takeable=False)
        point_idCurr = df._get_value(i, 'match_id', takeable=False)
        if (point_id0 == point_idCurr):
            for val in ["point_id",	"team",	"skill","skill_type","start_zone","end_zone","end_subzone",	"skill_subtype",	"num_players",	"num_players_numeric",	"home_team_score",	"visiting_team_score",	"home_setter_position",	"visiting_setter_position", "start_coordinate",	"mid_coordinate",	"end_coordinate",	"start_coordinate_x",	"start_coordinate_y",	"mid_coordinate_x",	"mid_coordinate_y",	"end_coordinate_x",	"end_coordinate_y",	"set_number",	"team_touch_id",	"home_team",	"visiting_team",	"point_won_by",	"winning_attack",	"serving_team",	"phase"	,"after_set_change",	"after_timeout",	"possession_id",	"after_serve_possession",	"total_data",	"home_touch"	,"away_touch"]:
                val1 = df._get_value(i-3,  val, takeable=False)
                df._set_value(i, val + "3", val1)
    if (i>3):
        point_id0 = df._get_value(i-4, 'match_id', takeable=False)
        point_idCurr = df._get_value(i, 'match_id', takeable=False)
        if (point_id0 == point_idCurr):
            for val in ["point_id",	"team",	"skill","skill_type","start_zone","end_zone","end_subzone",	"skill_subtype",	"num_players",	"num_players_numeric",	"home_team_score",	"visiting_team_score",	"home_setter_position",	"visiting_setter_position", "start_coordinate",	"mid_coordinate",	"end_coordinate",	"start_coordinate_x",	"start_coordinate_y",	"mid_coordinate_x",	"mid_coordinate_y",	"end_coordinate_x",	"end_coordinate_y",	"set_number",	"team_touch_id",	"home_team",	"visiting_team",	"point_won_by",	"winning_attack",	"serving_team",	"phase"	,"after_set_change",	"after_timeout",	"possession_id",	"after_serve_possession",	"total_data",	"home_touch"	,"away_touch"]:
                val1 = df._get_value(i-4,  val, takeable=False)
                df._set_value(i, val + "4", val1)
    counter += 1
    print(counter)



df.to_csv(r'.csv')


