# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

label start:

    show bckgrnd

    show desk

    define a = Character("Agent")
    define c = Character("Client")
    define i = Character("Instructor")
    define s = Character("*Scene*")


# The game starts here.

#label start:

    show really at left with moveinleft:
        xzoom 0.5 yzoom 0.5
    $ secret_message = renpy.file("test.txt").read().decode('utf-8').replace('\r', '')
    #$ mood = _(mystore.read())

    i "%(secret_message)s"
    i "We're going to simmulate a scene and see wether you're gonna choose the right desicions or not."
    i "And based on your tests, I'm gonna help you improve your level so it can be more and more adaptive with every case you'll face in the future."

    hide really
    show hmm at left:
        xzoom 0.5 yzoom 0.5

    i "What do you think ? Do you want to start ?"

    menu:
        "Yes":
            jump yes
        "No":
            jump no

    label yes:
        i "Let's begin then."
        hide hmm
        show really at left:
            xzoom 0.5 yzoom 0.5
        jump begin
    label no:
        hide hmm
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        i "Oh !"
        hide shocked
        show really at left:
            xzoom 0.5 yzoom 0.5
        i "Maybe next time."
        return

label begin:

    hide really
    s "The client enters ..."

    show really at left:
        xzoom 0.5 yzoom 0.5

    i "Smile so he can feel comfortable in your presence."
    i "Did he smile back ?"

    hide really
    show hmm at left:
        xzoom 0.5 yzoom 0.5

    menu :
        "Yes":
            jump yes1
        "No":
            jump no2
    label yes1:
        i "Lucky you. This means he's having a good day."
        hide hmm
        show really at left:
            xzoom 0.5 yzoom 0.5
        jump action
    label no2:
        i "This means he's having a bad day. You may face some problems dealing with him."
        hide hmm
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        i "Don't panic. We'll see how to deal with that."
        jump action

label action:
    show really at left:
            xzoom 0.5 yzoom 0.5
    i "Here he comes ... see you !"
    hide really
    hide shocked
    show normal at right behind desk with moveinright:
        xzoom 0.5 yzoom 0.5
    c "Good morning Sir"
    show speaking_1 at right behind desk:
        xzoom 0.5 yzoom 0.5
    a "Hey, welcome ... How are you ?"
    hide speaking_1
    show speaking_2 at right behind desk:
        xzoom 0.5 yzoom 0.5
    c "Good thanks ... How about you ?"
    hide speaking_2
    show speaking_3 at right behind desk:
        xzoom 0.5 yzoom 0.5
    a "I am doing well thanks"

label qst1:
    hide shocked
    hide angry
    show speaking_3 at right behind desk:
        xzoom 0.5 yzoom 0.5
    a " How can I help you ?"
    c "I want to inssure my car"
    menu:
        "Which inssurance service do you want to benifit from ?":
            jump QestA
        "Do you already have any experience with any other inssurance agency ?":
            jump QestB
        "How can I help you ?":
            jump QestC
        "Have you ever inssured in our agency ?":
            jump QestD
    label QestA:
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        hide speaking_3
        show angry at right behind desk:
            xzoom 0.5 yzoom 0.5
        i "Bad choice ... let's repeat it again."
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        jump qst1
    label QestB:
        show really at left:
            xzoom 0.5 yzoom 0.5
        i "Nice move"
        hide really
        a "Do you already have any experience with any other inssurance agencies ?"
        show speaking_1 at right behind desk:
            xzoom 0.5 yzoom 0.5
        hide really
        jump qst2
    label QestC:
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        hide speaking_3
        show angry at right behind desk:
            xzoom 0.5 yzoom 0.5
        i "Bad choice ... let's repeat it again."
        jump qst1
    label QestD:
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        hide speaking_3
        show angry at right behind desk:
            xzoom 0.5 yzoom 0.5
        i "Bad choice ... let's repeat it again."
        jump qst1
