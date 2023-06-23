import time,os,json
from Schools import Schools

def parse():
    script_dir = os.path.dirname(__file__)
    rel_path = "prereqs.json"
    abs_file_path = os.path.join(script_dir, rel_path)
    prereqs = []
    prereq_obj = []

    ##Opens JSON file, initializes and saves it as a JSON object

    with open(abs_file_path, "r") as f:
        prereqs = json.load(f)

    for x in prereqs["schools"]:
        prereq_obj.append(Schools(x["name"],x["human"],x["english"],x["biochem"],x["orgo"],x["genchem"],x["sharedchem"],x["math"],x["advanced_math"],x["physics"],x["biology"],x["advanced_biology"],x["stats"],x["notes"]))

    return prereq_obj

def user_verif():
    script_dir = os.path.dirname(__file__)
    rel_path = "user.json"
    abs_file_path = os.path.join(script_dir, rel_path)
    thing = []

    ##Opens JSON file, initializes and saves it as a JSON object

    with open(abs_file_path, "r") as f:
        thing = json.load(f)

    while True:

        verif = input("Do you have an account? (y/n): ")

        if verif == "y":
            user = input("Enter your username: ")
            temp = []
            for x in thing["user"]:
                if x["name"] == user:
                    print("User found!")
                    return x["biochem"],x["orgo"],x["genchem"],x["bio"],x["adv_bio"],x["phys"],x["math"],x["adv_math"],x["english"],x["stats"],x["human"]
            print("User not found!")
        elif verif == "n":
            orgo = []
            math = 0
            biochem = []
            human = []
            advanced_math = []
            physics = []
            english = []
            genchem = []
            bio = []
            advbio = []
            stats = []

            save = input("Save this profile? (Input name if yes, input n if no): ")

            if save == "n":
                save = False

            orgo.append(int(input("How many semesters of orgos did you take? ")))
            orgo.append(int(input("How many of those had labs? ")))


            biochem.append(int(input("How many semesters of biochems did you take? ")))
            biochem.append(int(input("How many of those had labs? ")))


            genchem.append(int(input("How many semesters of general/inorganic chem did you take? ")))
            genchem.append(int(input("How many of those had labs? ")))


            math = int(input("How many semesters of math did you take? (No stats) "))

            advanced_math = int(input("Of those, how many semesters of advanced_math (lin alg/DE) did you take? "))

            stats = int(input("How many semesters of stats did you take? "))

            bio.append(int(input("How many semesters of biology (Including advanced) did you take? ")))
            bio.append(int(input("How many of those had labs? ")))

            advbio.append(int(input("How many semesters of advanced biology (genetics, mol/cell bio) did you take? ")))
            advbio.append(int(input("How many of those had labs? ")))

            physics.append(int(input("How many semesters of physics did you take? ")))
            physics.append(int(input("How many of those had labs? ")))

            english = int(input("How many semesters of english did you take? "))

            human = int(input("How many semesters of humanities (Not English) did you take? "))

            if isinstance(save, str):
                temp_obj = {
                    "name": save,
                    "biochem": biochem,
                    "orgo": orgo,
                    "genchem": genchem,
                    "bio": bio,
                    "adv_bio": advbio,
                    "phys": physics,
                    "math": math,
                    "adv_math": advanced_math,
                    "stats": stats,
                    "english": english,
                    "human": human
                }
                thing["user"].append(temp_obj)
                script_dir = os.path.dirname(__file__)
                rel_path = "user.json"
                abs_file_path = os.path.join(script_dir, rel_path)

                with open(abs_file_path, "w") as f:
                    json_string = json.dumps(thing, indent=4)
                    f.write(json_string)

            return biochem,orgo,genchem,bio,advbio,physics,math,advanced_math,english,stats,human
            


