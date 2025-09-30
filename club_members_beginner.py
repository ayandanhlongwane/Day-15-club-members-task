# club_members_beginner.py
students = ["Ayanda", "Mutale", "Snai", "Daniel", "Rejoice"]
club_A = {"Ayanda", "Mutale", "Daniel"}
club_B = {"Rejoice", "Daniel", "Ayanda"}
print("Club A members:", club_A)
print("Club B members:", club_B)
common = club_A & club_B    
print("Members in both clubs:", common)
only_A = club_A - club_B    
only_B = club_B - club_A
print("Only in Club A:", only_A)
print("Only in Club B:", only_B)