label qst2:
    hide shocked
    hide angry
    show sad at right behind desk:
        xzoom 0.5 yzoom 0.5
    c "Yes i had a bad experience, cause those agencies seek nothing but profit, they don't care about their clients."
    menu:
        "Whould you mind telling me why ?":
            jump QestE
        "I totaly disagree":
            jump QestF
        "We are not like others":
            jump QestG
        "No, inssurance agencies are looking just for profit":
            jump QestH
    label QestE:
        show really at left:
            xzoom 0.5 yzoom 0.5
        i "Nice move again ..."
        show speaking_1 at right:
            xzoom 0.5 yzoom 0.5
        hide really
        a "Would you mind telling me why you have this impression on inssurance agencies."
        jump qst3
    label QestF:
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        hide speaking_3
        show angry at right behind desk:
            xzoom 0.5 yzoom 0.5
        i "Bad choice"
        show shocked at left:
            xzoom 0.5 yzoom 0.5

        jump qst2
    label QestG:
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        hide speaking_3
        show angry at right behind desk:
            xzoom 0.5 yzoom 0.5
        i "Bad choice"
        show shocked at left:
            xzoom 0.5 yzoom 0.5

        jump qst2
    label QestH:
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        hide speaking_3
        show angry at right behind desk:
            xzoom 0.5 yzoom 0.5
        i "Bad choice"
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        jump qst2
label qst3:
    hide shocked
    hide angry
    show sad at right behind desk:
        xzoom 0.5 yzoom 0.5
    c "I had an accident, but my formal inssurance agency didn't cover my losts."
    menu:
        "So ? What do you know about our agency ?":
            jump QestI
        "We are differnet from other agencies":
            jump QestJ
        "That's too bad":
            jump QestK
    label QestI:
        show really at left:
            xzoom 0.5 yzoom 0.5
        i "DAAMN you're so good."
        hide really
        show speaking_1 at right behind desk:
            xzoom 0.5 yzoom 0.5
        a "So ? What do you know about our agency ?"
        jump qst4
    label QestJ:
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        hide speaking_1
        show angry at right behind desk:
            xzoom 0.5 yzoom 0.5
        i "Bad decision ... let's repeat."
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        jump qst3
    label QestK:
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        hide speaking_1
        show angry at right behind desk:
            xzoom 0.5 yzoom 0.5
        i "Bad decision ... let's repeat."
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        jump qst3
    label QestL:
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        hide speaking_1
        show angry at right behind desk:
            xzoom 0.5 yzoom 0.5
        i "Bad decision ... let's repeat."
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        jump qst3
label qst4:
    hide shocked
    hide angry
    show shy at right behind desk:
        xzoom 0.5 yzoom 0.5
    c "Not too much, but I think you're not that different."
    menu:
        "You are wrong":
            jump QestM
        "I totaly understand, but we have some offers that may satisfy you. Tell me about your needs.":
            jump QestN
    label QestM:
        show angry at right behind desk:
            xzoom 0.5 yzoom 0.5
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        i "Wrong"
        jump qst4
    label QestN:
        show really at left:
            xzoom 0.5 yzoom 0.5
        i "Perfect"
        show really at left:
            xzoom 0.5 yzoom 0.5
        jump qst5
label qst5:
    hide really
    hide shocked
    hide angry
    show speaking_2 at right behind desk:
        xzoom 0.5 yzoom 0.5
    c "I want an inssurance plan for every risk or damage my vehicle may take, but it should be less cheaper and with exacly the same features my formal inssurance gave me."
    menu:
        "What are you asking sir is insane.":
            jump QestO
        "We have exacly what are you looking for. And it is much more cheaper than what provides your formal inssurance agency.":
            jump QestP
        "Yes, we can provide you with that inssurance plan, but it will cost you a bit expensive.":
            jump QestQ
    label QestO:
        show angry at right behind desk:
            xzoom 0.5 yzoom 0.5
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        i "Not the perfect choice."
        jump qst5
    label QestP:
        show really at left:
            xzoom 0.5 yzoom 0.5
        i "Awesome !"
        hide really
        jump qst6
    label QestQ:
        show angry at right behind desk:
            xzoom 0.5 yzoom 0.5
        show shocked at left:
            xzoom 0.5 yzoom 0.5
        i "Not the perfect choice."
        jump qst5
label qst6:
    a "We have exacly what are you looking for. And it is much more cheaper than what provides your formal inssurance agency."
    show speaking_1 at right behind desk:
        xzoom 0.5 yzoom 0.5
    c "Awesome, I want to sing up for your plan."
    a "Sure thing sir, our offer fits people with needs as yourself, I would like to tell you about the documents that we'll need."
    show hmm at left:
        xzoom 0.5 yzoom 0.5
    i "Good job ... see you in the next chapter."
    return
