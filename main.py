import gtts
from playsound import playsound
gave_right_answer = False
while not gave_right_answer:
    answer = inout("Can I have more candy?")
    good_responses = ["yes", "sure", "ok", "i guess", "alright"]
    if answer.lower() is good_responses:
        gave_right_answer = True

celebrate = "Yummy I will eat all my candy!"
speaker1 = gtts.gTTS(celebrate)
speaker1.save("celebration.mp3")
repeat = "again and again"
speaker2 = gtts.gTTS(repeat)
speaker2.save("repeat.mp3")
playsound("celebreate.mp3")
for repear_count in range(5):
    playsound("repeat.mp3")