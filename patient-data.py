# dict of possible symptoms
symptoms = {
    "General": (
        "Breathlessness or difficulty in breathing",
        "Dyspnea (shortness of breath)",
        "High pitched breathing",
        "Fever",
        "Weakness",
        "extreme tiredness",
        "Weight loss",
        "Chills",
        "Lowering of blood pressure",
        "Sudden drop in blood pressure",
        "Severe pain",
        "Low cholesterol level",
        "Nausea and vomiting",
        "Loss of consciousness",
        "Altered level of consciousness",
        "Altered mental state",
        "Loss of sensation",
        "Back pain",
        "Internal bleeding",
        "Flank pain and tenderness",
        "Numbness",
        "Seizures",
        "Stroke",
        "Sudden growth",
        "Clammy skin or sweaty skin",
        "Melanomas",
        "Clot bursting",
        "Thrombosis",
        "Tear in inner line of the vessel",
        "Blood leak in between layers of walls",
        "Signs of hypovolemic shock",
        "Sense of impending doom",
        "Painful mass in an extremity",
        "Constant pain",
        "Fainting",
    ),
    "Head": (
        "Head ache",
        "Pain in jaw",
        "Pain above and behind eye",
        "Blurred/Double vision",
        "Sudden loss of vision(focal paralysis)",
        "Focal neurological deficits",
        "Sub hyaloid retinal haemorrhage",
        "Anisocoria (eye)",
        "Nystagmus (eye)",
        "Trouble speaking",
        "Intracerebral haemorrhage",
    ),
    "Neck": (
        "pain in neck",
        "Coughing",
        "Swelling in neck",
        "Hoarseness (harsh, raspy, or strained voice)",
        "Nuchal rigidity",
    ),
    "Upper Body": (
        "Chest pain",
        "Rapid heart rate",
        "frequent palpitation (heart beat)",
        "Hypertension (heart)",
        "Cardiac arrhythmia",
        "Pain in upper back",
        "Pain in abdomen",
        "Abdominal heart Rhythm",
        "Pulse near belly pain",
        "Swelling in abdomen",
    ),
    "Lower Body": (
        "Pain in pelvis/legs/buttock",
        "Pain behind the knees",
        "Edema in low leg",
        "Reduced kidney function",
        "Haematuria",
        "Foot pain",
        "Swelling in ankle and legs",
        "Discoloured toe",
        "Ulcer on the skin of the feet that don’t heal",
    ),
}

# set of all tests
test = (
    "ANGIOGRAM",  # 0
    "BLOOD TEST",  # 1
    "CT",  # 2
    "DSA",  # 3
    "ECHOCARDIOGRAM",  # 4
    "MRA",  # 5
    "MRI",  # 6
    "ULTRASOUND",  # 7
    "X-RAYS",  # 8
)

# dict of possible diseases
diseases = {
    "Ventricular Anuerysm": {
        "symptoms": {68, 59, 61, 54},
        "tests": [test[2], test[7], test[8]],
    },
    "Aneurysm Of Sinus Of Valsalva": {
        "symptoms": {52, 54, 14, 2},
        "tests": [test[2], test[7], test[8]],
    },
    "Aneurysm Following Cardiac Surgery": {
        "symptoms": {52, 1},
        "tests": [test[2], test[7], test[8]],
    },
    "Aortic Aneurysm": {
        "symptoms": {37, 47, 57, 48},
        "tests": [test[2], test[6], test[7], test[8]],
    },
    "Thoracic Aneurysm": {
        "symptoms": {49, 50, 13, 3},
        "tests": [test[2], test[4], test[7], test[8]],
    },
    "Abdominal Aneurysm": {
        "symptoms": {18, 60, 53, 14},
        "tests": [test[2], test[1], test[7], test[8]],
    },
    "Berry Aneurysm": {
        "symptoms": {21, 38, 45, 39},
        "tests": [test[0], test[2], test[3], test[6], test[8]],
    },
    "Fusiform Aneurysm": {
        "symptoms": {30, 36},
        "tests": [test[0], test[2], test[3], test[6], test[8]],
    },
    "Dissecting Aneurysm": {
        "symptoms": {57, 23, 40},
        "tests": [test[0], test[2], test[3], test[6], test[8]],
    },
    "Charcot–Bouchard Aneurysm": {
        "symptoms": {46, 23, 40, 17},
        "tests": [test[0], test[2], test[3], test[6], test[8]],
    },
    "Mycotic Aneurysm": {
        "symptoms": {4, 16, 22, 33},
        "tests": [test[0], test[2], test[3], test[6], test[8]],
    },
    "Popliteal Aneurysm": {
        "symptoms": {63, 64, 67, 70},
        "tests": [test[2], test[3], test[6], test[7], test[8]],
    },
    "Renal Aneurysm": {
        "symptoms": {20, 55, 65, 27},
        "tests": [test[2], test[7], test[8]],
    },
    "Intraparenchymal Aneurysm": {
        "symptoms": {51, 56, 44, 41},
        "tests": [test[2], test[7], test[8]],
    },
    "Capillary Aneurysm": {
        "symptoms": {28, 24, 26},
        "tests": [test[2], test[7], test[8]],
    },
    "Peripheral Aneurysm": {
        "symptoms": {35, 67, 68, 69},
        "tests": [test[2], test[7], test[8]],
    },
    "Visceral Aneurysm": {
        "symptoms": {11, 19, 10},
        "tests": [test[2], test[7], test[8]],
    },
    "Pseudo Aneurysm": {"symptoms": {29}, "tests": [test[2], test[7], test[8]]},
}


