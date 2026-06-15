team1 = input("Enter Team 1 Name: ")
score1 = int(input(f"Enter {team1} Score: "))

team2 = input("Enter Team 2 Name: ")
score2 = int(input(f"Enter {team2} Score: "))

margin = abs(score1 - score2)

if score1 > score2:
    winner = team1

    announcement = f"""
============================================================

WINNER ANNOUNCEMENT

Congratulations to {winner} for securing an impressive victory by {margin} points.

MATCH SUMMARY

The match was highly competitive, with both teams displaying determination and skill throughout the contest. {winner} maintained a slight advantage and successfully converted it into a well-deserved win.

REMARKS

• {team1} demonstrated strong effort and teamwork.
• {team2} fought hard and remained competitive until the end.
• The close scoreline reflects the quality of both teams.

CLOSING MESSAGE

Both teams should be proud of their performance. We look forward to witnessing more exciting matches in the future.

============================================================
"""

elif score2 > score1:
    winner = team2

    announcement = f"""
============================================================

WINNER ANNOUNCEMENT

Congratulations to {winner} for securing an impressive victory by {margin} points.

MATCH SUMMARY

The match was highly competitive, with both teams displaying determination and skill throughout the contest. {winner} maintained a slight advantage and successfully converted it into a well-deserved win.

REMARKS

• {team1} demonstrated strong effort and teamwork.
• {team2} fought hard and remained competitive until the end.
• The close scoreline reflects the quality of both teams.

CLOSING MESSAGE

Both teams should be proud of their performance. We look forward to witnessing more exciting matches in the future.

============================================================
"""

else:
    announcement = f"""
============================================================

MATCH RESULT

The match between {team1} and {team2} ended in a draw.

MATCH SUMMARY

Both teams delivered an outstanding performance and remained evenly matched throughout the contest.

REMARKS

• Excellent teamwork from both sides.
• Strong competitive spirit displayed by all participants.
• A draw is a reflection of the balanced performance of both teams.

CLOSING MESSAGE

Congratulations to both teams for a memorable and exciting contest.

============================================================
"""

print(announcement)