if __name__ == "__main__":
    ## Add users and objects for storing the stuff later
    prereqs = parse()
    orgo = []
    math = 0
    biochem = []
    human = []
    advanced_math = []
    physics = []
    english = []
    genchem = []
    bio = []
    advbio = []
    stats = []

    reqs_met = []
    all_reasons = []

    biochem,orgo,genchem,bio,advbio,physics,math,advanced_math,english,stats,human = user_verif()

    for i in prereqs:
        status = "Yes"
        reasons = []
        sharedchem = []
        sharedchemreq = []

        for x in i.sharedchem:
            if isinstance(x, str):
                sharedchem.append(x)
            else:
                sharedchemreq = x

        if i.human > human:
            reasons.append("You need "+ str(i.human - human)+ " more humanities courses.")
            status = "No"

        if i.bio[0] > bio[1]:
            reasons.append("You need "+ str(i.bio[0] - bio[0])+ " more biology courses.")
            status = "No"

        if i.bio[1] > bio[1]:
            reasons.append("You need "+ str(i.bio[1] - bio[1])+ " more biology courses with labs.")
            status = "No"

        if i.advbio[0] > advbio[0]:
            reasons.append("You need "+ str(i.advbio[0] - advbio[0])+ " more advanced biology courses.")
            status = "No"
        
        if i.advbio[1] > advbio[1]:
            reasons.append("You need "+ str(i.advbio[1] - advbio[1])+ " more advanced biology courses with labs.")
            status = "No"

        if i.math > math:
            reasons.append("You need "+ str(i.math - math)+ " more math courses.")
            status = "No"

        if i.stats > stats:
            reasons.append("You need "+ str(i.stats - stats)+ " more stats courses.")
            status = "No"

        if i.advmath > advanced_math:
            reasons.append("You need "+ str(i.advmath - advanced_math)+ " more advanced math courses.")
            status = "No"

        if i.eng > english:
            reasons.append("You need "+ str(i.eng - english)+ " more english courses.")
            status = "No"
        
        if i.physics[0] > physics[0]:
            reasons.append("You need "+ str(i.physics[0] - physics[0])+ " more physics courses.")
            status = "No"
        
        if i.physics[1] > physics[1]:
            reasons.append("You need "+ str(i.physics[1] - physics[1])+ " more physics courses with labs.")
            status = "No"

        sharedbiochem = False
        sharedorgo = False
        sharedgenchem = False

        ## For the JSON file, if there is less than 1 shared chem course for prereq, do not put it in sharedchem :)

        if sharedchem:
            totalchem = [0,0]
            for x in sharedchem:
                if x == "biochem":
                    totalchem[0] += biochem[0]
                    totalchem[1] += biochem[1]
                    sharedbiochem = True
                if x == "orgo":
                    totalchem[0] += orgo[0]
                    totalchem[1] += orgo[1]
                    sharedorgo = True
                if x == "genchem":
                    totalchem[0] += genchem[0]
                    totalchem[1] += genchem[1]
                    sharedgenchem = True
            if sharedbiochem and sharedgenchem and sharedorgo:
                if sharedchemreq[0] > totalchem[0]:
                    reasons.append("You need "+ str(sharedchemreq[0] - totalchem[0])+ " more organic/inorganic/bio chem courses.")
                    status = "No"
                if sharedchemreq[1] > totalchem[1]:
                    reasons.append("You need "+ str(sharedchemreq[1] - totalchem[1])+ " more organic/inorganic/bio chem courses with labs.")
                    status = "No"
            elif sharedgenchem and sharedorgo:
                if sharedchemreq[0] > totalchem[0]:
                    reasons.append("You need "+ str(sharedchemreq[0] - totalchem[0])+ " more organic/inorganic chem courses.")
                    status = "No"
                if sharedchemreq[1] > totalchem[1]:
                    reasons.append("You need "+ str(sharedchemreq[1] - totalchem[1])+ " more organic/inorganic chem courses with labs.")
                    status = "No"
                if i.biochem[0] > biochem[0]:
                    reasons.append("You need "+ str(i.biochem[0] - biochem[0])+ " more bio chem courses.")
                    status = "No"
                if i.biochem[1] > biochem[1]:
                    reasons.append("You need "+ str(i.biochem[1] - biochem[1])+ " more bio chem courses.")
                    status = "No"
            elif sharedorgo and sharedbiochem:
                if sharedchemreq[0] > totalchem[0]:
                    reasons.append("You need "+ str(sharedchemreq[0] - totalchem[0])+ " more organic/bio chem courses.")
                    status = "No"
                if sharedchemreq[1] > totalchem[1]:
                    reasons.append("You need "+ str(sharedchemreq[1] - totalchem[1])+ " more organic/bio chem courses with labs.")
                    status = "No"
                if i.genchem[0] > genchem[0]:
                    reasons.append("You need "+ str(i.genchem[0] - genchem[0])+ " more gen chem courses.")
                    status = "No"
                if i.genchem[1] > genchem[1]:
                    reasons.append("You need "+ str(i.genchem[1] - genchem[1])+ " more gen chem courses with labs.")
                    status = "No"
            elif sharedbiochem and sharedgenchem:
                if sharedchemreq[0] > totalchem[0]:
                    reasons.append("You need "+ str(sharedchemreq[0] - totalchem[0])+ " more inorganic/bio chem courses.")
                    status = "No"
                if sharedchemreq[1] > totalchem[1]:
                    reasons.append("You need "+ str(sharedchemreq[1] - totalchem[1])+ " more inorganic/bio chem courses.")
                    status = "No"
                if i.orgo[0] > orgo[0]:
                    reasons.append("You need "+ str(i.orgo[0] - orgo[0])+ " more orgo chem courses.")
                    status = "No"
                if i.orgo[1] > orgo[1]:
                    reasons.append("You need "+ str(i.orgo[1] - orgo[1])+ " more orgo chem courses with labs.")
                    status = "No"
            if i.orgo[1] > orgo[1]:
                reasons.append("You need "+ str(i.orgo[1] - orgo[1])+ " more orgo chem courses with labs.")
                status = "No"
            if i.genchem[0] > genchem[0]:
                    reasons.append("You need "+ str(i.genchem[0] - genchem[0])+ " more gen chem courses.")
                    status = "No"
            if i.genchem[1] > genchem[1]:
                reasons.append("You need "+ str(i.genchem[1] - genchem[1])+ " more gen chem courses with labs.")
                status = "No"
            if i.biochem[0] > biochem[0]:
                    reasons.append("You need "+ str(i.biochem[0] - biochem[0])+ " more bio chem courses.")
                    status = "No"
            if i.biochem[1] > biochem[1]:
                reasons.append("You need "+ str(i.biochem[1] - biochem[1])+ " more bio chem courses with labs.")
                status = "No"
        else:

            if i.orgo[0] > orgo[0]:
                    reasons.append("You need "+ str(i.orgo[0] - orgo[0])+ " more orgo chem courses.")
                    status = "No"
            if i.orgo[1] > orgo[1]:
                reasons.append("You need "+ str(i.orgo[1] - orgo[1])+ " more orgo chem courses with labs.")
                status = "No"
            if i.genchem[0] > genchem[0]:
                    reasons.append("You need "+ str(i.genchem[0] - genchem[0])+ " more gen chem courses.")
                    status = "No"
            if i.genchem[1] > genchem[1]:
                reasons.append("You need "+ str(i.genchem[1] - genchem[1])+ " more gen chem courses with labs.")
                status = "No"
            if i.biochem[0] > biochem[0]:
                    reasons.append("You need "+ str(i.biochem[0] - biochem[0])+ " more bio chem courses.")
                    status = "No"
            if i.biochem[1] > biochem[1]:
                reasons.append("You need "+ str(i.biochem[1] - biochem[1])+ " more bio chem courses with labs.")
                status = "No"
            
        
        reqs_met.append(status)
        all_reasons.append(reasons)

    while True:
        menu = input("Decide what you want to do: \n1. Print all \n2. Filter by not met \n3. Filter by met\n4. Exit \nPlease enter the number: ")
        if menu == '1':
            for x in range(0,len(prereqs)):
                print("--------------------------------------------------------------------------")
                print("School: " ,prereqs[x].name,"\tReqs Met: ", reqs_met[x])
                print("--------------------------------------------------------------------------")
                for i in all_reasons[x]:
                    print(i)

                print("\nNotes: ")
                for i in prereqs[x].notes:
                    print(i)
                print("--------------------------------------------------------------------------")
        elif menu == '2':
            for x in range(0,len(prereqs)):
                if reqs_met[x] == "No":
                    print("--------------------------------------------------------------------------")
                    print("School: " ,prereqs[x].name,"\tReqs Met: ", reqs_met[x])
                    print("--------------------------------------------------------------------------")
                    for i in all_reasons[x]:
                        print(i)

                    print("\nNotes: ")
                    for i in prereqs[x].notes:
                        print(i)
                    print("--------------------------------------------------------------------------")
        elif menu == '3':
            for x in range(0,len(prereqs)):
                if reqs_met[x] == "Yes":
                    print("--------------------------------------------------------------------------")
                    print("School: " ,prereqs[x].name,"\tReqs Met: ", reqs_met[x])
                    print("--------------------------------------------------------------------------")
                    for i in all_reasons[x]:
                        print(i)

                    print("\nNotes: ")
                    for i in prereqs[x].notes:
                        print(i)
                    print("--------------------------------------------------------------------------")
        elif menu == '4':
            break
        else:
            print("Please enter a valid input!")

    