# patient data type class
class Patient:
    # constructor to initialize instance variables
    def __init__(self, name, age, gen, bg, ht, wt, dis, tst):
        self.setDetails(name, age, gen, bg, ht, wt, dis, tst)

    # setter for the name
    def setName(self, name):
        self.name = name

    # setter for the age
    def setAge(self, age):
        self.age = age

    # setter for the age
    def setGen(self, gen):
        self.gen = gen

    # setter for the blood group
    def setBloodGroup(self, bg):
        self.bg = bg

    # setter for the height
    def setHeight(self, ht):
        self.ht = ht

    # setter for the weight
    def setWeight(self, wt):
        self.wt = wt

    # setter for disease
    def setDisease(self, dis):
        self.dis = dis

    # setter for disease
    def setTest(self, tst):
        self.tst = tst

    # setter for all instance variables
    def setDetails(self, name, age, gen, bg, ht, wt, dis, tst):
        self.setName(name)
        self.setAge(age)
        self.setGen(gen)
        self.setBloodGroup(bg)
        self.setHeight(ht)
        self.setWeight(wt)
        self.setDisease(dis)
        self.setTest(tst)

    # getter for all instance variables
    def getDetails(self):
        return (
            self.name,
            self.age,
            self.gen,
            self.bg,
            self.ht,
            self.wt,
            self.dis,
            self.tst,
        )


# function to check the symptoms of patient
def checkup():
    print("\nChoose the Symptoms of the patient from the following:")
    i = 1
    for body_part in symptoms:
        print(f"\nSymptoms of {body_part}:")
        for item in symptoms[body_part]:
            print(f"{i:02d} - {item}")
            i += 1

    chosen_sym = set()
    error_msg = "Invalid input. Please enter a number from list or exit."
    while True:
        inp = input("\nEnter the symptoms (exit to end): ")
        if inp.lower() == "exit":
            break
        else:
            try:
                sym_num = int(inp)
                if sym_num in range(1, i + 1):
                    chosen_sym.add(sym_num)
                else:
                    print(error_msg)
            except ValueError:
                print(error_msg)

    return chosen_sym


# function to match symptoms with disease
def diagnose(chosen_sym):
    if len(chosen_sym) == 0:
        return ("no aneurysm", [t for t in test])

    for disease in diseases:
        if len(diseases[disease]["symptoms"] - chosen_sym) == 0:
            return (disease, diseases[disease]["tests"])


# function to display output to user
# with disease information and prescribing tests
def display_output(disease, tests):
    print(f"\nThe Patient Has --> {disease}")
    if disease == "no aneurysm":
        print("Please take the following tests for confirmation:")
    else:
        print("Please take the following tests:")
    for test in tests.split(", "):
        print(test)


# driver code
if __name__ == "__main__":
    import csv, os

    # take user input for patient info
    print("\nEnter patient details\n")
    patient_name = input("Enter Name: ")
    patient_age = int(input("Enter Age: "))
    patient_gen = input("Enter Gender (M or F): ").strip().upper()
    patient_bg = input("Enter Blood Group: ")
    patient_ht = int(input("Enter Height: "))
    patient_wt = int(input("Enter Weight: "))
    patient_sym = checkup()
    patient_dis, patient_tst = diagnose(patient_sym)
    patient = Patient(
        patient_name,
        patient_age,
        patient_gen,
        patient_bg,
        patient_ht,
        patient_wt,
        patient_dis,
        str(patient_tst).strip("[]").replace("'", ""),
    )

    # display disease and test info to user
    display_output(patient.dis, patient.tst)

    # write patient info to CSV file
    filename = "patient.csv"
    info_fields = (
        "Name",
        "Age",
        "Gender",
        "Blood Group",
        "Height",
        "Weight",
        "Disease",
        "Prescribed Test",
    )
    with open(filename, "a+") as patient_file:
        csv_writer = csv.writer(patient_file, delimiter=",")
        # check if first character is empty
        if os.path.exists(filename) and os.stat(filename).st_size == 0:
            csv_writer.writerow(info_fields)
        csv_writer.writerow(patient.getDetails())
