
# Write code here
h = int(input('Enter hours hand-'))
m = int(input('Enter minute hand-'))

# validate the input
if (h < 0 or m < 0 or h > 12 or m > 60):
    print('Wrong input')

# Idea is to minute angle - hour agnle from clockwise from 12 hour point

# 1 minute in minute angle manke 6 degree. (60 minute -> 360 degree)
m_angle = m*6

# every hour point yeilds to 30degree-- 12 hours-360degree plus if minute hand moves hour hands move too
# Every minute after hour hand take 0.5 degree movement. clockwise
h_angle = h*30 + m*0.5

# Take abs difference b/w them
angle = abs(h_angle - m_angle)


if angle>180:
    print(360-angle)
else:
    print(angle)