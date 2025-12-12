Menu = """
MENU FUNCTIONS
1. Phonebook
2. Messages
3. Chat
4. Call Register
5. Tones
6. Settings
7. Call divert
8. Games
9. Calculator
10. Reminders
11. Clock
12. Profiles
13. SIM Services
"""
print(Menu)

menu_option = int(input("Enter an option: "))

match menu_option:

    case 1:
        phonebook_menu = """
PHONEBOOK
1. Search
2. Service Nos.
3. Add name
4. Erase
5. Edit
6. Assign tone
7. Send b’card
8. Options
9. Speed dials
10. Voice tags
"""
        print(phonebook_menu)

        phonebook_option = int(input("Enter a phonebook option: "))

        match phonebook_option:
            case 1: print("Search")
            case 2: print("Service Nos.")
            case 3: print("Add name")
            case 4: print("Erase")
            case 5: print("Edit")
            case 6: print("Assign tone")
            case 7: print("Send b’card")

            case 8:
                options_menu = """
OPTIONS
1. Type of view
2. Memory status
"""
                print(options_menu)

                option_choice = int(input("Choose your preferred choice: "))

                match option_choice:
                    case 1: print("Type of view")
                    case 2: print("Memory status")
                    case _: print("Invalid option")

            case 9: print("Speed dials")
            case 10: print("Voice tags")
            case _: print("Invalid phonebook option")

    case 2:
        messages_menu = """
MESSAGES
1. Write Messages
2. Inbox
3. Outbox
4. Picture Messages
5. Templates
6. Smileys
7. Message Settings
8. Info service
9. Voice mailbox number
10. Service command editor 
"""
        print(messages_menu)
        
        messages_option  = int(input("Enter a message option: "))
    
        match messages_option:
            case 1: print("Write Messages")
            case 2: print("Inbox") 
            case 3: print("Outbox")
            case 4: print("Picture Messages")
            case 5: print("Templates")
            case 6: print("Smileys")

            case 7:
                message_settings_menu = """
MESSAGE SETTINGS
1. Set 1
2. Common
"""
                print(message_settings_menu)

                message_settings_choice = int(input("Choose your preferred choice: "))

                match message_settings_choice:

                    case 1:
                        Set_1_menu = """
SET 1 
1. Message centre number
2. Message sent as 
3. Message validity
"""
                        print(Set_1_menu)

                    case 2:
                        Common_menu = """
COMMON
1. Delivery reports
2. Reply via same centre
3. Character support
"""
                        print(Common_menu)

                    case _: print("Invalid message settings option")

            case 8: print("Info Service")
            case 9: print("Voice mailbox number")
            case 10: print("Service command editor")
            case _: print("Invalid message option")


    case 3: 
        chat_menu = """
CHAT
"""
        print(chat_menu)
        

    case 4:
        call_register_menu = """
CALL REGISTER
1. Missed Calls
2. Received Calls 
3. Dailled Calls
4. Erase recent call lists
5. Show call duration
6. Show call costs
7. Call costs settings
8. Prepaid credit
"""
        print(call_register_menu)
        call_register_option = int(input("Enter an option: "))
        
        match call_register_option:
            case 1: print("Missed Calls")
            case 2: print("Recieved Calls")
            case 3: print("Dialled Calls")
            case 4: print("Erase recent call lists")
            case 5: 
                show_call_duration_menu = """

SHOW CALL DURATION
1. Last call duration
2. All calls' duration
3. Received calls' duration
4. Dialled calls' duration
5. Clear timers
"""
                print(show_call_duration_menu)
                show_call_duration_menu
                match show_call_duration_menu:
                    case 1: print("Last call duration")
                    case 2: print("All calls' duration")
                    case 3: print("Received calls' duration")
                    case 4: print("Dialled calls' duration")
                    case 5: print("Clear timers")
                 

            case 6:
                show_call_costs_menu = """

SHOW CALL COSTS
1. Last call costs
2. All calls' costs
3. Clear counters
"""
                print(show_call_costs_menu)
                show_call_costs_menu
                match show_call_costs_menu:
                    case 1: print("Last call costs")
                    case 2: print("All calls' costs")
                    case 3: print("Clear counters")
                

            case 7: 
                call_costs_settings_menu = """

CALL COSTS SETTINGS
1. Call costs limit
2. Show costs in
"""
                print(call_costs_settings_menu)
                call_costs_settings_menu
                match call_costs_settings_menu:
                    case 1: print("Call costs limit")
                    case 2: print("Show costs in")
             

            case 8: print("Prepaid credit")
            case _: print("Invalid option")

    case 5: 
        tones_menu = """
TONES
1. Ringing tone
2. Ringing volume
3. Incoming call alert
4. Composer
5. Message alert tone
6. Keypad tones
7. Warning and game tones
8. Vibrating alert
9. Screen saver
"""

        print(tones_menu)

        tones_option = int(input("Enter a tones option: "))

        match tones_option:
            case 1: print("Ringing tone")
            case 2: print("Ringing volume")
            case 3: print("Incoming call alert")
            case 4: print("Composer")
            case 5: print("Message alert tone")
            case 6: print("Keypad tones")
            case 7: print("Warning and game tones")
            case 8: print("Vibrating alert")
            case 9: print("Screen saver")
            case _: print("Invalid option")

    case 6:
        settings_menu = """
SETTINGS
1. Call settings 
2. Phone settings
3. Security settings
4. Restore factory settings
"""
        print(settings_menu)
        settings_option = int(input("Enter a settings option: "))
        
        match settings_option:
            case 1: 
                call_settings_menu = """
CALL SETTINGS
1. Automatic redial
2. Speed dialing
3. Call waiting options
4. Owner number sending
5. Phone line using
6. Automatic answer
"""

                print(call_settings_menu)

                call_settings_menu

                match call_settings_menu:
                    case 1: ("Automatic redial")
                    case 2: ("Speed dailing")
                    case 3: ("Call waiting options")
                    case 4: ("Owner number sending")
                    case 5: ("Phone line using")
                    case 6: ("Automatic answer")
                    case _: ("Invalid option")

            case 2: 
                phone_settings_menu = """
PHONE SETTINGS
1. Language
2. Cell info display
3. Welcome note
4. Network selection
5. Lights
6. Confirm SIM service actions
"""
                print(phone_settings_menu)
                phone_settings_menu
                match phone_settings_menu:
                    case 1: print("Language")
                    case 2: print("Cell info display")
                    case 3: print("Welcome note")
                    case 4: print("Network selection")
                    case 5: print("Lights")
                    case 6: print("Confirm SIM service actions")

            case 3:
                security_settings_menu = """
SECURITY SETTINGS
1. PIN code request
2. Call barring service
3. Fixed dialing'
4. Closed user group
5. Phone security
6. Change access codes
"""

                print(security_settings_menu)
                security_settings_menu
                match security_settings_menu:
                    case 1: print("PIN code request")
                    case 2: print("Call barring service")
                    case 3: print("Fixed dialing")
                    case 4: print("Closed user group")
                    case 5: print("Phone security")
                    case 6: print("Change access codes")



            
            case 4: print("Restore factory settings")
            case _: print("Invalid option")
            

    
    case 7: 
        call_divert_menu = """
CALL DIVERT
"""
        print(call_divert_menu)



    case 8: 
        games_menu = """
GAMES
"""
        print(games_menu)

    
    case 9: 
        calculator_menu = """
CALCULATOR
"""
        print(calculator_menu)

    
    case 10: 
        reminders_menu = """
REMINDERS
"""
        print(reminders_menu)

    case 11: 
        clock_menu = """
CLOCK
1. Alarm clock
2. Clock settings
3. Date settings
4. Stop watch
5. Countdown timer
6. Auto update and time
"""

        print(clock_menu)
        clock_menu
        match clock_menu:
            case 1: print("Alarm clock")
            case 2: print("Clock settings")
            case 3: print("Date settings")
            case 4: print("Stop watch")
            case 5: print("Countdownn timer")
            case 6: print("Auto update amd time")

    case 12: 
        profiles_menu = """
PROFILES
"""
        print(profiles_menu)


    case 13: 
        sim_services_menu = """
SIM SERVICES
"""
        print(sim_services_menu)

    case _: 
        invalid_option_menu = """
INVALID OPTION
"""
        print(invalid_option_menu)
                

           




